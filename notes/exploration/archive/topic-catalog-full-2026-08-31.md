---
cssclasses:
  - full-width
---
# Katalog Eksplorasi Topik Skripsi / Proposal

Tanggal: 2026-08-31
Updated: 2026-08-31
Target Document: Proposal terlebih dahulu, dapat dilanjutkan ke Skripsi
Bidang Utama: AI Engineering, Software Engineering, Computer Vision, Explainable AI

## Executive Summary

Eksplorasi baru menilai ide tentang mengecilkan model Computer Vision dan mengukur dampaknya terhadap explainability (kemampuan model memberikan alasan yang dapat diperiksa). Arah yang paling direkomendasikan adalah studi empiris pada klasifikasi cacat permukaan baja: model, dataset, dan eksperimen dapat dibatasi dengan jelas; hasilnya juga relevan untuk deployment edge. Kontribusi yang aman bukan mengklaim metode kompresi baru, melainkan protokol evaluasi yang menyamakan tingkat kompresi dan mengukur trade-off akurasi, efisiensi, faithfulness, serta konsistensi penjelasan.

Materi baru menambahkan kandidat AI systems/NLP: evaluasi kuantisasi Small Language Model (SLM) pada tugas Bahasa Indonesia dengan inferensi CPU. Kandidat ini layak sebagai opsi bersyarat, tetapi scope awal perlu dipersempit dan klaim kebaruan perlu diverifikasi lebih lanjut karena kuantisasi IndoBERT sudah pernah dipelajari.

Catatan eksplorasi saat ini sudah mengerucut dari ide AI umum menuju dua jalur besar: topik Software Engineering berbasis coding agent, dan topik Computer Vision x Explainable AI (XAI). Kandidat paling matang secara dokumentasi adalah **IndoAgentBench**, karena sudah melewati sesi grilling, punya pembanding literatur utama, serta klaim kebaruan yang sudah direvisi agar lebih jujur. Kandidat kedua yang kuat adalah **foundation-vs-supervised shortcut attribution**, tetapi lebih cocok sebagai skripsi ilmiah akademik daripada inovasi produk murni.

Rekomendasi praktis: jika ingin proposal yang paling siap dan dekat dengan produk perangkat lunak, pilih **Topik 01: IndoAgentBench**. Jika ingin topik Computer Vision yang lebih akademik dan potensial untuk eksperimen kuat, pilih **Topik 02**. Jika ingin tetap dalam jalur Skripsi Inovasi Produk berbasis XAI visual, pilih **Topik 03** atau **Topik 04** dengan scope yang ketat. Topik baru tentang pengelolaan riwayat eksekusi coding agent layak dipertimbangkan sebagai kandidat tambahan, tetapi novelty-nya harus dibatasi pada evaluasi komparatif yang terkontrol.

## Tabel Perbandingan Topik

