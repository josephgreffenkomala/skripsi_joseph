---
cssclasses:
  - full-width
---
# Detail Topik 04: Website Audit XAI untuk Model Klasifikasi Citra

Date: 2026-08-21
Catalog Reference: [`topic-catalog.md`](../topic-catalog.md)
Status: Kandidat produk; perlu scope ketat

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia**: Pengembangan Website Explainable AI untuk Audit Model Klasifikasi Citra Berbasis Peta Atribusi dan Uji Perturbasi
- **English**: Developing a Web-Based Explainable AI Audit Tool for Image Classification Models Using Attribution Maps and Perturbation Tests

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Ide ini membuat website sederhana untuk membantu pengguna mengevaluasi model klasifikasi citra. Pengguna mengunggah model dan citra atau dataset kecil, lalu sistem menampilkan prediksi, heatmap penjelasan, hasil uji perturbasi, dan laporan interpretabilitas.

Supaya tidak terlalu luas, website ini tidak mendukung semua jenis data dan semua framework. Fokusnya hanya klasifikasi citra dengan format model yang dibatasi, misalnya ONNX atau TorchScript, serta metode XAI yang terbatas.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

- **Kondisi Saat Ini (Existing State/Literature)**: Sudah ada tool besar seperti Captum, SHAP, LIME, InterpretML, Alibi, ExplainerDashboard, What-If Tool, dan Learning Interpretability Tool (LIT). Karena itu, "membuat XAI toolkit umum" bukan klaim yang kuat.
- **Keterbatasan / Gap**: Banyak tool bersifat library atau membutuhkan setup teknis. Peluang produk ada pada workflow web yang lebih mudah, laporan otomatis, uji stabilitas penjelasan, dan batasan format yang jelas.
- **Kebaruan Solusi Ini (Novelty Contribution)**: Produk difokuskan pada audit klasifikasi citra dengan attribution + perturbation report, bukan toolkit multi-modal.

| Fitur / Parameter | Solusi Conventional / Existing | Topik Ini (Proposed) |
|---|---|---|
| Cakupan | Banyak tool mendukung banyak modalitas/library | Fokus klasifikasi citra saja |
| Penggunaan | Sering perlu kode/notebook | Workflow web upload dan laporan |
| Output | Plot interpretasi terpisah | Laporan audit otomatis |
| Evaluasi | Penjelasan visual | Stabilitas prediksi dan heatmap terhadap perturbasi |
| Risiko novelty | Wrapper library | Produk audit dengan batasan dan evaluasi usability |

## 4. Perumusan Produk & Masalah (UGM Inovasi Produk)

- **Masalah Nyata**: Pengguna pemula sulit memakai library XAI karena perlu menulis kode, memahami preprocessing, dan merangkai visualisasi sendiri.
- **Solusi / Produk Inovatif**: Website audit XAI untuk klasifikasi citra yang menyediakan alur upload, prediksi, heatmap, perturbasi, dan laporan.
- **Batasan Masalah/Produk**: Hanya klasifikasi citra; model format dibatasi; dataset kecil; metode XAI terbatas; tidak mendukung text/tabular pada versi skripsi.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi / Framework**: Python, FastAPI/Streamlit, PyTorch/TorchScript atau ONNX Runtime, Grad-CAM, Integrated Gradients, Occlusion Sensitivity, SmoothGrad, report HTML/PDF.
- **Metode / Algoritma / Arsitektur**: Model upload validation, inference pipeline, attribution generation, perturbation testing, explanation stability scoring, report generation.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

- **Metode Pengujian**: Uji fungsional upload dan inferensi; uji pada 1-2 model/dataset contoh; ukur waktu proses; evaluasi stabilitas heatmap; lakukan usability test kecil jika memungkinkan.
- **Metrik Evaluasi**: Success rate fitur, waktu inferensi dan laporan, compatibility rate format model, prediction stability, heatmap stability, task completion time pengguna, dan skor usability sederhana.

## 7. Pemetaan ke Bab Skripsi/Proposal (Chapter Mapping)

- **Bab 1 Proposal**: Masalah aksesibilitas XAI untuk pengguna non-ahli dan kebutuhan audit model citra.
- **Bab 2 Proposal**: XAI visual, Grad-CAM/Integrated Gradients/Occlusion, XAI toolkit existing, dan konsep usability/produk.
- **Bab 3 Proposal**: Rancangan sistem web, format model/data, flow audit, metode XAI, metrik pengujian, dan rencana usability.
- **Bab 4 Proposal**: Jadwal desain UI, backend, integrasi XAI, report generation, pengujian, dan penulisan.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: Cocok untuk pembimbing AI terapan, rekayasa perangkat lunak, atau HCI ringan.
- **Ketersediaan data/infrastruktur**: Feasible jika model/dataset contoh disediakan sendiri. Risiko terbesar adalah format upload model.
- **Risiko kegagalan**: Scope creep ke multi-modal; upload model sulit distandardisasi; novelty lemah jika hanya wrapper library; evaluasi usability butuh responden.
- **Fallback plan**: Ganti upload model umum menjadi model registry terbatas atau template model yang sudah ditentukan. Fokuskan kontribusi pada audit workflow dan laporan.

## 9. Catatan Sumber & Literatur (Source Notes)

### 9.1 Sumber Utama (Core References)

| # | Judul | Penulis | Tahun | DOI/URL | Relevansi | BibTeX Key |
|---|---|---:|---|---|---|---|
| 1 | Captum | Meta/PyTorch | - | https://captum.ai/ | Library XAI PyTorch pembanding | captum |
| 2 | SHAP | Lundberg & Lee | 2017 | https://github.com/shap/shap | Pembanding XAI populer | lundberg2017shap |
| 3 | LIME | Ribeiro et al. | 2016 | https://arxiv.org/abs/1602.04938 | Metode XAI lokal | ribeiro2016lime |
| 4 | Learning Interpretability Tool (LIT) | Google | - | https://pair-code.github.io/lit/ | Tool interpretability browser-based pembanding | googleLIT |
| 5 | Grad-CAM | Selvaraju et al. | 2017 | https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html | Dasar XAI visual | selvaraju2017gradcam |

### 9.2 Gap yang Ditemukan dari Literatur

Gap yang masuk akal ada pada pengalaman produk yang lebih sederhana, laporan otomatis, dan uji stabilitas penjelasan untuk klasifikasi citra. Klaim "toolkit XAI multi-modal baru" harus dihindari karena terlalu luas dan sudah banyak pembanding.

## 10. Penyerahan ke Penulisan LaTeX (Draft Handoff)

- **Target File**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, `template/proposal/chapters/bab3-metodologi.tex`
- **Kebutuhan Gambar/Diagram**: Diagram arsitektur web, alur upload-inference-report, wireframe dashboard, contoh heatmap, tabel fitur dan metrik pengujian.
- **Pertanyaan ke Pengguna**: Apakah upload model harus umum, atau boleh dibatasi ke model yang sudah tersedia di aplikasi? Apakah target pengguna mahasiswa/pemula ML atau developer model?
