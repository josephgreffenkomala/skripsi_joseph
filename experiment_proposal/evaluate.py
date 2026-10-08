"""Greedy generation, automatic metrics, latency records, and paired bootstrap."""

from __future__ import annotations

import json
import random
import statistics
import time
from pathlib import Path
from typing import Any

import torch
from bert_score import BERTScorer
from peft import PeftModel
from rouge_score import rouge_scorer
from transformers import AutoTokenizer

from experiment_proposal.data import read_jsonl
from experiment_proposal.modeling import (
    RouteController,
    SequenceRouter,
    load_model,
)

Route = tuple[int, int, int, int, int]
METRICS = ("rouge1", "rouge2", "rougeL", "bertscore")


def _sync() -> None:
    if torch.cuda.is_available():
        torch.cuda.synchronize()


def _load_router(config: dict[str, Any], output_root: Path) -> SequenceRouter:
    router_config = json.loads(
        (output_root / "router" / "router_config.json").read_text()
    )
    router = SequenceRouter(router_config["input_dim"], router_config["hidden_dim"])
    router.load_state_dict(
        torch.load(
            output_root / "router" / "router.pt", map_location="cuda", weights_only=True
        )
    )
    return router.to("cuda").eval()


def _model_revision(output_root: Path) -> str | None:
    manifest = json.loads(
        (output_root / "run_manifest.json").read_text(encoding="utf-8")
    )
    return manifest.get("model_revision")


def _load_variant(
    config: dict[str, Any],
    output_root: Path,
    variant: str,
) -> tuple[torch.nn.Module, Route | None, SequenceRouter | None, float]:
    revision = _model_revision(output_root)
    model = load_model(config["model_id"], trainable=False, revision=revision)
    selection = json.loads((output_root / "lora_selection.json").read_text())
    static_route = tuple(
        json.loads((output_root / "static_route.json").read_text())["route_g2_to_g6"]
    )
    route: Route | None
    router: SequenceRouter | None = None
    beta = 0.0
    if variant in {"full_lora", "static_lora", "router_lora"}:
        selected = selection["variants"][variant]["selected"]
        model = PeftModel.from_pretrained(
            model, selected["checkpoint"], is_trainable=False
        )
        if variant == "full_lora":
            route = (1, 1, 1, 1, 1)
        elif variant == "static_lora":
            route = static_route
        else:
            route = None
            router = _load_router(config, output_root)
            beta = float(selected["beta"])
    elif variant == "router_only":
        route = None
        router = _load_router(config, output_root)
    else:
        raise ValueError(f"Unknown evaluation variant: {variant}")
    model.eval()
    return model, route, router, beta


def generate_one(
    model: torch.nn.Module,
    tokenizer: Any,
    row: dict[str, Any],
    route: Route | None,
    router: SequenceRouter | None,
    beta: float,
    max_new_tokens: int,
) -> dict[str, Any]:
    """Run greedy decoding and separately time prefill and token decoding."""
    device = torch.device("cuda")
    prompt_ids = torch.tensor([row["prompt_ids"]], dtype=torch.long, device=device)
    article_mask = torch.tensor(
        [row["article_mask"][: len(row["prompt_ids"])]], dtype=torch.bool, device=device
    )
    generated: list[int] = []
    eos_ids = model.generation_config.eos_token_id
    if eos_ids is None:
        eos_ids = {tokenizer.eos_token_id}
    elif isinstance(eos_ids, int):
        eos_ids = {eos_ids}
    else:
        eos_ids = set(eos_ids)
    controller = RouteController(
        model,
        article_mask,
        router=router,
        fixed_route=route,
        beta=beta,
    )
    _sync()
    total_start = time.perf_counter()
    with controller, torch.inference_mode():
        _sync()
        prefill_start = time.perf_counter()
        output = model(input_ids=prompt_ids, use_cache=True, return_dict=True)
        _sync()
        prefill_seconds = time.perf_counter() - prefill_start
        past = output.past_key_values
        next_token = output.logits[:, -1, :].argmax(dim=-1, keepdim=True)
        decode_start = time.perf_counter()
        for _ in range(max_new_tokens):
            token_id = int(next_token.item())
            generated.append(token_id)
            if token_id in eos_ids:
                break
            output = model(
                input_ids=next_token,
                past_key_values=past,
                use_cache=True,
                return_dict=True,
            )
            past = output.past_key_values
            next_token = output.logits[:, -1, :].argmax(dim=-1, keepdim=True)
        _sync()
        decode_seconds = time.perf_counter() - decode_start
    _sync()
    total_seconds = time.perf_counter() - total_start
    selected_route = controller.selected_route or (1, 1, 1, 1, 1)
    summary = tokenizer.decode(generated, skip_special_tokens=True).strip()
    return {
        "summary": summary,
        "route_g2_to_g6": list(selected_route),
        "active_layers": 8 + 4 * sum(selected_route),
        "input_tokens": len(row["prompt_ids"]),
        "output_tokens": len(generated),
        "total_seconds": total_seconds,
        "prefill_seconds": prefill_seconds,
        "decoding_seconds": decode_seconds,
    }