| No  | Judul Topik (Bahasa Indonesia)                                                                                                           | Ringkasan Kebaruan (Novelty)                                                                                                                                                         | Tingkat Kesulitan | Kelayakan (Feasibility)                                       | Rekomendasi   |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | ------------------------------------------------------------- | ------------- |
| 01  | IndoAgentBench: Benchmark Berbasis Pasangan Issue Indonesia-Inggris untuk Mengukur Kesenjangan Bahasa pada Coding Agent Repository-Level | Ekstensi terkontrol ke Bahasa Indonesia low-resource, kondisi translate-then-act, audit ekuivalensi bilingual, failure taxonomy, dan transformasi task anti-kontaminasi              | Sedang-Tinggi     | Tinggi jika task dibatasi 40-60 dan model/agent dibatasi      | *****         |
| 02  | Studi Empiris Shortcut Learning pada Foundation Model dan Supervised Model Menggunakan Attribution sebagai Diagnostic Tool               | Kombinasi controlled shortcut benchmark, foundation-vs-supervised sebagai axis utama, attribution diagnostic, dan domain umum                                                        | Tinggi            | Sedang-Tinggi jika hanya inference model pre-trained          | ****          |
| 03  | Pengembangan Toolkit Audit Explainable AI untuk Evaluasi Shortcut Learning pada Model Klasifikasi Penyakit Tanaman Berbasis Citra        | Menggeser XAI penyakit tanaman dari sekadar heatmap/ACE menuju toolkit audit dengan perturbasi, stability score, dan laporan shortcut learning                                       | Sedang-Tinggi     | Tinggi jika memakai PlantVillage + perturbasi terkontrol      | ****          |
| 04  | Pengembangan Website Explainable AI untuk Audit Model Klasifikasi Citra Berbasis Peta Atribusi dan Uji Perturbasi                        | Produk web audit XAI dengan upload terbatas, heatmap, perturbasi, stability score, dan laporan otomatis; bukan XAI toolkit umum                                                      | Sedang-Tinggi     | Sedang karena format upload model vision perlu dibatasi ketat | ***           |
| 05  | Studi Empiris Pengelolaan Riwayat Eksekusi pada Coding Agent Tingkat Repositori                                                          | Perbandingan terkontrol antara full, recent-only, summary, dan task-relevant history dengan metrik keberhasilan, konteks, biaya, dan perilaku trajectory; bukan teknik kompresi baru | Tinggi            | Sedang jika agent, model, benchmark, dan jumlah task dibatasi | *** bersyarat |
| 06  | Asisten Debugging Praktikum Pemrograman dengan Feedback Bertingkat                                                                       | Fokus pada pedagogical feedback control, bukan jawaban langsung; evaluasi kualitas hint, leakage, dan perbaikan bug                                                                  | Sedang            | Sedang-Tinggi jika dataset sintetis dan rubrik dibuat sendiri | ***           |
| 07  | Evaluasi Keandalan RAG Berbahasa Indonesia untuk Dokumen Institusi                                                                       | Protokol evaluasi RAG Indonesia dengan groundedness, citation accuracy, abstention, dan hallucination taxonomy                                                                       | Sedang            | Tinggi                                                        | ***           |
| 08  | Fairness dan Robustness Deteksi Ujaran Kebencian Bahasa Indonesia                                                                        | Menilai bias, robustness terhadap slang, dan error antar kelompok, bukan hanya F1 keseluruhan                                                                                        | Sedang            | Tinggi                                                        | ***           |
| 09  | Robust ASR Bahasa Indonesia Informal dan Dialek                                                                                          | Audit performa ASR pada bahasa informal, aksen, noise, dan code-switching Indonesia                                                                                                  | Tinggi            | Sedang                                                        | **            |
| 14  | Studi Empiris Kuantisasi Small Language Model pada NLP Bahasa Indonesia | Benchmark terkontrol yang menghubungkan ukuran model, bit-width, kualitas tugas Indonesia, dan efisiensi CPU; klaim pertama masih perlu diverifikasi | Sedang-Tinggi | Sedang-Tinggi jika model/runtime/tugas dibatasi | ⭐⭐⭐⭐ bersyarat |

## Ringkasan Singkat & Penjelasan Sederhana

### Topik 01: IndoAgentBench

- **Penjelasan Sederhana**: Topik ini mengecek apakah coding agent lebih susah menyelesaikan tugas pemrograman ketika instruksinya ditulis dalam Bahasa Indonesia dibanding Bahasa Inggris.
- **Kebaruan Utama**: Fokus pada Bahasa Indonesia, bukan klaim umum pertama tentang bahasa natural pada coding agent. Nilai tambahnya ada pada pasangan issue Indonesia-Inggris, kondisi translate-then-act, audit kesetaraan terjemahan, dan analisis jenis kegagalan.
- **Status**: Kandidat paling matang; klaim kebaruan sudah direvisi setelah pembanding Ren et al. (2026).
- **File Detail**: [`topic-01-indoagentbench.md`](../topic-01-indoagentbench.md)

### Topik 02: Foundation-vs-Supervised Shortcut Attribution

- **Penjelasan Sederhana**: Topik ini membandingkan apakah model vision modern seperti CLIP/DINOv2 lebih atau kurang mudah tertipu oleh pola sampingan seperti latar belakang dibanding model supervised biasa.
- **Kebaruan Utama**: Bukan membuat metode XAI baru, melainkan memakai attribution untuk mendiagnosis shortcut behavior secara terkontrol pada foundation model vs supervised model.
- **Status**: Kuat secara akademik, tetapi framing paling jujur adalah skripsi ilmiah akademik atau produk toolkit audit yang sangat minimal.
- **File Detail**: [`topic-02-foundation-shortcut-attribution.md`](../topic-02-foundation-shortcut-attribution.md)

### Topik 03: Toolkit Audit XAI Penyakit Tanaman

