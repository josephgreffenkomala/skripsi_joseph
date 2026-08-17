# Eksplorasi Topik Skripsi AI Gelombang 2

Date: 2026-06-08
Target: proposal

## Summary

Eksplorasi kedua ini mencari topik AI yang lebih segar dibanding klasifikasi NLP/vision standar. Fokus diarahkan ke AI agents, speech Indonesia, multimodal misinformation, AI education, cybersecurity, dan evaluasi model yang menghasilkan artefak/prototipe nyata.

## Stronger Candidate Topics

### 1. Evaluasi AI Coding Agent untuk Repositori Bahasa Indonesia / Tugas Mahasiswa

Ide: membangun benchmark kecil untuk menilai kemampuan AI coding agent menyelesaikan bug, menambah fitur, dan memperbaiki test pada repositori Python/JavaScript sederhana yang instruksinya ditulis dalam Bahasa Indonesia.

Data: repositori open-source kecil, tugas praktikum buatan sendiri, issue sintetis yang diverifikasi manual, unit test sebagai oracle.

Kebaruan: benchmark coding agent global seperti SWE-bench berbahasa Inggris dan berbasis issue GitHub; topik ini menguji interaksi instruksi Bahasa Indonesia, konteks lokal pembelajaran pemrograman, dan kualitas patch berbasis test.

Pembeda: bukan hanya prompt LLM untuk coding, tetapi evaluasi agentic workflow: membaca repo, menjalankan test, membuat patch, dan memperbaiki error.

Risiko: perlu desain dataset rapi agar tidak terlalu kecil atau terlalu mudah.

### 2. Asisten Debugging Praktikum Pemrograman dengan Feedback Bertingkat

Ide: sistem AI yang membaca error message, kode mahasiswa, dan hasil unit test, lalu memberi feedback bertingkat: hint konseptual, lokasi masalah, dan contoh perbaikan minimal tanpa langsung memberi jawaban penuh.

Data: soal praktikum yang dibuat sendiri, kumpulan submission salah dapat dibuat sintetis atau dari riwayat praktikum jika tersedia, test case sebagai ground truth.

Kebaruan: fokus pada pedagogical feedback control, bukan sekadar code generation. Evaluasi mengukur apakah bantuan terlalu membocorkan solusi, benar secara teknis, dan membantu mahasiswa memperbaiki bug.

Pembeda: banyak chatbot coding memberi jawaban langsung; topik ini mendesain guardrail edukatif dan rubrik kualitas feedback.

Risiko: data nyata mahasiswa perlu izin; versi tanpa data nyata tetap feasible dengan bug sintetis.

### 3. Robust ASR Bahasa Indonesia Informal dan Dialek Menggunakan Whisper/Model Multilingual

Ide: mengevaluasi dan mengadaptasi automatic speech recognition untuk Bahasa Indonesia informal, aksen, code-switching, atau dialek daerah.

Data: Mozilla Common Voice Indonesian, ASR-IndoCSC, Indonesian colloquial ASR datasets, WorldSpeech, atau rekaman kecil terkontrol dengan izin.

Kebaruan: membandingkan performa model ASR pada bahasa formal vs percakapan informal, lalu memperbaikinya dengan normalisasi teks, domain adaptation, atau fine-tuning ringan.

Pembeda: ASR Indonesia sering dievaluasi secara umum; topik ini menyorot real-world failure pada percakapan, aksen, noise, dan code-switching.

Risiko: fine-tuning audio perlu compute, tetapi evaluasi dan normalisasi pasca-ASR bisa dilakukan ringan.

### 4. Deteksi Misinformasi Multimodal Indonesia: Ketidaksesuaian Gambar dan Teks

Ide: sistem yang mendeteksi apakah gambar dan caption/artikel saling mendukung atau justru misleading, misalnya gambar lama dipakai untuk klaim baru.

Data: MuMiN, Indonesia Political Hoax Dataset, dataset hoax dari TurnBackHoax/MAFINDO jika dapat dikumpulkan, serta subset multimodal buatan dengan anotasi manual.

Kebaruan: banyak deteksi hoax Indonesia berbasis teks; topik ini menilai grounding antara teks dan gambar, termasuk reverse image evidence atau similarity-based evidence.

Pembeda: bukan hanya fake/real classification; menghasilkan alasan: klaim visual tidak cocok, konteks waktu salah, atau gambar tidak menjadi bukti klaim.

Risiko: pengumpulan data multimodal Indonesia perlu kerja manual, tetapi bisa dibuat kecil dan berkualitas.

### 5. Evaluasi AI Tutor pada Pendidikan Tinggi Indonesia

Ide: menguji apakah AI tutor benar-benar membantu critical thinking dan self-regulated learning, bukan hanya memberi jawaban cepat.

Data: dataset survei penggunaan AI pada mahasiswa Indonesia dari Zenodo/Mendeley, ditambah eksperimen kecil berbasis skenario belajar.

