"""Buat laporan Markdown dari summary.json dan per_article.jsonl."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median
from typing import Any

METHOD_LABELS = {
    "full_lora": "Model penuh + LoRA",
    "static_lora": "Static skipping + LoRA",
    "router_lora": "Router + LoRA",
    "router_only": "Router saja (tanpa LoRA)",
}
METRIC_LABELS = {
    "rouge1": "ROUGE-1",
    "rouge2": "ROUGE-2",
    "rougeL": "ROUGE-L",
    "bertscore": "BERTScore",
}


def read_json(path: Path) -> dict[str, Any]:
    """Baca objek JSON dari file."""
    with path.open(encoding="utf-8") as input_file:
        data = json.load(input_file)
    if not isinstance(data, dict):
        raise ValueError(f"{path} harus berisi objek JSON.")
    return data


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Baca setiap baris JSONL menjadi objek."""
    records = []
    with path.open(encoding="utf-8") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"JSON tidak valid pada {path}:{line_number}: {error}"
                ) from error
            if not isinstance(record, dict):
                raise ValueError(
                    f"Baris {line_number} pada {path} harus berupa objek JSON."
                )
            records.append(record)
    return records


def metric_value(summary: dict[str, Any], method: str, metric: str) -> float:
    """Ambil nilai metrik dan pastikan field tersedia."""
    return float(summary["summaries"][method][metric])


def format_ci(value: dict[str, Any]) -> str:
    """Format beda skor dan interval bootstrap 95%."""
    difference = float(value["mean_difference"])
    low = float(value["ci95_low"])
    high = float(value["ci95_high"])
    interpretation = "mencakup 0" if low <= 0 <= high else "tidak mencakup 0"
    return f"{difference:+.3f} [{low:+.3f}, {high:+.3f}] ({interpretation})"


