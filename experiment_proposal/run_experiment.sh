#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
CONFIG_PATH="${1:-experiment_proposal/config.json}"

if [[ "$CONFIG_PATH" != /* ]]; then
  CONFIG_PATH="$REPO_ROOT/$CONFIG_PATH"
fi

cd "$REPO_ROOT"

for stage in prepare router lora evaluate; do
  printf '\n== Modal stage: %s ==\n' "$stage"
  modal run -m experiment_proposal.modal_app \
    --stage "$stage" \
    --config-path "$CONFIG_PATH"
done

printf '\nAll stages completed. Results are in the Modal volume under the configured output directory.\n'
