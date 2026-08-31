---
cssclasses:
  - full-width
---
# Detail Topik 14: Evaluasi Kuantisasi Small Language Model untuk NLP Bahasa Indonesia

Date: 2026-08-31  
Updated: 2026-08-31  
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)

## Status Singkat

**Kandidat layak dengan scope bersyarat.** Ide ini menjanjikan karena menggabungkan ukuran model, tingkat presisi, tugas Bahasa Indonesia, dan pengukuran efisiensi CPU. Namun, topik belum boleh mengklaim sebagai penelitian pertama sebelum pencarian literatur diperluas sampai publikasi dan repositori terbaru. Scope awal juga terlalu lebar jika sekaligus mencakup IndoBERT, beberapa model generatif, lima tingkat presisi, empat tugas, serta QAT.

## 1. Opsi Judul

- **Bahasa Indonesia**: *Studi Empiris Pengaruh Tingkat Kuantisasi terhadap Akurasi dan Efisiensi Small Language Model pada Tugas NLP Bahasa Indonesia*
- **English**: *An Empirical Study of Quantization Levels on the Accuracy and Efficiency of Small Language Models for Indonesian NLP Tasks*
- **Alternatif produk**: *Pengembangan Benchmark Reproducible untuk Evaluasi Efisiensi Small Language Model Terkuantisasi pada NLP Bahasa Indonesia*

## 2. Penjelasan Sederhana

Model bahasa yang lebih kecil dan bobotnya disimpan dengan angka berpresisi rendah membutuhkan memori lebih sedikit dan berpotensi berjalan lebih cepat pada CPU. Masalahnya, model dapat kehilangan kemampuan memahami teks ketika presisinya diturunkan terlalu jauh. Penelitian ini membuat benchmark yang menjalankan konfigurasi model dan kuantisasi yang sama pada data Bahasa Indonesia, lalu mencatat dua hal sekaligus: seberapa baik jawabannya dan seberapa mahal komputasinya.

Produk yang paling masuk akal untuk format Skripsi Inovasi Produk adalah **harness benchmark** atau pipeline eksperimen yang menerima konfigurasi model/kuantisasi, menjalankan pengujian CPU secara konsisten, menyimpan hasil, dan menghasilkan tabel serta grafik otomatis. Nilai produk bukan sekadar kumpulan hasil eksperimen satu kali.

## 3. Analisis Kebaruan

### Kondisi Saat Ini

- IndoLEM adalah benchmark NLP Bahasa Indonesia dengan tujuh tugas dan IndoBERT sebagai model pralatih; benchmark ini menjadi baseline penting untuk tugas pemahaman bahasa Indonesia.
- Materi sumber merangkum studi Abdurrahman et al. (ICAICTA 2023) yang mengevaluasi kuantisasi IndoBERT. Ini berarti topik tidak boleh diposisikan sebagai kuantisasi IndoBERT yang belum pernah dilakukan.
- Literatur kuantisasi yang dirangkum dalam materi lebih sering mempelajari model bahasa umum, tugas Bahasa Inggris/multibahasa, atau deployment edge; sebagian menggunakan INT8 dan INT4, sementara INT2/INT3 lebih jarang.
- Studi CPU biasanya melaporkan throughput, latency, atau memori, sedangkan studi NLP Indonesia sering lebih berfokus pada skor tugas. Kombinasi evaluasi kualitas dan biaya CPU masih menjadi ruang yang menarik untuk diuji.

### Gap yang Masih Dapat Dipertahankan

- Belum jelas seberapa konsisten trade-off akurasi–latensi–memori pada **beberapa konfigurasi model** untuk tugas Bahasa Indonesia jika seluruh eksperimen dijalankan pada CPU yang sama.
- Studi IndoBERT terdahulu tidak otomatis menjawab perilaku model generatif kecil 1–7B atau format inferensi CPU seperti GGUF/llama.cpp.
- Perbandingan ukuran model dan bit-width perlu dikontrol dengan protokol yang reproducible: versi runtime, jumlah thread, panjang input, batch size, warm-up, dan pengukuran memori.
- Tugas sequence labeling, classification, dan generasi mungkin memiliki sensitivitas kuantisasi yang berbeda; perbedaan ini perlu diuji, bukan diasumsikan.

