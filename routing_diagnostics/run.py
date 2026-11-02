"""GPU diagnostics reusing prepared data, adapters, and routing implementation."""

from __future__ import annotations

import argparse
import gc
import json
import os
import random
import statistics
import sys
import time
from contextlib import nullcontext
from pathlib import Path
from typing import Any

import torch
from peft import PeftModel
from transformers import AutoTokenizer, GenerationConfig

from experiment_proposal.modeling import (
    RouteController,
    SequenceRouter,
    decoder_layers,
    load_model,
    load_router,
)
from experiment_proposal.train import (
    extract_features,
    greedy_route_target,
    sequence_nll,
)
from routing_diagnostics.analysis import (
    FULL_ROUTE,
    METRICS,
    ROUTES,
    Route,
    as_route,
    audit_saved,
    compare_routes,
    distribution,
    read_json,
    read_jsonl,
    summarize_probe,
    write_json,
)


def sample_validation(source: Path, count: int, seed: int) -> list[dict[str, Any]]:
    """Sample only validation data and reject inconsistent training sequences."""
    rows = read_jsonl(source / "prepared" / "validation.jsonl")
    if count < 1 or count > len(rows):
        raise ValueError(
            f"Requested {count} articles; validation contains {len(rows)}."
        )
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("Validation IDs must be unique.")
    selected = random.Random(seed).sample(rows, count)
    for row in selected:
        prompt, target = row["prompt_ids"], row["target_ids"]
        if row.get("split") != "validation":
            raise ValueError("Diagnostics accept only prepared validation articles.")
        if not prompt or not target or row["full_ids"] != prompt + target:
            raise ValueError(f"Inconsistent prompt/target sequence: {row['id']}")
        if len(row["article_mask"]) != len(row["full_ids"]) or not any(
            row["article_mask"][: len(prompt)]
        ):
            raise ValueError(f"Invalid article mask: {row['id']}")
    return selected


def generate_tokens(
    model: torch.nn.Module,
    row: dict[str, Any],
    route: Route | None,
    max_new_tokens: int,
    use_cache: bool = True,
) -> list[int]:
    """Generate deterministically with Transformers, with optional fixed skipping."""
    device = next(model.parameters()).device
    ids = torch.tensor([row["prompt_ids"]], dtype=torch.long, device=device)
    settings = GenerationConfig(
        do_sample=False,
        num_beams=1,
        max_new_tokens=max_new_tokens,
        eos_token_id=model.generation_config.eos_token_id,
        pad_token_id=(
            model.generation_config.pad_token_id
            if model.generation_config.pad_token_id is not None
            else model.config.eos_token_id
        ),
        bos_token_id=model.generation_config.bos_token_id,
        use_cache=use_cache,
    )
    context = (
        RouteController(model, None, fixed_route=route)
        if route is not None
        else nullcontext()
    )
    with context, torch.inference_mode():
        output = model.generate(
            input_ids=ids,
            attention_mask=torch.ones_like(ids),
            generation_config=settings,
            use_model_defaults=False,
        )
    return output[0, len(row["prompt_ids"]) :].tolist()


def check_cache_precision(
    model: torch.nn.Module,
    row: dict[str, Any],
    route: Route,
    tokens: int,
) -> dict[str, Any]:
    """Retest token mismatches at FP32 without hiding reduced-precision differences."""
    cached = generate_tokens(model, row, route, tokens)
    uncached = generate_tokens(model, row, route, tokens, use_cache=False)
    result = {
        "token_parity": cached == uncached,
        "cached": cached,
        "uncached": uncached,
        "fp32_token_parity": None,
        "status": "exact_match" if cached == uncached else "unresolved_mismatch",
    }
    if cached == uncached:
        return result
    dtype = next(model.parameters()).dtype
    # Qwen keeps RoPE buffers in FP32 even when its parameters are FP16.
    # model.half() alone would change those buffers and contaminate later routes.
    buffers = [
        (module, name, buffer.detach().clone())
        for module in model.modules()
        for name, buffer in module.named_buffers(recurse=False)
    ]
    try:
        model.float()
        fp32_cached = generate_tokens(model, row, route, tokens)
        fp32_uncached = generate_tokens(model, row, route, tokens, use_cache=False)
        result.update(
            fp32_token_parity=fp32_cached == fp32_uncached,
            fp32_cached=fp32_cached,
            fp32_uncached=fp32_uncached,
            status=(
                "reduced_precision_mismatch_disappears_at_fp32"
                if fp32_cached == fp32_uncached
                else "unresolved_mismatch"
            ),
        )
    finally:
        model.to(dtype=dtype)
        for module, name, buffer in buffers:
            setattr(module, name, buffer)
    return result


