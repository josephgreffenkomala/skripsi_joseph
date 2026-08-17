# Eksplorasi Topik Skripsi AI

Date: 2026-06-08
Target: proposal

## Summary

Eksplorasi ini memetakan beberapa ide skripsi AI yang feasible untuk tingkat sarjana, memiliki sumber data publik atau realistis untuk dikumpulkan, dan punya pembeda ilmiah dibanding penelitian umum sebelumnya. Rekomendasi terkuat saat ini adalah topik RAG Indonesia yang terukur, NLP bencana Indonesia, evaluasi/adaptasi LLM untuk bahasa daerah, fairness toksisitas bahasa Indonesia, dan prediksi kualitas udara Jakarta.

## Candidate Topics

### 1. Evaluasi Keandalan RAG Berbahasa Indonesia untuk Dokumen Institusi

Ide: membangun sistem tanya jawab berbasis Retrieval-Augmented Generation (RAG) untuk dokumen institusi publik, lalu mengevaluasi groundedness, citation accuracy, abstention, dan hallucination.

Data: dokumen PDF publik seperti peraturan akademik, pedoman kampus, SOP, atau regulasi pemerintah; benchmark kecil dibuat dari pasangan pertanyaan-jawaban yang diverifikasi manual.

Kebaruan: bukan sekadar membuat chatbot dokumen, tetapi membuat protokol evaluasi RAG berbahasa Indonesia dengan metrik keterlacakan kutipan dan kemampuan menolak menjawab saat bukti tidak tersedia.

Pembeda: penelitian RAG umum sering memakai dataset Inggris atau hanya mengukur akurasi jawaban; topik ini menekankan Bahasa Indonesia, dokumen nyata, citation faithfulness, dan error taxonomy.

Feasibility: tinggi. Bisa memakai model lokal/API, vector database ringan, dan dataset 100-300 QA terverifikasi.

### 2. Ekstraksi Informasi Krisis dari Tweet Bahasa Indonesia

Ide: model NLP untuk mengekstraksi struktur kejadian dari teks krisis: jenis bencana, lokasi, waktu, dampak, korban, kebutuhan bantuan, dan tingkat urgensi.

Data: dataset tweet krisis Indonesia yang memuat sekitar 56 ribu teks untuk banjir, gempa, kebakaran, dan kecelakaan; dapat ditambah dataset HumAID untuk transfer learning.

Kebaruan: naik dari klasifikasi sederhana ke semantic role labeling / slot filling yang lebih berguna untuk respons bencana.

Pembeda: banyak studi hanya klasifikasi relevan/tidak relevan atau jenis bencana; topik ini menghasilkan struktur informasi operasional yang dapat dipakai dashboard situational awareness.

Feasibility: tinggi-sedang. Bisa mulai dari IndoBERT/IndoBERTweet, LLM prompting sebagai baseline, lalu fine-tuning model sequence labeling.

### 3. Adaptasi LLM untuk Bahasa Daerah Indonesia Low-Resource

Ide: mengevaluasi dan meningkatkan performa model multilingual/LLM kecil pada tugas bahasa daerah Indonesia, misalnya Jawa, Sunda, Minangkabau, Bali, Bugis, atau Makassar.

Data: LoraxBench, NusaX, dan dataset parallel low-resource Indonesian local languages.

Kebaruan: membandingkan strategi murah untuk low-resource: prompt engineering, few-shot examples, translate-test, retrieval glossary, dan LoRA/adapters.

Pembeda: penelitian benchmark biasanya melaporkan performa model; skripsi ini menambahkan intervensi terukur untuk memperbaiki performa pada bahasa daerah tertentu.

Feasibility: sedang. Perlu GPU ringan bila fine-tuning, tetapi masih bisa dibuat feasible dengan model kecil dan eksperimen terbatas.

### 4. Fairness dan Robustness Deteksi Ujaran Kebencian Bahasa Indonesia

Ide: membangun dan mengevaluasi model deteksi hate speech/toxicity Bahasa Indonesia dengan perhatian pada kelompok demografis, calibration, dan robustness terhadap variasi bahasa informal.

Data: IndoToxic2024, Indonesian hate-speech superset, dataset abusive/hate speech dari SEACrowd.

Kebaruan: fokus pada fairness dan robustness, bukan hanya skor F1 keseluruhan.

Pembeda: studi terdahulu sering mengejar akurasi model; topik ini menilai apakah model lebih sering salah pada kelompok target tertentu, slang, atau gaya bahasa campuran.

Feasibility: tinggi. Data tersedia, model baseline jelas, dan evaluasi bisa dilakukan tanpa infrastruktur besar.

### 5. Prediksi Dini PM2.5 Jakarta dengan Uncertainty Estimation

