"""Modal entry point for preparing and running the research pipeline."""

from __future__ import annotations

import json
import os
import sys
import tarfile
from pathlib import Path
from typing import Any

import modal

CONFIG_PATH = Path(__file__).with_name("config.json")
IMAGE = (
    modal.Image.debian_slim(python_version="3.12")
    .uv_pip_install(requirements=[str(Path(__file__).with_name("requirements.txt"))])
    .add_local_python_source("experiment_proposal")
)
app = modal.App("qwen3-xlsum-sequence-routing", image=IMAGE)
volume = modal.Volume.from_name("experiment-proposal-data", create_if_missing=False)


def ensure_xlsum_data(dataset_dir: Path) -> None:
    """Download the official Indonesian XL-Sum archive if source files are absent."""
    expected_files = (
        "indonesian_train.jsonl",
        "indonesian_val.jsonl",
        "indonesian_test.jsonl",
    )
    if all((dataset_dir / filename).is_file() for filename in expected_files):
        return

    from huggingface_hub import hf_hub_download

    dataset_dir.mkdir(parents=True, exist_ok=True)
    archive_path = hf_hub_download(
        repo_id="csebuetnlp/xlsum",
        repo_type="dataset",
        filename="data/indonesian_XLSum_v2.0.tar.bz2",
    )
    with tarfile.open(archive_path, mode="r:bz2") as archive:
        members = {
            Path(member.name).name: member
            for member in archive.getmembers()
            if Path(member.name).name in expected_files and member.isfile()
        }
        missing = set(expected_files) - members.keys()
        if missing:
            raise FileNotFoundError(
                "The XL-Sum Indonesian archive did not contain expected files: "
                + ", ".join(sorted(missing))
            )
        for filename in expected_files:
            source = archive.extractfile(members[filename])
            if source is None:
                raise FileNotFoundError(
                    f"Could not read {filename} from the XL-Sum archive."
                )
            with source, (dataset_dir / filename).open("wb") as destination:
                destination.write(source.read())


@app.function(
    cpu=2,
    memory=16384,
    timeout=3600,
    retries=0,
    volumes={"/vol": volume},
)
def prepare_data(config_text: str) -> dict[str, Any]:
    """Filter and sample data without allocating a paid GPU."""
    os.environ["HF_HOME"] = "/vol/hf_cache"
    config = json.loads(config_text)
    dataset_dir = Path(config["dataset_dir"])
    ensure_xlsum_data(dataset_dir)
    from transformers import AutoTokenizer

    import transformers

    from experiment_proposal.data import prepare_dataset

    tokenizer = AutoTokenizer.from_pretrained(config["model_id"])
    result = prepare_dataset(
        tokenizer=tokenizer,
        dataset_dir=dataset_dir,
        output_dir=Path(config["output_dir"]) / "prepared",
        counts=config["counts"],
        seed=config["sample_seed"],
        instruction=config["prompt_instruction"],
        max_input_tokens=config["max_input_tokens"],
        max_target_tokens=config["max_target_tokens"],
        max_context_tokens=config["max_context_tokens"],
        max_source_rows_per_split=config.get("max_source_rows_per_split"),
    )
    revision = tokenizer.init_kwargs.get("_commit_hash")
    metadata = {
        "model_id": config["model_id"],
        "model_revision": revision,
        "transformers_version": transformers.__version__,
        "config": config,
    }
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "run_manifest.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    volume.commit()
    return result


@app.function(
    gpu="T4",
    cpu=2,
    memory=16384,
    timeout=86400,
    retries=0,
    volumes={"/vol": volume},
)
def execute_stage(stage: str, config_text: str) -> dict[str, Any]:
    """Execute one requested stage in a persistent Modal volume."""
    os.environ["HF_HOME"] = "/vol/hf_cache"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    config = json.loads(config_text)
    if stage == "router":
        from experiment_proposal.train import train_router

        result = train_router(config)
    elif stage == "lora":
        from experiment_proposal.train import train_lora_variants

        result = train_lora_variants(config)
    elif stage == "evaluate":
        from experiment_proposal.evaluate import evaluate

        result = evaluate(config)
    else:
        raise ValueError(f"Unsupported stage {stage!r}.")
    import torch

    manifest_path = Path(config["output_dir"]) / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["config"] = config
    manifest["runtime"] = {
        "python_version": sys.version,
        "torch_version": torch.__version__,
        "cuda_version": torch.version.cuda,
        "gpu_name": torch.cuda.get_device_name(0),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    volume.commit()
    return result


@app.local_entrypoint()
def main(
    stage: str = "prepare",
    config_path: str = "experiment_proposal/config.json",
) -> None:
    """Submit one experiment stage; the user starts this command manually."""
    if stage not in {"prepare", "router", "lora", "evaluate"}:
        raise ValueError("--stage must be prepare, router, lora, or evaluate.")
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    config_text = json.dumps(config)
    if stage == "prepare":
        result = prepare_data.remote(config_text)
    else:
        result = execute_stage.remote(stage, config_text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
