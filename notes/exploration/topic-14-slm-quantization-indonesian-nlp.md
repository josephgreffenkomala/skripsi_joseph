---
cssclasses:
  - full-width
---
# Detail Topik 14: Evaluasi Faktorial Kuantisasi Small Language Model untuk NLP Bahasa Indonesia

Date: 2026-08-31

Updated: 2026-09-03

Catalog Reference: [`topic-catalog.md`](topic-catalog.md)

## Status Singkat

**Kandidat layak dengan desain yang telah dipersempit; belum dipilih secara final.** Fokus kandidat ini adalah evaluasi faktorial terkontrol atas hubungan antara **ukuran model**, **tingkat kuantisasi**, dan **jenis tugas NLP Bahasa Indonesia**, dengan kualitas serta biaya inferensi yang diukur pada lingkungan CPU-only yang sama.

Model utama yang direncanakan adalah dua ukuran dalam keluarga Qwen3, yaitu Qwen3-0.6B dan Qwen3-1.7B. Penggunaan satu keluarga model mengurangi variasi arsitektur dan runtime sehingga pengaruh ukuran model dan kuantisasi dapat dianalisis dengan lebih terarah. Penelitian tidak akan melakukan pelatihan model besar, *fine-tuning*, *quantization-aware training* (QAT), atau evaluasi model 4B ke atas.

Kebaruan yang ditargetkan bersifat **empiris dan metodologis**, bukan berupa algoritma kuantisasi baru. Klaim sebagai penelitian “pertama” belum boleh digunakan sebelum pencarian literatur sistematis selesai.

## 1. Opsi Judul

### Judul utama

- **Bahasa Indonesia**: *Studi Empiris Interaksi Ukuran Model dan Tingkat Kuantisasi terhadap Kualitas NLP Bahasa Indonesia dan Efisiensi Inferensi CPU*
- **Bahasa Inggris**: *An Empirical Study of Model Size and Quantization Level Interactions on Indonesian NLP Quality and CPU Inference Efficiency*

### Alternatif berorientasi eksperimen

- **Bahasa Indonesia**: *Analisis Faktorial Ukuran Model dan Tingkat Kuantisasi pada Tugas NLP Bahasa Indonesia di Lingkungan CPU-Only*
- **Bahasa Inggris**: *A Factorial Analysis of Model Size and Quantization Level on Indonesian NLP Tasks in CPU-Only Environments*

### Alternatif lebih ringkas

- **Bahasa Indonesia**: *Evaluasi Degradasi Kemampuan Bahasa Indonesia pada Small Language Model Qwen3 Terkuantisasi*
- **Bahasa Inggris**: *Evaluating Indonesian Language Capability Degradation in Quantized Qwen3 Small Language Models*

## 2. Penjelasan Sederhana

Model bahasa berukuran kecil dapat dijalankan pada perangkat konsumen, tetapi ukuran parameter dan tingkat presisi bobot memengaruhi kualitas jawaban, penggunaan memori, ukuran berkas, serta kecepatan inferensi. Kuantisasi mengurangi presisi representasi bobot agar model lebih hemat sumber daya. Akan tetapi, model yang lebih kecil mungkin lebih sensitif terhadap kuantisasi, dan dampaknya dapat berbeda antarjenis tugas Bahasa Indonesia.

Penelitian ini tidak hanya membandingkan model sebelum dan sesudah dikuantisasi. Eksperimen akan menguji kombinasi dua ukuran Qwen3, tiga tingkat representasi bobot, dan dua tugas NLP Bahasa Indonesia. Hasilnya akan digunakan untuk menjawab apakah terdapat interaksi antara ukuran model dan tingkat kuantisasi, tugas mana yang paling sensitif, serta konfigurasi mana yang memberikan keseimbangan terbaik antara kualitas, latensi, penggunaan memori, dan ukuran model.

