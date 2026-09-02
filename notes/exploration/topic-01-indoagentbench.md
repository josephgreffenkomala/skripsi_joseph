---
cssclasses:
  - full-width
---
# Detail Topik 01: IndoAgentBench

Date: 2026-08-21
Updated: 2026-09-03
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)
Status: Kandidat paling matang; belum final dipilih

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia**: IndoAgentBench: Benchmark Berbasis Pasangan Issue Indonesia-Inggris untuk Mengukur Kesenjangan Bahasa pada Coding Agent Repository-Level
- **English**: IndoAgentBench: A Paired Indonesian-English Issue Benchmark for Measuring Language Gaps in Repository-Level Coding Agents

Alternatif judul yang menonjolkan desain eksperimen:

- **Bahasa Indonesia**: Studi Eksperimental Pengaruh Bahasa Instruksi terhadap Kinerja Coding Agent pada Tugas Tingkat Repositori
- **English**: An Experimental Study of Instruction Language Effects on Coding Agent Performance in Repository-Level Tasks

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Coding agent adalah sistem AI yang tidak hanya menulis potongan kode, tetapi juga membaca repositori, menjalankan test, memahami error, dan membuat patch. Masalahnya, banyak agent dan benchmark saat ini sangat berpusat pada Bahasa Inggris. Topik ini ingin menguji apakah instruksi dalam Bahasa Indonesia membuat agent lebih sering gagal dibanding instruksi yang setara dalam Bahasa Inggris.

Penelitian menggunakan **IndoAgentBench** sebagai rancangan evaluasi berpasangan untuk menjalankan tugas pemrograman repository-level dalam beberapa kondisi bahasa. Setiap task memiliki pasangan instruksi Bahasa Inggris dan Bahasa Indonesia yang diaudit agar maknanya setara. Analisis tidak hanya menggunakan skor benar/salah, tetapi juga mengelompokkan kegagalan, seperti salah memahami requirement, salah mencari lokasi kode, salah implementasi, atau gagal validasi test. Skrip pelaksana eksperimen berfungsi sebagai instrumen penelitian untuk menjaga konsistensi perlakuan dan pencatatan data.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

- **Kondisi Saat Ini (Existing State/Literature)**: Benchmark seperti SWE-bench, Multi-SWE-bench, dan SWE-PolyBench sudah menguji kemampuan agent pada repositori nyata. mHumanEval dan HumanEval-XL sudah menguji banyak bahasa natural, termasuk Bahasa Indonesia, tetapi pada level function-level. Ren et al. (2026) sudah menguji efek Bahasa Cina vs Inggris pada SWE-bench Lite.
- **Keterbatasan / Gap**: Belum ada catatan dalam notes yang menunjukkan benchmark repository-level khusus Bahasa Indonesia dengan audit ekuivalensi bilingual, kondisi translate-then-act, failure taxonomy, dan transformasi task anti-kontaminasi.
- **Kontribusi Penelitian (Novelty Contribution)**: Topik ini bukan "pertama menguji efek bahasa natural pada coding agent", karena klaim itu gugur. Kebaruan yang defensible adalah ekstensi terkontrol untuk Bahasa Indonesia low-resource dengan metode audit dan analisis kegagalan yang lebih rinci.

| Fitur / Parameter | Penelitian Terdahulu | Penelitian Ini |
|---|---|---|
| Bahasa natural | Dominan Inggris; Ren et al. menguji Cina | Fokus Bahasa Indonesia vs Inggris |
| Level tugas | Function-level atau repository-level umum | Repository-level coding agent dengan task berpasangan |
| Kondisi mitigasi | Umumnya direct prompt | English baseline, Indonesian direct, translate-then-act |
| Validasi bahasa | Terjemahan sering hanya diasumsikan setara | Audit ekuivalensi bilingual dengan rubrik |
| Analisis kegagalan | Skor akhir/resolution rate | Failure taxonomy berbasis trajectory |
| Kontaminasi benchmark | Risiko task sudah masuk data training | Transformasi task dan audit acceptance criteria |

## 4. Posisi dan Batasan Penelitian

- **Masalah Penelitian**: Belum tersedia bukti empiris yang memadai mengenai apakah coding agent menunjukkan kinerja dan pola kegagalan yang berbeda ketika menerima instruksi Bahasa Indonesia dan Bahasa Inggris yang setara pada tugas tingkat repositori.
- **Pendekatan Penelitian**: Eksperimen berpasangan yang membandingkan kondisi English, Indonesian direct, dan translate-then-act pada task yang sama, disertai audit ekuivalensi bilingual, test suite sebagai oracle, serta analisis trajectory dan taksonomi kegagalan.
- **Batasan Penelitian**: Fokus pada 40-60 task repository-level, satu bahasa pemrograman utama (Python), satu kerangka eksekusi agent, dua model atau keluarga model, dan tiga kondisi bahasa utama.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi / Framework**: SWE-bench atau subset task terkontrol, OpenHands/SWE-agent, skrip eksperimen sederhana, containerized test execution, Python, Git, pytest, dan logging trajectory.
- **Metode / Algoritma / Arsitektur**: Paired experimental design, bilingual equivalence audit, task transformation, automated test oracle, failure taxonomy, confidence interval, paired significance test.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

