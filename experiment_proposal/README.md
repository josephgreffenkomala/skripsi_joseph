# Menjalankan eksperimen di Modal

Pipeline menyiapkan data di Modal CPU dan menjalankan komputasi model di GPU T4. Perintah di bawah adalah panduan; belum ada job Modal yang dijalankan. Jalankan dari root repositori.

## Persiapan satu kali

```bash
uv tool install modal==1.6.1
modal setup
modal volume create experiment-proposal-data
modal volume put experiment-proposal-data experiment/data/xlsum/indonesian /xlsum/indonesian/
```

Volume harus berisi `indonesian_train.jsonl`, `indonesian_val.jsonl`, dan `indonesian_test.jsonl` di `/xlsum/indonesian/`.

## Smoke test alur kode

Mulai dengan subset 5/2/2. Profil ini hanya memeriksa bahwa preprocessing, routing, LoRA, inferensi, metrik, dan penyimpanan hasil dapat berjalan. Profil ini membaca paling banyak 100 baris train dan 50 baris dari tiap split lain agar persiapan data juga cepat. Skor, route, dan waktu smoke test tidak mewakili evaluasi penelitian dan tidak boleh dikutip sebagai hasil.

```bash
modal run -m experiment_proposal.modal_app --stage prepare --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage router --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage lora --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage evaluate --config-path experiment_proposal/smoke_config.json
```

Hasil smoke test tersimpan terpisah di `/experiment_proposal_smoke/`. Jalankan tahapan sesuai urutan. Periksa biaya dan kuota workspace sebelum memulai tahap komputasi.

## Jalankan eksperimen utama

Setelah memeriksa alur smoke test, gunakan profil utama 500/100/150 berikut dengan perintah tahap yang sama:

```bash
modal run -m experiment_proposal.modal_app --stage prepare --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage router --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage lora --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage evaluate --config-path experiment_proposal/config.json
```

Unduh hasil evaluasi ke direktori lokal:

```bash
modal volume get experiment-proposal-data /experiment_proposal_smoke/evaluation ./evaluation-smoke
```

Ganti path remote dengan `/experiment_proposal/evaluation` untuk mengunduh hasil eksperimen utama. Untuk memantau job, gunakan keluaran `modal run` atau dashboard Modal. Dataset dan checkpoint berada di volume `experiment-proposal-data`.
