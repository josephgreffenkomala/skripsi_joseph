# Menjalankan eksperimen di Modal

Pipeline ini menargetkan Modal GPU T4. Perintah di bawah hanya panduan; belum ada job Modal yang dijalankan. Jalankan dari root repositori.

## Persiapan satu kali

```bash
uv tool install modal==1.6.1
modal setup
modal volume create experiment-proposal-data
modal volume put experiment-proposal-data experiment/data/xlsum/indonesian /xlsum/indonesian/
```

Volume harus berisi `indonesian_train.jsonl`, `indonesian_val.jsonl`, dan `indonesian_test.jsonl` di `/xlsum/indonesian/`.

## Jalankan tahap berurutan

```bash
modal run -m experiment_proposal.modal_app --stage prepare
modal run -m experiment_proposal.modal_app --stage router
modal run -m experiment_proposal.modal_app --stage lora
modal run -m experiment_proposal.modal_app --stage evaluate
```

Setiap tahap menyimpan hasil di volume pada `/experiment_proposal/` dan dapat dijalankan ulang setelah menghentikan tahap sebelumnya. Data sampel default adalah 500/100/150; ubah `config.json` sebelum menjalankan tahap `prepare` jika ingin menyesuaikannya. Periksa biaya dan kuota workspace Modal sebelum memulai tahap komputasi.

Unduh hasil evaluasi ke direktori lokal:

```bash
modal volume get experiment-proposal-data /experiment_proposal/evaluation ./evaluation
```

Untuk memantau job, gunakan keluaran perintah `modal run` atau dashboard Modal. Dataset dan checkpoint tetap tersimpan pada volume bernama `experiment-proposal-data`.
