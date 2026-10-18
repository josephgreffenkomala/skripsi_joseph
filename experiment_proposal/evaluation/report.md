# Laporan Ringkas Hasil Eksperimen

- **Mode:** research
- **Jumlah artikel:** 150
- **Sumber:** `summary.json` dan `per_article.jsonl`

## Ringkasan utama

- **Router + LoRA** memiliki median waktu total 2.23 detik per artikel, 14.3% lebih cepat daripada model penuh + LoRA (2.60 detik).
- Dibanding static skipping + LoRA, skor router + LoRA lebih tinggi pada ROUGE-1, ROUGE-2, ROUGE-L, BERTScore; interval bootstrap untuk semua metrik dibanding pasangan ini mencakup 0.
- Varian router saja menghasilkan kualitas terendah pada empat metrik di tabel dan median keluaran lebih panjang; waktu perlu dibaca bersama panjang keluaran tersebut.

## Perbandingan metode

Skor kualitas adalah nilai F1 agregat yang tercantum pada `summary.json`. Waktu, jumlah token keluaran, dan layer aktif dihitung sebagai median dari data per artikel.

| Metode | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore | Median waktu (detik) | Prefill (detik) | Decoding (detik) | Token keluaran | Layer aktif |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Model penuh + LoRA | 0.260 | 0.075 | 0.203 | 0.737 | 2.60 | 0.08 | 2.51 | 42.00 | 28.00 |
| Static skipping + LoRA | 0.241 | 0.060 | 0.191 | 0.728 | 2.24 | 0.07 | 2.16 | 41.00 | 24.00 |
| Router + LoRA | 0.247 | 0.063 | 0.193 | 0.731 | 2.23 | 0.08 | 2.13 | 41.00 | 24.00 |
| Router saja (tanpa LoRA) | 0.217 | 0.059 | 0.159 | 0.705 | 2.60 | 0.04 | 2.56 | 93.50 | 24.00 |

## Perbandingan bootstrap berpasangan

Angka menunjukkan selisih rata-rata skor **router + LoRA dikurangi metode pembanding**, diikuti interval kepercayaan 95%. Nilai positif berarti skor router lebih tinggi. Interval yang mencakup 0 belum menunjukkan perbedaan yang jelas pada data ini.

| Pasangan | ROUGE-1 | ROUGE-2 | ROUGE-L | BERTScore |
|---|---:|---:|---:|---:|
| Router + LoRA − Model penuh + LoRA | -0.013 [-0.031, +0.004] (mencakup 0) | -0.012 [-0.023, -0.001] (tidak mencakup 0) | -0.009 [-0.023, +0.005] (mencakup 0) | -0.006 [-0.015, +0.002] (mencakup 0) |
| Router + LoRA − Static skipping + LoRA | +0.006 [-0.011, +0.023] (mencakup 0) | +0.003 [-0.008, +0.014] (mencakup 0) | +0.003 [-0.012, +0.018] (mencakup 0) | +0.004 [-0.006, +0.014] (mencakup 0) |
| Router + LoRA − Router saja (tanpa LoRA) | +0.030 [+0.010, +0.049] (tidak mencakup 0) | +0.004 [-0.008, +0.016] (mencakup 0) | +0.035 [+0.019, +0.050] (tidak mencakup 0) | +0.026 [+0.018, +0.034] (tidak mencakup 0) |

## Catatan evaluasi

Jumlah teks yang dipotong untuk perhitungan BERTScore: Model penuh + LoRA 0, Static skipping + LoRA 0, Router + LoRA 0, Router saja (tanpa LoRA) 0.

- Hasil ini merangkum artikel yang ada di file; hasil tidak otomatis berlaku untuk data atau lingkungan eksekusi lain.
- Skor metrik kemiripan terhadap ringkasan acuan tidak dengan sendirinya membuktikan faktualitas atau kualitas menyeluruh.
- Selisih waktu adalah deskripsi median pada data ini. Interval bootstrap yang tersedia menguji selisih skor kualitas, bukan variasi waktu atau variasi antar-seed.
