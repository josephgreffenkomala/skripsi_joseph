"""Run one full-layer Qwen3-0.6B summary inference on Modal's T4 GPU."""

import json
from pathlib import Path
from typing import Any

import modal

MODEL_ID = "Qwen/Qwen3-0.6B"
MAX_NEW_TOKENS = 256
VALIDATION_ROW_INDEX = 0
INSTRUCTION = (
    "Ringkas artikel berita berikut dalam bahasa Indonesia. Pertahankan informasi utama "
    "dan jangan menambahkan informasi yang tidak terdapat dalam artikel.\n\nArtikel:\n"
)

image = modal.Image.debian_slim(python_version="3.12").uv_pip_install(
    "torch==2.6.0",
    "transformers==4.51.3",
    "accelerate==1.6.0",
)
app = modal.App("qwen3-full-inference-once", image=image)


@app.function(
    gpu="T4",
    cpu=2,
    memory=8192,
    timeout=300,
    startup_timeout=300,
    retries=0,
)
def infer_once(article: str, example_id: str) -> dict[str, Any]:
    """Generate one summary with the unmodified full Qwen model on a T4."""
    import time

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    if not torch.cuda.is_available():
        raise RuntimeError("Modal function did not receive a CUDA GPU.")

    started_at = time.perf_counter()
    print(f"GPU: {torch.cuda.get_device_name(0)}", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to("cuda")
    model.eval()

    chat_text = tokenizer.apply_chat_template(
        [{"role": "user", "content": INSTRUCTION + article}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(
        chat_text,
        return_tensors="pt",
        add_special_tokens=False,
    ).to("cuda")
    input_tokens = inputs["input_ids"].shape[1]
    if input_tokens > 3840:
        raise ValueError(f"Prompt has {input_tokens} tokens; limit is 3,840.")

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            num_beams=1,
            temperature=None,
            top_p=None,
            top_k=None,
            use_cache=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    answer_ids = output[0, input_tokens:]
    result = {
        "model": MODEL_ID,
        "gpu": torch.cuda.get_device_name(0),
        "example_id": example_id,
        "input_tokens": input_tokens,
        "output_tokens": answer_ids.numel(),
        "elapsed_seconds": round(time.perf_counter() - started_at, 2),
        "summary": tokenizer.decode(answer_ids, skip_special_tokens=True).strip(),
    }
    return result


@app.local_entrypoint()
def main() -> None:
    """Read one existing validation example and invoke one remote inference."""
    data_path = (
        Path(__file__).resolve().parent
        / "data"
        / "xlsum"
        / "indonesian"
        / "indonesian_val.jsonl"
    )
    with data_path.open(encoding="utf-8") as dataset_file:
        for row_index, line in enumerate(dataset_file):
            if row_index == VALIDATION_ROW_INDEX:
                example = json.loads(line)
                break
        else:
            raise IndexError(f"Validation row {VALIDATION_ROW_INDEX} was not found.")

    print(f"Validation example: {example['id']}", flush=True)
    print(f"Reference: {example['summary'].strip()}", flush=True)
    result = infer_once.remote(example["text"].strip(), example["id"])
    print(f"\nFull-model output:\n{result['summary']}", flush=True)
    print(
        f"\nGPU: {result['gpu']} | input={result['input_tokens']} tokens | "
        f"output={result['output_tokens']} tokens | "
        f"function time={result['elapsed_seconds']}s",
        flush=True,
    )