### Kebaruan yang Aman

Kebaruan paling aman adalah **protokol benchmark terkontrol dan analisis empiris multidimensi**, bukan algoritma kuantisasi baru. Klaim yang dapat dipakai sementara:

> Penelitian ini mengevaluasi secara terkontrol hubungan antara ukuran model, tingkat kuantisasi, kualitas tugas NLP Bahasa Indonesia, dan biaya inferensi CPU dalam satu pipeline reproducible.

Klaim “pertama” harus ditunda sampai systematic search selesai. Hindari menyebut INT4 selalu cepat atau akurasi selalu turun; efeknya bergantung pada arsitektur, runtime, implementasi, dataset, dan perangkat keras.

### Matriks Perbandingan Novelty

| Aspek | Studi konvensional / pembanding | Topik ini |
|---|---|---|
| Fokus bahasa | Inggris, multibahasa, atau satu model Indonesia | Bahasa Indonesia dengan benchmark yang dipilih eksplisit |
| Model | Sering hanya satu keluarga atau satu ukuran | Perbandingan ukuran model dengan protokol sama; jumlah dibatasi |
| Presisi | Umumnya FP16/INT8/INT4 | FP16 sebagai baseline dan INT8/INT4 sebagai inti; INT3/INT2 opsional |
| Efisiensi | Latensi, throughput, atau memori dilaporkan terpisah | Kualitas dan biaya CPU diukur pada konfigurasi yang sama |
| Reproducibility | Detail runtime/thread sering tidak seragam | Harness menyimpan konfigurasi, seed, versi, hardware, dan raw result |
| Bentuk kontribusi | Paper atau tabel hasil | Benchmark/pipeline yang dapat digunakan ulang plus analisis |

## 4. Perumusan Produk dan Masalah (UGM Inovasi Produk)

- **Masalah nyata**: Pengguna perangkat dengan sumber daya terbatas sulit memilih kombinasi model dan kuantisasi yang cukup baik untuk Bahasa Indonesia. Angka parameter atau ukuran file saja tidak memberi tahu kualitas dan waktu inferensi.
- **Solusi/produk**: Benchmark harness CLI yang menjalankan dataset, model, runtime, dan skema kuantisasi yang telah ditentukan; menghasilkan JSON/CSV, ringkasan metrik, grafik accuracy–latency–memory, dan laporan konfigurasi.
- **Batasan produk**:
  1. Satu sistem operasi dan satu mesin CPU sebagai lingkungan utama.
  2. Maksimal 2–3 model dan 1–2 tugas inti pada eksperimen final.
  3. FP16/FP32 sebagai baseline sesuai dukungan runtime; INT8 dan INT4 sebagai perlakuan utama.
  4. INT3/INT2 dan QAT hanya eksperimen tambahan jika toolchain dan waktu memungkinkan.
  5. Tidak mengklaim penggunaan klinis, produksi, atau generalisasi ke semua model Bahasa Indonesia.
  6. Model encoder dan generatif dianalisis sebagai kelompok berbeda; jangan menyamakan metrik klasifikasi IndoBERT dengan kualitas generasi decoder-only.

## 5. Landasan Teknik dan Ilmiah

- **Small Language Model (SLM)**: model bahasa berukuran relatif kecil yang dapat dijalankan pada perangkat konsumen. Batas parameter harus didefinisikan operasional, bukan memakai label SLM secara longgar.
- **Kuantisasi**: pengurangan presisi representasi bobot dan/atau aktivasi, misalnya dari floating point ke INT8 atau INT4.
- **Post-training quantization (PTQ)**: kuantisasi setelah model selesai dilatih; lebih realistis untuk benchmark deployment.
- **Quantization-aware training (QAT)**: pelatihan yang mensimulasikan efek kuantisasi; sebaiknya bukan inti karena menambah biaya dan mengubah pertanyaan penelitian.
- **Runtime**: pilih satu jalur utama, misalnya GGUF dengan llama.cpp untuk model decoder-only CPU. Untuk IndoBERT, gunakan runtime encoder yang konsisten dan laporkan hasilnya sebagai kelompok terpisah.
- **Dataset kandidat**: IndoLEM atau IndoNLU untuk tugas diskriminatif; IndoNLG/FacQA/TyDi QA hanya jika runtime dan format evaluasinya siap. Mulai dari dataset yang split dan metriknya paling stabil.

