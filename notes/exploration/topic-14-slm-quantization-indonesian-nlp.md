---
cssclasses:
  - full-width
---
# Detail Topik 14: Ketahanan Kuantisasi Lintas-SLM untuk NLP Bahasa Indonesia

Date: 2026-08-31

Updated: 2026-09-03

Catalog Reference: [`topic-catalog.md`](topic-catalog.md)

## Status Singkat

**Kandidat utama yang layak dilanjutkan, tetapi belum dipilih secara final.** Fokus kandidat ini adalah evaluasi terkontrol terhadap **ketahanan kuantisasi beberapa Small Language Model (SLM) dengan orientasi bahasa berbeda** pada tugas Bahasa Indonesia dan lingkungan inferensi CPU konsumen.

Penelitian tidak dikunci pada keluarga Qwen. Kandidat model inti sementara adalah satu SLM multibahasa umum berukuran sangat kecil, satu SLM multibahasa dari keluarga berbeda, dan satu SLM yang berorientasi pada bahasa Asia Tenggara. Kandidat operasionalnya adalah Qwen3-0.6B, Gemma 3 1B, dan Sailor2-1B-Chat. Daftar tersebut harus dikunci setelah pilot memastikan kompatibilitas `llama.cpp`, kemampuan dasar Bahasa Indonesia, stabilitas format jawaban, kebutuhan RAM, dan waktu inferensi.

Kebaruan tidak berasal dari penggunaan banyak model atau kuantisasi itu sendiri. SLMQuant telah membandingkan kuantisasi lintas arsitektur SLM, penelitian Qwen3 telah membandingkan ukuran serta metode kuantisasi, dan penelitian multilingual telah menunjukkan bahwa dampak kuantisasi berbeda menurut bahasa dan tugas. Posisi yang masih defensible adalah **perbandingan degradasi relatif dan transisi kesalahan per sampel pada SLM multibahasa umum versus SLM berorientasi Asia Tenggara untuk tugas Bahasa Indonesia**, dengan kualitas dan biaya inferensi diukur melalui satu pipeline GGUF/CPU yang konsisten.

## 1. Opsi Judul

### Judul utama

- **Bahasa Indonesia**: *Evaluasi Ketahanan Kuantisasi pada Small Language Model Multibahasa Umum dan Berorientasi Asia Tenggara untuk Tugas Bahasa Indonesia di Lingkungan CPU*
- **Bahasa Inggris**: *Evaluating Quantization Robustness of General Multilingual and Southeast Asian-Oriented Small Language Models on Indonesian Tasks in a CPU Environment*

### Alternatif lebih ringkas

- **Bahasa Indonesia**: *Evaluasi Ketahanan Kuantisasi Small Language Model pada Tugas Bahasa Indonesia dan Inferensi CPU*
- **Bahasa Inggris**: *Evaluating Small Language Model Quantization Robustness on Indonesian Tasks and CPU Inference*

### Alternatif yang menonjolkan analisis kesalahan

- **Bahasa Indonesia**: *Studi Empiris Degradasi Kualitas dan Transisi Kesalahan Small Language Model Terkuantisasi pada Tugas Bahasa Indonesia*
- **Bahasa Inggris**: *An Empirical Study of Quality Degradation and Error Transitions in Quantized Small Language Models on Indonesian Tasks*

Judul tidak menyebut merek model sebelum pilot selesai. Nama dan versi model akan dicantumkan dalam batasan penelitian dan metodologi setelah konfigurasi final dibekukan.

## 2. Penjelasan Sederhana

SLM dapat dijalankan pada perangkat konsumen, tetapi kuantisasi yang memperkecil model dapat mengubah kualitas jawabannya. Dampak tersebut belum tentu sama pada setiap model. SLM multibahasa umum dan SLM yang dilatih lebih khusus untuk bahasa Asia Tenggara dapat memiliki kemampuan dasar, tokenizer, data pelatihan, dan sensitivitas kuantisasi yang berbeda.

Penelitian ini akan menjalankan beberapa SLM pada soal Bahasa Indonesia sebelum dan sesudah kuantisasi. Setiap varian kuantisasi dibandingkan dengan baseline presisi tertinggi dari model yang sama. Selain skor agregat, penelitian akan memeriksa contoh mana yang berubah dari benar menjadi salah, salah menjadi benar, atau mengalami kegagalan format. Pendekatan ini mencegah model dengan baseline lebih tinggi otomatis dianggap lebih tahan terhadap kuantisasi.