Kebaruan: menghubungkan desain prompt/tutor dengan kompetensi belajar, ethical awareness, dan self-regulation.

Pembeda: bukan adopsi AI secara deskriptif saja; ada prototipe tutor dan evaluasi perilaku/hasil belajar.

Risiko: butuh desain eksperimen manusia sederhana dan etik riset.

### 6. Cybersecurity LLM Agent untuk Analisis Log dan Triage Kerentanan

Ide: agent yang membaca log keamanan, CVE/OSV advisories, dependency file, lalu memberi prioritas tindakan: kerentanan mana yang relevan, patch apa yang dibutuhkan, dan bukti dari sumber.

Data: OSV database, CVE records, repositori vulnerable open-source, benchmark seperti SEC-bench/CAIBench sebagai inspirasi.

Kebaruan: bukan offensive hacking; fokus defensive triage dan reproducible evidence.

Pembeda: penelitian cybersecurity LLM agent banyak menilai exploit generation; topik ini lebih aman, aplikatif, dan bisa dievaluasi dengan ground truth advisory.

Risiko: scope harus dijaga supaya tidak masuk eksploitasi berbahaya.

### 7. Evaluasi Memori Jangka Panjang pada Personal AI Assistant Bahasa Indonesia

Ide: mengukur apakah assistant dapat mengingat preferensi pengguna, menghindari kontradiksi, dan memperbarui memori dalam percakapan panjang berbahasa Indonesia.

Data: skenario sintetis multi-turn dalam Bahasa Indonesia, terinspirasi MemoryAgentBench; bisa dibuat 50-100 skenario dengan ground truth.

Kebaruan: benchmark memori agent dalam konteks Indonesia dan percakapan natural, termasuk konflik preferensi dan perubahan instruksi.

Pembeda: evaluasi LLM biasanya single-turn; topik ini menilai persistensi, update, retrieval memory, dan privacy-aware memory.

Risiko: perlu definisi metrik yang jelas: recall, contradiction rate, stale-memory rate, privacy leakage.

### 8. Synthetic Data untuk Bahasa Indonesia: Kapan Membantu dan Kapan Merusak?

Ide: meneliti penggunaan synthetic data dari LLM untuk meningkatkan model klasifikasi Bahasa Indonesia pada domain low-resource, sambil mengukur distribution shift dan label noise.

Data: dataset kecil nyata untuk intent classification, toxic detection, hoax, atau edukasi; synthetic augmentation dari beberapa LLM; evaluasi pada test set nyata.

Kebaruan: fokus pada diagnosis kualitas synthetic data, bukan hanya menambah data.

Pembeda: menghasilkan panduan kapan synthetic data aman dipakai pada Bahasa Indonesia, termasuk filter semantic similarity, diversity, dan uncertainty.

Risiko: perlu eksperimen yang disiplin agar tidak terlalu luas.

## Top Picks

1. Asisten Debugging Praktikum Pemrograman dengan Feedback Bertingkat.
2. Evaluasi AI Coding Agent untuk Instruksi Bahasa Indonesia.
3. Robust ASR Bahasa Indonesia Informal dan Dialek.
4. Deteksi Misinformasi Multimodal Indonesia.
5. Evaluasi Memori Personal AI Assistant Bahasa Indonesia.

## Sources

- MIT AI Agent Index 2025: https://aiagentindex.mit.edu/
- SWE-Lancer benchmark: https://openai.com/index/swe-lancer/
- SEC-bench repository: https://github.com/SEC-bench/SEC-bench
- CAIBench paper: https://arxiv.org/abs/2510.24317
- MemoryAgentBench dataset: https://www.modelscope.cn/datasets/AI-ModelScope/MemoryAgentBench
- Mozilla Common Voice Indonesian: https://datacollective.mozillafoundation.org/datasets/cmn2e8ats01eno107glwgoasv
- ASR-IndoCSC: https://magichub.com/datasets/indonesian-conversational-speech-corpus/
- WorldSpeech dataset: https://modelscope.cn/datasets/disco-eth/WorldSpeech
- MuMiN dataset: https://mumin-dataset.github.io/index
- Indonesia Political Hoax Dataset: https://data.mendeley.com/datasets/mzx5rd397v
- AI in Indonesian higher education dataset: https://zenodo.org/records/19680489
- AI adoption in Indonesian higher education dataset: https://data.mendeley.com/datasets/b89t4x2c2y

## Writing Handoff

Topik paling menarik untuk proposal inovasi produk adalah asisten debugging praktikum, karena bisa dibuat sebagai produk nyata, dataset bisa dikontrol, evaluasi bisa objektif dengan unit test/rubrik, dan pembeda ilmiahnya jelas.

## Open Questions

- Apakah pengguna lebih suka topik yang dekat dengan software engineering, pendidikan, speech, atau misinformation?
- Apakah skripsi harus tetap berupa produk/prototipe atau boleh lebih eksperimental?
- Apakah memungkinkan melakukan evaluasi kecil dengan manusia?
