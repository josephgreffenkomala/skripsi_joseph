"""Dataset loading, filtering, and deterministic subset preparation."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from transformers import PreTrainedTokenizerBase

SPLITS = ("train", "validation", "test")
DATA_FILES = {
    "train": "indonesian_train.jsonl",
    "validation": "indonesian_val.jsonl",
    "test": "indonesian_test.jsonl",
}
DEDUP_PRIORITY = ("test", "validation", "train")


def read_jsonl(path: Path, max_rows: int | None = None) -> list[dict[str, Any]]:
    """Read a JSON Lines file and reject malformed rows with file context."""
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as data_file:
        for line_number, line in enumerate(data_file, start=1):
            if max_rows is not None and len(rows) >= max_rows:
                break
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid JSON at {path}:{line_number}") from error
            rows.append(row)
    return rows


def _prompt_text(instruction: str, article: str) -> str:
    return f"{instruction}{article}"


def article_token_mask(
    tokenizer: PreTrainedTokenizerBase,
    instruction: str,
    article: str,
    prompt_length: int,
) -> list[int]:
    """Mark prompt tokens whose character offsets overlap the article text."""
    chat_text = tokenizer.apply_chat_template(
        [{"role": "user", "content": _prompt_text(instruction, article)}],
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    article_start = chat_text.rfind(article)
    if article_start < 0:
        raise ValueError("Could not locate article text in the rendered Qwen prompt.")
    article_end = article_start + len(article)
    encoded = tokenizer(
        chat_text,
        add_special_tokens=False,
        return_offsets_mapping=True,
    )
    offsets = encoded["offset_mapping"]
    if len(offsets) != prompt_length:
        raise ValueError("Prompt token IDs and offset mapping have different lengths.")
    return [int(start < article_end and end > article_start) for start, end in offsets]


def _encode_row(
    tokenizer: PreTrainedTokenizerBase,
    instruction: str,
    row: dict[str, Any],
    split: str,
    row_index: int,
    max_input_tokens: int,
    max_target_tokens: int,
    max_context_tokens: int,
) -> tuple[dict[str, Any] | None, str | None]:
    article = str(row.get("text", "")).strip()
    summary = str(row.get("summary", "")).strip()
    if not article or not summary:
        return None, "empty"

    prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": _prompt_text(instruction, article)}],
        tokenize=True,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    full = tokenizer.apply_chat_template(
        [
            {"role": "user", "content": _prompt_text(instruction, article)},
            {"role": "assistant", "content": summary},
        ],
        tokenize=True,
        add_generation_prompt=False,
        enable_thinking=False,
    )
    if full[: len(prompt)] != prompt:
        raise ValueError("Chat prompt is not a prefix of the teacher-forcing sequence.")

    target = full[len(prompt) :]
    if len(prompt) > max_input_tokens:
        return None, "article_too_long"
    if len(target) > max_target_tokens:
        return None, "summary_too_long"
    if len(full) > max_context_tokens:
        return None, "context_too_long"

    return (
        {
            "id": str(row.get("id", f"{split}-{row_index}")),
            "split": split,
            "row_index": row_index,
            "article": article,
            "reference": summary,
            "prompt_ids": prompt,
            "full_ids": full,
            "target_ids": target,
            "article_mask": article_token_mask(
                tokenizer, instruction, article, len(prompt)
            )
            + [0] * (len(full) - len(prompt)),
        },
        None,
    )


def prepare_dataset(
    tokenizer: PreTrainedTokenizerBase,
    dataset_dir: Path,
    output_dir: Path,
    counts: dict[str, int],
    seed: int,
    instruction: str,
    max_input_tokens: int,
    max_target_tokens: int,
    max_context_tokens: int,
    max_source_rows_per_split: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Filter all source splits, deduplicate, sample, and write JSONL artifacts."""
    accepted: dict[str, list[dict[str, Any]]] = {split: [] for split in SPLITS}
    rejected: dict[str, dict[str, int]] = {
        split: {
            "empty": 0,
            "article_too_long": 0,
            "summary_too_long": 0,
            "context_too_long": 0,
            "duplicate_within_split": 0,
            "duplicate_across_splits": 0,
        }
        for split in SPLITS
    }
    source_rows_scanned: dict[str, int] = {}

    for split in SPLITS:
        path = dataset_dir / DATA_FILES[split]
        row_limit = (
            max_source_rows_per_split.get(split)
            if max_source_rows_per_split is not None
            else None
        )
        source_rows = read_jsonl(path, max_rows=row_limit)
        source_rows_scanned[split] = len(source_rows)
        for row_index, row in enumerate(source_rows):
            prepared, reason = _encode_row(
                tokenizer,
                instruction,
                row,
                split,
                row_index,
                max_input_tokens,
                max_target_tokens,
                max_context_tokens,
            )
            if prepared is None:
                rejected[split][reason or "empty"] += 1
            else:
                accepted[split].append(prepared)

    seen_articles: dict[str, str] = {}
    for split in DEDUP_PRIORITY:
        split_seen: set[str] = set()
        unique: list[dict[str, Any]] = []
        for row in accepted[split]:
            article = row["article"]
            if article in split_seen:
                rejected[split]["duplicate_within_split"] += 1
                continue
            split_seen.add(article)
            previous_split = seen_articles.get(article)
            if previous_split is not None:
                rejected[split]["duplicate_across_splits"] += 1
                continue
            seen_articles[article] = split
            unique.append(row)
        accepted[split] = unique

    output_dir.mkdir(parents=True, exist_ok=True)
    selected: dict[str, list[dict[str, Any]]] = {}
    for split in SPLITS:
        requested = counts[split]
        pool = accepted[split]
        if len(pool) < requested:
            raise ValueError(
                f"Split {split} has {len(pool)} eligible rows; {requested} requested."
            )
        indices = sorted(random.Random(seed).sample(range(len(pool)), requested))
        selected[split] = [pool[index] for index in indices]
        target = output_dir / f"{split}.jsonl"
        with target.open("w", encoding="utf-8") as data_file:
            for row in selected[split]:
                data_file.write(json.dumps(row, ensure_ascii=False) + "\n")

    manifest = {
        "counts_requested": counts,
        "counts_selected": {split: len(rows) for split, rows in selected.items()},
        "source_rows_scanned": source_rows_scanned,
        "eligible_before_sampling": {
            split: len(rows) for split, rows in accepted.items()
        },
        "rejected": rejected,
        "sample_seed": seed,
        "selected_ids": {
            split: [row["id"] for row in rows] for split, rows in selected.items()
        },
    }
    (output_dir / "data_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest
