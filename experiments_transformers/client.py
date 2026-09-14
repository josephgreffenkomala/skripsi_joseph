"""Small adapter for local Hugging Face Transformers causal language models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .config import LABELS, VERBALIZERS


@dataclass(frozen=True)
class Prediction:
    """Parsed prediction and first-token label log probabilities."""

    label: str | None
    generated_text: str
    scores: dict[str, float]
    raw_response: dict[str, Any]


class TransformersClient:
    """Load and run one local causal LM through Transformers."""

    def __init__(
        self,
        model_path: str,
        *,
        device: str = "cpu",
        torch_dtype: str = "auto",
        dynamic_int8: bool = False,
    ) -> None:
        try:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise RuntimeError(
                "Pilot Transformers membutuhkan torch dan transformers. "
                "Install dengan: pip install torch transformers"
            ) from exc

        self.torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path, trust_remote_code=True
        )
        dtype = self._resolve_dtype(torch_dtype)
        model_kwargs: dict[str, Any] = {"trust_remote_code": True}
        if dtype is not None:
            model_kwargs["torch_dtype"] = dtype
        self.model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)
        self.device = torch.device(device)
        if dynamic_int8:
            if self.device.type != "cpu":
                raise ValueError("dynamic_int8 hanya didukung pada CPU")
            self.model = torch.quantization.quantize_dynamic(
                self.model, {torch.nn.Linear}, dtype=torch.qint8
            )
        self.model.to(self.device)
        self.model.eval()

    def _resolve_dtype(self, value: str) -> Any:
        if value == "auto":
            return None
        if value == "float32":
            return self.torch.float32
        if value == "bfloat16":
            return self.torch.bfloat16
        raise ValueError("torch_dtype harus auto, float32, atau bfloat16")

    def complete(self, prompt: str, *, seed: int, max_new_tokens: int) -> Prediction:
        """Generate a deterministic answer and expose first-token logits."""
        self.torch.manual_seed(seed)
        encoded = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        input_length = encoded["input_ids"].shape[1]
        with self.torch.inference_mode():
            result = self.model.generate(
                **encoded,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                return_dict_in_generate=True,
                output_scores=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        generated_ids = result.sequences[0, input_length:]
        generated_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        label = VERBALIZERS.get(generated_text.strip()[:1].upper())
        scores = self._label_scores(result.scores[0] if result.scores else None)
        return Prediction(label, generated_text, scores, {"sequence": generated_text})

    def _label_scores(self, logits: Any) -> dict[str, float]:
        scores = {label: float("nan") for label in LABELS}
        if logits is None:
            return scores
        log_probs = self.torch.log_softmax(logits[0], dim=-1)
        for token, label in VERBALIZERS.items():
            token_ids = self.tokenizer.encode(token, add_special_tokens=False)
            if len(token_ids) == 1:
                scores[label] = float(log_probs[token_ids[0]].item())
        return scores
