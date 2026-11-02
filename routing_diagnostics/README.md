# Diagnosis sequence-level routing

Folder ini menguji tiga pertanyaan sebelum eksperimen diperbesar:

1. Apakah model penuh sebelum LoRA sudah dapat meringkas, dan bagaimana kualitasnya setelah LoRA?
2. Apakah target router beragam, dan apakah router mempelajarinya lebih baik daripada selalu memilih route mayoritas?
3. Apakah pemilihan route per artikel punya potensi dibanding satu route tetap?

Pipeline membaca data/checkpoint eksperimen lama dan menulis hasil ke direktori baru. Tidak ada pelatihan ulang. Data baru yang diproses hanya berasal dari `prepared/validation.jsonl`; train digunakan untuk membaca target dan fitur yang sudah disimpan. Distribusi test lama boleh dirangkum sebagai audit deskriptif, tetapi tidak dipakai untuk memilih konfigurasi baru.

## Jalankan dari root repositori

Pakai instalasi Modal dan dependensi yang sama dengan `experiment_proposal` (lihat `experiment_proposal/requirements.txt`). Semua perintah berikut dijalankan manual; membuat kode ini tidak menjalankan job GPU.

Audit JSON lokal, tanpa GPU, tanpa koneksi Modal, tanpa library model:

```bash
python3 -m routing_diagnostics.analysis
```

Audit lengkap target dan prediksi dari fitur tersimpan di volume, menggunakan CPU:

```bash
modal run -m routing_diagnostics.modal_app --stage audit
```

Perbandingan baseline, 20 artikel validasi:

```bash
modal run -m routing_diagnostics.modal_app --stage baseline
```

Seluruh 32 route pada 8 artikel validasi, memakai backbone asli tanpa LoRA:

```bash
modal run -m routing_diagnostics.modal_app --stage probe
```

Atau jalankan audit, baseline, dan probe dalam satu job:

```bash
modal run -m routing_diagnostics.modal_app --stage all
```

`all` memakai GPU juga untuk bagian audit. `audit` tersendiri memakai CPU saja. Default command tanpa `--stage` adalah audit CPU.

Ubah `source_root` di `routing_diagnostics/config.json` bila ingin membaca run lain, misalnya `/vol/experiment_proposal_smoke_5x`. Semua tahap memakai bobot/tokenizer pada revisi yang tercatat di `run_manifest.json`. Jika manifest lama tidak mencatat revisi, kode hanya memulihkannya bila cache berisi tepat satu snapshot lengkap model tersebut. Sumber pemulihan dan keterbatasan pencatatan historis disimpan dalam manifest diagnosis; manifest sumber tidak diubah. Cache yang kosong atau ambigu menyebabkan error, tanpa memakai revisi `main` secara diam-diam. Ukuran sampel dan batas generasi dapat diubah di file yang sama. Seed diagnosis terpisah dari seed eksperimen lama. Sampel baseline dan probe menggunakan urutan acak yang sama; dengan ukuran default, 8 artikel probe merupakan bagian dari 20 artikel baseline.

Setiap command Modal membuat direktori unik `/vol/routing_diagnostics/<run-id>_<stage>`, dan mencetak path-nya. Contoh pengunduhan (ganti `<run-id>_<stage>` dengan nama aktual):

```bash
modal volume get experiment-proposal-data /routing_diagnostics/<run-id>_<stage> ./routing_diagnostics/outputs
```

