---
cssclasses:
  - full-width
---
# Detail Topik 05: Studi Empiris Pengelolaan Riwayat Eksekusi pada Coding Agent Tingkat Repositori

Date: 2026-08-21  
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)  
Status: Kandidat baru — direkomendasikan secara bersyarat

## 1. Opsi Judul (Title Candidates)

- **Bahasa Indonesia, rekomendasi**: *Studi Empiris Pengelolaan Riwayat Eksekusi pada Coding Agent Tingkat Repositori*
- **Bahasa Indonesia, alternatif produk**: *Pengembangan Harness Evaluasi Kebijakan Konteks untuk Coding Agent Tingkat Repositori*
- **English**: *An Empirical Study of Execution-History Management in Repository-Level Coding Agents*

Judul yang paling aman adalah judul pertama. Judul tersebut tidak menjanjikan algoritma kompresi baru dan memungkinkan hasil penelitian menunjukkan bahwa kebijakan tertentu tidak selalu unggul.

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)

Coding agent bekerja melalui rangkaian langkah: menerima issue, mencari file, membaca kode, menjalankan tes, melihat error, mengedit file, lalu menjalankan tes kembali. Setiap langkah menghasilkan riwayat eksekusi. Jika semua riwayat dipertahankan, konteks dapat menjadi besar dan mahal. Jika terlalu banyak dipotong, agent dapat kehilangan informasi penting seperti penyebab error, file yang sudah diubah, atau hasil tes sebelumnya.

Penelitian ini membuat harness yang menjalankan agent pada task pemrograman yang sama, tetapi menyajikan riwayat eksekusi dengan beberapa kebijakan:

1. **Full chronological history**: seluruh riwayat dipertahankan.
2. **Recent-only history**: hanya sejumlah langkah terakhir dipertahankan.
3. **Summarized history**: riwayat lama diringkas, sedangkan langkah terbaru dipertahankan secara rinci.
4. **Task-relevant history**: hanya interaksi yang berkaitan dengan file, simbol, atau error yang sedang dikerjakan dipertahankan.

Variabel lain harus dibuat sama: model, agent scaffold, tools, repository commit, prompt task, batas langkah, dan prosedur evaluasi.

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)

### Kondisi Saat Ini

Trajectory coding agent memang sudah dapat direkam sebagai pasangan thought/action/observation serta query konteks aktual yang diberikan ke model. SWE-agent juga mendokumentasikan metrik seperti jumlah langkah dan biaya trajectory. 

Literatur terbaru sudah bergerak lebih spesifik. **ContextBench** memperkenalkan evaluasi proses untuk retrieval konteks pada coding agent dengan metrik context recall, precision, dan efficiency, serta gold context pada 1.136 task dari 66 repositori. **Context as a Tool (CAT)** mengusulkan context management sebagai tool yang dapat dipanggil agent, dengan long-term summary dan short-term recent interactions, serta membandingkannya dengan baseline kompresi statis.

### Keterbatasan / Gap yang Masih Bisa Diambil

Gap yang realistis bukan ketiadaan penelitian context management. Gap yang masih dapat diambil untuk skripsi adalah:

- belum tentu tersedia studi mahasiswa yang mereproduksi perbandingan beberapa kebijakan retensi pada satu agent dan satu model dengan kontrol eksperimen yang eksplisit;
- hasil akhir task saja belum cukup untuk menunjukkan informasi mana yang hilang atau dipertahankan;
- trade-off antara success rate, context token, input token, tool calls, dan jenis kegagalan dapat dianalisis dalam satu protokol yang sederhana dan dapat diulang;
- task dengan panjang trajectory berbeda dapat memperlihatkan kapan kebijakan recent-only mulai merusak pemulihan dari error.

Pernyataan terakhir adalah hipotesis yang perlu diuji, bukan fakta yang boleh ditulis sebagai kesimpulan sebelum eksperimen.

### Kebaruan Solusi Ini

Kebaruan yang dapat dipertahankan:

1. harness evaluasi terbuka/reproduktif untuk menukar kebijakan pengelolaan riwayat tanpa mengubah agent utama;
2. controlled ablation study pada benchmark repository-level dengan empat kebijakan yang didefinisikan secara operasional;
3. analisis Pareto antara keberhasilan penyelesaian task dan biaya konteks;
4. taxonomy kegagalan yang menghubungkan kehilangan konteks dengan kegagalan localization, error recovery, regression checking, atau patch submission.

Klaim yang harus dihindari:

- “penelitian pertama tentang context management pada coding agent”;
- “menciptakan metode kompresi baru”;
- “task-relevant history pasti paling baik”;
- generalisasi ke semua model, agent, bahasa pemrograman, dan jenis task.

### Matriks Perbandingan Novelty