Penelitian dilaksanakan sebagai **eksperimen komputasional terkontrol**. Skrip evaluasi digunakan sebagai instrumen penelitian untuk menjalankan model dan dataset secara konsisten, mencatat metadata lingkungan, menyimpan hasil mentah, serta menghitung metrik. Luaran utamanya adalah temuan empiris dan analisis ilmiah mengenai pengaruh serta interaksi faktor-faktor yang diuji.

## 3. Fokus dan Pertanyaan Penelitian

### Fokus utama

Hubungan yang akan diuji dapat diringkas sebagai berikut:

> ukuran model × tingkat kuantisasi × jenis tugas NLP Bahasa Indonesia → kualitas tugas + biaya inferensi CPU

Analisis tidak berhenti pada efek tunggal setiap faktor. Fokus ilmiahnya adalah mengetahui apakah pengaruh kuantisasi berubah ketika ukuran model atau jenis tugas berubah.

### Pertanyaan penelitian sementara

1. Bagaimana tingkat kuantisasi memengaruhi kualitas Qwen3-0.6B dan Qwen3-1.7B pada tugas NLP Bahasa Indonesia?
2. Apakah terdapat interaksi antara ukuran model dan tingkat kuantisasi terhadap degradasi kualitas?
3. Apakah dampak kuantisasi berbeda menurut karakteristik tugas NLP Bahasa Indonesia?
4. Konfigurasi mana yang memberikan *Pareto trade-off* terbaik antara kualitas, latensi, *throughput*, penggunaan RAM, dan ukuran model pada lingkungan CPU-only?

Pertanyaan tambahan mengenai apakah kuantisasi memberikan dampak yang tidak proporsional terhadap Bahasa Indonesia dibanding Bahasa Inggris dapat dipertimbangkan setelah ketersediaan dataset berpasangan dan kelayakan waktu diverifikasi. Pertanyaan lintas bahasa bukan scope minimum.

## 4. Analisis Kebaruan

### 4.1 Kondisi Penelitian Sebelumnya

- IndoLEM dan IndoNLU telah menyediakan benchmark serta baseline untuk pemahaman Bahasa Indonesia.
- Abdurrahman et al. (2023) telah mengevaluasi kuantisasi pada IndoBERT. Oleh karena itu, kandidat ini tidak boleh diklaim sebagai penelitian pertama tentang kuantisasi model Bahasa Indonesia.
- Metode dan skema kuantisasi seperti INT8, GPTQ, AWQ, serta format GGUF telah digunakan secara luas untuk mengurangi kebutuhan memori model bahasa.
- Dokumentasi Qwen dan `llama.cpp` telah menyediakan dukungan untuk menjalankan dan menguantisasi Qwen3. Implementasi kuantisasi itu sendiri bukan kontribusi baru penelitian ini.

### 4.2 Gap yang Ditargetkan

Gap sementara yang akan diverifikasi adalah belum ditemukannya evaluasi terkontrol yang secara bersamaan:

1. menggunakan beberapa ukuran SLM generatif dalam satu keluarga model;
2. membandingkan beberapa tingkat kuantisasi dengan runtime dan perangkat keras yang sama;
3. mengevaluasi lebih dari satu karakteristik tugas NLP Bahasa Indonesia;
4. menganalisis interaksi ukuran model, tingkat kuantisasi, dan jenis tugas; serta
5. menghubungkan kualitas tugas dengan latensi, *throughput*, RAM, dan ukuran berkas pada inferensi CPU-only.

Kombinasi tersebut adalah **hipotesis kebaruan**, bukan fakta final. Pencarian literatur sistematis tetap wajib dilakukan sebelum topik diterima dan sebelum frasa “belum ada” digunakan dalam proposal.

### 4.3 Kebaruan yang Aman

Rumusan kontribusi sementara yang defensible adalah:

> Penelitian ini menawarkan evaluasi faktorial terkontrol atas hubungan antara ukuran model, tingkat kuantisasi, dan karakteristik tugas NLP Bahasa Indonesia, dengan mengukur kualitas serta biaya inferensi pada lingkungan CPU-only yang konsisten dan prosedur eksperimen yang dapat direproduksi.

Kontribusi ilmiah yang ditargetkan dibagi menjadi dua lapisan utama:

| Lapisan kontribusi | Bentuk kontribusi |
|---|---|
| Empiris | Bukti mengenai degradasi kualitas Qwen3 kecil pada beberapa tingkat kuantisasi dan tugas Bahasa Indonesia |
| Metodologis | Desain faktorial dan analisis interaksi ukuran model × tingkat kuantisasi × jenis tugas |

Skrip eksperimen, konfigurasi, hasil mentah, dan metadata lingkungan akan disertakan sebagai artefak pendukung reprodusibilitas, bukan sebagai sumber kebaruan tersendiri.

### 4.4 Batas Klaim

Penelitian tidak akan mengklaim:

- algoritma atau metode kuantisasi baru;
- penelitian pertama yang menguantisasi model Bahasa Indonesia;
- hasil yang berlaku untuk semua SLM, bahasa, CPU, atau runtime;
- bahwa kuantisasi selalu mempercepat inferensi atau selalu menurunkan kualitas;
- bahwa perbedaan Q8_0 dan Q4_K_M hanya disebabkan oleh nominal bit-width tanpa mempertimbangkan implementasi format GGUF.

## 5. Posisi Penelitian dan Batasan

### Masalah penelitian

Belum tersedia bukti empiris yang memadai untuk menjelaskan bagaimana ukuran model dan tingkat kuantisasi berinteraksi dalam memengaruhi kualitas tugas NLP Bahasa Indonesia serta biaya inferensi pada CPU konsumen. Jumlah parameter atau ukuran berkas saja tidak cukup untuk menerangkan konfigurasi yang memberikan keseimbangan kualitas dan efisiensi, sedangkan kuantisasi yang lebih agresif dapat menimbulkan degradasi yang berbeda antarukuran model dan karakteristik tugas.

### Pendekatan penelitian

Penelitian menggunakan eksperimen faktorial terkontrol dengan prosedur berikut:

- memvariasikan ukuran model, tingkat kuantisasi, dan jenis tugas sebagai faktor eksperimen;
- mengendalikan runtime, perangkat keras, *warm-up*, jumlah *thread*, panjang konteks, dan konfigurasi *decoding*;
- menggunakan contoh uji dan protokol evaluasi yang sama pada konfigurasi yang dibandingkan;
- mencatat versi model, dataset, runtime, CPU, *seed*, dan konfigurasi eksperimen;
- mengukur kualitas, latensi, *throughput*, penggunaan RAM, dan ukuran berkas; serta
- menganalisis efek utama, efek interaksi, degradasi relatif terhadap baseline, interval kepercayaan, dan *Pareto frontier*.

Skrip berbasis CLI hanya berfungsi sebagai instrumen untuk mengotomatisasi prosedur di atas dan menjaga konsistensi pengukuran.

### Batasan penelitian

1. Lingkungan utama hanya satu laptop: AMD Ryzen 3 5300U, RAM 9 GB, tanpa GPU, dan ruang penyimpanan kosong awal sekitar 8,5 GB.
2. Model inti dibatasi pada Qwen3-0.6B dan Qwen3-1.7B dalam tahap *post-training* yang sama.
3. Representasi inti dibatasi pada BF16/F16 sebagai baseline sesuai dukungan runtime, Q8_0, dan Q4_K_M.
4. Runtime utama dibatasi pada satu versi `llama.cpp` dengan format GGUF.
5. Eksperimen final menggunakan dua tugas Bahasa Indonesia dengan keluaran yang dapat dinilai secara otomatis.
6. Mode *thinking* dinonaktifkan, panjang konteks dan jumlah token keluaran dibatasi, serta konfigurasi decoding disamakan.
7. Model akan dievaluasi secara berurutan untuk membatasi penggunaan disk.
8. Model 4B atau lebih besar, *fine-tuning*, QAT, GPTQ, AWQ, INT2/INT3, dan perbandingan banyak runtime tidak termasuk scope inti.
9. Hasil hanya digeneralisasikan pada model, tugas, runtime, dan perangkat keras yang diuji.