Ide: model time-series untuk memprediksi PM2.5/AQI Jakarta beberapa jam atau hari ke depan, dengan interval ketidakpastian dan penjelasan fitur.

Data: WHO air quality database, TUMI Jakarta air quality historical endpoint/AQICN, World Bank satellite-derived PM2.5, data cuaca publik jika tersedia.

Kebaruan: bukan hanya prediksi titik, tetapi peringatan dini berbasis probabilitas, kalibrasi, dan interpretasi faktor cuaca/polutan.

Pembeda: banyak studi PM2.5 memakai LSTM/RF untuk akurasi; topik ini mengukur reliability peringatan, false alarm, missed alarm, dan uncertainty calibration.

Feasibility: tinggi-sedang. Tantangan utama adalah kebersihan dan kelengkapan data time-series.

### 6. Sistem Rekomendasi Produk Pangan Kemasan Berbasis Nutrisi untuk Konteks Indonesia

Ide: sistem AI yang menormalisasi data produk pangan, memprediksi atribut nutrisi/processing level yang hilang, lalu merekomendasikan alternatif lebih sehat dalam kategori produk yang sama.

Data: Open Food Facts product database, termasuk produk berbahasa Indonesia bila cukup; dapat ditambah scraping terbatas dari label produk dengan verifikasi manual.

Kebaruan: rekomendasi bukan berdasarkan rating pengguna, tetapi nutritional constraints, missing data imputation, dan kesamaan kategori produk.

Pembeda: studi umum sering klasifikasi Nutri-Score/NOVA; topik ini menggabungkan prediksi atribut hilang dan rekomendasi substitusi yang dapat dijelaskan.

Feasibility: sedang. Perlu filtering data Indonesia dan desain evaluasi yang rapi.

### 7. Legal NLP Putusan Pengadilan Indonesia dengan Penjelasan Faktor Putusan

Ide: model yang memprediksi kategori/durasi hukuman atau ekstraksi faktor hukum dari putusan pengadilan Indonesia, disertai penjelasan berbasis kutipan teks.

Data: Direktori Putusan Mahkamah Agung atau dataset dari studi legal NLP Indonesia bila dapat diakses.

Kebaruan: menggabungkan prediksi dengan evidence extraction agar model tidak hanya memberi label.

Pembeda: penelitian legal prediction sering hanya prediksi outcome; topik ini menekankan keterjelasan bukti dan konsistensi faktor putusan.

Feasibility: sedang-rendah. Data bisa besar tetapi preprocessing PDF/HTML legal sering melelahkan, serta perlu kehati-hatian etika.

## Shortlist

Paling kuat untuk skripsi yang rapi dan feasible:

1. Evaluasi keandalan RAG Bahasa Indonesia.
2. Ekstraksi informasi krisis dari tweet Indonesia.
3. Fairness deteksi ujaran kebencian Bahasa Indonesia.
4. Adaptasi LLM untuk bahasa daerah low-resource.
5. Prediksi PM2.5 Jakarta dengan uncertainty.

## Sources

- IndoMMLU dataset and paper: https://huggingface.co/datasets/indolem/IndoMMLU
- IndoToxic2024 paper: https://arxiv.org/abs/2406.19349
- Indonesian hate-speech superset: https://huggingface.co/datasets/manueltonneau/indonesian-hate-speech-superset
- LoraxBench publication page: https://research.google/pubs/lorax-a-multitask-multilingual-benchmark-suite-for-20-indonesian-languages/
- NusaX paper: https://arxiv.org/abs/2205.15960
- NusaAksara paper: https://arxiv.org/abs/2502.18148
- Indonesian crisis-event tweet dataset: https://pmc.ncbi.nlm.nih.gov/articles/PMC12164043/
- HumAID events dataset: https://huggingface.co/datasets/QCRI/HumAID-events
- RAGTruth repository: https://github.com/ParticleMedia/RAGTruth
- Tau-bench paper: https://arxiv.org/abs/2406.12045
- WHO Ambient Air Quality Database: https://www.who.int/data/gho/data/themes/air-pollution/who-air-Quality-database
- TUMI Jakarta air quality dataset page: https://hub.tumidata.org/en/dataset/air_quality_historical_data_platform_jakarta
- Open Food Facts datasets: https://huggingface.co/openfoodfacts/datasets

## Writing Handoff

Topik yang paling siap diturunkan ke proposal adalah RAG Bahasa Indonesia, NLP bencana, dan fairness toksisitas. Ketiganya punya data jelas, masalah nyata, baseline model jelas, dan pembeda ilmiah yang dapat ditulis sebagai rumusan masalah.

## Open Questions

- Apakah skripsi diinginkan sebagai penelitian model murni atau produk/prototipe AI?
- Apakah tersedia GPU lokal/cloud?
- Lebih tertarik domain sosial-bahasa, lingkungan, kesehatan, hukum, atau developer tools?
