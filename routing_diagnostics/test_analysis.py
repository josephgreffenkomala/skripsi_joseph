"""Tests for diagnostic interpretations that could otherwise be misleading."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from routing_diagnostics.analysis import (
    METRICS,
    ROUTES,
    audit_saved,
    compare_routes,
    distribution,
    summarize_probe,
    write_json,
)


class AnalysisTests(unittest.TestCase):
    """Check route collapse, oracle comparisons, and incomplete artifacts."""

    def test_majority_baseline_exposes_collapsed_predictions(self) -> None:
        """High bit accuracy must not hide failure to learn varied targets."""
        majority, minority = (1, 1, 0, 1, 1), (1, 1, 1, 1, 1)
        result = compare_routes([majority] * 9 + [minority], [majority] * 10)
        self.assertEqual(result["targets"]["unique_routes"], 2)
        self.assertEqual(result["predictions"]["unique_routes"], 1)
        self.assertEqual(
            result["exact_route_accuracy"], result["constant_majority_accuracy"]
        )
        self.assertAlmostEqual(result["bit_accuracy"], 0.98)
        self.assertEqual(distribution([])["dominant_fraction"], None)

    def test_oracle_headroom_is_compared_at_equal_depth(self) -> None:
        """Opposite route preferences create headroom even at a fixed depth."""
        preferred = [(1, 1, 0, 0, 0), (0, 0, 0, 1, 1)]
        records = []
        for route_preference in preferred:
            records.append(
                {
                    "routes": [
                        {
                            "route": list(route),
                            "nll": 1.0 if route == route_preference else 2.0,
                            "scores": {
                                metric: 1.0 if route == route_preference else 0.0
                                for metric in METRICS
                            },
                        }
                        for route in ROUTES
                    ]
                }
            )
        summary = summarize_probe(records, 0.0)
        self.assertAlmostEqual(summary["objective_headroom"], 0.5)
        self.assertAlmostEqual(
            summary["quality"]["rougeL"]["reference_oracle_headroom"], 0.5
        )
        self.assertAlmostEqual(summary["per_depth"]["16"]["rougeL"]["headroom"], 0.5)
        self.assertEqual(summary["oracle_objective_routes"]["unique_routes"], 2)

    def test_uniform_preferences_have_zero_headroom(self) -> None:
        """A varied oracle must not be invented when all routes tie."""
        records = [
            {
                "routes": [
                    {"route": route, "nll": 1.0, "scores": dict.fromkeys(METRICS, 0.5)}
                    for route in ROUTES
                ]
            }
        ]
        result = summarize_probe(records, 0.0)
        self.assertEqual(result["objective_headroom"], 0.0)
        self.assertEqual(result["best_fixed_objective_route"], [0] * 5)
        self.assertEqual(result["quality"]["rouge1"]["reference_oracle_headroom"], 0.0)
        records[0]["routes"].pop()
        with self.assertRaises(ValueError):
            summarize_probe(records, 0.0)

    def test_audit_reports_missing_targets_instead_of_inferring_them(self) -> None:
        """Saved output predictions do not stand in for unavailable targets."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "evaluation").mkdir()
            (root / "evaluation" / "per_article.jsonl").write_text(
                '{"routes": {"router_lora": [1, 1, 0, 1, 1]}}\n', encoding="utf-8"
            )
            result = audit_saved(root)
            self.assertFalse(result["targets"])
            self.assertIn(
                "route_targets/train/targets_lambda_*.json", result["missing"]
            )
            self.assertEqual(
                result["saved_predictions"]["variants"]["router_lora"]["n"], 1
            )
            with self.assertRaises(ValueError):
                write_json(root / "bad.json", {"nll": float("nan")})


if __name__ == "__main__":
    unittest.main()