def implementation_checks(
    model: torch.nn.Module, row: dict[str, Any], tokens: int
) -> dict[str, Any]:
    """Check all-active parity, cache parity, and actual adaptive prefill execution."""
    device = next(model.parameters()).device
    native = generate_tokens(model, row, None, tokens)
    all_active = generate_tokens(model, row, FULL_ROUTE, tokens)
    fixed_route = (1, 1, 0, 1, 1)
    cached = generate_tokens(model, row, fixed_route, tokens)
    uncached = generate_tokens(model, row, fixed_route, tokens, use_cache=False)

    # A constant router makes the expected skipped group unambiguous.
    constant_router = SequenceRouter(model.config.hidden_size, 4).to(device)
    with torch.no_grad():
        for parameter in constant_router.parameters():
            parameter.zero_()
        constant_router.network[-1].bias.copy_(
            torch.tensor([1, 1, -1, 1, 1], device=device)
        )
    constant_router.eval()
    ids = torch.tensor([row["prompt_ids"]], dtype=torch.long, device=device)
    mask = torch.tensor(
        [row["article_mask"][: ids.shape[1]]], dtype=torch.bool, device=device
    )
    execution: dict[str, Any] = {}
    for mode in ("fixed", "adaptive"):
        calls = [0] * 28
        handles = []

        def counter(index: int) -> Any:
            def hook(_module: Any, _inputs: Any, _output: Any) -> None:
                calls[index] += 1

            return hook

        for index, layer in enumerate(decoder_layers(model)):
            handles.append(layer.register_forward_hook(counter(index)))
        try:
            controller = RouteController(
                model,
                mask if mode == "adaptive" else None,
                router=constant_router if mode == "adaptive" else None,
                fixed_route=fixed_route if mode == "fixed" else None,
            )
            with controller, torch.inference_mode():
                output = model(input_ids=ids, use_cache=True, return_dict=True)
                prefill_calls = list(calls)
                next_id = output.logits[:, -1].argmax(-1, keepdim=True)
                model(
                    input_ids=next_id,
                    past_key_values=output.past_key_values,
                    use_cache=True,
                )
                decode_calls = [
                    total - prefill
                    for total, prefill in zip(calls, prefill_calls, strict=True)
                ]
                execution[mode] = {
                    "selected_route": list(controller.selected_route),
                    "prefill_layer_calls": prefill_calls,
                    "one_decode_step_layer_calls": decode_calls,
                    "skipped_g4_executed_in_prefill": any(prefill_calls[12:16]),
                    "skipped_g4_executed_in_decode": any(decode_calls[12:16]),
                }
        finally:
            for handle in handles:
                handle.remove()
    return {
        "all_active_token_parity": native == all_active,
        "fixed_cached_vs_uncached_token_parity": cached == uncached,
        "fixed_cached_token_ids": cached,
        "fixed_uncached_token_ids": uncached,
        "execution": execution,
        "adaptive_prefill_matches_design": not execution["adaptive"][
            "skipped_g4_executed_in_prefill"
        ],
    }


def _score(scorer: Any, reference: str, prediction: str) -> dict[str, float]:
    return {
        metric: score.fmeasure
        for metric, score in scorer.score(reference, prediction).items()
    }


def _record(
    model: torch.nn.Module,
    tokenizer: Any,
    row: dict[str, Any],
    route: Route,
    limit: int,
    scorer: Any,
) -> dict[str, Any]:
    torch.cuda.synchronize()
    start = time.perf_counter()
    token_ids = generate_tokens(model, row, route, limit)
    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    prediction = tokenizer.decode(token_ids, skip_special_tokens=True).strip()
    return {
        "route": list(route),
        "active_layers": 8 + 4 * sum(route),
        "nll": sequence_nll(model, row, route, torch.device("cuda")),
        "prediction": prediction,
        "scores": _score(scorer, row["reference"], prediction),
        "output_tokens": len(token_ids),
        "hit_token_limit": len(token_ids) == limit
        and token_ids[-1]
        not in (
            [model.generation_config.eos_token_id]
            if isinstance(model.generation_config.eos_token_id, int)
            else model.generation_config.eos_token_id or []
        ),
        "seconds_single_run_not_benchmark": elapsed,
    }


