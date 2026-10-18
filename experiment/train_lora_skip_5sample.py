"""Run a tiny LoRA training smoke run on five XL-Sum Indonesian examples."""

import json
import random
from pathlib import Path

import torch
from peft import LoraConfig, TaskType, get_peft_model
from torch import nn
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen3-0.6B"
SAMPLE_COUNT = 5
SAMPLE_SEED = 42
TRAIN_SEED = 43
ROUTE = (1, 0, 1, 0, 1)
MAX_INPUT_TOKENS = 3840
MAX_TARGET_TOKENS = 256
MAX_CONTEXT_TOKENS = 4096
LEARNING_RATE = 1e-4


class SkippedDecoderLayer(nn.Module):
    """Pass the hidden state through without running the decoder layer."""

    def forward(
        self, hidden_states: torch.Tensor, *args: object, **kwargs: object
    ) -> tuple[torch.Tensor]:
        """Return the input as the first item expected by Transformers 4.51."""
        return (hidden_states,)


def load_five_examples(
    tokenizer: AutoTokenizer, data_path: Path
) -> list[dict[str, object]]:
    """Select five deterministic train examples and prepare causal-LM labels."""
    with data_path.open(encoding="utf-8") as data_file:
        row_count = sum(1 for _ in data_file)

    selected_indices = set(
        random.Random(SAMPLE_SEED).sample(range(row_count), SAMPLE_COUNT)
    )
    examples: list[dict[str, object]] = []
    instruction = (
        "Ringkas artikel berita berikut dalam bahasa Indonesia. Pertahankan informasi utama "
        "dan jangan menambahkan informasi yang tidak terdapat dalam artikel.\n\nArtikel:\n"
    )

    with data_path.open(encoding="utf-8") as data_file:
        for row_index, line in enumerate(data_file):
            if row_index not in selected_indices:
                continue

            row = json.loads(line)
            article = row["text"].strip()
            summary = row["summary"].strip()
            if not article or not summary:
                raise ValueError(f"Sample indeks {row_index} kosong setelah trim.")

            user_prompt = instruction + article
            prompt_ids = tokenizer.apply_chat_template(
                [{"role": "user", "content": user_prompt}],
                tokenize=True,
                add_generation_prompt=True,
                enable_thinking=False,
            )
            complete_ids = tokenizer.apply_chat_template(
                [
                    {"role": "user", "content": user_prompt},
                    {"role": "assistant", "content": summary},
                ],
                tokenize=True,
                add_generation_prompt=False,
                enable_thinking=False,
            )
            if complete_ids[: len(prompt_ids)] != prompt_ids:
                raise ValueError(
                    "Token prompt tidak menjadi prefiks token percakapan lengkap."
                )

            target_ids = complete_ids[len(prompt_ids) :]
            if len(prompt_ids) > MAX_INPUT_TOKENS:
                raise ValueError(
                    f"Sample indeks {row_index} melewati batas token masukan."
                )
            if len(target_ids) > MAX_TARGET_TOKENS:
                raise ValueError(
                    f"Sample indeks {row_index} melewati batas token ringkasan."
                )
            if len(complete_ids) > MAX_CONTEXT_TOKENS:
                raise ValueError(
                    f"Sample indeks {row_index} melewati batas context window."
                )

            labels = [-100] * len(prompt_ids) + target_ids
            examples.append(
                {
                    "id": row["id"],
                    "row_index": row_index,
                    "input_ids": complete_ids,
                    "labels": labels,
                    "input_tokens": len(prompt_ids),
                    "target_tokens": len(target_ids),
                }
            )

    if len(examples) != SAMPLE_COUNT:
        raise ValueError(f"Dipilih {len(examples)} contoh, seharusnya {SAMPLE_COUNT}.")
    return examples