## 6. Landasan Teknik dan Ilmiah

- **Small Language Model (SLM)**: dalam penelitian ini didefinisikan secara operasional sebagai model generatif dengan ukuran hingga 1,7 miliar parameter yang dapat dijalankan pada CPU konsumen yang tersedia.
- **Kuantisasi bobot**: pengurangan presisi representasi bobot untuk menurunkan kebutuhan penyimpanan dan memori. Penelitian berfokus pada *post-training weight quantization* yang tersedia melalui `llama.cpp`.
- **GGUF**: format model untuk ekosistem `llama.cpp` yang menyimpan bobot, metadata model, tokenizer, dan konfigurasi yang diperlukan untuk inferensi lokal.
- **Q8_0 dan Q4_K_M**: skema kuantisasi GGUF yang menjadi perlakuan inti. Keduanya akan disebut dengan nama format aktual, bukan disederhanakan sebagai INT8 dan INT4 murni.
- **Desain faktorial**: desain yang memungkinkan estimasi efek ukuran model, tingkat kuantisasi, jenis tugas, dan interaksi di antara faktor-faktor tersebut.
- **Pareto frontier**: kumpulan konfigurasi yang tidak dapat ditingkatkan pada satu dimensi, misalnya kualitas, tanpa memperburuk dimensi lain seperti latensi atau memori.

## 7. Rencana Pengujian dan Parameter Ukur

### 7.1 Desain Minimum

| Faktor | Level yang direncanakan |
|---|---|
| Ukuran model | Qwen3-0.6B, Qwen3-1.7B |
| Representasi bobot | BF16/F16, Q8_0, Q4_K_M |
| Jenis tugas | Satu tugas pilihan ganda/klasifikasi berbasis prompt dan satu tugas QA singkat |
| Runtime | Satu versi `llama.cpp` |
| Perangkat | Satu CPU dan konfigurasi sistem yang tetap |

Desain minimum menghasilkan 2 × 3 × 2 = **12 kombinasi utama**. Pengukuran performa setiap kombinasi akan diulang 3–5 kali setelah *warm-up*. Pengujian kualitas menggunakan contoh yang sama, prompt yang sama, suhu deterministik, batas keluaran yang sama, serta parser jawaban yang terdokumentasi.

Dataset final belum dikunci. Kandidat akan dipilih berdasarkan lisensi, stabilitas test split, ukuran data, representasi Bahasa Indonesia, kesesuaian dengan model generatif, dan ketersediaan metrik otomatis. IndoMMLU dapat dipertimbangkan untuk tugas pilihan ganda, sedangkan subset Bahasa Indonesia dari benchmark QA dapat dipertimbangkan untuk tugas jawaban singkat.

### 7.2 Metrik

- **Kualitas tugas**: akurasi untuk pilihan ganda; exact match dan token-level F1 untuk QA singkat.
- **Degradasi kualitas**: perubahan absolut dan relatif terhadap baseline BF16/F16 pada ukuran model yang sama.
- **Efisiensi**: waktu pemuatan model, *time to first token*, latensi total, token per detik, dan *peak* RAM.
- **Kompresi**: ukuran berkas dan rasio kompresi terhadap baseline.
- **Trade-off**: konfigurasi pada *Pareto frontier* kualitas–latensi–memori–ukuran berkas.
- **Reproducibility**: identifier model dan dataset, hash berkas bila tersedia, versi `llama.cpp`, opsi kompilasi, CPU, jumlah thread, panjang konteks, seed, prompt, dan konfigurasi decoding.

