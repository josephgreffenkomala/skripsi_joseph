# Detail Topik 02: Foundation-vs-Supervised Shortcut Attribution

Date: 2026-08-21
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)
Status: Kandidat kuat secara akademik; belum final dipilih

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia**: Studi Empiris Shortcut Learning pada Foundation Model dan Supervised Model Menggunakan Attribution sebagai Diagnostic Tool
- **English**: An Empirical Study of Shortcut Learning in Foundation and Supervised Vision Models Using Attribution as a Diagnostic Tool

Alternatif jika ingin dibungkus sebagai produk:

- **Bahasa Indonesia**: Rancang Bangun Toolkit Audit Shortcut Learning untuk Model Visi Komputer Berbasis Attribution Diagnostic
- **English**: Designing a Shortcut Learning Audit Toolkit for Vision Models Using Attribution Diagnostics

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Model visi komputer bisa terlihat akurat, tetapi sebenarnya mengambil keputusan dari pola yang salah, misalnya latar belakang, tekstur, watermark, atau warna tertentu. Pola sampingan seperti ini disebut shortcut. Topik ini membandingkan apakah model modern seperti CLIP dan DINOv2 lebih tahan terhadap shortcut dibanding model supervised seperti ResNet atau ViT biasa.

Attribution tidak diposisikan sebagai metode baru, melainkan sebagai alat diagnosis: saat prediksi berubah karena latar belakang ditukar atau cue palsu ditambahkan, peta attribution membantu melihat bagian gambar mana yang dipakai model.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

- **Kondisi Saat Ini (Existing State/Literature)**: Sudah ada banyak metode attribution untuk CLIP/VLM seperti CCI/COVAR, exCLIP, EZPC, OSP, dan Distance Explainer. Sudah ada juga benchmark shortcut seperti Whac-A-Mole.
- **Keterbatasan / Gap**: Catatan literatur menunjukkan belum ada kombinasi lengkap: controlled shortcut benchmark, foundation-vs-supervised sebagai axis utama, attribution diagnostic, dan domain umum.
- **Kebaruan Solusi Ini (Novelty Contribution)**: Topik ini tidak mengklaim metode XAI baru. Kontribusinya adalah studi empiris terkontrol yang membandingkan pretraining paradigm dan memakai attribution untuk menjelaskan mengapa model lebih atau kurang shortcut-reliant.

| Fitur / Parameter | Solusi Conventional / Existing | Topik Ini (Proposed) |
|---|---|---|
| Fokus attribution | Metode baru atau faithfulness CLIP | Attribution sebagai diagnostic tool |
| Model | CLIP variants atau supervised saja | CLIP/DINOv2 vs ResNet/ViT supervised |
| Shortcut benchmark | Ada, tetapi tidak selalu attribution/foundation axis | Controlled shortcut sebagai axis eksperimen utama |
| Domain | Banyak domain-specific | General-domain dengan perturbasi terkontrol |
| Kontribusi | Metode atau robustness umum | Perbandingan perilaku shortcut lintas pretraining paradigm |

## 4. Perumusan Produk & Masalah (UGM Inovasi Produk)

- **Masalah Nyata**: Pengguna model vision sering hanya melihat akurasi, padahal model bisa mengambil shortcut yang tidak terlihat dari metrik biasa.
- **Solusi / Produk Inovatif**: Jika dipilih sebagai inovasi produk, bentuknya adalah toolkit audit yang menjalankan perturbasi shortcut dan menghasilkan attribution report. Jika dipilih sebagai skripsi ilmiah akademik, produk dapat dibatasi sebagai pipeline eksperimen reproducible.
- **Batasan Masalah/Produk**: Tidak membuat metode attribution baru; tidak training model besar; fokus pada inference model pre-trained dan benchmark perturbasi terkontrol.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi / Framework**: PyTorch, OpenCLIP, DINOv2, torchvision models, Captum/Grad-CAM, dataset publik seperti Waterbirds, UrbanCars, ImageNet-derived subset, atau CUB jika tersedia.
- **Metode / Algoritma / Arsitektur**: Counterfactual background/texture/watermark perturbation, attribution maps, deletion/insertion score, attribution agreement analysis, worst-group accuracy, shortcut sensitivity score.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

