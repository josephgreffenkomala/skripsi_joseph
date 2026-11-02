"""Modal entrypoints for CPU artifact audit and small T4 diagnostics."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

import modal

image = (
    modal.Image.debian_slim(python_version="3.12")
    .uv_pip_install(requirements=["experiment_proposal/requirements.txt"])
    .add_local_python_source("experiment_proposal", "routing_diagnostics")
)
app = modal.App("qwen3-routing-diagnostics", image=image)
volume = modal.Volume.from_name("experiment-proposal-data", create_if_missing=False)


def _execute(stage: str, config_text: str) -> dict[str, Any]:
    """Run a diagnosis and persist partial files even if a check fails."""
    os.environ["HF_HOME"] = "/vol/hf_cache"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    from routing_diagnostics.run import run

    try:
        return run(json.loads(config_text), stage)
    finally:
        volume.commit()


@app.function(cpu=2, memory=8192, timeout=1800, retries=0, volumes={"/vol": volume})
def audit_artifacts(config_text: str) -> dict[str, Any]:
    """Inspect cached feature predictions and targets without allocating a GPU."""
    return _execute("audit", config_text)


@app.function(
    gpu="T4", cpu=2, memory=16384, timeout=14400, retries=0, volumes={"/vol": volume}
)
def diagnose(stage: str, config_text: str) -> dict[str, Any]:
    """Generate baseline and/or 32-route validation examples."""
    return _execute(stage, config_text)


@app.local_entrypoint()
def main(
    stage: str = "audit", config_path: str = "routing_diagnostics/config.json"
) -> None:
    """Submit only the explicitly selected stage, defaulting to CPU audit."""
    if stage not in {"audit", "baseline", "probe", "all"}:
        raise ValueError("--stage must be audit, baseline, probe, or all.")
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    run_id = (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid4().hex[:8]
    )
    config["output_root"] = str(Path(config["output_root"]) / f"{run_id}_{stage}")
    text = json.dumps(config)
    result = (
        audit_artifacts.remote(text)
        if stage == "audit"
        else diagnose.remote(stage, text)
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
