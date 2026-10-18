# Menjalankan eksperimen di Modal

Pipeline menyiapkan data di Modal CPU dan menjalankan komputasi model di GPU T4. Jalankan perintah dari root repositori.

## Persiapan satu kali

```bash
uv tool install modal==1.6.1
modal setup
modal volume create experiment-proposal-data
```

Tahap `prepare` mengunduh arsip resmi XL-Sum Indonesia ke volume jika file sumber belum tersedia. Unduhan pertama memerlukan koneksi internet dan akan disimpan di volume untuk pemakaian berikutnya.

## Smoke test alur kode

Profil smoke saat ini menggunakan subset 100/30/40 (train/validation/test). Profil ini hanya memeriksa bahwa preprocessing, routing, LoRA, inferensi, metrik, dan penyimpanan hasil dapat berjalan. Persiapan data membaca paling banyak 1.500 baris train dan 500 baris dari tiap split lain; artikel dengan prompt di atas 1.024 token disaring tanpa pemotongan. Batas keluaran smoke adalah 128 token. Laporan Markdown menampilkan acuan dan keluaran tiap metode secara berdampingan. Skor, route, dan waktu smoke test tidak mewakili evaluasi penelitian dan tidak boleh dikutip sebagai hasil.

```bash
modal run -m experiment_proposal.modal_app --stage prepare --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage router --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage lora --config-path experiment_proposal/smoke_config.json
modal run -m experiment_proposal.modal_app --stage evaluate --config-path experiment_proposal/smoke_config.json
```

Hasil extended smoke tersimpan terpisah di `/experiment_proposal_smoke_5x/`. Jalankan tahapan sesuai urutan. Periksa biaya dan kuota workspace sebelum memulai tahap komputasi.

Unduh contoh ringkasan yang mudah dibaca setelah tahap evaluasi:

```bash
modal volume get experiment-proposal-data /experiment_proposal_smoke_5x/evaluation/smoke_report.md ./smoke_report.md
```

## Jalankan eksperimen utama

Profil utama menggunakan 500/100/150 sampel. Tahap `prepare` memindai seluruh split, membuang artikel jika prompt lengkap setelah format chat mencapai 1.024 token atau lebih, lalu mengambil sampel dari data yang lolos. Artikel tidak dipotong. Jumlah yang dibuang dan jumlah kandidat yang tersedia dicatat dalam `prepared/data_manifest.json`; tahap prepare berhenti dengan error jika kandidat tidak cukup untuk memenuhi jumlah sampel.

Gunakan profil utama berikut dengan perintah tahap yang sama:

```bash
modal run -m experiment_proposal.modal_app --stage prepare --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage router --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage lora --config-path experiment_proposal/config.json
modal run -m experiment_proposal.modal_app --stage evaluate --config-path experiment_proposal/config.json
```

Atau jalankan seluruh tahap secara berurutan dengan satu command:

```bash
./experiment_proposal/run_experiment.sh
```

Script berhenti jika suatu tahap gagal. Untuk memakai konfigurasi lain, berikan path config sebagai argumen, misalnya `./experiment_proposal/run_experiment.sh experiment_proposal/smoke_config.json`.

Unduh hasil evaluasi ke direktori lokal:

```bash
modal volume get experiment-proposal-data /experiment_proposal_smoke/evaluation ./evaluation-smoke
```

Ganti path remote dengan `/experiment_proposal/evaluation` untuk mengunduh hasil eksperimen utama. Untuk memantau job, gunakan keluaran `modal run` atau dashboard Modal. Dataset dan checkpoint berada di volume `experiment-proposal-data`.
