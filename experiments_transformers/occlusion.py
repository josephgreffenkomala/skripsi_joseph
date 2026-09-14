"""Word occlusion for native Transformers inference."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .client import Prediction, TransformersClient
from .config import PROMPT_TEMPLATE


@dataclass(frozen=True)
class OcclusionResult:
    """Sensitivity result for one removed word."""

    position: int
    word: str
    score_delta: float
    occluded_prediction: str | None
    occluded_scores: dict[str, float]


def split_words(review: str) -> list[str]:
    """Split review into whitespace-delimited units."""
    return re.findall(r"\S+", review)


def target_score(prediction: Prediction, target_label: str | None) -> float:
    """Return the target label score."""
    if target_label is None:
        return float("nan")
    return prediction.scores.get(target_label, float("nan"))


def run_occlusion(
    client: TransformersClient,
    review: str,
    baseline: Prediction,
    *,
    seed: int,
    max_new_tokens: int,
) -> list[OcclusionResult]:
    """Run leave-one-out word occlusion against a fixed baseline target."""
    words = split_words(review)
    baseline_score = target_score(baseline, baseline.label)
    results = []
    for position, word in enumerate(words):
        occluded_review = " ".join(words[:position] + words[position + 1 :])
        prediction = client.complete(
            PROMPT_TEMPLATE.format(review=occluded_review),
            seed=seed,
            max_new_tokens=max_new_tokens,
        )
        results.append(
            OcclusionResult(
                position,
                word,
                baseline_score - target_score(prediction, baseline.label),
                prediction.label,
                prediction.scores,
            )
        )
    return results