def main() -> None:
    """Train LoRA adapters for one pass while holding the selected route fixed."""
    project_dir = Path(__file__).resolve().parent
    data_path = project_dir / "data" / "xlsum" / "indonesian" / "indonesian_train.jsonl"
    cache_dir = project_dir / ".cache" / "huggingface"
    output_dir = project_dir / "outputs" / "lora_skip_5sample_route_10101"
    if output_dir.exists():
        raise FileExistsError(
            f"Output already exists; refusing to overwrite: {output_dir}"
        )

    torch.set_num_threads(4)
    random.seed(TRAIN_SEED)
    torch.manual_seed(TRAIN_SEED)

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, cache_dir=cache_dir, local_files_only=True
    )
    examples = load_five_examples(tokenizer, data_path)
    print(f"Selected {len(examples)} train examples with seed {SAMPLE_SEED}.")
    for example in examples:
        print(
            f"{example['id']}: input={example['input_tokens']} tokens, "
            f"target={example['target_tokens']} tokens"
        )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        cache_dir=cache_dir,
        local_files_only=True,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
    )
    model.config.use_cache = False
    model.gradient_checkpointing_enable(
        gradient_checkpointing_kwargs={"use_reentrant": False}
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        inference_mode=False,
        r=4,
        lora_alpha=8,
        lora_dropout=0.05,
        target_modules=["q_proj", "v_proj"],
    )
    model = get_peft_model(model, lora_config)
    model.enable_input_require_grads()
    model.print_trainable_parameters()

    base_model = model.get_base_model()
    layers = base_model.model.layers
    group_size = 4
    active_group_names = (
        ["G1"]
        + [
            f"G{group_number}"
            for group_number, is_active in zip(range(2, 7), ROUTE)
            if is_active
        ]
        + ["G7"]
    )
    active_indices = {
        index
        for group_name in active_group_names
        for index in range(
            (int(group_name[1:]) - 1) * group_size,
            int(group_name[1:]) * group_size,
        )
    }
    skipped_indices = [
        index for index in range(len(layers)) if index not in active_indices
    ]
    original_layers = {index: layers[index] for index in skipped_indices}
    for index in skipped_indices:
        layers[index] = SkippedDecoderLayer()

    trainable_parameters = [
        parameter for parameter in model.parameters() if parameter.requires_grad
    ]
    optimizer = torch.optim.AdamW(
        trainable_parameters, lr=LEARNING_RATE, weight_decay=0.0
    )
    losses: list[float] = []

    try:
        model.train()
        for step, example in enumerate(examples, start=1):
            input_ids = torch.tensor([example["input_ids"]], dtype=torch.long)
            labels = torch.tensor([example["labels"]], dtype=torch.long)
            attention_mask = torch.ones_like(input_ids)

            optimizer.zero_grad(set_to_none=True)
            output = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels,
                use_cache=False,
            )
            loss = output.loss
            loss.backward()
            torch.nn.utils.clip_grad_norm_(trainable_parameters, max_norm=1.0)
            optimizer.step()
            loss_value = float(loss.detach())
            losses.append(loss_value)
            print(f"step {step}/{SAMPLE_COUNT}: loss={loss_value:.4f}", flush=True)
            del output, loss, input_ids, labels, attention_mask
    finally:
        for index, layer in original_layers.items():
            layers[index] = layer

    model.eval()
    output_dir.mkdir(parents=True, exist_ok=False)
    model.save_pretrained(output_dir)
    manifest = {
        "model_id": MODEL_ID,
        "split": "train",
        "sample_seed": SAMPLE_SEED,
        "train_seed": TRAIN_SEED,
        "route_g2_to_g6": list(ROUTE),
        "active_group_names": active_group_names,
        "samples": [
            {
                "id": example["id"],
                "row_index": example["row_index"],
                "input_tokens": example["input_tokens"],
                "target_tokens": example["target_tokens"],
            }
            for example in examples
        ],
        "learning_rate": LEARNING_RATE,
        "epochs": 1,
        "step_losses": losses,
        "note": "Exploratory five-example run; not thesis evaluation or research result.",
    }
    (output_dir / "run_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Saved LoRA adapter and run manifest to {output_dir}")


if __name__ == "__main__":
    main()
