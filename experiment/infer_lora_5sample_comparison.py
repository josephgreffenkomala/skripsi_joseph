"""Compare five-example LoRA inference on one train and one held-out article."""

import json
import time
from contextlib import nullcontext
from pathlib import Path
from typing import Any

import torch
from peft import PeftModel
from torch import nn
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen3-0.6B"
ROUTE = (1, 0, 1, 0, 1)
TRAIN_SAMPLE_ROW_INDEX = 7296
MAX_NEW_TOKENS = 256
INSTRUCTION = (
    "Ringkas artikel berita berikut dalam bahasa Indonesia. Pertahankan informasi utama "
    "dan jangan menambahkan informasi yang tidak terdapat dalam artikel.\n\nArtikel:\n"
)


class SkippedDecoderLayer(nn.Module):
    """Pass hidden states through without evaluating this decoder layer."""

    def forward(
        self, hidden_states: torch.Tensor, *args: Any, **kwargs: Any
    ) -> tuple[torch.Tensor]:
        """Return the hidden state in the tuple shape expected by Transformers."""
        return (hidden_states,)


def read_row(path: Path, row_index: int) -> dict[str, str]:
    """Read one row from the XL-Sum JSONL file by its zero-based index."""
    with path.open(encoding="utf-8") as data_file:
        for current_index, line in enumerate(data_file):
            if current_index == row_index:
                row = json.loads(line)
                return {
                    "id": row["id"],
                    "article": row["text"].strip(),
                    "reference": row["summary"].strip(),
                }
    raise IndexError(f"Row {row_index} not found in {path}.")


def prompt_tensors(tokenizer: Any, article: str) -> dict[str, torch.Tensor]:
    """Prepare a final-format, non-thinking Qwen prompt for greedy decoding."""
    chat = tokenizer.apply_chat_template(
        [{"role": "user", "content": INSTRUCTION + article}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    encoded = tokenizer(chat, return_tensors="pt", add_special_tokens=False)
    if encoded["input_ids"].shape[1] > 3840:
        raise ValueError("Prompt exceeds the approved 3,840-token input limit.")
    return encoded


def generate_once(
    model: PeftModel,
    tokenizer: Any,
    article: str,
    disable_adapter: bool,
) -> str:
    """Generate one summary with fixed greedy decoding settings."""
    encoded = prompt_tensors(tokenizer, article)
    adapter_context = model.disable_adapter() if disable_adapter else nullcontext()
    with adapter_context, torch.inference_mode():
        generated = model.generate(
            **encoded,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            num_beams=1,
            temperature=None,
            top_p=None,
            top_k=None,
            use_cache=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    completion = generated[0, encoded["input_ids"].shape[1] :]
    return tokenizer.decode(completion, skip_special_tokens=True).strip()


def main() -> None:
    """Run four controlled model conditions for two XL-Sum articles."""
    project_dir = Path(__file__).resolve().parent
    cache_dir = project_dir / ".cache" / "huggingface"
    adapter_dir = project_dir / "outputs" / "lora_skip_5sample_route_10101"
    data_dir = project_dir / "data" / "xlsum" / "indonesian"
    output_dir = project_dir / "outputs" / "lora_inference_comparison_2samples_256"
    if output_dir.exists():
        raise FileExistsError(f"Refusing to overwrite existing results: {output_dir}")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, cache_dir=cache_dir, local_files_only=True
    )
    with (adapter_dir / "run_manifest.json").open(encoding="utf-8") as manifest_file:
        manifest = json.load(manifest_file)
    train_example = read_row(
        data_dir / "indonesian_train.jsonl", TRAIN_SAMPLE_ROW_INDEX
    )
    train_ids = {sample["id"] for sample in manifest["samples"]}
    if train_example["id"] not in train_ids:
        raise ValueError("Selected train article is not listed in the LoRA manifest.")
    heldout_example = read_row(data_dir / "indonesian_val.jsonl", 0)
    examples = [
        {"split": "train_member", **train_example},
        {"split": "held_out_validation", **heldout_example},
    ]

    torch.set_num_threads(4)
    torch.manual_seed(43)
    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        cache_dir=cache_dir,
        local_files_only=True,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
    )
    model = PeftModel.from_pretrained(base_model, adapter_dir, is_trainable=False)
    model.eval()
    decoder_layers = model.get_base_model().model.layers
    skipped_indices = [index for index in range(28) if (index // 4) + 1 in {3, 5}]
    originals = {index: decoder_layers[index] for index in skipped_indices}
    results: list[dict[str, Any]] = []

    conditions = [
        ("base_full", True, False),
        ("lora_full", False, False),
        ("base_route_10101", True, True),
        ("lora_route_10101", False, True),
    ]
    try:
        for example in examples:
            print(
                f"\n{example['split']} | {example['id']} | "
                f"reference: {example['reference']}",
                flush=True,
            )
            for condition_name, disable_adapter, skip_route in conditions:
                if skip_route:
                    for index in skipped_indices:
                        decoder_layers[index] = SkippedDecoderLayer()
                start = time.perf_counter()
                summary = generate_once(
                    model, tokenizer, example["article"], disable_adapter
                )
                elapsed_seconds = time.perf_counter() - start
                if skip_route:
                    for index, original_layer in originals.items():
                        decoder_layers[index] = original_layer
                result = {
                    "split": example["split"],
                    "id": example["id"],
                    "condition": condition_name,
                    "summary": summary,
                    "elapsed_seconds": elapsed_seconds,
                }
                results.append(result)
                print(
                    f"{condition_name} ({elapsed_seconds:.1f}s): {summary}",
                    flush=True,
                )
    finally:
        for index, original_layer in originals.items():
            decoder_layers[index] = original_layer

    output_dir.mkdir(parents=True, exist_ok=False)
    payload = {
        "model_id": MODEL_ID,
        "adapter": str(adapter_dir.relative_to(project_dir)),
        "route_g2_to_g6": list(ROUTE),
        "max_new_tokens": MAX_NEW_TOKENS,
        "decoding": {"do_sample": False, "num_beams": 1},
        "examples": [
            {
                "split": example["split"],
                "id": example["id"],
                "reference": example["reference"],
                "results": [
                    result for result in results if result["id"] == example["id"]
                ],
            }
            for example in examples
        ],
        "note": "Exploratory two-example comparison; not a quality evaluation.",
    }
    (output_dir / "results.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nSaved results to {output_dir / 'results.json'}", flush=True)


if __name__ == "__main__":
    main()
