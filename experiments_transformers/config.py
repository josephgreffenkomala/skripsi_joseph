"""Frozen defaults for the native Transformers pilot."""

from __future__ import annotations

from dataclasses import dataclass

LABELS = ("positive", "neutral", "negative")
VERBALIZERS = {"A": "positive", "B": "neutral", "C": "negative"}
PILOT_ROW_INDICES = (0, 1, 2, 3, 4)

PROMPT_TEMPLATE = """Klasifikasikan sentimen ulasan Bahasa Indonesia berikut.
Jawab hanya dengan satu huruf: A untuk positive, B untuk neutral, atau C untuk negative.

Ulasan: {review}
Jawaban:"""


@dataclass(frozen=True)
class ExperimentConfig:
    """Configuration shared by baseline and quantized model runs."""

    model_name: str = "Qwen3-0.6B"
    temperature: float = 0.0
    top_p: float = 1.0
    seed: int = 42
    max_new_tokens: int = 1
    device: str = "cpu"
    torch_dtype: str = "auto"