- **Penjelasan Sederhana**: Topik ini membuat alat untuk memeriksa apakah model deteksi penyakit tanaman benar-benar melihat gejala pada daun, atau hanya mengandalkan latar belakang, cahaya, dan artefak dataset.
- **Kebaruan Utama**: Setelah Amara et al. (2024), sekadar memakai ACE/Grad-CAM pada PlantVillage tidak cukup baru. Kebaruan harus diletakkan pada audit robustness, perturbasi, stability score, dan laporan evaluasi.
- **Status**: Cocok untuk Skripsi Inovasi Produk jika produk toolkit/dashboard dibuat nyata dan scope domain dibatasi.
- **File Detail**: [`topic-03-plant-xai-audit-toolkit.md`](topic-03-plant-xai-audit-toolkit.md)

### Topik 04: Website Audit XAI untuk Citra

- **Penjelasan Sederhana**: Topik ini membuat website yang membantu pengguna mengunggah model klasifikasi citra dan mendapatkan penjelasan visual serta laporan audit sederhana.
- **Kebaruan Utama**: Bukan "XAI toolkit multi-modal"; kebaruan ada pada workflow upload terbatas, laporan otomatis, uji perturbasi, dan edukasi interpretasi untuk pengguna pemula.
- **Status**: Layak sebagai produk, tetapi perlu scope ketat agar tidak kalah oleh Captum, LIT, SHAP, dan tool XAI besar lain.
- **File Detail**: [`topic-04-vision-xai-audit-website.md`](topic-04-vision-xai-audit-website.md)

### Topik 05: Pengelolaan Riwayat Eksekusi Coding Agent

- **Penjelasan Sederhana**: Topik ini menguji seberapa banyak catatan kerja agent yang perlu dibawa ke langkah berikutnya ketika agent mencari file, menjalankan tes, membaca error, dan mengedit kode.
- **Kebaruan Utama**: Kebaruan yang aman bukan “menemukan context management”, melainkan menyediakan ablation study yang menyamakan model, agent, tools, task, dan batas token, lalu mengisolasi pengaruh kebijakan retensi riwayat terhadap hasil dan biaya.
- **Peringatan Novelty**: ContextBench sudah mengukur retrieval konteks pada trajectory, sedangkan Context as a Tool sudah mengembangkan kompresi riwayat dan membandingkan static compression. Topik ini harus menghindari klaim sebagai metode kompresi baru.
- **File Detail**: [`topic-05-execution-context-management.md`](topic-05-execution-context-management.md)

### Topik 14: Kuantisasi Small Language Model untuk NLP Bahasa Indonesia

- **Penjelasan Sederhana**: Menguji seberapa kecil presisi model dapat diturunkan agar model Bahasa Indonesia tetap cukup akurat, tetapi lebih hemat memori dan cepat dijalankan pada CPU.
- **Kebaruan Utama**: Protokol benchmark reproducible yang menggabungkan ukuran model, tingkat kuantisasi, kualitas tugas Indonesia, dan biaya inferensi CPU. Topik tidak boleh mengklaim kuantisasi IndoBERT sebagai hal baru karena sudah ada studi terkait.
- **Status**: ⭐⭐⭐⭐ kandidat bersyarat; harus dipersempit dan klaim literatur 2024–2026 diverifikasi.
- **File Detail**: [`topic-14-slm-quantization-indonesian-nlp.md`](../topic-14-slm-quantization-indonesian-nlp.md)

## Panduan Pemilihan untuk Mahasiswa

Pilih **IndoAgentBench** jika ingin topik yang paling siap diturunkan ke proposal, dekat dengan software engineering, dan punya produk berbentuk benchmark harness. Risiko utamanya adalah biaya eksperimen agent dan kualitas pasangan issue bilingual, tetapi keduanya bisa dikendalikan dengan scope kecil.

Pilih **Topik 02** jika ingin eksperimen Computer Vision yang lebih kuat secara paper/literatur. Topik ini lebih riset daripada produk; cocok jika dosen pembimbing menerima skripsi ilmiah akademik atau jika produk cukup berupa toolkit benchmark.

Pilih **Topik 03** jika ingin kompromi antara Computer Vision, XAI, dan Skripsi Inovasi Produk. Ini lebih mudah dipresentasikan sebagai prototipe dibanding Topik 02, tetapi klaim kebaruan harus disiplin: audit dan robustness, bukan sekadar visualisasi Grad-CAM.