Eksperimen akan menggunakan model sumber, prosedur konversi, versi `llama.cpp`, perangkat keras, prompt, dan konfigurasi decoding yang terdokumentasi. Luaran utama adalah temuan empiris dan analisis ilmiah. Pipeline evaluasi, konfigurasi, dan hasil per sampel berfungsi sebagai artefak reprodusibilitas, bukan sumber kebaruan yang berdiri sendiri.

## 3. Fokus dan Pertanyaan Penelitian

### Fokus utama

Hubungan yang akan diuji adalah:

> identitas/orientasi model × tingkat kuantisasi × kondisi tugas Bahasa Indonesia → degradasi kualitas + transisi kesalahan + biaya inferensi CPU

Identitas model diperlakukan sebagai faktor komposit. Perbedaan antarmodel tidak boleh diatribusikan secara kausal hanya kepada orientasi bahasa, arsitektur, ukuran, tokenizer, atau data pelatihan karena seluruh karakteristik tersebut berbeda secara bersamaan.

### Pertanyaan penelitian sementara

1. Bagaimana Q8_0 dan Q4_K_M memengaruhi kualitas setiap SLM dibandingkan baseline BF16/F16 model yang sama pada tugas Bahasa Indonesia?
2. Apakah SLM yang diuji menunjukkan pola degradasi relatif dan transisi kesalahan yang berbeda setelah kuantisasi?
3. Apakah pola sensitivitas kuantisasi berbeda antar-kondisi tugas atau dataset Bahasa Indonesia?
4. Pada kategori soal atau karakteristik input apa perubahan benar-ke-salah paling sering terjadi?
5. Konfigurasi model dan tingkat kuantisasi mana yang memberikan *Pareto trade-off* terbaik antara kualitas, latensi, *throughput*, penggunaan RAM, dan ukuran berkas pada CPU konsumen?

Eksperimen pasangan Indonesia–Inggris dapat ditambahkan setelah eksperimen inti selesai. Jika dilakukan, item harus benar-benar berpasangan dan ekuivalensi terjemahannya harus diaudit; hasilnya digunakan untuk membandingkan degradasi lintas bahasa, bukan sebagai scope minimum.

## 4. Analisis Kebaruan

### 4.1 Kondisi Penelitian Sebelumnya

- Abdurrahman et al. (2023) telah mengevaluasi kuantisasi pada IndoBERT. Kuantisasi model Bahasa Indonesia bukan topik yang belum pernah diteliti.
- Marchisio et al. (2024) telah menguji dampak kuantisasi lintas bahasa, skala model, dan tugas. Klaim bahwa kuantisasi memengaruhi bahasa atau tugas secara tidak seragam bukan novelty baru.
- Zheng et al. (2025) telah mengevaluasi beberapa ukuran Qwen3, metode post-training quantization, bit-width, dan tugas. Interaksi ukuran Qwen3 dengan kuantisasi bukan lagi pembeda yang cukup.
- SLMQuant (Wang et al., 2025) telah mengevaluasi beberapa arsitektur SLM, algoritma kuantisasi, dataset, dan konsumsi inferensi. Benchmark kuantisasi lintas-SLM secara umum bukan novelty baru.
- Cersosimo (2026) telah membandingkan banyak model sub-3B untuk deployment lokal menggunakan analisis performa, efisiensi, pola kegagalan, dan Pareto frontier. Membandingkan beberapa SLM pada hardware terbatas juga bukan kontribusi yang berdiri sendiri.
- Sailor2 telah menyediakan model yang dioptimalkan untuk bahasa Asia Tenggara, termasuk Bahasa Indonesia. Memakai model regional bukan novelty; yang diteliti adalah perubahan kemampuannya setelah kuantisasi dalam protokol terkontrol.

### 4.2 Gap yang Ditargetkan

Penelusuran awal belum menemukan satu penelitian akademik yang menggabungkan seluruh elemen berikut:

