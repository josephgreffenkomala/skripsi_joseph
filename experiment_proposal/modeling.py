"""Qwen layer groups, router, and sequence-level conditional execution."""

from __future__ import annotations

from contextlib import AbstractContextManager
from pathlib import Path
from typing import Any

import torch
from torch import nn
from transformers import AutoModelForCausalLM


class SkippedLayer(nn.Module):
    """Identity layer returning the tuple layout expected by Qwen decoder blocks."""

    def forward(
        self,
        hidden_states: torch.Tensor,
        *args: Any,
        **kwargs: Any,
    ) -> tuple[torch.Tensor]:
        """Pass hidden states through unchanged."""
        return (hidden_states,)


class SequenceRouter(nn.Module):
    """MLP predicting active/skip logits for the five middle layer groups."""

    def __init__(self, input_dim: int = 1024, hidden_dim: int = 64) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 5),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        """Return five logits, one for each of groups G2 through G6."""
        return self.network(features)


def decoder_layers(model: nn.Module) -> nn.ModuleList:
    """Resolve the Qwen decoder layer list through optional PEFT wrappers."""
    base_model = model.get_base_model() if hasattr(model, "get_base_model") else model
    try:
        return base_model.model.layers
    except AttributeError as error:
        raise TypeError(
            "Expected a Qwen causal language model with model.layers."
        ) from error


def load_model(
    model_id: str,
    trainable: bool = False,
    revision: str | None = None,
) -> nn.Module:
    """Load Qwen in FP16 on the active CUDA device."""
    if not torch.cuda.is_available():
        raise RuntimeError("This experiment is configured for a Modal CUDA GPU.")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        revision=revision,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to("cuda")
    model.config.use_cache = not trainable
    if trainable:
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )
        model.enable_input_require_grads()
    return model


def freeze_backbone(model: nn.Module) -> None:
    """Disable gradients for all model parameters."""
    for parameter in model.parameters():
        parameter.requires_grad = False


def save_router(router: SequenceRouter, path: Path, metadata: dict[str, Any]) -> None:
    """Save router weights and their configuration metadata."""
    path.mkdir(parents=True, exist_ok=True)
    torch.save(router.cpu().state_dict(), path / "router.pt")
    import json

    (path / "router_config.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


def load_router(path: Path, device: torch.device) -> SequenceRouter:
    """Load a saved router onto the requested device."""
    import json

    config = json.loads((path / "router_config.json").read_text(encoding="utf-8"))
    router = SequenceRouter(config["input_dim"], config["hidden_dim"])
    weights = torch.load(path / "router.pt", map_location=device, weights_only=True)
    router.load_state_dict(weights)
    router.to(device).eval()
    return router


class RouteController(AbstractContextManager["RouteController"]):
    """Patch inactive groups and choose one route at the G1 output hook."""

    def __init__(
        self,
        model: nn.Module,
        article_mask: torch.Tensor | None,
        router: SequenceRouter | None = None,
        fixed_route: tuple[int, int, int, int, int] | None = None,
        beta: float = 0.0,
    ) -> None:
        self.model = model
        self.layers = decoder_layers(model)
        self.article_mask = article_mask
        self.router = router
        self.fixed_route = fixed_route
        self.beta = beta
        self.selected_route: tuple[int, int, int, int, int] | None = fixed_route
        self.probabilities: torch.Tensor | None = None
        self.regularizer: torch.Tensor | None = None
        self.originals: dict[int, nn.Module] = {}
        self.hook: Any = None

    def __enter__(self) -> "RouteController":
        if len(self.layers) != 28:
            raise ValueError(f"Expected 28 Qwen layers, found {len(self.layers)}.")
        self.originals = {index: self.layers[index] for index in range(4, 24)}
        if self.fixed_route is not None:
            self._apply_route(self.fixed_route)
        self.hook = self.layers[3].register_forward_hook(self._after_first_group)
        return self

    def __exit__(self, *_: object) -> None:
        if self.hook is not None:
            self.hook.remove()
        for index, layer in self.originals.items():
            self.layers[index] = layer

    def _apply_route(self, route: tuple[int, int, int, int, int]) -> None:
        for group_offset, active in enumerate(route):
            first_layer = 4 + group_offset * 4
            for index in range(first_layer, first_layer + 4):
                self.layers[index] = self.originals[index] if active else SkippedLayer()

    def _after_first_group(
        self,
        _module: nn.Module,
        _inputs: tuple[Any, ...],
        output: Any,
    ) -> Any:
        if self.selected_route is not None:
            return output
        if self.router is None or self.article_mask is None:
            raise RuntimeError(
                "Adaptive routing requires a router and article-token mask."
            )
        hidden = output[0]
        mask = self.article_mask[:, : hidden.shape[1]].to(
            hidden.device, dtype=hidden.dtype
        )
        denominator = mask.sum(dim=1, keepdim=True).clamp_min(1.0)
        features = (hidden * mask.unsqueeze(-1)).sum(dim=1) / denominator
        logits = self.router(features.float())
        probabilities = logits.sigmoid()
        hard = (logits >= 0).to(torch.int64).squeeze(0).tolist()
        self.probabilities = probabilities
        self.regularizer = self.beta * probabilities.sum()
        route_values = tuple(int(value) for value in hard)
        route: tuple[int, int, int, int, int] = (
            route_values[0],
            route_values[1],
            route_values[2],
            route_values[3],
            route_values[4],
        )
        self.selected_route = route
        self._apply_route(route)
        return output