Pilih **Topik 04** jika ingin membangun aplikasi web yang jelas terlihat sebagai produk. Jaga agar scope hanya klasifikasi citra dengan format model yang sangat terbatas; jangan membuat klaim multi-modal umum.

Untuk **Topik 05**, pilih hanya jika tersedia akses API/model dan infrastruktur eksperimen yang cukup. Topik ini kuat sebagai studi empiris software engineering, tetapi lebih lemah sebagai “produk inovatif” apabila hanya menghasilkan tabel perbandingan. Agar sesuai dengan Skripsi Inovasi Produk, hasilnya sebaiknya berupa harness/prototipe evaluasi yang dapat mengatur kebijakan konteks, merekam trajectory, menghitung metrik, dan menghasilkan laporan reproduktif.

Untuk **Topik 14**, pilih jika ingin masuk ke AI systems/NLP dan memiliki CPU dengan RAM yang cukup. Mulai dari satu keluarga model, satu tugas utama, serta FP16/FP32–INT8–INT4. Jangan menggabungkan IndoBERT encoder dan LLM generatif dalam satu klaim umum; perlakukan sebagai jalur eksperimen berbeda atau pilih salah satunya. Bentuk produk yang disarankan adalah benchmark harness yang dapat digunakan ulang, bukan hanya tabel hasil.

## Memori Canonical dari Eksplorasi Sebelumnya

Bagian ini menyerap informasi penting dari catatan brainstorming dan keputusan yang sudah tidak dipertahankan sebagai file terpisah.

### Kandidat AI umum yang tersimpan sebagai opsi, belum dipilih

| Kandidat | Inti masalah dan pembeda | Status canonical |
|---|---|---|
| RAG Bahasa Indonesia untuk dokumen institusi | Evaluasi groundedness, citation accuracy, abstention, hallucination, dan error taxonomy pada dokumen nyata | Opsi cadangan; feasible tinggi, tetapi bukan arah utama saat ini |
| Ekstraksi informasi krisis dari teks Indonesia | Slot filling/semantic role labeling untuk bencana, lokasi, waktu, dampak, korban, dan kebutuhan bantuan | Opsi cadangan; data dan evaluasi cukup jelas |
| Adaptasi LLM bahasa daerah low-resource | Perbandingan prompt, few-shot, translate-test, glossary retrieval, dan LoRA/adapters | Opsi cadangan; perlu membatasi bahasa dan compute |
| Fairness dan robustness ujaran kebencian Indonesia | Evaluasi bias antar kelompok, slang, code-switching, dan calibration, bukan hanya F1 | Opsi cadangan; feasible tinggi |
| Prediksi PM2.5 Jakarta | Probabilistic forecast, uncertainty calibration, false alarm, missed alarm, dan faktor cuaca/polutan | Opsi cadangan; kualitas time-series menjadi risiko |
| Rekomendasi pangan berbasis nutrisi | Normalisasi produk, imputasi atribut nutrisi, dan rekomendasi substitusi dalam kategori sama | Belum dipilih; data Indonesia dan evaluasi menjadi risiko |
| Legal NLP putusan Indonesia | Prediksi outcome atau durasi dengan evidence extraction | Belum dipilih; preprocessing dan etika membuat feasibility lebih rendah |

### Kandidat agent, education, speech, dan safety yang tersimpan

| Kandidat | Inti masalah dan pembeda | Status canonical |
|---|---|---|
| Asisten debugging praktikum bertingkat | Hint konseptual → lokasi masalah → perbaikan minimal, dengan kontrol solution leakage dan test oracle | Opsi kuat untuk produk, tetapi human/education scope belum dipilih |
| ASR Indonesia informal dan dialek | Perbandingan formal versus informal, aksen, noise, code-switching, dan normalisasi/fine-tuning ringan | Opsi cadangan; data audio dan compute menjadi risiko |
| Misinformasi multimodal Indonesia | Uji ketidaksesuaian gambar–caption dan evidence grounding, bukan teks saja | Opsi cadangan; anotasi manual cukup mahal |
| AI tutor pendidikan tinggi | Hubungan desain tutor dengan critical thinking, self-regulation, dan ethical awareness | Belum dipilih; memerlukan human study dan pertimbangan etik |
| Defensive cybersecurity LLM agent | Triage log/CVE/OSV dengan prioritas dan evidence reproducible, bukan offensive exploit | Belum dipilih; scope keamanan harus ketat |
| Memori jangka panjang personal assistant Indonesia | Recall, contradiction rate, stale-memory, update preference, dan privacy leakage | Belum dipilih; definisi benchmark perlu diperdalam |
| Synthetic data Indonesia | Kapan data sintetis membantu atau merusak model melalui distribution shift, diversity, dan label noise | Belum dipilih; berisiko terlalu luas |