1. perbandingan SLM multibahasa umum dan SLM berorientasi Asia Tenggara;
2. evaluasi yang berfokus pada tugas Bahasa Indonesia;
3. baseline presisi tinggi, Q8_0, dan Q4_K_M yang dibuat melalui pipeline GGUF konsisten;
4. pengukuran kualitas dan biaya inferensi aktual pada satu CPU konsumen;
5. degradasi absolut dan relatif terhadap baseline masing-masing model;
6. analisis berpasangan per sampel berupa *prediction agreement*, benar-ke-salah, salah-ke-benar, perubahan jawaban salah, dan kegagalan format; serta
7. analisis sensitivitas menurut kondisi tugas atau kategori soal dan Pareto frontier kualitas--efisiensi.

Kombinasi tersebut tetap merupakan **hipotesis gap**. Literature review sistematis wajib dilakukan sebelum proposal menggunakan frasa “belum tersedia” atau klaim kebaruan yang lebih kuat.

### 4.3 Kebaruan yang Aman

Rumusan kontribusi yang defensible adalah:

> Penelitian ini menawarkan evaluasi terkontrol atas degradasi relatif dan transisi kesalahan akibat kuantisasi pada beberapa SLM dengan orientasi bahasa berbeda dalam tugas Bahasa Indonesia, dengan seluruh konfigurasi diuji melalui pipeline GGUF dan lingkungan CPU yang konsisten.

| Lapisan kontribusi | Bentuk kontribusi |
|---|---|
| Empiris | Bukti per-model dan per-sampel mengenai perubahan kualitas tugas Bahasa Indonesia pada Q8_0 dan Q4_K_M |
| Metodologis | Protokol baseline-terpasang yang membandingkan degradasi relatif, transisi jawaban, kondisi tugas, dan biaya inferensi |
| Praktis | Pemetaan konfigurasi yang non-dominated untuk deployment CPU konsumen pada ruang eksperimen yang diuji |

### 4.4 Batas Klaim

Penelitian tidak akan mengklaim:

- algoritma atau metode kuantisasi baru;
- benchmark kuantisasi SLM pertama;
- penelitian pertama mengenai dampak kuantisasi lintas bahasa;
- bahwa orientasi bahasa, arsitektur, tokenizer, ukuran, atau data pelatihan merupakan penyebab tunggal perbedaan antarmodel;
- bahwa SLM berorientasi Asia Tenggara pasti lebih baik atau lebih tahan terhadap kuantisasi;
- bahwa hasil berlaku untuk seluruh SLM, dataset, runtime, CPU, atau bahasa;
- bahwa Q8_0 dan Q4_K_M identik dengan INT8 dan INT4 murni; atau
- bahwa kuantisasi selalu mempercepat inferensi atau selalu menurunkan kualitas.

## 5. Posisi Penelitian dan Batasan

### Masalah penelitian

Benchmark kuantisasi umum belum langsung menjawab bagaimana SLM dengan orientasi bahasa berbeda mempertahankan kemampuan Bahasa Indonesia ketika dijalankan pada CPU konsumen. Skor absolut antarmodel juga tidak cukup karena model memiliki kemampuan awal yang berbeda. Diperlukan evaluasi yang memasangkan setiap varian kuantisasi dengan baseline modelnya sendiri serta memeriksa perubahan pada tingkat contoh.

### Pendekatan penelitian

Penelitian menggunakan eksperimen terkontrol dengan prosedur berikut:

- memilih maksimal tiga instruction-tuned SLM berukuran sekitar 0,5--1,7 miliar parameter;
- mewakili sekurang-kurangnya satu model multibahasa umum dan satu model berorientasi Asia Tenggara;
- mengonversi checkpoint sumber sendiri dan menghasilkan seluruh varian dengan versi `llama.cpp` serta prosedur kuantisasi yang sama;
- menjalankan contoh, prompt, parser, panjang konteks, decoding, jumlah thread, dan perangkat keras yang sama pada seluruh konfigurasi;
- membandingkan setiap varian Q8_0 dan Q4_K_M dengan baseline presisi tertinggi dari model yang sama;
- menyimpan keluaran dan status penilaian pada tingkat sampel;
- mengukur kualitas, transisi kesalahan, latensi, *throughput*, RAM, dan ukuran berkas; serta
- menganalisis interval kepercayaan berpasangan dan Pareto frontier.