def _bootstrap_differences(
    records: list[dict[str, Any]],
    primary: str,
    comparator: str,
    samples: int,
    seed: int,
) -> dict[str, dict[str, float]]:
    """Calculate paired percentile confidence intervals from saved per-item scores."""
    rng = random.Random(seed)
    result: dict[str, dict[str, float]] = {}
    for metric in METRICS:
        differences = [
            row["scores"][primary][metric] - row["scores"][comparator][metric]
            for row in records
        ]
        draws = []
        for _ in range(samples):
            indices = [rng.randrange(len(differences)) for _ in differences]
            draws.append(statistics.mean(differences[index] for index in indices))
        draws.sort()

        def percentile(probability: float) -> float:
            position = (len(draws) - 1) * probability
            lower = int(position)
            upper = min(lower + 1, len(draws) - 1)
            weight = position - lower
            return draws[lower] * (1 - weight) + draws[upper] * weight

        result[metric] = {
            "mean_difference": statistics.mean(differences),
            "ci95_low": percentile(0.025),
            "ci95_high": percentile(0.975),
        }
    return result


def evaluate(config: dict[str, Any]) -> dict[str, Any]:
    """Generate all test outputs, score them, and write reproducible result files."""
    output_root = Path(config["output_dir"])
    rows = read_jsonl(output_root / "prepared" / "test.jsonl")
    tokenizer = AutoTokenizer.from_pretrained(
        config["model_id"], revision=_model_revision(output_root)
    )
    bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    rouge = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=False)
    bert = BERTScorer(
        model_type="bert-base-multilingual-cased",
        num_layers=9,
        lang="id",
        idf=False,
        rescale_with_baseline=False,
        device="cuda",
    )
    variants = ["full_lora", "static_lora", "router_lora", "router_only"]
    records_by_id: dict[str, dict[str, Any]] = {
        row["id"]: {
            "id": row["id"],
            "reference": row["reference"],
            "predictions": {},
            "scores": {},
            "timings": {},
        }
        for row in rows
    }
    bert_truncations = {variant: 0 for variant in variants}
    for variant in variants:
        model, route, router, beta = _load_variant(config, output_root, variant)
        for warmup_index in range(config["warmup_runs"]):
            generate_one(
                model,
                tokenizer,
                rows[warmup_index % len(rows)],
                route,
                router,
                beta,
                config["max_new_tokens"],
            )
        for row in rows:
            repeats = [
                generate_one(
                    model,
                    tokenizer,
                    row,
                    route,
                    router,
                    beta,
                    config["max_new_tokens"],
                )
                for _ in range(config["timing_repeats"])
            ]
            selected = repeats[0]
            prediction = selected["summary"]
            rouge_scores = rouge.score(row["reference"], prediction)
            prediction_ids = bert_tokenizer.encode(prediction, add_special_tokens=False)
            reference_ids = bert_tokenizer.encode(
                row["reference"], add_special_tokens=False
            )
            if len(prediction_ids) > 510:
                prediction_ids = prediction_ids[:510]
                bert_truncations[variant] += 1
            if len(reference_ids) > 510:
                reference_ids = reference_ids[:510]
                bert_truncations[variant] += 1
            bert_prediction = bert_tokenizer.decode(
                prediction_ids, skip_special_tokens=True
            )
            bert_reference = bert_tokenizer.decode(
                reference_ids, skip_special_tokens=True
            )
            _, _, bert_f1 = bert.score([bert_prediction], [bert_reference])
            scores = {
                metric: float(rouge_scores[metric].fmeasure)
                for metric in ("rouge1", "rouge2", "rougeL")
            }
            scores["bertscore"] = float(bert_f1[0].item())
            record = records_by_id[row["id"]]
            record["predictions"][variant] = prediction
            record["scores"][variant] = scores
            record["timings"][variant] = {
                key: statistics.median(item[key] for item in repeats)
                for key in (
                    "total_seconds",
                    "prefill_seconds",
                    "decoding_seconds",
                    "output_tokens",
                    "active_layers",
                )
            }
            record.setdefault("routes", {})[variant] = selected["route_g2_to_g6"]
        del model, router
        torch.cuda.empty_cache()

    records = list(records_by_id.values())
    results_path = output_root / "evaluation"
    results_path.mkdir(parents=True, exist_ok=True)
    with (results_path / "per_article.jsonl").open(
        "w", encoding="utf-8"
    ) as result_file:
        for record in records:
            result_file.write(json.dumps(record, ensure_ascii=False) + "\n")

    summaries: dict[str, Any] = {}
    for variant in variants:
        summaries[variant] = {
            metric: statistics.mean(
                record["scores"][variant][metric] for record in records
            )
            for metric in METRICS
        }
        summaries[variant]["median_total_seconds"] = statistics.median(
            record["timings"][variant]["total_seconds"] for record in records
        )
        summaries[variant]["median_prefill_seconds"] = statistics.median(
            record["timings"][variant]["prefill_seconds"] for record in records
        )
        summaries[variant]["median_decoding_seconds"] = statistics.median(
            record["timings"][variant]["decoding_seconds"] for record in records
        )
        summaries[variant]["median_output_tokens"] = statistics.median(
            record["timings"][variant]["output_tokens"] for record in records
        )
    comparisons = {
        f"router_lora_vs_{comparator}": _bootstrap_differences(
            records,
            "router_lora",
            comparator,
            config["bootstrap_samples"],
            config["bootstrap_seed"],
        )
        for comparator in ("full_lora", "static_lora", "router_only")
    }
    result = {
        "run_mode": config.get("run_mode", "research"),
        "interpretation": (
            "Software smoke test only; do not use these scores or timings as research results."
            if config.get("run_mode") == "smoke_test_only"
            else "Research evaluation."
        ),
        "summaries": summaries,
        "paired_bootstrap": comparisons,
        "bertscore_truncated_texts": bert_truncations,
    }
    (results_path / "summary.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return result
