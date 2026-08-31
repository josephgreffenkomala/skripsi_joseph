# Detail Topik 03: Toolkit Audit XAI Penyakit Tanaman

Date: 2026-08-21
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)
Status: Kandidat kuat untuk Skripsi Inovasi Produk

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia**: Pengembangan Toolkit Audit Explainable AI untuk Evaluasi Shortcut Learning pada Model Klasifikasi Penyakit Tanaman Berbasis Citra
- **English**: Developing an Explainable AI Audit Toolkit for Evaluating Shortcut Learning in Image-Based Plant Disease Classification Models

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Model deteksi penyakit tanaman bisa mendapat akurasi tinggi, tetapi belum tentu benar-benar melihat gejala penyakit pada daun. Bisa saja model terbantu oleh latar belakang yang bersih, pencahayaan tertentu, bayangan, atau pola dataset yang tidak relevan. Topik ini membuat alat audit yang menampilkan penjelasan visual dan menguji model dengan perubahan terkontrol, misalnya mengganti latar belakang atau mengubah brightness.

Produk akhirnya dapat berupa dashboard, toolkit Python, atau notebook pipeline yang menghasilkan laporan: prediksi model, heatmap, skor fokus ke daun, stabilitas penjelasan, dan indikasi shortcut learning.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

- **Kondisi Saat Ini (Existing State/Literature)**: XAI untuk penyakit tanaman sudah banyak. Amara et al. (2024) sudah menerapkan ACE pada InceptionV3 dan PlantVillage serta membahas bias latar belakang, bayangan, dan pencahayaan.
- **Keterbatasan / Gap**: Sekadar menerapkan Grad-CAM/ACE pada PlantVillage tidak lagi cukup baru. Peluang kebaruan ada pada toolkit audit interaktif, uji perturbasi kuantitatif, stability score, dan laporan evaluasi yang dapat dipakai ulang.
- **Kebaruan Solusi Ini (Novelty Contribution)**: Mengubah fokus dari "menjelaskan prediksi" menjadi "mengaudit apakah penjelasan dan prediksi stabil serta selaras dengan area/gejala yang relevan".

| Fitur / Parameter | Solusi Conventional / Existing | Topik Ini (Proposed) |
|---|---|---|
| Fokus | Heatmap/konsep untuk interpretasi | Audit shortcut dan robustness |
| Dataset | PlantVillage apa adanya | PlantVillage + perturbasi terkontrol / citra lapangan opsional |
| Output | Visualisasi XAI | Laporan audit dengan skor dan rekomendasi |
| Evaluasi | Akurasi + inspeksi visual | Focus ratio, deletion/insertion, stability terhadap perturbasi |
| Pengguna | Peneliti/model developer | Pengguna toolkit audit model visi pertanian |

## 4. Perumusan Produk & Masalah (UGM Inovasi Produk)

- **Masalah Nyata**: Model klasifikasi penyakit tanaman sulit dipercaya jika hanya dinilai dari akurasi, karena model dapat memakai shortcut visual yang tidak relevan.
- **Solusi / Produk Inovatif**: Toolkit audit XAI yang menerima model/dataset terbatas, menjalankan metode penjelasan, melakukan perturbasi, menghitung metrik audit, dan menghasilkan laporan.
- **Batasan Masalah/Produk**: Fokus pada klasifikasi citra daun, 3-5 kelas penyakit pada satu tanaman, model baseline ringan, metode XAI terbatas pada Grad-CAM/Grad-CAM++/Score-CAM, dan perturbasi terkontrol.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi / Framework**: PyTorch/TensorFlow, Grad-CAM, Score-CAM, PlantVillage, model ResNet/EfficientNet/MobileNet/ViT kecil, dashboard sederhana atau notebook reproducible.
- **Metode / Algoritma / Arsitektur**: Attribution map generation, leaf/background mask proxy, background swap, brightness/shadow perturbation, deletion/insertion, stability analysis.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

