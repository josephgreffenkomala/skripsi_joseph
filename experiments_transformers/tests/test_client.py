"""Tests for native pilot parsing without loading a model."""

from __future__ import annotations

import unittest

from experiments_transformers.client import Prediction


class TransformersPilotTest(unittest.TestCase):
    def test_prediction_dataclass_keeps_label_and_scores(self) -> None:
        prediction = Prediction("positive", "A", {"positive": -0.1}, {})
        self.assertEqual(prediction.label, "positive")
        self.assertEqual(prediction.scores["positive"], -0.1)


if __name__ == "__main__":
    unittest.main()
