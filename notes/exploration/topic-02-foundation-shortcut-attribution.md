---
cssclasses:
  - full-width
---
# Detail Topik 02: Foundation-vs-Supervised Shortcut Attribution

Date: 2026-08-21
Updated: 2026-09-03
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)
Status: Kandidat kuat secara akademik; belum final dipilih

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia**: Studi Empiris Shortcut Learning pada Foundation Model dan Supervised Model Menggunakan Attribution sebagai Diagnostic Tool
- **English**: An Empirical Study of Shortcut Learning in Foundation and Supervised Vision Models Using Attribution as a Diagnostic Tool

Alternatif yang menonjolkan protokol evaluasi:

- **Bahasa Indonesia**: Evaluasi Ketergantungan Shortcut pada Foundation Model dan Supervised Model melalui Perturbasi Terkontrol dan Analisis Attribution
- **English**: Evaluating Shortcut Reliance in Foundation and Supervised Models through Controlled Perturbations and Attribution Analysis

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Model visi komputer bisa terlihat akurat, tetapi sebenarnya mengambil keputusan dari pola yang salah, misalnya latar belakang, tekstur, watermark, atau warna tertentu. Pola sampingan seperti ini disebut shortcut. Topik ini membandingkan apakah model modern seperti CLIP dan DINOv2 lebih tahan terhadap shortcut dibanding model supervised seperti ResNet atau ViT biasa.

Attribution tidak diposisikan sebagai metode baru, melainkan sebagai alat diagnosis: saat prediksi berubah karena latar belakang ditukar atau cue palsu ditambahkan, peta attribution membantu melihat bagian gambar mana yang dipakai model.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

- **Kondisi Saat Ini (Existing State/Literature)**: Sudah ada banyak metode attribution untuk CLIP/VLM seperti CCI/COVAR, exCLIP, EZPC, OSP, dan Distance Explainer. Sudah ada juga benchmark shortcut seperti Whac-A-Mole.
- **Keterbatasan / Gap**: Catatan literatur menunjukkan belum ada kombinasi lengkap: controlled shortcut benchmark, foundation-vs-supervised sebagai axis utama, attribution diagnostic, dan domain umum.
- **Kontribusi Penelitian (Novelty Contribution)**: Topik ini tidak mengklaim metode XAI baru. Kontribusinya adalah studi empiris terkontrol yang membandingkan pretraining paradigm dan memakai attribution untuk menganalisis mengapa model lebih atau kurang shortcut-reliant.

| Fitur / Parameter | Penelitian Terdahulu | Penelitian Ini |
|---|---|---|
| Fokus attribution | Metode baru atau faithfulness CLIP | Attribution sebagai diagnostic tool |
| Model | CLIP variants atau supervised saja | CLIP/DINOv2 vs ResNet/ViT supervised |
| Shortcut benchmark | Ada, tetapi tidak selalu attribution/foundation axis | Controlled shortcut sebagai axis eksperimen utama |
| Domain | Banyak domain-specific | General-domain dengan perturbasi terkontrol |
| Kontribusi | Metode atau robustness umum | Perbandingan perilaku shortcut lintas pretraining paradigm |

## 4. Posisi dan Batasan Penelitian

- **Masalah Penelitian**: Akurasi agregat belum cukup untuk menunjukkan apakah foundation model dan supervised model memanfaatkan fitur objek yang relevan atau shortcut seperti latar belakang, tekstur, watermark, dan warna.
- **Pendekatan Penelitian**: Eksperimen komparatif menggunakan perturbasi shortcut terkontrol, performa per kelompok, perubahan prediksi, dan attribution sebagai alat diagnosis. Pipeline komputasi hanya digunakan untuk menjaga konsistensi dan reprodusibilitas eksperimen.
- **Batasan Penelitian**: Tidak mengembangkan metode attribution baru, tidak melatih model besar, serta berfokus pada inferensi model pre-trained dan benchmark perturbasi terkontrol.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi / Framework**: PyTorch, OpenCLIP, DINOv2, torchvision models, Captum/Grad-CAM, dataset publik seperti Waterbirds, UrbanCars, ImageNet-derived subset, atau CUB jika tersedia.
- **Metode / Algoritma / Arsitektur**: Counterfactual background/texture/watermark perturbation, attribution maps, deletion/insertion score, attribution agreement analysis, worst-group accuracy, shortcut sensitivity score.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

- **Metode Pengujian**: Bandingkan model pada citra original dan citra dengan shortcut terkontrol. Hitung perubahan prediksi, performa per grup, dan perubahan attribution map.
- **Metrik Evaluasi**: Accuracy, worst-group accuracy, shortcut sensitivity, prediction flip rate, attribution overlap/agreement, deletion/insertion score, robustness terhadap background swap atau cue palsu.

## 7. Pemetaan ke Bab Proposal dan Skripsi Ilmiah Akademik (Chapter Mapping)

- **Bab 1 Proposal**: Latar belakang shortcut learning, risiko akurasi yang menipu, tujuan membandingkan foundation dan supervised model.
- **Bab 2 Proposal**: CLIP attribution, DINOv2/foundation model, shortcut learning, Whac-A-Mole, COVAR, dan pembanding robustness.
- **Bab 3 Proposal**: Deskripsi data, desain perturbasi, model yang dibandingkan, metode attribution, kontrol eksperimen, metrik, dan rancangan analisis.
- **Bab 4 Proposal**: Jadwal penyiapan dataset, studi pendahuluan, inferensi model, penghitungan attribution, analisis, dan penulisan.
- **Bab 1 Skripsi**: Latar belakang, perumusan masalah, batasan penelitian, tujuan, dan manfaat penelitian.
- **Bab 2 Skripsi**: Tinjauan pustaka tentang shortcut learning, foundation model, supervised learning, attribution, dan evaluasi robustness.
- **Bab 3 Skripsi**: Metodologi yang mencakup data, pembentukan shortcut terkontrol, pemilihan model, variabel eksperimen, metrik, dan analisis statistik.
- **Bab 4 Skripsi**: Implementasi lingkungan dan instrumen eksperimen, preprocessing, inferensi, pembentukan perturbasi, dan penghitungan attribution.
- **Bab 5 Skripsi**: Hasil performa per kelompok, shortcut sensitivity, perubahan prediksi dan attribution, pembahasan terhadap studi terdahulu, serta keterbatasan.
- **Bab 6 Skripsi**: Simpulan yang menjawab perumusan masalah dan saran penelitian lanjutan.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: Cocok untuk pembimbing AI, Computer Vision, XAI, atau evaluasi model.
- **Ketersediaan data/infrastruktur**: Feasible dengan model pre-trained dan inference. Training besar tidak disarankan.
- **Risiko kegagalan**: Perbandingan model dengan paradigma pretraining berbeda dapat dipengaruhi arsitektur dan prosedur adaptasi; integrasi multi-model rumit; dataset tertentu sulit diakses; attribution CLIP/DINOv2 membutuhkan desain yang hati-hati.
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
- **Pertanyaan ke Pengguna**: Dataset dan jenis shortcut apa yang paling relevan? Model serta metode attribution mana yang realistis dijalankan dengan sumber daya komputasi yang tersedia?