- **Metode Pengujian**: Latih atau gunakan model baseline, jalankan prediksi pada citra original dan citra perturbasi, bandingkan perubahan prediksi dan heatmap, lalu buat laporan audit.
- **Metrik Evaluasi**: Accuracy, precision, recall, F1-score, focus ratio pada area daun, deletion/insertion score, stability score, prediction flip rate, runtime laporan, dan usability sederhana jika berbentuk aplikasi.

## 7. Pemetaan ke Bab Skripsi/Proposal (Chapter Mapping)

- **Bab 1 Proposal**: Masalah kebutuhan model pertanian yang dapat diaudit, risiko shortcut learning, tujuan toolkit.
- **Bab 2 Proposal**: Deteksi penyakit tanaman, Grad-CAM/Score-CAM/ACE, shortcut learning, dan Amara et al. (2024) sebagai pembanding wajib.
- **Bab 3 Proposal**: Dataset, preprocessing, baseline model, rancangan toolkit, metode XAI, skenario perturbasi, dan metrik audit.
- **Bab 4 Proposal**: Jadwal implementasi baseline, toolkit, eksperimen, evaluasi, dan penulisan.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: Cocok untuk pembimbing Computer Vision, Machine Learning, XAI, atau sistem AI terapan.
- **Ketersediaan data/infrastruktur**: PlantVillage tersedia dan model ringan cukup untuk S1. Citra lapangan opsional dapat memperkuat, tetapi tidak wajib untuk versi awal.
- **Risiko kegagalan**: Jika hanya membuat heatmap, kebaruan lemah. Jika terlalu banyak metode XAI, scope membesar. Jika klaim agronomi terlalu jauh, validasi domain jadi lemah.
- **Fallback plan**: Fokus pada toolkit audit untuk satu tanaman dan 3-5 kelas; gunakan perturbasi terkontrol tanpa mengklaim diagnosis agronomi klinis/produksi.

## 9. Catatan Sumber & Literatur (Source Notes)

### 9.1 Sumber Utama (Core References)

| # | Judul | Penulis | Tahun | DOI/URL | Relevansi | BibTeX Key |
|---|---|---:|---|---|---|---|
| 1 | Grad-CAM: Visual Explanations From Deep Networks via Gradient-Based Localization | Selvaraju et al. | 2017 | https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html | Dasar metode heatmap visual | selvaraju2017gradcam |
| 2 | Interpretability Beyond Feature Attribution: TCAV | Kim et al. | 2018 | https://arxiv.org/abs/1711.11279 | Dasar konsep-level XAI | kim2018tcav |
| 3 | Explainability of Deep Learning-Based Plant Disease Classifiers Through Automated Concept Identification | Amara et al. | 2024 | https://arxiv.org/pdf/2412.07408 | Pembanding utama; ACE pada PlantVillage | amara2024plantxai |
| 4 | TensorFlow Datasets: plant_village | TensorFlow | - | https://www.tensorflow.org/datasets/catalog/plant_village | Dataset utama | tensorflowPlantVillage |
| 5 | Plant Production and Protection | FAO | - | https://www.fao.org/plant-production-protection/about/en | Latar belakang dampak penyakit/hama tanaman | faoPlantProtection |

### 9.2 Gap yang Ditemukan dari Literatur

Gap yang aman: bukan menerapkan ACE/Grad-CAM, tetapi membuat protokol dan perangkat audit dengan perturbasi, stability score, focus ratio, dan laporan. Klaim yang harus dihindari: "pertama menjelaskan model penyakit tanaman dengan XAI" atau "pertama menemukan bias background pada PlantVillage".

## 10. Penyerahan ke Penulisan LaTeX (Draft Handoff)

- **Target File**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, `template/proposal/chapters/bab3-metodologi.tex`
- **Kebutuhan Gambar/Diagram**: Diagram pipeline toolkit, contoh output dashboard, tabel skenario perturbasi, tabel perbandingan metode XAI, bagan alir metodologi.
- **Pertanyaan ke Pengguna**: Produk akhir ingin dashboard web, toolkit Python, atau notebook pipeline? Tanaman/kelas penyakit apa yang dipilih? Apakah ingin menambah citra lokal?
