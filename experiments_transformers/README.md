# Pilot Transformers

Pilot ini adalah salinan terpisah dari pilot `experiments/`: lima sampel SmSA, prediksi baseline dan model terkuantisasi, serta leave-one-out word occlusion. Runtime menggunakan model native Hugging Face melalui `AutoModelForCausalLM`, bukan GGUF/llama.cpp.

## Instalasi

```bash
pip install torch transformers
```

Model terkuantisasi harus berupa checkpoint yang dapat dimuat Transformers (misalnya checkpoint torchao/GPTQ/AWQ yang kompatibel dengan versi library yang digunakan). Untuk CPU konsumen, gunakan checkpoint yang memang mendukung backend CPU; opsi `--torch-dtype float32` adalah baseline paling aman.

Jika belum memiliki checkpoint terkuantisasi, gunakan `--dynamic-int8` untuk mengkuantisasi layer linear kondisi kedua secara dinamis saat runtime:

```bash
  --baseline-model /path/to/Qwen3-0.6B \
  --quantized-model /path/to/Qwen3-0.6B \
  --dynamic-int8
```

## Menjalankan pilot

```bash
python3 -m experiments_transformers.pilot \
  --dataset "$PWD/experiments/data/smsa_test_preprocess.tsv" \
  --baseline-model /path/to/Qwen3-0.6B \
  --quantized-model /path/to/Qwen3-0.6B-quantized \
  --torch-dtype float32 \
  --output-dir experiments_transformers/results/pilot
```

Output sama dengan pilot lama dan tidak menimpa `experiments/results/pilot`. Skor sensitivitas berasal dari log-probabilitas token pertama untuk A/B/C. Pastikan tokenizer, prompt, seed, device, dan versi Transformers dicatat; peak RSS yang dicatat adalah proses Python yang memuat model.