### Batasan penelitian

1. Lingkungan utama dibatasi pada AMD Ryzen 3 5300U, RAM 9 GB, tanpa GPU, dan ruang kosong awal sekitar 8,5 GB.
2. Model final dibatasi maksimal tiga SLM instruction-tuned berukuran sekitar 0,5--1,7B.
3. Kandidat awal adalah Qwen3-0.6B, Gemma 3 1B, dan Sailor2-1B-Chat; semuanya masih harus lulus pilot.
4. Representasi inti dibatasi pada BF16/F16 sebagai baseline operasional, Q8_0, dan Q4_K_M.
5. Runtime dibatasi pada satu commit atau versi `llama.cpp` dengan opsi kompilasi yang sama.
6. Eksperimen inti memakai dua dataset atau kondisi tugas Bahasa Indonesia dengan keluaran yang dapat dinilai otomatis.
7. Jika hanya satu dataset mewakili setiap jenis tugas, hasil disebut per “kondisi tugas/dataset”, bukan efek umum jenis tugas.
8. Mode *thinking* dinonaktifkan jika tersedia; panjang konteks, token keluaran, template chat, dan decoding dikendalikan.
9. Model dijalankan serta disimpan secara berurutan untuk membatasi penggunaan disk.
10. Fine-tuning, QAT, GPTQ, AWQ, INT2/INT3, model 3B ke atas, dan perbandingan banyak runtime tidak termasuk scope inti.
11. Perbandingan Indonesia–Inggris bukan scope minimum.

## 6. Landasan Teknik dan Ilmiah

- **Small Language Model**: model generatif berukuran sekitar 0,5--1,7B yang secara operasional dapat dijalankan pada perangkat penelitian.
- **Orientasi bahasa model**: pengelompokan deskriptif berdasarkan dokumentasi pengembang, misalnya multibahasa umum atau berorientasi Asia Tenggara; bukan variabel kausal yang berdiri sendiri.
- **Post-training weight quantization**: pengurangan presisi bobot setelah pelatihan untuk menurunkan kebutuhan penyimpanan dan memori.
- **GGUF**: format model ekosistem `llama.cpp` yang memuat bobot, tokenizer, metadata, dan konfigurasi inferensi.
- **Q8_0 dan Q4_K_M**: skema kuantisasi GGUF yang dilaporkan dengan nama format aktual.
- **Degradasi relatif**: perubahan skor varian terkuantisasi terhadap baseline presisi tinggi dari model yang sama.
- **Transisi kesalahan**: perubahan status atau isi jawaban pada sampel yang sama antara baseline dan varian kuantisasi.
- **Pareto frontier**: konfigurasi non-dominated ketika kualitas dan satu atau lebih biaya deployment dipertimbangkan bersama.

## 7. Rencana Pengujian dan Parameter Ukur

### 7.1 Desain Minimum

| Faktor | Level yang direncanakan |
|---|---|
| Model | Maksimal tiga model: Qwen3-0.6B, Gemma 3 1B, Sailor2-1B-Chat sebagai kandidat awal |
| Orientasi deskriptif | Multibahasa umum dan berorientasi Asia Tenggara |
| Representasi bobot | BF16/F16, Q8_0, Q4_K_M |
| Kondisi tugas/dataset | Satu pilihan ganda/klasifikasi berbasis prompt dan satu QA singkat |
| Runtime | Satu commit/versi `llama.cpp` |
| Perangkat | Satu CPU dan konfigurasi sistem tetap |

Jika tiga model lulus pilot, desain menghasilkan 3 × 3 × 2 = **18 kombinasi utama**. Kualitas dihitung pada contoh uji yang sama. Pengukuran sistem diulang 3--5 kali setelah warm-up; pengulangan ini mengukur variabilitas latensi dan throughput, bukan menambah observasi independen untuk kualitas model.

Dataset final dipilih berdasarkan lisensi, provenance, risiko kontaminasi, stabilitas test split, ukuran, representasi Bahasa Indonesia, kompatibilitas dengan model generatif, dan metrik otomatis. IndoMMLU dapat menjadi salah satu kandidat, tetapi tidak boleh menjadi satu-satunya bukti jika risiko kontaminasi tidak dapat dikendalikan.

