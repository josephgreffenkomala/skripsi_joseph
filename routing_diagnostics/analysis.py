"""Dependency-free summaries of targets, predictions, and exhaustive route probes."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import statistics
from collections import Counter
from pathlib import Path
from typing import Any

Route = tuple[int, ...]
ROUTES = tuple(itertools.product((0, 1), repeat=5))
FULL_ROUTE = (1, 1, 1, 1, 1)
METRICS = ("rouge1", "rouge2", "rougeL")


def read_json(path: Path) -> Any:
    """Read a UTF-8 JSON artifact."""
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read nonempty JSONL records with line-numbered errors."""
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON in {path}:{number}") from error
    return rows


def write_json(path: Path, value: Any) -> None:
    """Write an artifact while rejecting nonfinite numeric results."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def as_route(values: Any) -> Route:
    """Validate the five binary group decisions."""
    route = tuple(values)
    if len(route) != 5 or any(bit not in (0, 1) for bit in route):
        raise ValueError(f"Expected five binary route decisions, got {values!r}")
    return route


def route_key(route: Route) -> str:
    """Return a stable key for a route."""
    return "".join(str(bit) for bit in as_route(route))


def distribution(routes: list[Route]) -> dict[str, Any]:
    """Describe route diversity without treating diversity as proof of usefulness."""
    counts = Counter(as_route(route) for route in routes)
    total = len(routes)
    ordered = sorted(counts, key=lambda route: (-counts[route], route))
    return {
        "n": total,
        "unique_routes": len(counts),
        "counts": {route_key(route): counts[route] for route in ordered},
        "dominant_fraction": max(counts.values()) / total if total else None,
        "entropy_bits": -sum(
            (count / total) * math.log2(count / total) for count in counts.values()
        ),
        "active_fraction_g2_to_g6": [
            statistics.mean(route[index] for route in routes) for index in range(5)
        ]
        if total
        else [],
    }


def compare_routes(targets: list[Route], predictions: list[Route]) -> dict[str, Any]:
    """Compare paired decisions and a constant majority-target baseline."""
    if not targets or len(targets) != len(predictions):
        raise ValueError(
            "Paired targets/predictions must be nonempty and equally sized."
        )
    targets = [as_route(route) for route in targets]
    predictions = [as_route(route) for route in predictions]
    majority = min(Counter(targets), key=lambda route: (-targets.count(route), route))
    return {
        "targets": distribution(targets),
        "predictions": distribution(predictions),
        "exact_route_accuracy": statistics.mean(
            target == prediction
            for target, prediction in zip(targets, predictions, strict=True)
        ),
        "bit_accuracy": statistics.mean(
            left == right
            for target, prediction in zip(targets, predictions, strict=True)
            for left, right in zip(target, prediction, strict=True)
        ),
        "constant_majority_route": list(majority),
        "constant_majority_accuracy": targets.count(majority) / len(targets),
    }


def summarize_probe(records: list[dict[str, Any]], penalty: float) -> dict[str, Any]:
    """Estimate in-sample route headroom, not achievable held-out router performance."""
    if not records:
        raise ValueError("Exhaustive probe is empty.")
    grids = []
    for record in records:
        grid = {as_route(item["route"]): item for item in record["routes"]}
        if len(record["routes"]) != 32 or set(grid) != set(ROUTES):
            raise ValueError(
                "Each probe article must contain all 32 routes exactly once."
            )
        for item in grid.values():
            if not math.isfinite(item["nll"]) or any(
                not math.isfinite(item["scores"][metric]) for metric in METRICS
            ):
                raise ValueError("Nonfinite loss or quality metric in probe.")
        grids.append(grid)

    def objective(item: dict[str, Any]) -> float:
        return item["nll"] + penalty * sum(item["route"]) / 5

    def tie(route: Route) -> tuple[int, Route]:
        return sum(route), route

    best_fixed = min(
        ROUTES,
        key=lambda route: (
            statistics.mean(objective(grid[route]) for grid in grids),
            tie(route),
        ),
    )
    oracle = [
        min(ROUTES, key=lambda route: (objective(grid[route]), tie(route)))
        for grid in grids
    ]
    result: dict[str, Any] = {
        "n": len(records),
        "lambda": penalty,
        "best_fixed_objective_route": list(best_fixed),
        "oracle_objective_routes": distribution(oracle),
        "mean_fixed_objective": statistics.mean(
            objective(grid[best_fixed]) for grid in grids
        ),
        "mean_oracle_objective": statistics.mean(
            objective(grid[route]) for grid, route in zip(grids, oracle, strict=True)
        ),
        "quality": {},
        "per_depth": {},
    }
    result["objective_headroom"] = (
        result["mean_fixed_objective"] - result["mean_oracle_objective"]
    )
    for metric in METRICS:
        fixed = max(
            ROUTES,
            key=lambda route: (
                statistics.mean(grid[route]["scores"][metric] for grid in grids),
                -sum(route),
                tuple(-bit for bit in route),
            ),
        )
        oracle_scores = [
            max(item["scores"][metric] for item in grid.values()) for grid in grids
        ]
        fixed_mean = statistics.mean(grid[fixed]["scores"][metric] for grid in grids)
        nll_route_mean = statistics.mean(
            grid[route]["scores"][metric]
            for grid, route in zip(grids, oracle, strict=True)
        )
        result["quality"][metric] = {
            "full_route_mean": statistics.mean(
                grid[FULL_ROUTE]["scores"][metric] for grid in grids
            ),
            "best_fixed_route": list(fixed),
            "best_fixed_mean": fixed_mean,
            "reference_oracle_mean": statistics.mean(oracle_scores),
            "reference_oracle_headroom": statistics.mean(oracle_scores) - fixed_mean,
            "nll_objective_oracle_mean": nll_route_mean,
        }
        # Compare equally deep routes too: a quality oracle could otherwise just use all layers.
        for active in range(6):
            candidates = [route for route in ROUTES if sum(route) == active]
            fixed_at_depth = max(
                candidates,
                key=lambda route: statistics.mean(
                    grid[route]["scores"][metric] for grid in grids
                ),
            )
            fixed_score = statistics.mean(
                grid[fixed_at_depth]["scores"][metric] for grid in grids
            )
            oracle_score = statistics.mean(
                max(grid[route]["scores"][metric] for route in candidates)
                for grid in grids
            )
            result["per_depth"].setdefault(str(8 + 4 * active), {})[metric] = {
                "best_fixed_route": list(fixed_at_depth),
                "best_fixed_mean": fixed_score,
                "reference_oracle_mean": oracle_score,
                "headroom": oracle_score - fixed_score,
            }
    return result


def audit_saved(
    source_root: Path, predictions_path: Path | None = None
) -> dict[str, Any]:
    """Inspect saved JSON artifacts locally without model dependencies or a GPU."""
    result: dict[str, Any] = {
        "source_root": str(source_root.resolve()),
        "targets": {},
        "missing": [],
    }
    for split in ("train", "validation"):
        paths = sorted(
            (source_root / "route_targets" / split).glob("targets_lambda_*.json")
        )
        if not paths:
            result["missing"].append(f"route_targets/{split}/targets_lambda_*.json")
        for path in paths:
            result["targets"][f"{split}/{path.name}"] = distribution(read_json(path))
    selection_path = source_root / "router_selection.json"
    if selection_path.is_file():
        result["router_selection"] = read_json(selection_path)
    else:
        result["missing"].append("router_selection.json")
    predictions_path = (
        predictions_path or source_root / "evaluation" / "per_article.jsonl"
    )
    if predictions_path.is_file():
        records = read_jsonl(predictions_path)
        variants = sorted({name for row in records for name in row.get("routes", {})})
        result["saved_predictions"] = {
            "path": str(predictions_path),
            "note": "Existing evaluation only; these predictions are not used to select new settings.",
            "variants": {
                variant: distribution(
                    [
                        row["routes"][variant]
                        for row in records
                        if variant in row.get("routes", {})
                    ]
                )
                for variant in variants
            },
        }
    else:
        result["missing"].append(str(predictions_path))
    return result


def main() -> None:
    """Write a local artifact audit without accessing Modal."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path("experiment_proposal"))
    parser.add_argument("--predictions", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("routing_diagnostics/outputs/saved_audit.json"),
    )
    args = parser.parse_args()
    result = audit_saved(args.source_root, args.predictions)
    write_json(args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