### 7.3 Analisis

1. Bandingkan setiap konfigurasi kuantisasi dengan baseline pada ukuran model dan contoh yang sama.
2. Ukur apakah degradasi akibat Q8_0 dan Q4_K_M berbeda antara Qwen3-0.6B dan Qwen3-1.7B.
3. Uji apakah pola degradasi berbeda antara kedua jenis tugas.
4. Laporkan interval kepercayaan bootstrap untuk metrik kualitas jika sesuai.
5. Pisahkan variabilitas kualitas model dari variabilitas pengukuran performa sistem.
6. Sajikan hasil sebagai tabel faktorial, grafik degradasi, grafik kualitas terhadap biaya, dan *Pareto frontier*.

Analisis tidak boleh menyimpulkan hubungan kausal di luar faktor yang dikontrol. Perbedaan hasil hanya berlaku untuk konfigurasi eksperimen yang diuji.

## 8. Pemetaan ke Bab Proposal dan Skripsi Ilmiah Akademik

- **Proposal Bab 1**: keterbatasan inferensi SLM pada perangkat konsumen, kesenjangan bukti mengenai pengaruh ukuran dan kuantisasi, rumusan masalah, tujuan, batasan, serta manfaat ilmiah dan praktis penelitian.
- **Proposal Bab 2**: SLM multibahasa, Qwen3, kuantisasi bobot, GGUF/`llama.cpp`, benchmark NLP Bahasa Indonesia, penelitian kuantisasi IndoBERT, evaluasi sistem CPU, dan gap penelitian.
- **Proposal Bab 3**: deskripsi umum penelitian, data, desain faktorial, rancangan metode, kontrol lingkungan, prosedur pengujian, metrik, serta metode analisis.
- **Proposal Bab 4**: jadwal verifikasi literatur, studi pendahuluan pada perangkat keras, penyiapan instrumen eksperimen, pelaksanaan eksperimen, analisis, dan penulisan.
- **Skripsi Bab 1**: latar belakang, perumusan masalah, batasan penelitian, tujuan, dan manfaat penelitian.
- **Skripsi Bab 2**: tinjauan pustaka mengenai SLM, kuantisasi, evaluasi NLP Bahasa Indonesia, inferensi CPU, dan penelitian terdahulu yang menjadi dasar gap.
- **Skripsi Bab 3**: metodologi penelitian yang mencakup data, faktor dan variabel eksperimen, rancangan metode, kontrol eksperimen, serta rancangan pengujian dan analisis.
- **Skripsi Bab 4**: implementasi lingkungan dan instrumen eksperimen, integrasi model/dataset dengan `llama.cpp`, prosedur pengukuran sumber daya, dan validasi parser.
- **Skripsi Bab 5**: hasil eksperimen faktorial, analisis efek utama dan interaksi, degradasi kualitas, *Pareto frontier*, pembahasan terhadap penelitian terdahulu, serta keterbatasan temuan.
- **Skripsi Bab 6**: simpulan yang menjawab perumusan masalah dan tujuan penelitian serta saran untuk penelitian lanjutan.

## 9. Risiko dan Kelayakan Akademik