### 7.2 Metrik

- **Kualitas tugas**: akurasi untuk pilihan ganda; exact match dan token-level F1 untuk QA singkat.
- **Kepatuhan format**: valid-answer rate dan kategori kegagalan parser yang diperiksa manual pada sampel audit.
- **Degradasi**: selisih absolut dan relatif terhadap baseline model yang sama.
- **Transisi per sampel**: prediction agreement, benar-ke-salah, salah-ke-benar, tetap-benar, tetap-salah dengan jawaban sama, dan tetap-salah dengan jawaban berubah.
- **Analisis strata**: degradasi dan transisi menurut kategori soal, panjang input, atau karakteristik linguistik yang tersedia sebelum analisis.
- **Efisiensi**: waktu pemuatan, time to first token, latensi total, token per detik, dan peak RAM.
- **Kompresi**: ukuran berkas dan rasio kompresi terhadap baseline.
- **Trade-off**: Pareto frontier kualitas--latensi--memori--ukuran berkas.
- **Reproducibility**: identifier dan revisi model/dataset, hash berkas, versi `llama.cpp`, opsi kompilasi, CPU, jumlah thread, panjang konteks, seed, prompt, chat template, serta decoding.

### 7.3 Analisis

1. Bandingkan Q8_0 dan Q4_K_M dengan baseline presisi tinggi pada model dan sampel yang sama.
2. Hitung interval kepercayaan bootstrap berpasangan untuk selisih metrik kualitas.
3. Bandingkan distribusi degradasi relatif dan transisi kesalahan antarmodel tanpa mengklaim penyebab tunggal.
4. Laporkan skor absolut untuk konteks, tetapi gunakan perubahan terhadap baseline sebagai analisis ketahanan utama.
5. Pisahkan variabilitas kualitas model dari variabilitas pengukuran performa sistem.
6. Laporkan latensi dengan median, interval kuantil, warm-up, jumlah pengulangan, dan kondisi thread yang tetap.
7. Sajikan tabel hasil faktorial, diagram transisi, kurva degradasi, serta Pareto frontier.

## 8. Pemetaan ke Bab Proposal dan Skripsi Ilmiah Akademik

- **Proposal Bab 1**: kebutuhan deployment SLM Bahasa Indonesia pada perangkat konsumen, masalah degradasi kuantisasi, rumusan masalah, tujuan, batasan, dan manfaat.
- **Proposal Bab 2**: SLM multibahasa dan regional, kuantisasi bobot, GGUF/`llama.cpp`, benchmark Bahasa Indonesia, SLMQuant, kuantisasi multilingual, serta pembanding Qwen3.
- **Proposal Bab 3**: kriteria pemilihan model/dataset, pilot, pipeline konversi, desain eksperimen, protokol baseline-terpasang, metrik, kontrol, dan analisis.
- **Proposal Bab 4**: jadwal systematic mapping, pilot, implementasi instrumen, eksperimen, analisis, dan penulisan.
- **Skripsi Bab 1**: latar belakang, perumusan masalah, batasan penelitian, tujuan, dan manfaat.
- **Skripsi Bab 2**: kajian SLM, orientasi bahasa, kuantisasi, evaluasi NLP Bahasa Indonesia, inferensi CPU, dan penelitian terdahulu.
- **Skripsi Bab 3**: metodologi data, pemilihan model, faktor eksperimen, kontrol, metrik, serta analisis statistik.
- **Skripsi Bab 4**: implementasi pipeline konversi/evaluasi, integrasi model dan dataset, validasi parser, serta profiling sumber daya.
- **Skripsi Bab 5**: hasil degradasi dan transisi kesalahan, perbandingan pola antarmodel, efisiensi, Pareto frontier, pembahasan, dan keterbatasan.
- **Skripsi Bab 6**: simpulan yang menjawab pertanyaan penelitian dan saran penelitian lanjutan.

## 9. Risiko dan Kelayakan Akademik

