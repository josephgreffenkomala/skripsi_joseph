"""Offline CPU checks on an actual tiny randomly initialized Qwen3."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import torch
from transformers import Qwen3Config, Qwen3ForCausalLM

from experiment_proposal.modeling import SequenceRouter, decoder_layers, save_router
from routing_diagnostics.analysis import ROUTES, write_json
from routing_diagnostics.run import (
    _cached_router_audit,
    check_cache_precision,
    generate_tokens,
    implementation_checks,
    resolve_manifest_revision,
    sample_validation,
)


class ModelingTests(unittest.TestCase):
    """Validate cache handling and detect the source adaptive-prefill discrepancy."""

    @classmethod
    def setUpClass(cls) -> None:
        """Construct a CPU model with the real 28-layer Qwen forward loop."""
        torch.set_num_threads(1)
        torch.manual_seed(7)
        config = Qwen3Config(
            vocab_size=32,
            hidden_size=16,
            intermediate_size=32,
            num_hidden_layers=28,
            num_attention_heads=2,
            num_key_value_heads=1,
            head_dim=8,
            eos_token_id=31,
            pad_token_id=0,
            sliding_window=None,
        )
        cls.model = Qwen3ForCausalLM(config).eval()
        cls.row = {
            "id": "validation-example",
            "split": "validation",
            "prompt_ids": [1, 2, 3],
            "target_ids": [4, 31],
            "full_ids": [1, 2, 3, 4, 31],
            "article_mask": [0, 1, 1, 0, 0],
        }

    def test_cache_parity_for_every_fixed_route_and_layer_restoration(self) -> None:
        """All 32 patterns must decode consistently and restore original modules."""
        originals = list(decoder_layers(self.model))
        for route in ROUTES:
            with self.subTest(route=route):
                cached = generate_tokens(self.model, self.row, route, 3)
                uncached = generate_tokens(
                    self.model, self.row, route, 3, use_cache=False
                )
                self.assertEqual(cached, uncached)
                self.assertTrue(
                    all(
                        left is right
                        for left, right in zip(
                            originals, decoder_layers(self.model), strict=True
                        )
                    )
                )

    def test_execution_audit_detects_adaptive_prefill_issue(self) -> None:
        """The report must catch actual skipped-group execution, not just mask bits."""
        result = implementation_checks(self.model, self.row, 3)
        self.assertTrue(result["all_active_token_parity"])
        self.assertTrue(result["fixed_cached_vs_uncached_token_parity"])
        self.assertFalse(result["execution"]["fixed"]["skipped_g4_executed_in_prefill"])
        self.assertTrue(
            result["execution"]["adaptive"]["skipped_g4_executed_in_prefill"]
        )
        self.assertFalse(
            result["execution"]["adaptive"]["skipped_g4_executed_in_decode"]
        )
        self.assertFalse(result["adaptive_prefill_matches_design"])

    def test_generation_remains_greedy_with_qwen_sampling_defaults(self) -> None:
        """Model-specific sampling defaults must not override diagnostic settings."""
        original = self.model.generation_config.do_sample
        self.model.generation_config.do_sample = True
        try:
            ids = torch.tensor([self.row["prompt_ids"]], dtype=torch.long)
            with torch.inference_mode():
                expected = self.model.generate(
                    input_ids=ids,
                    attention_mask=torch.ones_like(ids),
                    do_sample=False,
                    num_beams=1,
                    max_new_tokens=3,
                )[0, ids.shape[1] :].tolist()
            self.assertEqual(generate_tokens(self.model, self.row, None, 3), expected)
            self.assertEqual(
                generate_tokens(self.model, self.row, (1, 1, 1, 1, 1), 3), expected
            )
            self.assertTrue(self.model.generation_config.do_sample)
        finally:
            self.model.generation_config.do_sample = original

    def test_cache_precision_retest_preserves_mismatch_and_restores_dtype(self) -> None:
        """A precision retest must retain the FP16 failure and restore model dtype."""
        model = torch.nn.Linear(2, 2).half()
        model.register_buffer(
            "rope_example", torch.tensor([1.1234567], dtype=torch.float32)
        )
        original = model.weight.detach().clone()
        original_buffer = model.rope_example.clone()
        with patch(
            "routing_diagnostics.run.generate_tokens",
            side_effect=[[1, 2], [1, 3], [4, 5], [4, 5]],
        ):
            result = check_cache_precision(model, {}, (0, 0, 1, 0, 0), 2)
        self.assertFalse(result["token_parity"])
        self.assertTrue(result["fp32_token_parity"])
        self.assertEqual(
            result["status"], "reduced_precision_mismatch_disappears_at_fp32"
        )
        self.assertEqual(model.weight.dtype, torch.float16)
        self.assertTrue(torch.equal(model.weight, original))
        self.assertEqual(model.rope_example.dtype, torch.float32)
        self.assertTrue(torch.equal(model.rope_example, original_buffer))
        with patch(
            "routing_diagnostics.run.generate_tokens", side_effect=[[1], [2], [3], [4]]
        ):
            result = check_cache_precision(model, {}, (0, 0, 1, 0, 0), 1)
        self.assertEqual(result["status"], "unresolved_mismatch")
        self.assertEqual(model.weight.dtype, torch.float16)

    def test_sampling_rejects_test_rows_and_misaligned_sequences(self) -> None:
        """The GPU diagnostic must not quietly consume a mislabeled test split."""
        import json

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "prepared").mkdir()
            path = root / "prepared" / "validation.jsonl"
            path.write_text(json.dumps(self.row) + "\n", encoding="utf-8")
            self.assertEqual(sample_validation(root, 1, 42)[0]["id"], self.row["id"])
            invalid = dict(self.row, split="test")
            path.write_text(json.dumps(invalid) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                sample_validation(root, 1, 42)
            invalid = dict(self.row, full_ids=[1, 2, 3, 31])
            path.write_text(json.dumps(invalid) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                sample_validation(root, 1, 42)

    def test_saved_router_audit_uses_original_logit_threshold(self) -> None:
        """CPU audit must reproduce logits >= 0, even near sigmoid rounding ties."""
        import json

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "source"
            output = Path(directory) / "output"
            router = SequenceRouter(16, 4)
            with torch.no_grad():
                for parameter in router.parameters():
                    parameter.zero_()
                router.network[-1].bias.fill_(-1e-8)
            save_router(router, root / "router", {"input_dim": 16, "hidden_dim": 4})
            write_json(root / "router_selection.json", {"selected_lambda": 0.1})
            (root / "features").mkdir()
            (root / "prepared").mkdir()
            for split in ("train", "validation"):
                (root / "prepared" / f"{split}.jsonl").write_text(
                    json.dumps({"id": f"{split}-1"}) + "\n", encoding="utf-8"
                )
                torch.save(torch.zeros(1, 16), root / "features" / f"{split}.pt")
                write_json(
                    root / "route_targets" / split / "targets_lambda_0.1.json",
                    [[0] * 5],
                )
            result = _cached_router_audit(root, output)
            self.assertEqual(
                result["splits"]["validation"]["exact_route_accuracy"], 1.0
            )
            self.assertTrue((output / "router_validation_paired.json").is_file())

    def test_revision_recovery_rejects_missing_and_ambiguous_snapshots(self) -> None:
        """Recover a legacy null revision only with unambiguous cache evidence."""
        manifest = {"model_revision": None, "config": {"model_id": "Qwen/Qwen3-0.6B"}}
        with (
            tempfile.TemporaryDirectory() as directory,
            patch.dict("os.environ", HF_HOME=directory),
        ):
            with self.assertRaises(ValueError):
                resolve_manifest_revision(manifest)
            root = Path(directory) / "hub/models--Qwen--Qwen3-0.6B/snapshots"
            first = root / ("a" * 40)
            first.mkdir(parents=True)
            (first / "config.json").write_text("{}", encoding="utf-8")
            (first / "model.safetensors").touch()
            result = resolve_manifest_revision(manifest)
            self.assertEqual(result["model_revision"], "a" * 40)
            self.assertEqual(
                result["revision_resolution"]["source"], "sole_complete_cached_snapshot"
            )
            self.assertIsNone(manifest["model_revision"])
            second = root / ("b" * 40)
            second.mkdir()
            (second / "config.json").write_text("{}", encoding="utf-8")
            (second / "model.safetensors").touch()
            with self.assertRaises(ValueError):
                resolve_manifest_revision(manifest)


if __name__ == "__main__":
    unittest.main()