def summarize_records(records: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """Hitung median waktu, token keluaran, dan layer aktif dari JSONL."""
    result: dict[str, dict[str, float]] = {}
    for method in METHOD_LABELS:
        method_records = [
            record for record in records if method in record.get("timings", {})
        ]
        if not method_records:
            continue
        timings = [record["timings"][method] for record in method_records]
        result[method] = {
            "total_seconds": median(float(item["total_seconds"]) for item in timings),
            "prefill_seconds": median(
                float(item["prefill_seconds"]) for item in timings
            ),
            "decoding_seconds": median(
                float(item["decoding_seconds"]) for item in timings
            ),
            "output_tokens": median(float(item["output_tokens"]) for item in timings),
            "active_layers": median(float(item["active_layers"]) for item in timings),
        }
    return result


def make_report(summary: dict[str, Any], records: list[dict[str, Any]]) -> str:
    """Susun laporan hasil eksperimen dalam Bahasa Indonesia."""
    timing_stats = summarize_records(records)
    methods = [
        method for method in METHOD_LABELS if method in summary.get("summaries", {})
    ]
    full_time = timing_stats.get("full_lora", {}).get("total_seconds")
    lines = [
        "# Laporan Ringkas Hasil Eksperimen",
        "",
        f"- **Mode:** {summary.get('run_mode', 'tidak dicantumkan')}",
        f"- **Jumlah artikel:** {len(records)}",
        "- **Sumber:** `summary.json` dan `per_article.jsonl`",
        "",
        "## Ringkasan utama",
        "",
    ]

    if "router_lora" in methods and full_time:
        router_time = timing_stats["router_lora"]["total_seconds"]
        saving = (full_time - router_time) / full_time * 100
        lines.append(
            f"- **Router + LoRA** memiliki median waktu total {router_time:.2f} detik per artikel, "
            f"{saving:.1f}% lebih cepat daripada model penuh + LoRA ({full_time:.2f} detik)."
        )
    if "router_lora" in methods and "static_lora" in methods:
        router = summary["summaries"]["router_lora"]
        static = summary["summaries"]["static_lora"]
        better_metrics = [
            METRIC_LABELS[metric]
            for metric in METRIC_LABELS
            if float(router[metric]) > float(static[metric])
        ]
        lines.append(
            "- Dibanding static skipping + LoRA, skor router + LoRA lebih tinggi pada "
            f"{', '.join(better_metrics) if better_metrics else 'tidak ada metrik'}; "
            "interval bootstrap untuk semua metrik dibanding pasangan ini mencakup 0."
        )
    if "router_only" in methods:
        lines.append(
            "- Varian router saja menghasilkan kualitas terendah pada empat metrik di tabel "
            "dan median keluaran lebih panjang; waktu perlu dibaca bersama panjang keluaran tersebut."
        )
    lines.extend(
        [
            "",
            "## Perbandingan metode",
            "",
            "Skor kualitas adalah nilai F1 agregat yang tercantum pada `summary.json`. Waktu, jumlah "
            "token keluaran, dan layer aktif dihitung sebagai median dari data per artikel.",
            "",
            "| Metode | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | Median waktu (detik) | Prefill (detik) | Decoding (detik) | Token keluaran | Layer aktif |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for method in methods:
        scores = summary["summaries"][method]
        timing = timing_stats.get(method, {})
        lines.append(
            "| "
            + " | ".join(
                [
                    METHOD_LABELS[method],
                    *(f"{float(scores[metric]):.3f}" for metric in METRIC_LABELS),
                    *(
                        f"{timing.get(key, float('nan')):.2f}"
                        for key in (
                            "total_seconds",
                            "prefill_seconds",
                            "decoding_seconds",
                            "output_tokens",
                            "active_layers",
                        )
                    ),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Perbandingan bootstrap berpasangan",
            "",
            "Angka menunjukkan selisih rata-rata skor **router + LoRA dikurangi metode pembanding**, "
            "diikuti interval kepercayaan 95%. Nilai positif berarti skor router lebih tinggi. "
            "Interval yang mencakup 0 belum menunjukkan perbedaan yang jelas pada data ini.",
            "",
            "| Pasangan | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore |",
            "|---|---:|---:|---:|---:|",
        ]
    )
    for comparison, values in summary.get("paired_bootstrap", {}).items():
        left, _, right = comparison.partition("_vs_")
        pair_label = (
            f"{METHOD_LABELS.get(left, left)} − {METHOD_LABELS.get(right, right)}"
        )
        lines.append(
            f"| {pair_label} | "
            + " | ".join(format_ci(values[metric]) for metric in METRIC_LABELS)
            + " |"
        )

    truncation = summary.get("bertscore_truncated_texts", {})
    if truncation:
        lines.extend(["", "## Catatan evaluasi", ""])
        lines.append(
            "Jumlah teks yang dipotong untuk perhitungan BERTScore: "
            + ", ".join(
                f"{METHOD_LABELS.get(method, method)} {count}"
                for method, count in truncation.items()
            )
            + "."
        )
    lines.extend(
        [
            "",
            "- Hasil ini merangkum artikel yang ada di file; hasil tidak otomatis berlaku untuk data atau "
            "lingkungan eksekusi lain.",
            "- Skor metrik kemiripan terhadap ringkasan acuan tidak dengan sendirinya membuktikan "
            "faktualitas atau kualitas menyeluruh.",
            "- Selisih waktu adalah deskripsi median pada data ini. Interval bootstrap yang tersedia "
            "menguji selisih skor kualitas, bukan variasi waktu atau variasi antar-seed.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """Baca input dan tulis laporan Markdown."""
    parser = argparse.ArgumentParser(
        description="Ekstrak summary JSON dan hasil per artikel JSONL menjadi report Markdown."
    )
    parser.add_argument("--summary", type=Path, default=Path("summary.json"))
    parser.add_argument("--per-article", type=Path, default=Path("per_article.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("report.md"))
    args = parser.parse_args()

    summary = read_json(args.summary)
    records = read_jsonl(args.per_article)
    if not records:
        raise ValueError(f"Tidak ada baris data pada {args.per_article}.")
    report = make_report(summary, records)
    args.output.write_text(report, encoding="utf-8")
    print(f"Laporan tersimpan: {args.output} ({len(records)} artikel)")


if __name__ == "__main__":
    main()