### Kandidat Computer Vision dan XAI yang terserap

| Kandidat | Pelajaran yang dipertahankan | Status canonical |
|---|---|---|
| Audit penyakit tanaman | PlantVillage mudah dipakai, tetapi PlantVillage + InceptionV3 + ACE saja terlalu dekat dengan Amara et al.; perlu perturbasi, stabilitas, shortcut audit, atau data lapangan | Sudah menjadi Topik 03 |
| Audit chest X-ray TBC | Fokus dapat berupa lung-region alignment dan artefak luar paru, tetapi klaim diagnosis klinis tidak boleh dibuat dan validasi ahli menjadi risiko | Belum dipilih |
| Audit kerusakan jalan | Relevan untuk smart city; perlu object-detection explanation, false-positive taxonomy, dan metrik overlap | Belum dipilih; lebih kompleks daripada klasifikasi |
| Audit kualitas buah/makanan | Data lokal mudah dikumpulkan, tetapi novelty lemah tanpa data lokal atau audit shortcut yang rapi | Belum dipilih |
| Foundation versus supervised shortcut attribution | Studi empiris controlled perturbation dengan CLIP/DINOv2 versus CNN/ViT; bukan metode XAI baru | Sudah menjadi Topik 02 |
| Website XAI vision-first | Format model ideal dibatasi ONNX/TorchScript, input tensor tetap, metadata preprocessing wajib, dan fitur inti Grad-CAM/IG/Occlusion plus perturbasi brightness/blur/occlusion | Sudah menjadi Topik 04 |
| Website XAI tabular-first | Lebih mudah dengan scikit-learn + CSV + SHAP/LIME/permutation/PDP, tetapi kebaruan terutama integrasi, laporan Bahasa Indonesia, dan usability | Opsi fallback untuk Topik 04 |

### Keputusan metodologis yang dipertahankan

- Untuk benchmark coding agent: gunakan within-task paired comparison, samakan repository commit, tools, prompt structure, budget, test suite, dan environment. Ukur resolution rate, test pass, tool calls, token, biaya, waktu, invalid patch, regression, serta failure taxonomy.
- Untuk IndoAgentBench: kandidat desain yang pernah dipilih adalah OpenHands, tiga kondisi EN/ID direct/translate-then-act, subset task yang ditransformasi, dan analisis paired seperti McNemar + Wilson CI. Pilihan model free-tier dan jumlah run tetap menunggu validasi infrastruktur; jangan menganggap snapshot itu final.
- Untuk XAI vision: fokus pada klasifikasi citra, 2–3 metode attribution, perturbasi brightness/blur/crop/noise/occlusion, skor stabilitas prediksi dan heatmap, serta rasio fokus objek/latar. Jangan mengklaim explanation selalu benar.
- Untuk produk: self-service CLI/web, dokumentasi, contoh task, laporan otomatis, dan artifact yang dapat diulang lebih bernilai daripada demo satu kali.

### Daftar sumber lama yang sudah terserap

Sumber-sumber lama tidak lagi disimpan sebagai catatan mentah. Kesimpulan dan URL yang relevan sudah berada di file detail canonical; sumber penting yang menjadi pembatas novelty meliputi mHumanEval, HumanEval-XL, SWE-bench/Multi-SWE-bench, Ren et al. tentang bahasa Cina pada coding agent, Amara et al. tentang ACE pada PlantVillage, Captum, SHAP, Alibi, ExplainerDashboard, LIT, Grad-CAM, TCAV, PlantVillage, Montgomery/Shenzhen CXR, dan RDD2022.

Referensi tambahan yang tetap dipertahankan sebagai registry:

- [IndoMMLU](https://huggingface.co/datasets/indolem/IndoMMLU), [IndoToxic2024](https://arxiv.org/abs/2406.19349), [Indonesian hate-speech superset](https://huggingface.co/datasets/manueltonneau/indonesian-hate-speech-superset), [LoraxBench](https://research.google/pubs/lorax-a-multitask-multilingual-benchmark-suite-for-20-indonesian-languages/), [NusaX](https://arxiv.org/abs/2205.15960), [NusaAksara](https://arxiv.org/abs/2502.18148), [dataset krisis Indonesia](https://pmc.ncbi.nlm.nih.gov/articles/PMC12164043/), [HumAID](https://huggingface.co/datasets/QCRI/HumAID-events), [RAGTruth](https://github.com/ParticleMedia/RAGTruth), [τ-bench](https://arxiv.org/abs/2406.12045), [WHO Air Quality Database](https://www.who.int/data/gho/data/themes/air-pollution/who-air-Quality-database), [TUMI Jakarta air quality](https://hub.tumidata.org/en/dataset/air_quality_historical_data_platform_jakarta), dan [Open Food Facts](https://huggingface.co/openfoodfacts/datasets).
- [MIT AI Agent Index](https://aiagentindex.mit.edu/), [SWE-Lancer](https://openai.com/index/swe-lancer/), [SEC-bench](https://github.com/SEC-bench/SEC-bench), [CAIBench](https://arxiv.org/abs/2510.24317), [MemoryAgentBench](https://www.modelscope.cn/datasets/AI-ModelScope/MemoryAgentBench), [Common Voice Indonesian](https://datacollective.mozillafoundation.org/datasets/cmn2e8ats01eno107glwgoasv), [ASR-IndoCSC](https://magichub.com/datasets/indonesian-conversational-speech-corpus/), [WorldSpeech](https://modelscope.cn/datasets/disco-eth/WorldSpeech), [MuMiN](https://mumin-dataset.github.io/index), [Indonesia Political Hoax Dataset](https://data.mendeley.com/datasets/mzx5rd397v), dan dataset [AI pendidikan tinggi Indonesia](https://zenodo.org/records/19680489).
- Dasar XAI vision: [Grad-CAM](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html), [TCAV](https://arxiv.org/abs/1711.11279), [Concept Bottleneck Models](https://proceedings.mlr.press/v119/koh20a/koh20a.pdf), [PlantVillage](https://www.tensorflow.org/datasets/catalog/plant_village), [CXR Montgomery/Shenzhen](https://pmc.ncbi.nlm.nih.gov/articles/PMC4256233/), [RDD2022](https://arxiv.org/abs/2209.08538), dan [Amara et al.](https://arxiv.org/pdf/2412.07408).
- Pembanding XAI tools: [Captum](https://captum.ai/), [SHAP](https://github.com/shap/shap), [LIME](https://arxiv.org/abs/1602.04938), [InterpretML](https://interpret.ml/), [Alibi Explain](https://docs.seldon.ai/alibi-explain/), [ExplainerDashboard](https://explainerdashboard.readthedocs.io/), [What-If Tool](https://www.tensorflow.org/tensorboard/what_if_tool), dan [LIT](https://pair-code.github.io/lit/documentation/).
- Pembanding language/coding-agent: [mHumanEval](https://aclanthology.org/2025.naacl-long.570/), [HumanEval-XL](https://aclanthology.org/2024.lrec-main.735/), [StudentEval](https://aclanthology.org/2024.findings-acl.501/), [Multi-SWE-bench](https://arxiv.org/abs/2504.02605), [SWE-PolyBench](https://arxiv.org/abs/2504.08703), [DevEval](https://aclanthology.org/2024.findings-acl.214/), [Cross-Lingual-Thought Prompting](https://aclanthology.org/2023.findings-emnlp.826/), dan [Self-Explained Keywords](https://aclanthology.org/2025.findings-acl.324/).
- Pembanding foundation/shortcut attribution: [COVAR](https://arxiv.org/abs/2511.12978), [exCLIP](https://arxiv.org/abs/2408.14153), [Whac-A-Mole](https://arxiv.org/abs/2212.04825), [Marine species comparison](https://arxiv.org/abs/2607.02559), dan [EZPC](https://arxiv.org/abs/2603.28211). Kandidat lain yang pernah diperiksa: OSP, EarthShift, FAS VFM Benchmark, ShellfishNet, Automated Visual Attribute Reliance, PatchSAE, VL-SAE, TextCAM, Distance Explainer, LaZSL, dan CLIP Generalization; semua sudah tercermin dalam status novelty Topik 02.

## Catatan arsip

Catatan eksplorasi lama telah dipadatkan ke bagian di atas dan dihapus dari workspace. Jangan menghidupkan kembali file-file tanggalan tersebut; gunakan canonical files sebagai sumber kebenaran.