- **Risiko kebaruan**: benchmark lintas-SLM, kuantisasi multilingual, dan evaluasi Qwen3 sudah tersedia. Mitigasinya adalah menjaga fokus pada Bahasa Indonesia, orientasi model, baseline-terpasang, dan transisi per sampel.
- **Risiko confounding antarmodel**: model berbeda pada banyak dimensi sekaligus. Mitigasinya adalah memperlakukan identitas model sebagai faktor komposit dan menghindari klaim kausal tentang arsitektur atau data pelatihan.
- **Risiko floor effect**: model yang lemah dalam Bahasa Indonesia dapat memperoleh skor baseline terlalu rendah sehingga degradasi sulit ditafsirkan. Mitigasinya adalah menetapkan ambang kelayakan baseline pada pilot.
- **Risiko kompatibilitas**: salah satu arsitektur atau chat template dapat bermasalah pada versi `llama.cpp` yang dipilih. Mitigasinya adalah pilot konversi, prompt, dan parser sebelum model dikunci.
- **Risiko lisensi/akses**: Gemma memerlukan penerimaan ketentuan akses. Mitigasinya adalah memeriksa izin sejak awal dan mengganti model tanpa mengubah kategori desain bila akses tidak tersedia.
- **Risiko kontaminasi data**: dataset publik dapat muncul dalam data pelatihan model. Mitigasinya adalah mendokumentasikan provenance, menambah dataset yang lebih baru atau terkontrol, dan membatasi klaim.
- **Risiko komputasi**: 18 kombinasi tetap dapat memerlukan waktu panjang pada CPU. Mitigasinya adalah keluaran pendek, subset pilot terpisah, evaluasi berurutan, dan maksimal tiga model.
- **Risiko penyimpanan**: seluruh checkpoint dan varian dapat melebihi ruang kosong. Mitigasinya adalah mengonversi serta mengevaluasi satu model pada satu waktu dan menyimpan permanen hanya metadata, checksum, konfigurasi, dan hasil.
- **Risiko generalisasi**: satu CPU tidak mewakili semua perangkat. Posisi penelitian adalah eksperimen terkontrol pada satu CPU konsumen.

### Fallback plan

1. Jika hanya dua model yang lulus seluruh pilot, pertahankan satu model multibahasa umum dan satu model berorientasi Asia Tenggara sehingga desain menjadi 2 × 3 × 2 = 12 kombinasi.
2. Jika BF16/F16 tidak stabil, gunakan representasi tertinggi yang didukung sebagai baseline operasional dan dokumentasikan konsekuensinya.
3. Jika satu dataset tidak menghasilkan keluaran yang dapat dinilai stabil, ganti dengan tugas objektif lain tanpa menambah jumlah kondisi.
4. Jika QA terlalu lambat, batasi panjang jawaban dan gunakan subset terstratifikasi yang ditetapkan sebelum analisis.
5. Jika ruang penyimpanan terbatas, hapus artefak model antara batch hanya setelah checksum, konfigurasi, dan sumber unduhan tersimpan.
6. Jika perbandingan Indonesia–Inggris terlalu mahal atau ekuivalensinya lemah, keluarkan dari scope final tanpa memengaruhi eksperimen inti.

## 10. Catatan Sumber dan Literatur

### 10.1 Pembanding Utama

| # | Sumber | Tahun | URL | Konsekuensi terhadap novelty |
|---|---|---:|---|---|
| 1 | Marchisio et al., *How Does Quantization Affect Multilingual LLMs?* | 2024 | https://aclanthology.org/2024.findings-emnlp.935/ | Dampak kuantisasi lintas bahasa, skala, dan tugas sudah diteliti |
| 2 | Abdurrahman et al., *Implementing Quantization to Indonesian BERT Language Model* | 2023 | https://researchportal.hkust.edu.hk/en/publications/implementing-quantization-to-indonesian-bert-language-model-2/ | Kuantisasi model Bahasa Indonesia bukan novelty baru |
| 3 | Zheng et al., *An Empirical Study of Qwen3 Quantization* | 2025 | https://arxiv.org/abs/2505.02214 | Perbandingan ukuran dan kuantisasi Qwen3 telah dilakukan |
| 4 | Wang et al., *SLMQuant: Benchmarking Small Language Model Quantization for Practical Deployment* | 2025 | https://arxiv.org/abs/2511.13023 | Benchmark kuantisasi lintas arsitektur SLM dan konsumsi inferensi telah tersedia |
| 5 | Cersosimo, *Democratizing AI with Small Language Models* | 2026 | https://arxiv.org/abs/2607.16202 | Evaluasi lintas-SLM, pola kegagalan, efisiensi, dan Pareto deployment telah dilakukan |
| 6 | Sailor2 Team, *Sailor2: Sailing in South-East Asia with Inclusive Multilingual LLMs* | 2025 | https://arxiv.org/abs/2502.12982 | SLM regional untuk Bahasa Indonesia tersedia; novelty harus berada pada audit kuantisasinya |