- **Metode Pengujian**: Bandingkan model pada citra original dan citra dengan shortcut terkontrol. Hitung perubahan prediksi, performa per grup, dan perubahan attribution map.
- **Metrik Evaluasi**: Accuracy, worst-group accuracy, shortcut sensitivity, prediction flip rate, attribution overlap/agreement, deletion/insertion score, robustness terhadap background swap atau cue palsu.

## 7. Pemetaan ke Bab Skripsi/Proposal (Chapter Mapping)

- **Bab 1 Proposal**: Latar belakang shortcut learning, risiko akurasi yang menipu, tujuan membandingkan foundation dan supervised model.
- **Bab 2 Proposal**: CLIP attribution, DINOv2/foundation model, shortcut learning, Whac-A-Mole, COVAR, dan pembanding robustness.
- **Bab 3 Proposal**: Desain dataset/perturbasi, model yang dibandingkan, metode attribution, metrik, dan skenario eksperimen.
- **Bab 4 Proposal**: Jadwal setup dataset, inference model, attribution pipeline, analisis, dan penulisan.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: Cocok untuk pembimbing AI, Computer Vision, XAI, atau evaluasi model.
- **Ketersediaan data/infrastruktur**: Feasible dengan model pre-trained dan inference. Training besar tidak disarankan.
- **Risiko kegagalan**: Scope terlalu akademik untuk jalur inovasi produk; integrasi multi-model rumit; dataset tertentu sulit diakses; attribution CLIP/DINOv2 butuh desain hati-hati.
- **Fallback plan**: Batasi ke dua model foundation dan dua model supervised, satu jenis shortcut utama, dan satu metode attribution utama.

## 9. Catatan Sumber & Literatur (Source Notes)

### 9.1 Sumber Utama (Core References)

| # | Judul | Penulis | Tahun | DOI/URL | Relevansi | BibTeX Key |
|---|---|---:|---|---|---|---|
| 1 | Cluster-based Concept Importance / COVAR | Agarwal, Karanam, Gandhi | 2025 | https://arxiv.org/abs/2511.12978 | Pembanding utama CLIP attribution + spurious correlation | agarwal2025covar |
| 2 | exCLIP | Moller et al. | 2024 | https://arxiv.org/abs/2408.14153 | Attribution CLIP dual encoder | moller2024exclip |
| 3 | Whac-A-Mole | Li et al. | 2023 | https://arxiv.org/abs/2212.04825 | Controlled multi-shortcut benchmark | li2023whacamole |
| 4 | Marine species foundation model comparison | Saleh & Azghadi | 2026 | https://arxiv.org/abs/2607.02559 | Pembanding foundation vs supervised domain-specific | saleh2026marine |
| 5 | EZPC | Ozdemir et al. | 2026 | https://arxiv.org/abs/2603.28211 | Concept explanation untuk CLIP zero-shot | ozdemir2026ezpc |

### 9.2 Gap yang Ditemukan dari Literatur

Gap yang defensible adalah kombinasi empat fitur: controlled shortcut benchmark, foundation-vs-supervised sebagai axis utama, attribution sebagai diagnostic, dan domain umum. Klaim yang tidak boleh dipakai: metode attribution baru untuk CLIP, benchmark shortcut CLIP pertama, atau shortcut learning pertama pada foundation model.

## 10. Penyerahan ke Penulisan LaTeX (Draft Handoff)

- **Target File**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, `template/proposal/chapters/bab3-metodologi.tex`
- **Kebutuhan Gambar/Diagram**: Diagram pipeline perturbasi, matriks model vs shortcut, contoh attribution map original vs counterfactual, tabel metrik.
- **Pertanyaan ke Pengguna**: Apakah jalur TA boleh ilmiah akademik, atau harus inovasi produk? Dataset apa yang boleh dipakai? Apakah ingin tetap membawa aplikasi/toolkit kecil?