- **Metode Pengujian**: Jalankan task yang sama pada beberapa kondisi bahasa dan bandingkan hasil per task. Gunakan test suite sebagai oracle utama, lalu analisis trajectory untuk failure taxonomy.
- **Metrik Evaluasi**: Task resolution rate, test pass rate, invalid patch rate, regression rate, token/cost, waktu penyelesaian, jumlah tool calls, failure category, dan agreement antar annotator untuk audit ekuivalensi.

## 7. Pemetaan ke Bab Proposal dan Skripsi Ilmiah Akademik (Chapter Mapping)

- **Bab 1 Proposal**: Latar belakang penggunaan coding agent, kesenjangan bukti mengenai pengaruh bahasa instruksi, rumusan masalah, batasan, tujuan, serta manfaat ilmiah dan praktis penelitian.
- **Bab 2 Proposal**: mHumanEval, HumanEval-XL, SWE-bench, Multi-SWE-bench, SWE-PolyBench, Ren et al. (2026), dan benchmark agent terkait.
- **Bab 3 Proposal**: Data dan sumber task, desain eksperimen berpasangan, audit bilingual, kondisi perlakuan, instrumen pelaksana, metrik evaluasi, uji statistik, dan analisis kegagalan.
- **Bab 4 Proposal**: Jadwal pengumpulan task, penyiapan instrumen eksperimen, studi pendahuluan, eksperimen utama, analisis, dan penulisan.
- **Bab 1 Skripsi**: Latar belakang, perumusan masalah, batasan penelitian, tujuan, dan manfaat penelitian.
- **Bab 2 Skripsi**: Tinjauan pustaka tentang coding agent, benchmark tingkat repositori, evaluasi multibahasa, ekuivalensi terjemahan, dan analisis kegagalan.
- **Bab 3 Skripsi**: Metodologi yang mencakup data task, kondisi bahasa, audit ekuivalensi, kontrol eksperimen, metrik, dan rancangan analisis statistik.
- **Bab 4 Skripsi**: Implementasi lingkungan dan instrumen eksperimen, penyusunan task berpasangan, eksekusi terisolasi, test oracle, serta pencatatan trajectory.
- **Bab 5 Skripsi**: Hasil perbandingan antarbahasa, analisis berpasangan, taksonomi kegagalan, pembahasan terhadap studi terdahulu, dan keterbatasan temuan.
- **Bab 6 Skripsi**: Simpulan yang menjawab perumusan masalah dan saran penelitian lanjutan.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: Cocok untuk pembimbing dengan minat Software Engineering, AI/LLM, evaluasi sistem, atau pendidikan pemrograman.
- **Ketersediaan data/infrastruktur**: Feasible jika memakai task publik atau task kecil yang dibuat sendiri. Perlu akses API/model dan lingkungan eksekusi test.
- **Risiko kegagalan**: Biaya eksperimen agent membengkak; task terlalu sulit; pasangan terjemahan tidak setara; hasil beda bahasa tidak signifikan.
- **Fallback plan**: Kurangi task menjadi 30-40, gunakan satu model utama, lalu fokus pada estimasi efek bahasa secara berpasangan dan analisis failure taxonomy dengan batas generalisasi yang dinyatakan secara eksplisit.

## 9. Catatan Sumber & Literatur (Source Notes)

### 9.1 Sumber Utama (Core References)

| # | Judul | Penulis | Tahun | DOI/URL | Relevansi | BibTeX Key |
|---|---|---:|---|---|---|---|
| 1 | Chinese Language Is Not More Efficient Than English in Vibe Coding | Ren et al. | 2026 | https://arxiv.org/abs/2604.14210 | Pembanding utama; membatalkan klaim "pertama" secara umum | ren2026vibecoding |
| 2 | mHumanEval | Raihan et al. | 2025 | https://aclanthology.org/2025.naacl-long.570/ | Bukti multilingual code generation termasuk Bahasa Indonesia pada function-level | raihan2025mhumeval |
| 3 | HumanEval-XL | Peng et al. | 2024 | https://aclanthology.org/2024.lrec-main.735/ | Benchmark multilingual function-level | peng2024humanevalxl |
| 4 | Multi-SWE-bench | Zan et al. | 2025 | https://arxiv.org/abs/2504.02605 | Repository-level benchmark; multilingual dalam arti bahasa pemrograman | zan2025multiswebench |
| 5 | SWE-PolyBench | Rashid et al. | 2025 | https://arxiv.org/abs/2504.08703 | Repository-level benchmark multi-language programming | rashid2025swepolybench |

### 9.2 Gap yang Ditemukan dari Literatur

Klaim yang boleh dipakai: Bahasa Indonesia repository-level masih menjadi celah; translate-then-act, audit ekuivalensi bilingual, failure taxonomy, dan transformasi task adalah diferensiasi metodologis.

Klaim yang tidak boleh dipakai: "pertama menguji efek bahasa natural pada coding agent repository-level", "belum ada benchmark bahasa natural untuk coding agent", atau "belum ada multilingual natural language pada SWE-bench".

## 10. Penyerahan ke Penulisan LaTeX (Draft Handoff)

- **Target File**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, `template/proposal/chapters/bab3-metodologi.tex`
- **Kebutuhan Gambar/Diagram**: Bagan alir metodologi dan instrumen eksperimen, tabel kondisi bahasa, tabel failure taxonomy, serta diagram proses audit ekuivalensi.
- **Pertanyaan ke Pengguna**: Agent apa yang ingin dipakai? Berapa budget API/model? Task akan diambil dari benchmark existing, dibuat sendiri, atau campuran?