- **Risiko kebaruan**: penelitian baru dapat menunjukkan kombinasi eksperimen yang serupa. Mitigasinya adalah melakukan pencarian literatur sistematis sebelum topik diterima dan mempertahankan kontribusi pada analisis interaksi serta artefak yang dapat direproduksi.
- **Risiko kualitas model**: Qwen3-0.6B dapat memberikan skor rendah atau format jawaban tidak stabil. Mitigasinya adalah pilot pada dataset kandidat, prompt deterministik, parser tervalidasi, dan pelaporan kegagalan format secara terpisah.
- **Risiko komputasi**: baseline BF16/F16 atau Qwen3-1.7B dapat berjalan lambat pada CPU. Mitigasinya adalah konteks pendek, keluaran terbatas, evaluasi model secara berurutan, dan pemisahan subset pilot dari test set final.
- **Risiko penyimpanan**: seluruh varian model dapat melebihi ruang kosong jika disimpan bersamaan. Mitigasinya adalah evaluasi berurutan, pembersihan cache yang aman, dan penyimpanan permanen hanya untuk konfigurasi serta hasil mentah.
- **Risiko metodologis**: format GGUF menggunakan skema campuran sehingga nominal bit-width tidak sepenuhnya menggambarkan representasi setiap tensor. Mitigasinya adalah melaporkan nama skema aktual, ukuran berkas, metadata model, dan versi quantizer.
- **Risiko generalisasi**: hasil satu CPU tidak mewakili seluruh perangkat. Posisi penelitian adalah eksperimen terkontrol pada satu CPU konsumen, bukan benchmark perangkat keras universal.
- **Risiko scope**: penambahan banyak metode, model, atau tugas akan meningkatkan kombinasi secara cepat. Scope inti dikunci pada 12 kombinasi; eksperimen tambahan hanya dilakukan setelah eksperimen inti selesai.

### Fallback plan

1. Jika baseline Qwen3-1.7B terlalu lambat, pengujian kualitas tetap dilakukan tetapi pengukuran performa dibatasi pada subset yang dilaporkan secara eksplisit.
2. Jika salah satu dataset tidak menghasilkan jawaban yang dapat dinilai stabil, ganti dengan tugas objektif lain tanpa menambah jumlah tugas.
3. Jika BF16/F16 tidak berjalan stabil, gunakan representasi tertinggi yang didukung sebagai baseline operasional dan jelaskan konsekuensinya.
4. Jika ruang penyimpanan tidak cukup, evaluasi satu varian pada satu waktu dan pertahankan checksum, konfigurasi, serta tautan sumber model untuk reproduksi.

## 10. Catatan Sumber dan Literatur

### 10.1 Sumber Utama

| # | Sumber | Tahun | URL | Relevansi | Status |
|---|---|---:|---|---|---|
| 1 | Qwen Team, *Qwen3: Think Deeper, Act Faster* | 2025 | https://qwenlm.github.io/blog/qwen3/ | Spesifikasi keluarga Qwen3, termasuk varian 0.6B dan 1.7B | Terverifikasi dari sumber resmi |
| 2 | Qwen Team, *Qwen3-0.6B Model Card* | 2025 | https://huggingface.co/Qwen/Qwen3-0.6B | Spesifikasi model kecil Qwen3 dan dukungan multibahasa | Terverifikasi dari repositori resmi |
| 3 | Qwen Team, *Qwen3-1.7B-GGUF Model Card* | 2025 | https://huggingface.co/Qwen/Qwen3-1.7B-GGUF | Model GGUF resmi dan baseline Q8_0 | Terverifikasi dari repositori resmi |
| 4 | Qwen Team, *Run Qwen3 Locally with llama.cpp* | 2025–2026 | https://github.com/QwenLM/Qwen3/blob/main/docs/source/run_locally/llama.cpp.md | Dukungan Qwen3, GGUF, dan inferensi CPU | Terverifikasi dari dokumentasi resmi |
| 5 | Qwen Team, *Quantize Qwen3 with llama.cpp* | 2025–2026 | https://github.com/QwenLM/Qwen3/blob/main/docs/source/quantization/llama.cpp.md | Prosedur dan skema kuantisasi GGUF | Terverifikasi dari dokumentasi resmi |
| 6 | Koto et al., *IndoLEM and IndoBERT* | 2020 | https://aclanthology.org/2020.coling-main.66/ | Benchmark dan baseline Bahasa Indonesia | Terverifikasi |
| 7 | Wilie et al., *IndoNLU* | 2020 | https://arxiv.org/abs/2009.05387 | Alternatif benchmark NLU Bahasa Indonesia | Terverifikasi |
| 8 | Cahyawijaya et al., *IndoNLG* | 2021 | https://arxiv.org/abs/2104.08200 | Alternatif benchmark generasi Bahasa Indonesia | Terverifikasi |
| 9 | Abdurrahman et al., *Implementing Quantization to Indonesian BERT Language Model* | 2023 | https://researchportal.hkust.edu.hk/en/publications/implementing-quantization-to-indonesian-bert-language-model-2/ | Pembanding langsung kuantisasi IndoBERT | Rekam publikasi terverifikasi; detail paper perlu dibaca |
| 10 | Dettmers et al., *LLM.int8()* | 2022 | https://arxiv.org/abs/2208.07339 | Dasar teknis kuantisasi 8-bit | Perlu dimasukkan ke telaah pustaka |
| 11 | Frantar et al., *GPTQ* | 2022 | https://arxiv.org/abs/2210.17323 | Pembanding metode PTQ 3/4-bit | Perlu dimasukkan ke telaah pustaka |
| 12 | Lin et al., *AWQ* | 2023 | https://arxiv.org/abs/2306.00978 | Pembanding *activation-aware weight quantization* | Perlu dimasukkan ke telaah pustaka |

