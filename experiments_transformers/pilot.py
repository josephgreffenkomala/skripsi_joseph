"""Run the five-sample native Transformers word-occlusion pilot."""

from __future__ import annotations

import argparse
import csv
import json
import platform
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any

from experiments.dataset import load_smsa, select_pilot_examples
from experiments.heatmap import render_heatmap
from experiments.metrics import (
    peak_rss_bytes,
    sha256_file,
    system_metadata,
    write_jsonl,
)

from .client import Prediction, TransformersClient
from .config import ExperimentConfig, PROMPT_TEMPLATE
from .occlusion import OcclusionResult, run_occlusion


def parse_args() -> argparse.Namespace:
    """Parse command-line options."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument(
        "--baseline-model", required=True, help="Native model directory or Hub id"
    )
    parser.add_argument(
        "--quantized-model",
        required=True,
        help="Quantized Transformers model directory or Hub id",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("experiments_transformers/results/pilot"),
    )
    parser.add_argument("--device", default="cpu")
    parser.add_argument(
        "--torch-dtype", choices=("auto", "float32", "bfloat16"), default="auto"
    )
    return parser.parse_args()


def record(
    example: Any,
    condition: str,
    prediction: Prediction,
    elapsed: float,
    error: str | None = None,
) -> dict[str, Any]:
    """Serialize one prediction."""
    return {
        "row_index": example.row_index,
        "gold_label": example.label,
        "condition": condition,
        "prediction": prediction.label if error is None else None,
        "generated_text": prediction.generated_text if error is None else "",
        "scores": prediction.scores if error is None else {},
        "elapsed_seconds": elapsed,
        "peak_rss_bytes": peak_rss_bytes(),
        "parser_status": "ok" if error is None and prediction.label else "invalid",
        "error": error,
    }


def run_condition(
    model_path: str, condition: str, examples: list[Any], config: ExperimentConfig
) -> tuple[
    list[dict[str, Any]], list[dict[str, Any]], dict[int, list[OcclusionResult]]
]:
    """Run predictions and occlusion for one model condition."""
    client = TransformersClient(
        model_path, device=config.device, torch_dtype=config.torch_dtype
    )
    predictions, occlusions, heatmap_rows = [], [], {}
    for example in examples:
        started = time.perf_counter()
        try:
            baseline = client.complete(
                PROMPT_TEMPLATE.format(review=example.review),
                seed=config.seed,
                max_new_tokens=config.max_new_tokens,
            )
            sensitivity = run_occlusion(
                client,
                example.review,
                baseline,
                seed=config.seed,
                max_new_tokens=config.max_new_tokens,
            )
            predictions.append(
                record(example, condition, baseline, time.perf_counter() - started)
            )
            predictions[-1]["occlusion_forward_passes"] = len(sensitivity)
            occlusions.extend(
                {
                    "row_index": example.row_index,
                    "condition": condition,
                    "baseline_target_label": baseline.label,
                    "position": item.position,
                    "word": item.word,
                    "score_delta": item.score_delta,
                    "occluded_prediction": item.occluded_prediction,
                    "occluded_scores": item.occluded_scores,
                }
                for item in sensitivity
            )
            heatmap_rows[example.row_index] = sensitivity
        except Exception as exc:  # noqa: BLE001 - preserve per-sample failure in the artifact.
            predictions.append(
                record(
                    example,
                    condition,
                    Prediction(None, "", {}, {}),
                    time.perf_counter() - started,
                    str(exc),
                )
            )
    return predictions, occlusions, heatmap_rows


def write_csv(path: Path, records: list[dict[str, Any]]) -> None:
    """Write flat occlusion records as CSV."""
    fields = [
        "row_index",
        "condition",
        "baseline_target_label",
        "position",
        "word",
        "score_delta",
        "occluded_prediction",
        "occluded_scores",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record_data in records:
            row = dict(record_data)
            row["occluded_scores"] = json.dumps(row["occluded_scores"], sort_keys=True)
            writer.writerow(row)


def main() -> None:
    """Run both conditions and write provenance plus heatmaps."""
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    examples = select_pilot_examples(load_smsa(args.dataset))
    config = ExperimentConfig(device=args.device, torch_dtype=args.torch_dtype)
    metadata = {
        "model_name": config.model_name,
        "dataset": str(args.dataset),
        "dataset_sha256": sha256_file(args.dataset),
        "pilot_row_indices": [example.row_index for example in examples],
        "prompt_template": PROMPT_TEMPLATE,
        "config": asdict(config),
        "system": system_metadata(),
        "runtime": "Hugging Face Transformers / AutoModelForCausalLM",
        "python": platform.python_version(),
        "baseline_model": args.baseline_model,
        "quantized_model": args.quantized_model,
        "created_unix": time.time(),
    }
    all_predictions, all_occlusions = [], []
    heatmaps = {example.row_index: {} for example in examples}
    for condition, model_path in (
        ("baseline", args.baseline_model),
        ("quantized", args.quantized_model),
    ):
        predictions, occlusions, rows = run_condition(
            model_path, condition, examples, config
        )
        all_predictions.extend(predictions)
        all_occlusions.extend(occlusions)
        for row_index, values in rows.items():
            heatmaps[row_index][condition] = values
    write_jsonl(args.output_dir / "predictions.jsonl", iter(all_predictions))
    write_jsonl(args.output_dir / "occlusion.jsonl", iter(all_occlusions))
    write_csv(args.output_dir / "occlusion.csv", all_occlusions)
    for row_index, rows in heatmaps.items():
        if len(rows) == 2:
            render_heatmap(
                args.output_dir / f"heatmap-row-{row_index:04d}.svg",
                f"Qwen3-0.6B Transformers sensitivity, SmSA row {row_index}",
                rows,
            )
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    failures = [item for item in all_predictions if item["parser_status"] != "ok"]
    print(
        f"Pilot Transformers selesai: {len(all_predictions) - len(failures)}/{len(all_predictions)} prediksi berhasil. Hasil: {args.output_dir}"
    )
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