def resolve_manifest_revision(manifest: dict[str, Any]) -> dict[str, Any]:
    """Pin a legacy run to its only complete cached snapshot, recording recovery."""
    if manifest.get("model_revision"):
        return dict(manifest, revision_resolution={"source": "original_manifest"})
    model_id = manifest["config"]["model_id"]
    cache = Path(os.environ.get("HF_HOME", str(Path.home() / ".cache/huggingface")))
    snapshots = cache / "hub" / ("models--" + model_id.replace("/", "--")) / "snapshots"
    candidates = sorted(
        path
        for path in snapshots.glob("*")
        if path.is_dir()
        and len(path.name) == 40
        and all(character in "0123456789abcdef" for character in path.name)
        and (path / "config.json").is_file()
        and any(item.is_file() for item in path.glob("*.safetensors"))
    )
    if len(candidates) != 1:
        raise ValueError(
            "Source manifest lacks model_revision and its cache does not contain "
            "exactly one complete snapshot; refusing to guess or use main."
        )
    snapshot = candidates[0]
    print(
        f"Recovering unrecorded model revision from sole cached snapshot: {snapshot.name}",
        flush=True,
    )
    return dict(
        manifest,
        model_revision=snapshot.name,
        revision_resolution={
            "source": "sole_complete_cached_snapshot",
            "snapshot_path": str(snapshot),
            "original_manifest_revision": None,
            "limitation": "Recovered from current cache; the historical manifest did not record this revision.",
        },
    )


def _preflight(config: dict[str, Any]) -> tuple[Path, Path, dict[str, Any]]:
    source = Path(config["source_root"]).resolve()
    output = Path(config["output_root"]).resolve()
    if (
        output == source
        or output.is_relative_to(source)
        or source.is_relative_to(output)
    ):
        raise ValueError(
            "Output and source directories must be separate, non-nested trees."
        )
    original_manifest = read_json(source / "run_manifest.json")
    manifest = resolve_manifest_revision(original_manifest)
    source_config = manifest["config"]
    if not 1 <= config["max_new_tokens"] <= source_config["max_new_tokens"]:
        raise ValueError(
            "Diagnostic output limit must fit the original generation limit."
        )
    if not 1 <= config["parity_tokens"] <= config["max_new_tokens"]:
        raise ValueError("parity_tokens must be between 1 and max_new_tokens.")
    sample_validation(
        source,
        max(config["baseline_articles"], config["route_articles"]),
        config["seed"],
    )
    selection = read_json(source / "lora_selection.json")
    checkpoint = Path(selection["variants"]["full_lora"]["selected"]["checkpoint"])
    if not checkpoint.is_dir():
        raise FileNotFoundError(f"Full LoRA checkpoint missing: {checkpoint}")
    # Fail rather than overwrite a prior diagnostic run.
    output.mkdir(parents=True, exist_ok=False)
    write_json(
        output / "manifest.json",
        {
            "diagnostic_config": config,
            "source_manifest": original_manifest,
            "resolved_model_revision": manifest["model_revision"],
            "revision_resolution": manifest["revision_resolution"],
            "full_lora_checkpoint": str(checkpoint),
            "python": sys.version,
            "torch": torch.__version__,
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
            "note": "Development diagnostics on validation; reference oracles are not deployable routers.",
        },
    )
    return source, output, manifest


def _cached_router_audit(source: Path, output: Path) -> dict[str, Any]:
    """Pair saved training/validation features with targets for the chosen lambda."""
    selected_lambda = read_json(source / "router_selection.json")["selected_lambda"]
    router = load_router(source / "router", torch.device("cpu"))
    result = {"selected_lambda": selected_lambda, "splits": {}}
    for split in ("train", "validation"):
        rows = read_jsonl(source / "prepared" / f"{split}.jsonl")
        features = torch.load(
            source / "features" / f"{split}.pt", map_location="cpu", weights_only=True
        )
        targets = read_json(
            source
            / "route_targets"
            / split
            / f"targets_lambda_{selected_lambda:g}.json"
        )
        if len(features) != len(rows) or len(targets) != len(rows):
            raise ValueError(
                f"Cached features/targets do not match prepared {split} rows."
            )
        with torch.inference_mode():
            logits = router(features.float())
            probabilities = logits.sigmoid()
            predictions = (logits >= 0).int().tolist()
        result["splits"][split] = compare_routes(targets, predictions)
        write_json(
            output / f"router_{split}_paired.json",
            [
                {
                    "id": row["id"],
                    "target": target,
                    "prediction": prediction,
                    "probabilities": probability,
                }
                for row, target, prediction, probability in zip(
                    rows, targets, predictions, probabilities.tolist(), strict=True
                )
            ],
        )
    write_json(output / "router_cached_summary.json", result)
    return result