### 10.2 Verifikasi Literatur yang Masih Wajib

Sebelum kandidat diterima, pencarian literatur harus memeriksa setidaknya kombinasi kata kunci berikut pada arXiv, Google Scholar, Semantic Scholar, ACL Anthology, dan repositori implementasi:

- `Qwen3 quantization benchmark CPU`;
- `small language model quantization Indonesian`;
- `multilingual quantization degradation low-resource language`;
- `model size quantization interaction language model`;
- `GGUF quantization Indonesian NLP`;
- `quantization task sensitivity multilingual LLM`.

Pencarian harus mencatat studi yang membandingkan beberapa ukuran model, beberapa tingkat kuantisasi, evaluasi bahasa non-Inggris, evaluasi per tugas, dan inferensi CPU. Gap baru boleh dinyatakan final setelah pembanding terdekat ditemukan dan perbedaannya dijelaskan secara eksplisit.

### 10.3 Kesimpulan Gap Sementara

Gap yang ditargetkan bukan penggunaan Qwen, kuantisasi SLM, atau inferensi CPU secara terpisah. Kontribusi yang hendak diuji adalah **analisis interaksi ukuran model × tingkat kuantisasi × jenis tugas NLP Bahasa Indonesia** dalam satu lingkungan CPU-only yang terkontrol. Konfigurasi, skrip, metadata, dan hasil mentah disertakan untuk mendukung reprodusibilitas penelitian.

## 11. Penyerahan ke Penulisan LaTeX

- **Target file**: `template/proposal/chapters/bab1-pendahuluan.tex`, `template/proposal/chapters/bab2-penelitian-terkait.tex`, dan `template/proposal/chapters/bab3-metodologi.tex` setelah verifikasi literatur, dataset, dan baseline runtime dikunci.
- **Gambar/diagram**: bagan alir metodologi penelitian; alur data → model → kuantisasi → inferensi CPU → evaluasi; matriks eksperimen 2 × 3 × 2; dan contoh *Pareto frontier* kualitas–latensi–memori.
- **Keputusan yang masih terbuka**: dua dataset final, definisi keluaran dan parser untuk setiap tugas, baseline BF16/F16 yang benar-benar stabil, serta apakah perbandingan Indonesia–Inggris akan menjadi eksperimen tambahan.
- **Syarat sebelum drafting proposal**: pilot Qwen3-0.6B dan Qwen3-1.7B pada hardware target, estimasi durasi 12 kombinasi, dan verifikasi literatur mandiri terhadap klaim gap.
