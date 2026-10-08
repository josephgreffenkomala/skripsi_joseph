"""Router target search, router training, and LoRA adaptation stages."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import torch
from peft import LoraConfig, TaskType, get_peft_model
from torch import nn

from experiment_proposal.data import read_jsonl
from experiment_proposal.modeling import (
    RouteController,
    SequenceRouter,
    decoder_layers,
    freeze_backbone,
    load_model,
    save_router,
)

Route = tuple[int, int, int, int, int]


class _StopAfterFirstGroup(Exception):
    """Internal signal to stop feature extraction after G1."""


def _device() -> torch.device:
    return torch.device("cuda")


def _model_revision(output_root: Path) -> str | None:
    manifest_path = output_root / "run_manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(
            "Run `prepare` first to resolve and record the model revision."
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return manifest.get("model_revision")


def _batch(
    row: dict[str, Any], device: torch.device, prompt_only: bool = False
) -> tuple[torch.Tensor, torch.Tensor]:
    ids = row["prompt_ids"] if prompt_only else row["full_ids"]
    input_ids = torch.tensor([ids], dtype=torch.long, device=device)
    mask = torch.tensor(
        [row["article_mask"][: len(ids)]], dtype=torch.bool, device=device
    )
    return input_ids, mask


def _labels(
    row: dict[str, Any], device: torch.device
) -> tuple[torch.Tensor, torch.Tensor]:
    input_ids = torch.tensor([row["full_ids"]], dtype=torch.long, device=device)
    label_values = [-100] * len(row["prompt_ids"]) + row["target_ids"]
    labels = torch.tensor([label_values], dtype=torch.long, device=device)
    return input_ids, labels


@torch.inference_mode()
def extract_features(
    model: nn.Module,
    rows: list[dict[str, Any]],
    device: torch.device,
) -> torch.Tensor:
    """Extract article-token means from hidden states immediately after G1."""
    features: list[torch.Tensor] = []
    model.eval()
    for row in rows:
        input_ids, article_mask = _batch(row, device, prompt_only=True)
        captured: dict[str, torch.Tensor] = {}

        def capture_g1(
            _module: nn.Module, _inputs: tuple[Any, ...], output: Any
        ) -> Any:
            captured["hidden"] = output[0]
            raise _StopAfterFirstGroup

        handle = decoder_layers(model)[3].register_forward_hook(capture_g1)
        try:
            with torch.inference_mode():
                model(input_ids=input_ids, use_cache=False, return_dict=True)
        except _StopAfterFirstGroup:
            pass
        finally:
            handle.remove()
        hidden = captured["hidden"].float()
        mask = article_mask[:, : hidden.shape[1]].to(hidden.dtype)
        features.append(
            (
                (hidden * mask.unsqueeze(-1)).sum(dim=1)
                / mask.sum(dim=1, keepdim=True).clamp_min(1)
            )
            .squeeze(0)
            .cpu()
        )
        del input_ids, article_mask, hidden
    return torch.stack(features)


@torch.inference_mode()
def sequence_nll(
    model: nn.Module,
    row: dict[str, Any],
    route: Route,
    device: torch.device,
) -> float:
    """Compute average teacher-forced NLL for one fixed layer route."""
    input_ids, labels = _labels(row, device)
    with RouteController(model, None, fixed_route=route):
        output = model(
            input_ids=input_ids, labels=labels, use_cache=False, return_dict=True
        )
    return float(output.loss.float().item())


def greedy_route_target(
    model: nn.Module,
    row: dict[str, Any],
    penalty: float,
    device: torch.device,
    nll_cache: dict[Route, float] | None = None,
) -> Route:
    """Greedily remove one active middle group at a time under the NLL objective."""
    current: Route = (1, 1, 1, 1, 1)
    cached_nll = nll_cache if nll_cache is not None else {}

    def objective(candidate: Route) -> float:
        if candidate not in cached_nll:
            cached_nll[candidate] = sequence_nll(model, row, candidate, device)
        return cached_nll[candidate] + penalty * sum(candidate) / 5

    current_score = objective(current)
    while True:
        candidates = []
        for group_index, active in enumerate(current):
            if active:
                candidate_values = list(current)
                candidate_values[group_index] = 0
                candidate = (
                    candidate_values[0],
                    candidate_values[1],
                    candidate_values[2],
                    candidate_values[3],
                    candidate_values[4],
                )
                candidates.append((objective(candidate), candidate))
        if not candidates:
            break
        best_score, best_route = min(candidates, key=lambda item: (item[0], item[1]))
        if best_score >= current_score:
            break
        current, current_score = best_route, best_score
    return current


def _make_targets(
    model: nn.Module,
    rows: list[dict[str, Any]],
    penalties: list[float],
    output_dir: Path,
    device: torch.device,
) -> dict[float, list[Route]]:
    """Create and cache greedy route targets for all requested penalties."""
    output_dir.mkdir(parents=True, exist_ok=True)
    targets: dict[float, list[Route]] = {}
    missing = [
        penalty
        for penalty in penalties
        if not (output_dir / f"targets_lambda_{penalty:g}.json").exists()
    ]
    for penalty in penalties:
        cache_path = output_dir / f"targets_lambda_{penalty:g}.json"
        if cache_path.exists():
            targets[penalty] = [
                tuple(route) for route in json.loads(cache_path.read_text())
            ]
        else:
            targets[penalty] = []
    if missing:
        row_caches: list[dict[Route, float]] = [{} for _ in rows]
        for penalty in missing:
            routes = [
                greedy_route_target(model, row, penalty, device, row_caches[index])
                for index, row in enumerate(rows)
            ]
            targets[penalty] = routes
            (output_dir / f"targets_lambda_{penalty:g}.json").write_text(
                json.dumps(routes) + "\n", encoding="utf-8"
            )
    return targets


def _router_epoch(
    router: SequenceRouter,
    features: torch.Tensor,
    targets: torch.Tensor,
    optimizer: torch.optim.Optimizer | None,
    device: torch.device,
) -> float:
    """Run one full router epoch and return mean binary cross-entropy."""
    training = optimizer is not None
    router.train(training)
    losses: list[float] = []
    for start in range(0, len(features), 32):
        batch_features = features[start : start + 32].to(device)
        batch_targets = targets[start : start + 32].to(device)
        with torch.set_grad_enabled(training):
            logits = router(batch_features)
            loss = nn.functional.binary_cross_entropy_with_logits(logits, batch_targets)
            if optimizer is not None:
                optimizer.zero_grad(set_to_none=True)
                loss.backward()
                optimizer.step()
        losses.append(float(loss.detach().item()))
    return sum(losses) / len(losses)


def train_router(config: dict[str, Any]) -> dict[str, Any]:
    """Generate target routes, train one router per lambda, and select on validation."""
    random.seed(config["router_seed"])
    torch.manual_seed(config["router_seed"])
    device = _device()
    output_root = Path(config["output_dir"])
    revision = _model_revision(output_root)
    prepared_dir = output_root / "prepared"
    train_rows = read_jsonl(prepared_dir / "train.jsonl")
    validation_rows = read_jsonl(prepared_dir / "validation.jsonl")
    model = load_model(config["model_id"], trainable=False, revision=revision)
    freeze_backbone(model)

    train_features = extract_features(model, train_rows, device)
    validation_features = extract_features(model, validation_rows, device)
    feature_dir = output_root / "features"
    feature_dir.mkdir(parents=True, exist_ok=True)
    torch.save(train_features, feature_dir / "train.pt")
    torch.save(validation_features, feature_dir / "validation.pt")

    penalties = config["route_lambdas"]
    targets_dir = output_root / "route_targets"
    train_targets = _make_targets(
        model, train_rows, penalties, targets_dir / "train", device
    )
    validation_targets = _make_targets(
        model, validation_rows, penalties, targets_dir / "validation", device
    )

    candidate_results: list[dict[str, Any]] = []
    for penalty in penalties:
        router = SequenceRouter(1024, config["router_hidden_dim"]).to(device)
        optimizer = torch.optim.AdamW(
            router.parameters(),
            lr=config["router_lr"],
            weight_decay=config["router_weight_decay"],
        )
        y_train = torch.tensor(train_targets[penalty], dtype=torch.float32)
        y_validation = torch.tensor(validation_targets[penalty], dtype=torch.float32)
        best_loss = float("inf")
        best_state: dict[str, torch.Tensor] | None = None
        stale_epochs = 0
        for epoch in range(config["router_max_epochs"]):
            _router_epoch(router, train_features, y_train, optimizer, device)
            validation_loss = _router_epoch(
                router, validation_features, y_validation, None, device
            )
            if validation_loss < best_loss:
                best_loss = validation_loss
                best_state = {
                    key: value.detach().cpu().clone()
                    for key, value in router.state_dict().items()
                }
                stale_epochs = 0
            else:
                stale_epochs += 1
            if stale_epochs >= config["router_patience"]:
                break
        if best_state is None:
            raise RuntimeError("Router training did not produce a checkpoint.")
        router.load_state_dict(best_state)
        router.eval()
        with torch.inference_mode():
            validation_routes = (router(validation_features.to(device)) >= 0).to(
                torch.int64
            )
        predicted_routes = [
            tuple(int(bit) for bit in row) for row in validation_routes.cpu().tolist()
        ]
        route_objectives = [
            sequence_nll(model, row, route, device) + penalty * sum(route) / 5
            for row, route in zip(validation_rows, predicted_routes, strict=True)
        ]
        validation_objective = sum(route_objectives) / len(route_objectives)
        candidate_path = output_root / "router_candidates" / f"lambda_{penalty:g}"
        save_router(
            router,
            candidate_path,
            {
                "input_dim": 1024,
                "hidden_dim": config["router_hidden_dim"],
                "lambda": penalty,
            },
        )
        candidate_results.append(
            {
                "lambda": penalty,
                "validation_bce": best_loss,
                "validation_route_objective": validation_objective,
                "checkpoint": str(candidate_path),
            }
        )
        del router, optimizer

    del model
    torch.cuda.empty_cache()
    selected = min(
        candidate_results,
        key=lambda item: (item["validation_route_objective"], item["lambda"]),
    )
    selected_path = Path(selected["checkpoint"])
    final_path = output_root / "router"
    final_path.mkdir(parents=True, exist_ok=True)
    for file in selected_path.iterdir():
        (final_path / file.name).write_bytes(file.read_bytes())
    result = {
        "selected_lambda": selected["lambda"],
        "candidates": candidate_results,
        "router_seed": config["router_seed"],
    }
    (output_root / "router_selection.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    return result


def _add_lora(model: nn.Module, config: dict[str, Any]) -> nn.Module:
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        inference_mode=False,
        r=config["lora_rank"],
        lora_alpha=config["lora_alpha"],
        lora_dropout=config["lora_dropout"],
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
    )
    return get_peft_model(model, lora_config)


def _loss_for_row(
    model: nn.Module,
    row: dict[str, Any],
    device: torch.device,
    route: Route | None,
    router: SequenceRouter | None,
    beta: float,
) -> torch.Tensor:
    input_ids, labels = _labels(row, device)
    article_mask = torch.tensor([row["article_mask"]], dtype=torch.bool, device=device)
    controller = RouteController(
        model,
        article_mask,
        router=router,
        fixed_route=route,
        beta=beta,
    )
    with controller:
        output = model(
            input_ids=input_ids, labels=labels, use_cache=False, return_dict=True
        )
        loss = output.loss.float()
        if controller.regularizer is not None:
            loss = loss + controller.regularizer.float()
    return loss


def _evaluate_lora(
    model: nn.Module,
    rows: list[dict[str, Any]],
    device: torch.device,
    route: Route | None,
    router: SequenceRouter | None,
    beta: float,
) -> float:
    model.eval()
    values: list[float] = []
    with torch.inference_mode():
        for row in rows:
            values.append(
                float(_loss_for_row(model, row, device, route, router, beta).item())
            )
    return sum(values) / len(values)


def _select_static_route(
    model: nn.Module,
    validation_rows: list[dict[str, Any]],
    penalty: float,
    device: torch.device,
) -> Route:
    """Select a fixed route by validation objective with proposal tie-breaks."""
    candidates: list[tuple[float, int, Route]] = []
    for bits in range(32):
        route = (
            (bits >> 0) & 1,
            (bits >> 1) & 1,
            (bits >> 2) & 1,
            (bits >> 3) & 1,
            (bits >> 4) & 1,
        )
        losses = [sequence_nll(model, row, route, device) for row in validation_rows]
        objective = sum(losses) / len(losses) + penalty * sum(route) / 5
        candidates.append((objective, sum(route), route))
    return min(candidates, key=lambda item: (item[0], item[1], item[2]))[2]


def train_lora_variants(config: dict[str, Any]) -> dict[str, Any]:
    """Train full, static, and router-adaptive LoRA variants; save validation choices."""
    random.seed(config["router_seed"])
    torch.manual_seed(config["router_seed"])
    device = _device()
    output_root = Path(config["output_dir"])
    revision = _model_revision(output_root)
    prepared_dir = output_root / "prepared"
    train_rows = read_jsonl(prepared_dir / "train.jsonl")
    validation_rows = read_jsonl(prepared_dir / "validation.jsonl")
    selection = json.loads((output_root / "router_selection.json").read_text())
    penalty = float(selection["selected_lambda"])
    router = SequenceRouter(1024, config["router_hidden_dim"]).to(device)
    router_config = json.loads(
        (output_root / "router" / "router_config.json").read_text()
    )
    router.load_state_dict(
        torch.load(
            output_root / "router" / "router.pt", map_location=device, weights_only=True
        )
    )
    router.eval()
    for parameter in router.parameters():
        parameter.requires_grad = False

    base_model = load_model(config["model_id"], trainable=False, revision=revision)
    static_route = _select_static_route(base_model, validation_rows, penalty, device)
    (output_root / "static_route.json").write_text(
        json.dumps({"route_g2_to_g6": static_route, "lambda": penalty}) + "\n",
        encoding="utf-8",
    )
    del base_model
    torch.cuda.empty_cache()

    variants: dict[str, dict[str, Any]] = {}
    route_options: dict[str, tuple[Route | None, SequenceRouter | None]] = {
        "full_lora": ((1, 1, 1, 1, 1), None),
        "static_lora": (static_route, None),
        "router_lora": (None, router),
    }
    for variant, (route, active_router) in route_options.items():
        beta_values = config["lora_beta_values"] if variant == "router_lora" else [0.0]
        beta_results: list[dict[str, Any]] = []
        for beta in beta_values:
            model = _add_lora(
                load_model(config["model_id"], trainable=True, revision=revision),
                config,
            )
            optimizer = torch.optim.AdamW(
                [
                    parameter
                    for parameter in model.parameters()
                    if parameter.requires_grad
                ],
                lr=config["lora_learning_rate"],
                weight_decay=config["lora_weight_decay"],
            )
            best_loss = float("inf")
            best_epoch = 0
            stale_epochs = 0
            best_dir = output_root / "lora_candidates" / variant / f"beta_{beta:g}"
            for epoch in range(config["lora_max_epochs"]):
                model.train()
                optimizer.zero_grad(set_to_none=True)
                for index, row in enumerate(train_rows, start=1):
                    loss = _loss_for_row(model, row, device, route, active_router, beta)
                    accumulation = config["gradient_accumulation_steps"]
                    window_start = ((index - 1) // accumulation) * accumulation
                    window_size = min(accumulation, len(train_rows) - window_start)
                    (loss / window_size).backward()
                    if index % config[
                        "gradient_accumulation_steps"
                    ] == 0 or index == len(train_rows):
                        torch.nn.utils.clip_grad_norm_(
                            [
                                parameter
                                for parameter in model.parameters()
                                if parameter.requires_grad
                            ],
                            max_norm=1.0,
                        )
                        optimizer.step()
                        optimizer.zero_grad(set_to_none=True)
                validation_loss = _evaluate_lora(
                    model, validation_rows, device, route, active_router, beta
                )
                if validation_loss < best_loss:
                    best_loss = validation_loss
                    best_epoch = epoch + 1
                    stale_epochs = 0
                    best_dir.mkdir(parents=True, exist_ok=True)
                    model.save_pretrained(best_dir)
                else:
                    stale_epochs += 1
                if stale_epochs >= config["lora_patience"]:
                    break
            beta_results.append(
                {
                    "beta": beta,
                    "validation_nll": best_loss,
                    "best_epoch": best_epoch,
                    "checkpoint": str(best_dir),
                }
            )
            del model, optimizer
            torch.cuda.empty_cache()

        chosen = min(
            beta_results, key=lambda item: (item["validation_nll"], item["beta"])
        )
        variants[variant] = {"candidates": beta_results, "selected": chosen}

    variants["router_only"] = {
        "uses_lora": False,
        "router": str(output_root / "router"),
    }
    result = {
        "static_route": static_route,
        "variants": variants,
        "router_config": router_config,
    }
    (output_root / "lora_selection.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    return result