| Fitur / Parameter | Baseline / Literatur | Topik Ini (Proposed) |
|---|---|---|
| Fokus | Retrieval konteks atau metode kompresi agent | Perbandingan kebijakan retensi riwayat dalam kondisi terkontrol |
| Perubahan utama | Sering memperkenalkan framework/model baru | Hanya kebijakan penyusunan konteks yang dimanipulasi |
| Evaluasi | Success rate, retrieval metrics, atau bounded context | Success, token, tool calls, runtime, trajectory, dan failure taxonomy |
| Kontribusi | Metode/framework baru pada karya terkait | Harness eksperimen dan bukti trade-off yang dapat direproduksi |
| Klaim novelty | Harus dibandingkan langsung dengan ContextBench dan CAT | Novelty moderat; aman bila diposisikan sebagai studi empiris terkontrol |

## 4. Perumusan Produk & Masalah (UGM Inovasi Produk)

### Masalah Nyata

Coding agent repository-level menghasilkan riwayat interaksi yang panjang. Praktik mempertahankan, memotong, atau meringkas riwayat dapat memengaruhi kemampuan agent menyelesaikan task, tetapi keputusan tersebut sering tertanam dalam implementasi agent dan sulit dibandingkan secara adil.

### Solusi / Produk Inovatif

Prototipe **Execution Context Evaluation Harness** yang terdiri atas:

- adapter agent dan model;
- trajectory recorder;
- context-policy engine untuk empat kebijakan;
- token/cost/latency meter;
- evaluator patch dan test;
- generator laporan serta klasifikasi kegagalan.

Produk ini harus dipandang sebagai alat eksperimen, bukan sebagai coding agent baru.

### Batasan Masalah/Produk

- satu keluarga LLM dan satu agent scaffold;
- satu benchmark utama, misalnya SWE-bench Verified atau subset yang dapat dijalankan;
- 20–50 task terpilih dengan kriteria panjang dan bahasa yang jelas;
- maksimal empat kebijakan konteks;
- summarization menggunakan model/prosedur tetap, bukan prompt yang berubah per task;
- tidak melatih model baru;
- tidak mengklaim hasil berlaku untuk seluruh coding agent;
- biaya API, nondeterminism, dan perubahan versi model dicatat sebagai faktor eksperimen.

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)

- **Teknologi**: Python, API LLM, Docker, Git, benchmark SWE, SQLite/JSONL untuk trajectory, dan pandas untuk agregasi hasil.
- **Model agent**: SWE-agent atau scaffold repository-level yang memiliki log trajectory dan evaluator patch yang jelas.
- **Representasi trajectory**: task, message, tool call, observation, file/symbol touched, test result, dan token usage.
- **Context policy engine**: modul deterministik yang menerima trajectory hingga waktu `t` dan mengembalikan konteks yang dikirim ke model.
- **Ringkasan**: summary terstruktur dengan field tujuan, temuan, file relevan, perubahan, error terakhir, tes yang sudah dijalankan, dan open hypotheses.
- **Relevance filter**: aturan eksplisit berbasis file/error/simbol/task, dengan fallback agar tidak diam-diam memakai informasi masa depan.
- **Kontrol eksperimen**: seed jika tersedia, temperature, versi prompt, commit repository, time budget, step budget, dan retry policy harus dikunci.

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)

### Metode Pengujian

Gunakan within-task comparison: setiap task dijalankan pada semua kebijakan dengan konfigurasi agent yang sama. Karena hasil LLM bersifat nondeterministik, gunakan beberapa replikasi per kondisi bila biaya memungkinkan. Jika biaya terbatas, catat ini sebagai batasan dan gunakan pasangan task yang sama serta konfigurasi deterministik yang tersedia.

### Metrik Evaluasi

- **Task success**: patch lulus test resmi atau evaluator benchmark.
- **Patch correctness**: test pass rate dan pemeriksaan regresi.
- **Context cost**: input tokens, output tokens, total tokens, peak context size, dan estimasi biaya.
- **Operational efficiency**: jumlah tool calls, jumlah turn, wall-clock runtime, dan jumlah retry.
- **Context quality**: recall/precision terhadap file atau context gold jika benchmark mendukung; jika tidak, gunakan anotasi manual terbatas dan laporkan keterbatasannya.
- **Failure taxonomy**: kehilangan informasi error, salah mengingat file yang berubah, pengulangan eksplorasi, regression setelah edit, dan premature submission.
- **Trade-off**: success per 1.000 token, biaya per task berhasil, serta frontier keberhasilan-versus-konteks.

### Hipotesis Awal

- H1: full history tidak selalu menghasilkan success rate tertinggi ketika trajectory panjang.
- H2: recent-only mengurangi biaya konteks, tetapi lebih rentan kehilangan informasi lintas fase.
- H3: summary atau task-relevant history dapat mengurangi biaya tanpa penurunan success yang besar pada sebagian task.
- H4: dampak kebijakan berbeda menurut panjang trajectory, jumlah error recovery, dan jumlah file yang disentuh.

Hipotesis ini harus diperlakukan sebagai dugaan yang dapat ditolak.

## 7. Pemetaan ke Bab Skripsi/Proposal

