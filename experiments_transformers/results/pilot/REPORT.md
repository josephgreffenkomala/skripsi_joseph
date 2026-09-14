# Pilot Transformers: Qwen3-0.6B

Tanggal run: 2026-09-14  
Runtime: Hugging Face Transformers 5.17.0 + PyTorch 2.14.0+cpu  
Dataset: `experiments/data/smsa_test_preprocess.tsv`  
Sampel: SmSA baris 0–4  
Perangkat: CPU, `torch_dtype=float32`, `max_new_tokens=1`, seed 42

## Kondisi

- **Baseline:** native checkpoint `/home/joseph/llama-models/Qwen3-0.6B`.
- **Quantized:** checkpoint yang sama, dengan dynamic INT8 pada layer linear saat runtime (`--dynamic-int8`). Ini adalah pembanding pilot untuk native CPU; bukan checkpoint GGUF.

## Hasil prediksi

| Kondisi | Prediksi valid | Benar | Waktu rata-rata per prediksi |
|---|---:|---:|---:|
| Baseline | 5/5 | 4/5 | 45,38 detik |
| Dynamic INT8 | 4/5 | 0/5 | 23,94 detik |

Semua lima sampel berlabel `negative`. Baseline memprediksi empat sampel dengan benar, sedangkan dynamic INT8 menghasilkan empat prediksi `positive` dan satu output kosong. Hasil ini hanya pilot kecil dan belum cukup untuk menyimpulkan degradasi kualitas umum.

## Occlusion

Tersedia 480 baris word occlusion, yaitu 240 perturbasi per kondisi. Heatmap tersedia pada lima file `heatmap-row-*.svg`.

## Reproduksi

```bash
/tmp/skripsi-transformers-venv/bin/python -m experiments_transformers.pilot \
  --dataset experiments/data/smsa_test_preprocess.tsv \
  --baseline-model /home/joseph/llama-models/Qwen3-0.6B \
  --quantized-model /home/joseph/llama-models/Qwen3-0.6B \
  --torch-dtype float32 \
  --dynamic-int8 \
  --output-dir experiments_transformers/results/pilot
```