Pipeline tidak memindah/mengganti checkpoint sumber. Cache unduhan Hugging Face digunakan bersama di `/vol/hf_cache`. Contoh penggunaan volume mengikuti [dokumentasi Modal](https://modal.com/docs/guide/volumes).

## Hasil yang dibaca

| File | Pertanyaan yang dijawab |
| --- | --- |
| `saved_audit.json` | Distribusi target tiap lambda dan route keluaran run lama; file yang tidak tersedia ditandai. |
| `router_cached_summary.json` | Akurasi route/bit pada train dan validation dari fitur sebelum LoRA; pembanding konstan memakai route target mayoritas pada split yang sama, hanya untuk diagnosis. |
| `router_train_paired.json`, `router_validation_paired.json` | ID, target, prediksi, dan probabilitas untuk masing-masing artikel. |
| `implementation_checks.json` | Kesetaraan semua lapisan aktif, decoding cache/tanpa cache, eksekusi nyata kelompok yang dilewati, serta perbandingan loop generasi lama dengan `model.generate`. |
| `baseline_summary.json` | Rata-rata NLL dan F1 ROUGE-1/2/L model penuh sebelum/sesudah adapter full-LoRA. |
| `baseline_report.md`, `baseline_examples.json` | Artikel asli, acuan, dan kedua ringkasan untuk dibaca berdampingan. |
| `router_feature_drift.json` | Perubahan keputusan/probabilitas router saat G1 memakai adapter **adaptive-LoRA** yang sebenarnya. |
| `route_probe.json`, `route_probe_report.md` | NLL, F1 ROUGE, ringkasan, dan panjang keluaran pada semua 32 route, untuk tiap artikel. |
| `route_probe_summary.json` | Potensi selisih oracle per artikel vs route tetap; perbandingan juga pada jumlah lapisan aktif yang sama; regret pencarian greedy vs seluruh 32 route. |
| `manifest.json` | Konfigurasi diagnosis, konfigurasi sumber, revisi model, dan runtime. |

F1 ROUGE memakai implementasi yang sama dengan eksperimen sebelumnya (`rouge-score`, tanpa stemming). BERTScore tidak dihitung agar diagnosis kecil ini lebih ringan. NLL dan ROUGE tetap perlu dibaca bersama artikel asli; keduanya tidak menjamin faktualitas.

## Cara menafsirkan

- **Baseline sebelum dan sesudah LoRA sama-sama buruk:** kemampuan model, prompt, atau data perlu diperiksa sebelum mengatribusikan kegagalan ke routing.
- **Baseline memburuk setelah LoRA:** periksa pelatihan dan pasangan prompt/target; belum otomatis membuktikan LoRA penyebab tunggal.
- **Target hampir seragam:** prediksi seragam mungkin sesuai target. Periksa distribusi tiap lambda dan hasil probe sebelum memperbesar router.
- **Target beragam tetapi prediksi seragam:** periksa pembelajaran router, fitur, dan ketidakseimbangan label.
- **Oracle per artikel nyaris tidak lebih baik daripada satu route tetap:** potensi adaptivitas pada sampel/model/objective ini kecil.
- **Oracle lebih baik:** ada potensi yang belum tentu dapat diprediksi dari artikel saja. Oracle memakai ringkasan acuan sehingga **bukan metode inferensi** dan bukan hasil router yang dapat dicapai begitu saja.
- **Route terbaik menurut NLL tidak memberi ROUGE baik:** objective pembentukan target mungkin kurang selaras dengan kualitas generasi. Ini diagnosis, bukan kesimpulan dari satu artikel.

Route tetap dan oracle dipilih serta dinilai pada sampel validasi kecil yang sama. Selisih ini optimistis dan tidak membuktikan keunggulan pada test. Probe memakai **model tanpa LoRA**, sehingga tidak mengukur batas kemampuan setelah setiap route diadaptasi. Jangan membandingkan route sembarang memakai adapter full-LoRA seolah semua route sudah dilatih.

## Pemeriksaan implementasi yang penting

Pada pemeriksaan lokal menggunakan Qwen3 kecil acak dengan Transformers 4.51.3, `RouteController` lama memilih route setelah G1 tetapi kelompok yang dipilih untuk dilewati masih dijalankan pada **prefill pertama**. Loop decoder mengambil salinan daftar lapisan sebelum hook mengganti modul. Pemeriksaan baru menghitung pemanggilan lapisan pada prefill dan satu langkah decoding untuk mendeteksi kondisi ini pada model sebenarnya.

Temuan tersebut dicatat sebagai ketidaksesuaian rancangan, bukan otomatis penyebab ringkasan buruk. Baseline dan probe di folder ini menggunakan **route tetap yang dipasang sebelum forward**, sehingga diagnosisnya tidak mengandalkan routing adaptif yang bermasalah. Pipeline sumber belum diubah.

Pemeriksaan token dengan/tanpa KV cache dan semua lapisan aktif harus cocok sebelum probe dilanjutkan. Pada sweep 32 route, mismatch FP16 disimpan lalu diperiksa lagi menggunakan FP32. Jika mismatch menghilang pada FP32, probe dilanjutkan dengan status eksplisit `reduced_precision_mismatch_disappears_at_fp32`; jika tetap berbeda, tahap dihentikan. Bobot dan buffer dipulihkan sebelum pengukuran route berikutnya. Keluaran dan NLL tetap dihitung pada FP16, dan jumlah kasus tersebut dilaporkan dalam ringkasan. Mismatch loop generasi lama vs native dicatat untuk investigasi. Pengukuran waktu hanya satu kali per generasi, tidak mencakup protokol benchmark, dan **tidak dipakai untuk menyimpulkan speedup**.

## Verifikasi lokal

```bash
python3 -m unittest routing_diagnostics.test_analysis
experiment/.venv/bin/python -m unittest routing_diagnostics.test_modeling
ruff check routing_diagnostics
ruff format --check routing_diagnostics
```

Tes model memakai Qwen3 kecil berbobot acak pada CPU. Tidak mengunduh model, tidak menjalankan Modal, dan tidak mengukur kualitas ringkasan.