## 6. Rencana Pengujian dan Parameter Ukur

### Desain Minimum yang Direkomendasikan

Mulai dengan satu pertanyaan inti: **pada satu atau dua tugas Bahasa Indonesia, konfigurasi model-kuantisasi mana yang memberi kualitas memadai dengan biaya CPU terendah?** Desain minimum:

- 2 model dalam satu keluarga atau dua ukuran yang kompatibel dengan runtime yang sama.
- 1 tugas utama, misalnya klasifikasi sentimen untuk model encoder atau QA/generasi untuk model decoder-only.
- FP16/FP32, INT8, dan INT4.
- 3–5 pengulangan pengukuran latency setelah warm-up.
- Full test set jika terjangkau; subset hanya untuk pengembangan dan harus dibedakan dari hasil final.

### Metrik

- **Kualitas tugas**: accuracy/F1 untuk klasifikasi, F1 untuk NER, EM/F1 untuk QA, ROUGE/BLEU/ChrF untuk generasi atau penerjemahan.
- **Efisiensi**: latency per sampel atau token, throughput, peak RAM, ukuran file model, dan waktu pemuatan model.
- **Trade-off**: persentase penurunan skor terhadap baseline, speedup, compression ratio, serta Pareto frontier kualitas–latensi–memori.
- **Reproducibility**: versi model, hash/identifier dataset, runtime, compiler/build, CPU, jumlah thread, batch size, panjang konteks, seed, dan konfigurasi decoding.

### Analisis

Gunakan perbandingan berpasangan pada contoh yang sama. Laporkan interval kepercayaan bootstrap jika sesuai, tetapi jangan menjadikan uji statistik sebagai pengganti pengukuran yang terkontrol. Visual utama: kurva skor versus bit-width, latency versus bit-width, dan tabel Pareto konfigurasi.

## 7. Pemetaan ke Bab Skripsi/Proposal

- **Proposal Bab 1**: keterbatasan sumber daya, kebutuhan inferensi lokal Bahasa Indonesia, masalah pemilihan konfigurasi, rumusan masalah, tujuan benchmark.
- **Proposal Bab 2**: SLM, kuantisasi, IndoLEM/IndoNLU/IndoNLG, studi kuantisasi IndoBERT, CPU inference, dan gap evaluasi.
- **Proposal Bab 3**: desain harness, pemilihan model/dataset/runtime, protokol pengukuran, metrik, dan bagan alir.
- **Proposal Bab 4**: jadwal persiapan benchmark, implementasi harness, eksperimen, analisis, dan penulisan.
- **Skripsi Bab 4**: arsitektur benchmark dan format konfigurasi.
- **Skripsi Bab 5**: implementasi runner, adapter dataset/model, pencatatan metrik, dan generator laporan.
- **Skripsi Bab 6**: hasil eksperimen, analisis trade-off, keterbatasan, kesimpulan, dan saran.

## 8. Risiko dan Kelayakan Akademik

- **Kesesuaian bidang**: kuat untuk AI engineering, machine learning systems, dan NLP; perlu dikonfirmasi dengan keahlian pembimbing.
- **Infrastruktur**: dataset dan model dasar tersedia, tetapi model 3–7B pada CPU dapat membuat eksperimen lama. Runtime CPU dan ruang penyimpanan harus diuji lewat pilot kecil.
- **Risiko metodologis**: perbandingan encoder versus decoder tidak apple-to-apple; format GPTQ/AWQ/GGUF tidak selalu setara; BitsAndBytes tidak otomatis menjadi pilihan terbaik untuk CPU; hasil dapat dipengaruhi jumlah thread dan implementasi kernel.
- **Risiko novelty**: publikasi baru dapat menggugurkan klaim “belum ada”. Posisi kontribusi harus dipindahkan ke benchmark reproducible dan kombinasi eksperimen yang benar-benar belum ditemukan.
- **Risiko hasil**: semua konfigurasi bisa terlalu lambat atau skor terlalu mirip. Itu tetap dapat menjadi hasil jika baseline, confidence interval, dan Pareto trade-off dilaporkan dengan baik.
- **Fallback plan**: jika model 3–7B tidak layak pada CPU, batasi ke model hingga sekitar 1–3B; jika QA/generasi tidak stabil, gunakan satu tugas klasifikasi atau NER; jika INT3/INT2 gagal, hapus dari scope final dan pertahankan INT8/INT4.