def _baseline(
    source: Path, output: Path, manifest: dict[str, Any], config: dict[str, Any]
) -> dict[str, Any]:
    from rouge_score import rouge_scorer

    rows = sample_validation(source, config["baseline_articles"], config["seed"])
    source_config = manifest["config"]
    model = load_model(
        source_config["model_id"], revision=manifest["model_revision"]
    ).eval()
    tokenizer = AutoTokenizer.from_pretrained(
        source_config["model_id"], revision=manifest["model_revision"]
    )
    scorer = rouge_scorer.RougeScorer(list(METRICS), use_stemmer=False)
    checks = implementation_checks(model, rows[0], config["parity_tokens"])
    write_json(output / "implementation_checks.json", checks)
    if (
        not checks["all_active_token_parity"]
        or not checks["fixed_cached_vs_uncached_token_parity"]
    ):
        raise RuntimeError(
            "Fixed routing parity failed; inspect implementation_checks.json before scoring."
        )
    # Detect discrepancies with the manual inference loop used in the previous run.
    from experiment_proposal.evaluate import generate_one

    legacy = generate_one(
        model, tokenizer, rows[0], FULL_ROUTE, None, 0.0, config["parity_tokens"]
    )
    native = tokenizer.decode(
        generate_tokens(model, rows[0], FULL_ROUTE, config["parity_tokens"]),
        skip_special_tokens=True,
    ).strip()
    checks["original_manual_vs_native_summary_parity"] = legacy["summary"] == native
    checks["original_manual_summary"] = legacy["summary"]
    checks["native_summary"] = native
    write_json(output / "implementation_checks.json", checks)

    router = load_router(source / "router", torch.device("cuda"))
    before_features = extract_features(model, rows, torch.device("cuda"))
    records = [
        {
            "id": row["id"],
            "article": row["article"],
            "reference": row["reference"],
            "variants": {},
        }
        for row in rows
    ]
    for row, record in zip(rows, records, strict=True):
        record["variants"]["full_base"] = _record(
            model, tokenizer, row, FULL_ROUTE, config["max_new_tokens"], scorer
        )
        write_json(output / "baseline_examples.json", records)
        print(f"baseline base {row['id']}", flush=True)
    selection = read_json(source / "lora_selection.json")
    checkpoint = selection["variants"]["full_lora"]["selected"]["checkpoint"]
    model = PeftModel.from_pretrained(model, checkpoint, is_trainable=False).eval()
    for row, record in zip(rows, records, strict=True):
        record["variants"]["full_lora"] = _record(
            model, tokenizer, row, FULL_ROUTE, config["max_new_tokens"], scorer
        )
        write_json(output / "baseline_examples.json", records)
        print(f"baseline LoRA {row['id']}", flush=True)
    # Full-LoRA and adaptive-LoRA adapters differ: measure router feature drift using
    # the actual adaptive adapter, not the full baseline adapter.
    model = model.unload()
    adaptive_checkpoint = selection["variants"]["router_lora"]["selected"]["checkpoint"]
    model = PeftModel.from_pretrained(
        model, adaptive_checkpoint, is_trainable=False
    ).eval()
    after_features = extract_features(model, rows, torch.device("cuda"))
    with torch.inference_mode():
        before_logits = router(before_features.to("cuda")).cpu()
        after_logits = router(after_features.to("cuda")).cpu()
        before_probs = before_logits.sigmoid()
        after_probs = after_logits.sigmoid()
    before_routes, after_routes = (
        (before_logits >= 0).int().tolist(),
        (after_logits >= 0).int().tolist(),
    )
    drift = {
        "before_routes": distribution(before_routes),
        "after_adaptive_lora_routes": distribution(after_routes),
        "route_change_fraction": statistics.mean(
            a != b for a, b in zip(before_routes, after_routes, strict=True)
        ),
        "mean_absolute_probability_change": float(
            (before_probs - after_probs).abs().mean()
        ),
        "per_article": [
            {"id": row["id"], "before": before, "after": after}
            for row, before, after in zip(
                rows, before_probs.tolist(), after_probs.tolist(), strict=True
            )
        ],
    }
    write_json(output / "router_feature_drift.json", drift)
    summary = {
        variant: {
            "n": len(rows),
            "mean_nll": statistics.mean(
                record["variants"][variant]["nll"] for record in records
            ),
            "mean_scores": {
                metric: statistics.mean(
                    record["variants"][variant]["scores"][metric] for record in records
                )
                for metric in METRICS
            },
            "mean_output_tokens": statistics.mean(
                record["variants"][variant]["output_tokens"] for record in records
            ),
        }
        for variant in ("full_base", "full_lora")
    }
    summary["full_lora_minus_base"] = {
        "mean_nll_difference": summary["full_lora"]["mean_nll"]
        - summary["full_base"]["mean_nll"],
        "mean_score_differences": {
            metric: summary["full_lora"]["mean_scores"][metric]
            - summary["full_base"]["mean_scores"][metric]
            for metric in METRICS
        },
    }
    write_json(output / "baseline_summary.json", summary)
    lines = [
        "# Diagnosis baseline",
        "",
        "Data validasi; diagnosis pengembangan, bukan hasil akhir penelitian.",
        "",
        "| Model | NLL | ROUGE-1 | ROUGE-2 | ROUGE-L |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for variant in ("full_base", "full_lora"):
        values = summary[variant]
        scores = values["mean_scores"]
        lines.append(
            f"| {variant} | {values['mean_nll']:.4f} | {scores['rouge1']:.4f} | {scores['rouge2']:.4f} | {scores['rougeL']:.4f} |"
        )
    lines.append("")
    for record in records:
        lines.extend(
            [
                f"## {record['id']}",
                "",
                "### Artikel asli",
                "",
                record["article"],
                "",
                "### Acuan",
                "",
                record["reference"],
                "",
            ]
        )
        for variant, values in record["variants"].items():
            lines.extend(
                [
                    f"### {variant}",
                    "",
                    values["prediction"],
                    "",
                    f"ROUGE: {values['scores']}; NLL: {values['nll']:.4f}",
                    "",
                ]
            )
    (output / "baseline_report.md").write_text("\n".join(lines), encoding="utf-8")
    del model, router
    gc.collect()
    torch.cuda.empty_cache()
    return summary


def _probe(
    source: Path, output: Path, manifest: dict[str, Any], config: dict[str, Any]
) -> dict[str, Any]:
    from rouge_score import rouge_scorer

    rows = sample_validation(source, config["route_articles"], config["seed"])
    source_config = manifest["config"]
    model = load_model(
        source_config["model_id"], revision=manifest["model_revision"]
    ).eval()
    checks = implementation_checks(model, rows[0], config["parity_tokens"])
    write_json(output / "probe_implementation_checks.json", checks)
    if (
        not checks["all_active_token_parity"]
        or not checks["fixed_cached_vs_uncached_token_parity"]
    ):
        raise RuntimeError("Fixed routing parity failed before exhaustive probe.")
    tokenizer = AutoTokenizer.from_pretrained(
        source_config["model_id"], revision=manifest["model_revision"]
    )
    scorer = rouge_scorer.RougeScorer(list(METRICS), use_stemmer=False)
    penalty = float(read_json(source / "router_selection.json")["selected_lambda"])
    records = []
    for row in rows:
        record = {
            "id": row["id"],
            "article": row["article"],
            "reference": row["reference"],
            "routes": [],
        }
        for route in ROUTES:
            cache_check = check_cache_precision(
                model, row, route, config["parity_tokens"]
            )
            if cache_check["status"] == "unresolved_mismatch":
                write_json(
                    output / "failed_cache_check.json",
                    {
                        "id": row["id"],
                        "route": route,
                        **cache_check,
                    },
                )
                raise RuntimeError(
                    "Cached/uncached route outputs differ; inspect failed_cache_check.json."
                )
            values = _record(
                model, tokenizer, row, route, config["max_new_tokens"], scorer
            )
            values["cache_check"] = cache_check
            record["routes"].append(values)
            write_json(output / "probe_in_progress.json", record)
            print(f"probe {row['id']} route={route}", flush=True)
        # Reuse all 32 cached NLLs to reproduce the original local search exactly.
        nll_cache = {as_route(item["route"]): item["nll"] for item in record["routes"]}
        greedy = greedy_route_target(
            model, row, penalty, torch.device("cuda"), nll_cache
        )
        exact = min(
            ROUTES,
            key=lambda route: (
                nll_cache[route] + penalty * sum(route) / 5,
                sum(route),
                route,
            ),
        )
        record["greedy_target"] = list(greedy)
        record["exact_objective_target"] = list(exact)
        record["greedy_objective_regret"] = (
            nll_cache[greedy]
            + penalty * sum(greedy) / 5
            - (nll_cache[exact] + penalty * sum(exact) / 5)
        )
        records.append(record)
        write_json(output / "route_probe.json", records)
    summary = summarize_probe(records, penalty)
    summary["cache_precision_checks"] = {
        "total": sum(len(record["routes"]) for record in records),
        "fp16_mismatches_matching_at_fp32": sum(
            item["cache_check"]["status"]
            == "reduced_precision_mismatch_disappears_at_fp32"
            for record in records
            for item in record["routes"]
        ),
        "note": "Generations and NLL remain FP16; every token mismatch is retained and retested at FP32.",
    }
    summary["greedy_mean_objective_regret"] = statistics.mean(
        record["greedy_objective_regret"] for record in records
    )
    summary["greedy_targets"] = distribution(
        [record["greedy_target"] for record in records]
    )
    write_json(output / "route_probe_summary.json", summary)
    lines = [
        "# Diagnosis seluruh 32 route",
        "",
        "Backbone asli tanpa LoRA. Oracle menggunakan acuan validasi dan tidak dapat dipakai saat inferensi.",
        "",
        "Gain dihitung pada sampel yang sama; optimistis dan bukan bukti generalisasi router.",
        "",
        "## Ringkasan",
        "",
        "```json",
        json.dumps(summary, indent=2),
        "```",
        "",
    ]
    for record in records:
        lines.extend(
            [
                f"## {record['id']}",
                "",
                "### Artikel",
                "",
                record["article"],
                "",
                "### Acuan",
                "",
                record["reference"],
                "",
            ]
        )
        for item in record["routes"]:
            lines.extend(
                [
                    f"### Route {item['route']} ({item['active_layers']} lapisan)",
                    "",
                    item["prediction"],
                    "",
                    f"NLL {item['nll']:.4f}; ROUGE {item['scores']}",
                    "",
                ]
            )
    (output / "route_probe_report.md").write_text("\n".join(lines), encoding="utf-8")
    del model
    gc.collect()
    torch.cuda.empty_cache()
    return summary


def run(config: dict[str, Any], stage: str) -> dict[str, Any]:
    """Run requested diagnostics into a fresh directory without updating source files."""
    if stage not in {"audit", "baseline", "probe", "all"}:
        raise ValueError(f"Unknown stage {stage!r}")
    if stage != "audit" and not torch.cuda.is_available():
        raise RuntimeError(
            "GPU stages require CUDA; use routing_diagnostics.analysis for a local JSON audit."
        )
    source, output, manifest = _preflight(config)
    torch.manual_seed(config["seed"])
    result: dict[str, Any] = {"output_root": str(output)}
    if stage in {"audit", "all"}:
        write_json(output / "saved_audit.json", audit_saved(source))
        result["router"] = _cached_router_audit(source, output)
    if stage in {"baseline", "all"}:
        result["baseline"] = _baseline(source, output, manifest, config)
    if stage in {"probe", "all"}:
        result["probe"] = _probe(source, output, manifest, config)
    write_json(output / "summary.json", result)
    return result


def main() -> None:
    """Run on a local CUDA machine with already downloaded source artifacts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config", type=Path, default=Path("routing_diagnostics/config.json")
    )
    parser.add_argument("--stage", choices=("baseline", "probe", "all"), default="all")
    args = parser.parse_args()
    print(json.dumps(run(read_json(args.config), args.stage), indent=2))


if __name__ == "__main__":
    main()