- **Bab 1**: masalah pertumbuhan execution history, dampaknya pada biaya dan kesinambungan reasoning, rumusan produk harness, tujuan, manfaat, dan batasan.
- **Bab 2**: coding agent repository-level, SWE-bench, trajectory, context retrieval, context compression, ContextBench, CAT, dan posisi penelitian.
- **Bab 3**: definisi formal context policy, desain eksperimen, variabel kontrol, benchmark subset, metrik, dan prosedur replikasi.
- **Bab 4**: arsitektur harness, pipeline trajectory, context-policy engine, penyimpanan data, dan rancangan laporan.
- **Bab 5**: implementasi adapter, recorder, policy engine, evaluator, dan dashboard/laporan.
- **Bab 6**: hasil, uji statistik/deskriptif, analisis trade-off, failure taxonomy, ancaman validitas, kesimpulan, dan saran.

Untuk proposal, isi Bab 4–6 ditulis sebagai rancangan dan rencana pengujian, bukan hasil yang sudah terjadi.

## 8. Risiko & Kelayakan Akademik (Risk & Academic Feasibility)

- **Kesesuaian dengan bidang dosen pembimbing**: sesuai dengan AI engineering dan software engineering; perlu dikonfirmasi apakah pembimbing menerima skripsi berbasis evaluasi agent.
- **Ketersediaan data/infrastruktur**: benchmark dan kode agent tersedia, tetapi eksperimen membutuhkan API/model, storage trajectory, waktu komputasi, dan biaya.
- **Risiko kebaruan**: tinggi. CAT dan ContextBench membuat klaim luas sulit dipertahankan.
- **Risiko metodologis**: policy filter dan summarizer dapat mengubah kualitas agent dengan cara yang tidak sebanding; definisi “task-relevant” juga berpotensi subjektif.
- **Risiko biaya/nondeterminism**: hasil dapat bervariasi antar-run dan benchmark repository-level mahal.
- **Fallback plan**: batasi task pada subset 20–30; gunakan replay trajectory untuk membandingkan context assembly bila rerun agent terlalu mahal; fokuskan kontribusi pada harness dan analisis failure, bukan peningkatan success rate.
- **Keputusan kelayakan**: **layak bersyarat**, dengan rekomendasi akademik ***. Naikkan menjadi rekomendasi kuat hanya setelah pilot kecil menunjukkan empat policy dapat diimplementasikan tanpa mengubah tool behavior dan hasil dapat direproduksi.

## 9. Catatan Sumber & Literatur (Source Notes)

### 9.1 Sumber Utama (Core References)

| # | Judul | Penulis | Tahun | DOI/URL | Relevansi | BibTeX Key |
|---|---|---|---:|---|---|---|
| 1 | ContextBench: A Benchmark for Context Retrieval in Coding Agents | Han Li dkk. | 2026 | [arXiv:2602.05892](https://arxiv.org/abs/2602.05892) | Baseline proses: context recall, precision, efficiency, dan gold context | `li2026contextbench` |
| 2 | Context as a Tool: Context Management for Long-Horizon SWE-Agents | Shukai Liu dkk. | 2025 | [arXiv:2512.22087](https://arxiv.org/abs/2512.22087) | Pembanding langsung untuk summary, recent working memory, dan static compression | `liu2025contexttool` |
| 3 | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | John Yang dkk. | 2024 | [NeurIPS paper](https://papers.neurips.cc/paper_files/paper/2024/file/5a7c947568c1b1328ccc5230172e1e7c-Paper-Conference.pdf) | Agent, ACI, trajectory, turns, cost, dan repository-level issue resolution | `yang2024sweagent` |
| 4 | SWE-agent trajectory documentation | SWE-agent project | Berjalan | [Trajectory format](https://github.com/SWE-agent/SWE-agent/blob/main/docs/usage/trajectories.md) | Format observasi/action/query untuk recorder dan replay | `sweagent-trajectory` |

### 9.2 Gap yang Ditemukan dari Literatur

Gap yang tersisa cukup sempit: penelitian ini dapat memberikan replikasi dan ablation study yang transparan mengenai kebijakan retensi history pada konfigurasi terbatas. Nilai akademiknya bergantung pada disiplin kontrol eksperimen, analisis kegagalan, dan publikasi artifact. Tanpa itu, topik ini hanya menjadi perbandingan implementasi yang sudah dikenal.

## 10. Penyerahan ke Penulisan LaTeX (Draft Handoff)

- **Target File**: proposal/chapters/ jika topik dipilih untuk proposal; kemudian skripsi/chapters/ untuk implementasi dan hasil.
- **Kebutuhan Gambar/Diagram**: bagan alir eksperimen, arsitektur harness, sequence diagram agent–tool–policy engine, skema data trajectory, dan diagram Pareto success-versus-context-cost.
- **Pilot wajib sebelum finalisasi**: jalankan 3–5 task pada full, recent-only, dan summary; ukur apakah policy benar-benar mengubah konteks yang dikirim dan apakah log dapat direplay.
- **Pertanyaan ke Pengguna**: model/agent apa yang realistis digunakan, berapa anggaran API, dan apakah dosen menginginkan produk yang dapat dipakai atau studi evaluasi murni?