## 9. Catatan Sumber dan Literatur

### 9.1 Sumber Utama

| # | Sumber | Tahun | URL | Relevansi | Status |
|---|---|---:|---|---|---|
| 1 | Koto et al., *IndoLEM and IndoBERT* | 2020 | https://aclanthology.org/2020.coling-main.66/ | Benchmark dan baseline Indonesia | Terverifikasi |
| 2 | Abdurrahman et al., *Implementing Quantization to Indonesian BERT Language Model* | 2023 | https://researchportal.hkust.edu.hk/en/publications/implementing-quantization-to-indonesian-bert-language-model-2/ | Pembanding langsung kuantisasi IndoBERT | Terverifikasi sebagai rekam publikasi; detail angka perlu dibaca dari paper |
| 3 | Wilie et al., *IndoNLU* | 2020 | https://arxiv.org/abs/2009.05387 | Alternatif benchmark NLU | Terverifikasi |
| 4 | Cahyawijaya et al., *IndoNLG* | 2021 | https://arxiv.org/abs/2104.08200 | Alternatif benchmark generasi | Terverifikasi |
| 5 | Dettmers et al., *LLM.int8()* | 2022 | https://arxiv.org/abs/2208.07339 | Dasar teknis INT8 | Perlu dimasukkan ke telaah pustaka |
| 6 | Frantar et al., *GPTQ* | 2022 | https://arxiv.org/abs/2210.17323 | Dasar PTQ 3/4-bit | Perlu dimasukkan ke telaah pustaka |
| 7 | Lin et al., *AWQ* | 2023 | https://arxiv.org/abs/2306.00978 | Dasar activation-aware weight quantization | Perlu dimasukkan ke telaah pustaka |

### 9.2 Klaim dari Materi yang Masih Perlu Diverifikasi

Nama seperti Sciammarelli et al. (2026), Tyndall et al. (2025), Kusama et al. (2025), Zhou et al. (2025), dan Oh et al. (2026), termasuk angka speedup/latency yang dikutip, perlu dicocokkan dengan judul paper, venue, DOI/URL, versi preprint, hardware, dan konfigurasi eksperimennya sebelum masuk ke proposal. Catatan ini tidak menjadikan angka tersebut sebagai fakta final.

### 9.3 Kesimpulan Gap

Gap awal yang layak diteliti adalah kurangnya benchmark yang menyatukan skor tugas Bahasa Indonesia dan biaya inferensi CPU dengan protokol yang konsisten. Gap ini lebih defensible daripada klaim bahwa belum ada penelitian tentang kuantisasi IndoBERT atau belum ada penggunaan model kecil untuk Bahasa Indonesia.

## 10. Penyerahan ke Penulisan LaTeX

- **Target file**: `proposal/chapters/bab-1-pendahuluan.tex`, `proposal/chapters/bab-2-penelitian-terkait.tex`, dan `proposal/chapters/bab-3-metode.tex` setelah model, dataset, dan runtime dikunci.
- **Gambar/diagram**: arsitektur benchmark, alur dataset → model → kuantisasi → inferensi CPU → evaluasi, serta Pareto frontier kualitas–latensi–memori.
- **Pertanyaan terbuka**: apakah fokus final pada model encoder (IndoBERT + classification/NER) atau model decoder-only (QA/generasi)? CPU dan RAM apa yang tersedia? Apakah produk utama harus berupa CLI benchmark atau cukup pipeline eksperimen reproducible?