### 10.2 Sumber Model dan Runtime

| Komponen | URL | Catatan |
|---|---|---|
| Qwen3-0.6B | https://huggingface.co/Qwen/Qwen3-0.6B | Kandidat SLM multibahasa umum, Apache-2.0 |
| Gemma 3 1B IT | https://huggingface.co/google/gemma-3-1b-it | Kandidat keluarga berbeda dengan dukungan multibahasa; akses berlisensi perlu diterima |
| Sailor2-1B-Chat | https://huggingface.co/sail/Sailor2-1B-Chat | Kandidat berorientasi Asia Tenggara dan Bahasa Indonesia, Apache-2.0 |
| Qwen3 `llama.cpp` guide | https://github.com/QwenLM/Qwen3/blob/main/docs/source/run_locally/llama.cpp.md | Dasar dukungan runtime dan GGUF |
| IndoLEM | https://aclanthology.org/2020.coling-main.66/ | Kandidat sumber tugas Bahasa Indonesia |
| IndoNLU | https://arxiv.org/abs/2009.05387 | Kandidat benchmark Bahasa Indonesia |
| IndoNLG | https://arxiv.org/abs/2104.08200 | Kandidat sumber tugas generatif Bahasa Indonesia |

### 10.3 Verifikasi Literatur yang Masih Wajib

Systematic mapping harus memeriksa kombinasi kata kunci berikut pada ACM Digital Library, IEEE Xplore, ACL Anthology, arXiv, Google Scholar, dan Semantic Scholar:

- `SLM quantization benchmark multilingual CPU`;
- `small language model quantization Indonesian`;
- `Southeast Asian language model quantization`;
- `Sailor2 quantization benchmark Indonesian`;
- `GGUF quantization Indonesian NLP`;
- `quantization prediction flip language model`;
- `quantization error transition multilingual LLM`;
- `general multilingual regional language model quantization comparison`.

Untuk setiap pembanding, catat model, ukuran, orientasi bahasa, dataset, bahasa evaluasi, metode/skema kuantisasi, runtime, hardware, metrik kualitas, metrik sistem, analisis per sampel, dan ketersediaan artefak.

### 10.4 Kesimpulan Gap Sementara

Topik generik “membandingkan beberapa SLM terkuantisasi” tidak cukup novel. Gap yang masih layak adalah **evaluasi degradasi relatif dan transisi kesalahan pada SLM multibahasa umum versus SLM berorientasi Asia Tenggara dalam tugas Bahasa Indonesia**, menggunakan pipeline GGUF dan CPU yang konsisten. Klaim ini baru boleh difinalkan setelah systematic mapping dan pilot selesai.

## 11. Penyerahan ke Penulisan LaTeX

- **Target file**: bab proposal baru ditulis setelah model, dataset, baseline, dan gap literatur dikunci.
- **Gambar/diagram**: alur checkpoint sumber → konversi F16 → Q8_0/Q4_K_M → inferensi CPU → evaluasi per sampel → transisi kesalahan → profiling → Pareto frontier; matriks 3 × 3 × 2; dan diagram kategori transisi jawaban.
- **Keputusan terbuka**: model mana yang lulus pilot, dua dataset final, ambang baseline minimum, baseline presisi tertinggi yang stabil, metode pengukuran peak RAM, serta kelayakan ekstensi Indonesia–Inggris.
- **Syarat sebelum drafting proposal**: systematic mapping pembanding langsung; pilot ketiga kandidat pada hardware target; verifikasi seluruh varian berasal dari checkpoint sumber dan quantizer yang sama; estimasi durasi 18 kombinasi; validasi parser; dan audit awal risiko kontaminasi dataset.
