# AGENTS.md — Pedoman dan Referensi Penulisan Skripsi UGM

> **Panduan resmi:** `@examples/pedoman_ta.pdf`  
> **Contoh Proposal:** `@examples/contoh_proposal.pdf`  
> **Contoh Skripsi:** `@examples/contoh_skripsi.pdf`

---

## Aturan Prioritas (WAJIB DIKUTI)

1. **Pedoman (`pedoman_ta.pdf`) adalah prioritas UTAMA**
2. Jika ada perbedaan antara pedoman dan contoh PDF, **ikuti pedoman**
3. Contoh PDF hanya sebagai referensi format/visual, bukan aturan

---

## Topik dan Jenis TA Saat Ini

Topik tugas akhir telah dikunci pada **sequence-level routing untuk penghematan komputasi decoder-only small language model (SLM)**. Arah utama penelitian adalah membuat router ringan yang menggunakan representasi prompt/sequence untuk memilih layer atau kelompok layer yang dijalankan secara konsisten selama proses decoding.

Keputusan yang sudah dikunci:

- Mekanisme utama: **sequence-level routing / input-adaptive layer skipping**.
- Objek umum: **decoder-only SLM**.
- Bentuk intervensi: penambahan router ringan dan mekanisme eksekusi layer kondisional.
- Sasaran umum: mengkaji trade-off antara kualitas keluaran dan efisiensi inferensi.
- Backbone utama: **Qwen3-0.6B** (`Qwen/Qwen3-0.6B`), disetujui pada 6 Oktober 2026.
- Judul yang disetujui pada 6 Oktober 2026: **Sequence-Level Routing untuk Efisiensi Inferensi Qwen3-0.6B pada Peringkasan Berita Bahasa Indonesia**. Versi Inggris: **Sequence-Level Routing for Efficient Qwen3-0.6B Inference in Indonesian News Summarization**.
- Dataset utama: **XL-Sum subset Indonesia** (`csebuetnlp/xlsum`, konfigurasi `indonesian`) untuk **peringkasan berita bahasa Indonesia**, disetujui pada 6 Oktober 2026.
- Bentuk routing, direvisi pada 6 Oktober 2026: satu router menghasilkan keputusan biner aktif/lewati (1/0) untuk setiap kelompok tengah. Keputusan dibuat sekali berdasarkan prompt dan dipertahankan pada sisa prefill serta seluruh decoding, tanpa klasifikasi ID pola atau budget jumlah layer aktif tetap.
- Rancangan pelatihan awal: hanya router yang dilatih, sementara bobot Qwen dibekukan. LoRA belum termasuk rancangan awal dan hanya dipertimbangkan melalui keputusan berikutnya jika diperlukan.
- Pembanding: **full model dan static layer skipping**. Full model menjadi acuan kualitas dan biaya penuh. Static menggunakan satu pola tetap yang dipilih menggunakan data validation dan kemudian diterapkan pada seluruh artikel. Efisiensi utama dibandingkan menggunakan waktu inferensi aktual pada lingkungan dan pengaturan yang sama, tanpa penyetaraan biaya buatan berdasarkan jumlah layer.

Rincian desain eksperimen yang disetujui berikutnya pada 6 Oktober 2026:

- Sebanyak 28 layer dibagi menjadi 7 kelompok berurutan, masing-masing 4 layer. Kelompok pertama dan terakhir selalu aktif; skipping hanya pada 5 kelompok tengah. Ini asumsi desain, bukan bukti pentingnya kelompok awal/akhir.
- Revisi pada 6 Oktober 2026: budget tetap 24/20 layer dan dua router terpisah dihapus. Lima kelompok tengah masing-masing dapat aktif atau dilewati; jumlah layer aktif dapat berbeda antarartikel. Ruang keputusan secara matematis mencakup 32 pola, tetapi router tidak mengklasifikasikan 32 ID route dan tidak diwajibkan mengevaluasi seluruh pola untuk pelatihan.
- Representasi router: rata-rata hidden state token artikel setelah kelompok pertama, tanpa token instruksi, token khusus, dan padding. Hasil kelompok pertama digunakan kembali untuk sisa prefill. Route digunakan pada sisa prefill dan seluruh decoding; cache disiapkan untuk layer aktif.
- Router, direvisi pada 19 Oktober 2026: satu MLP ringan menggunakan representasi artikel untuk menghasilkan keputusan biner bagi masing-masing kelompok G2 sampai G6. Rincian arsitektur internal dan konfigurasi operasional MLP tidak dikunci pada tahap proposal dan akan ditetapkan pada tahap implementasi serta pemilihan konfigurasi menggunakan data validasi.
- Pelatihan setelah revisi: hanya router dilatih dan Qwen tetap dibekukan. Target route dibuat secara offline melalui pencarian bertahap berbasis rata-rata NLL teacher forcing dan penalti proporsi kelompok tengah aktif. Router dilatih dengan binary cross-entropy with logits; konfigurasi awal menggunakan AdamW, learning rate 10^-3, weight decay 10^-4, paling banyak 50 epoch, dan early stopping lima epoch. Kandidat nilai penalti ditetapkan sebagai {0, 0,01, 0,05, 0,10, 0,20}; satu nilai dipilih menggunakan validation. Seed pemilihan subset adalah 42 dan seed utama pelatihan router adalah 43. Seed tambahan 44 dan 45 dapat digunakan untuk analisis ketahanan jika sumber daya mencukupi; tidak ada kewajiban enumerasi 32 pola untuk pelatihan router.
- Static: satu pola tetap dipilih menggunakan validation dan diterapkan pada seluruh artikel serta seluruh decoding. Pola dipilih menggunakan objective route yang sama; jika skor seri, dipilih pola dengan kelompok aktif lebih sedikit, lalu urutan leksikografis menaik dengan nilai 0 didahulukan. Waktu inferensi aktual menjadi ukuran efisiensi utama; jumlah layer aktif dan panjang keluaran dilaporkan sebagai informasi tambahan. Random routing dikeluarkan dari ruang lingkup penelitian.
- Evaluasi kualitas diperbarui pada 6 Oktober 2026: evaluasi sepenuhnya otomatis; penilaian manual dan pemeriksaan faktualitas manual pada sampel dikeluarkan atas permintaan pengguna. ROUGE-1, ROUGE-2, ROUGE-L, dan BERTScore disetujui sebagai metrik otomatis. BERTScore melengkapi kecocokan teks ROUGE dengan kemiripan representasi kontekstual antara ringkasan hasil generasi dan acuan. Komponen skor dan agregasi, disetujui pada 6 Oktober 2026: gunakan F1 untuk ROUGE-1, ROUGE-2, ROUGE-L, dan BERTScore; hitung F1 per artikel, kemudian ambil rata-rata aritmetika per metrik dengan bobot sama untuk setiap artikel. Laporkan empat skor secara terpisah, tanpa menggabungkannya menjadi satu angka dan tanpa menghitung F1 dari rata-rata precision/recall. Implementasi, preprocessing metrik, encoder/layer BERTScore, konfigurasi IDF/rescaling, penanganan batas token encoder, serta penanganan beberapa seed pada bootstrap belum ditetapkan. Paired bootstrap dengan interval kepercayaan dua sisi 95% untuk selisih rata-rata F1 antarmetode disetujui pada 6 Oktober 2026: resampling dilakukan pada artikel dengan pengembalian, memakai indeks artikel yang sama untuk kedua metode, dan dihitung terpisah per metrik dari skor tersimpan. Konfigurasi bootstrap, disetujui pada 6 Oktober 2026: metode persentil dengan 10.000 resampling dan seed bootstrap 42; batas interval adalah persentil 2,5% dan 97,5% dari distribusi selisih rata-rata F1 hasil resampling. Seed bootstrap digunakan terpisah dari pemilihan subset dan seed pelatihan. Pasangan pembandingan setelah revisi: router terhadap full model dan static skipping. Pembagian per-budget, enam pasangan, dan tujuh konfigurasi pada rancangan lama tidak lagi berlaku. Waktu inferensi aktual pada lingkungan dan pengaturan yang sama menjadi ukuran efisiensi utama; jumlah layer aktif dan panjang keluaran dilaporkan sebagai informasi tambahan. Interval dihitung terpisah untuk masing-masing dari empat metrik. Penanganan beberapa seed pelatihan masih perlu ditetapkan. Interval berbasis artikel ini tidak dengan sendirinya mencakup variasi antarseed. Tidak ada klaim bahwa metrik kemiripan terhadap acuan menjamin faktualitas atau kualitas menyeluruh.
- Evaluasi efisiensi: waktu total per artikel termasuk overhead representasi/routing, waktu prefill dan decoding, serta jumlah token keluaran. Batch 1, warm-up dan pengulangan; perangkat, presisi dan konfigurasi generasi sama antarmetode. Mode non-thinking ditetapkan. Batas context window 4.096 token dan batas keluaran `max_new_tokens=256` disetujui pada 6 Oktober 2026; input maksimal 3.840 token termasuk instruksi dan format chat. Batas keluaran adalah maksimum, bukan panjang wajib. Greedy decoding (`do_sample=False`, `num_beams=1`) disetujui pada 6 Oktober 2026 untuk seluruh metode: token dengan skor tertinggi dipilih pada setiap langkah, tanpa sampling. Aturan penghentian, disetujui pada 6 Oktober 2026: generasi berhenti ketika model menghasilkan token akhir respons sesuai konfigurasi model atau mencapai 256 token keluaran, tanpa panjang minimum yang dipaksakan. Aturan yang sama digunakan pada seluruh metode. Pengaturan tambahan yang memengaruhi skor token, jumlah warm-up/pengulangan, serta statistik pelaporan belum ditentukan.
- Penanganan artikel panjang, disetujui pada 6 Oktober 2026: artikel disaring jika prompt lengkap yang memuat artikel utuh melebihi 3.840 token menurut tokenizer Qwen3-0.6B, termasuk instruksi dan format chat; tidak dilakukan pemotongan artikel. Penyaringan berlaku pada seluruh split dan himpunan artikel evaluasi sama untuk seluruh metode. Jumlah artikel yang dikeluarkan dan tersisa dicatat menggunakan format prompt final yang telah disetujui. Batas ringkasan acuan, disetujui pada 6 Oktober 2026: maksimum 256 token termasuk token akhir respons, dihitung menggunakan tokenizer Qwen3-0.6B. Pasangan artikel–ringkasan dengan acuan melebihi batas disaring tanpa pemotongan ringkasan pada train, validation, dan test. Jumlah pasangan yang dikeluarkan karena batas artikel dan batas ringkasan serta jumlah akhir tiap split akan dicatat. Gabungan prompt dan target teacher forcing diperiksa agar tetap dalam konteks 4.096 token. Kebijakan yang dipilih harus diterapkan konsisten pada seluruh metode.
- Preprocessing teks, disetujui pada 6 Oktober 2026: hapus whitespace (termasuk spasi dan baris kosong) hanya di awal dan akhir artikel serta ringkasan acuan. Pasangan dikeluarkan jika artikel atau ringkasannya kosong setelah langkah tersebut. Huruf besar, tanda baca, whitespace internal, dan isi teks lainnya dipertahankan. Preprocessing berlaku pada seluruh split sebelum penyusunan prompt dan pemeriksaan batas token. Jumlah pasangan kosong yang dikeluarkan dicatat. Preprocessing metrik ROUGE ditentukan terpisah.
- Duplikasi artikel, disetujui pada 6 Oktober 2026: artikel dianggap duplikat jika teksnya persis sama setelah preprocessing. Dalam satu split, pertahankan kemunculan pertama menurut urutan asli dataset beserta ringkasan acuannya. Jika artikel muncul antarsplit, pertahankan pasangan pada split dengan prioritas test, kemudian validation, kemudian train; salinan pada split lain dikeluarkan, tanpa memindahkan pasangan antarsplit. Pemeriksaan dilakukan sebelum pemilihan subset; identitas dan jumlah pasangan yang dikeluarkan akan dicatat.
- Pemilihan subset, disetujui pada 6 Oktober 2026: jika sebagian data digunakan, ambil sampel acak tanpa pengembalian pada masing-masing split setelah preprocessing, penyaringan, dan penanganan duplikasi, dengan seed tetap 42. Simpan identitas sampel terpilih dan gunakan subset evaluasi yang sama untuk seluruh metode. Jumlah sampel setiap split ditentukan setelah waktu dan memori terukur. Seed 42 ini berlaku untuk pemilihan subset; seed pelatihan router belum ditetapkan.
- Format prompt final, disetujui pada 6 Oktober 2026: "Ringkas artikel berita berikut dalam bahasa Indonesia. Pertahankan informasi utama dan jangan menambahkan informasi yang tidak terdapat dalam artikel." diikuti satu baris kosong, "Artikel:", baris baru, dan teks artikel utuh. Instruksi dan artikel dimuat sebagai pesan pengguna dalam format chat Qwen dengan mode non-thinking. Format yang sama digunakan untuk pembentukan label dan seluruh metode evaluasi; batas masukan dihitung setelah format chat diterapkan.
- Lingkungan awal, disetujui pada 6 Oktober 2026: laptop lokal, CPU AMD Ryzen 3 5300U (4 core/8 thread), RAM terbaca sekitar 9,1 GiB, grafis Radeon terintegrasi; eksekusi CPU dengan FP32 dan batch 1. Skala data ditentukan setelah waktu dan memori terukur sebagai bagian pemeriksaan implementasi eksperimen utama. Lingkungan evaluasi akhir belum dikunci; jika berubah, seluruh pembanding dievaluasi pada lingkungan akhir yang sama.

Pertanyaan penelitian yang disepakati pada 6 Oktober 2026:

1. Bagaimana pengaruh sequence-level routing terhadap kualitas ringkasan dan waktu inferensi Qwen3-0.6B pada XL-Sum Indonesia?
2. Apakah router terlatih memberikan trade-off kualitas–efisiensi yang lebih baik daripada static skipping dengan mempertimbangkan kualitas ringkasan dan biaya inferensi?

Hal yang **belum dikunci** dan masih harus diputuskan: rincian batasan tambahan, penggunaan seed pelatihan tambahan, pengaturan tambahan yang memengaruhi skor token, aturan penyaringan tambahan, jumlah sampel tiap split, perangkat keras/presisi lingkungan evaluasi akhir dan versi perangkat lunak, rincian operasional ROUGE dan konfigurasi BERTScore, jumlah warm-up/pengulangan serta statistik pelaporan, jadwal, dan klaim kontribusi. Penggunaan LoRA di luar rancangan awal juga belum diputuskan.

Fokus pekerjaan adalah penyelesaian penelitian dan penulisan. Tidak ada tahap pilot terpisah; pemeriksaan kebenaran implementasi, baseline, dan evaluasi kualitas–efisiensi tetap menjadi bagian eksperimen utama.

Proposal aktif berada di `latex/proposal/` dan telah menjadi **draf parsial** topik sequence-level routing pada Qwen3-0.6B untuk XL-Sum Indonesia. Judul telah ditetapkan; rincian yang dinyatakan belum ditetapkan dan placeholder metadata masih perlu dilengkapi. Folder `template/` tetap merupakan referensi template, bukan naskah aktif.

Aturan setelah penguncian arah topik:

- Jangan menganggap isi proposal lama sebagai scope penelitian yang berlaku.
- Jangan mengunci model, dataset, runtime, perangkat keras, metrik, jadwal, atau desain eksperimen yang lebih rinci tanpa keputusan eksplisit berikutnya.
- Jangan menyalin klaim kontribusi, hasil pilot, atau kesimpulan dari topik sebelumnya ke proposal baru.
- Jika menambahkan rincian yang belum diputuskan, tandai sebagai hipotesis atau opsi yang masih perlu diverifikasi, bukan sebagai keputusan final.

### Aturan Folder Notes

- Hanya menulis atau memperbarui file di folder `notes/` jika pengguna secara eksplisit meminta sesuatu untuk ditulis sebagai notes/catatan.
- Jika pengguna meminta penulisan notes, simpan file tersebut di folder `notes/`, bukan di root repository.
- Jangan otomatis menambahkan ide eksplorasi ke `notes/` tanpa permintaan eksplisit pengguna.

---

## Struktur PROPOSAL (`proposal/`)

> Class: `\documentclass[proposal,indonesia]{ugmskripsi}`

### Bagian Awal
| Elemen | Ada? | Keterangan |
|--------|------|-----------|
| Halaman Sampul | ✅ | "PROPOSAL TUGAS AKHIR" |
| Halaman Pengesahan | ✅ | Wajib ada, muncul di Daftar Isi |
| Daftar Isi | ✅ | Hanya Daftar Isi |
| Intisari | ✅ | Bahasa Indonesia saja |
| Abstract | ✅ | Contoh memiliki, pedoman tidak menyebut — ikuti contoh |

### Bagian Utama
| Bab | Judul | Isi |
|-----|-------|-----|
| **Bab 1** | Pendahuluan | Latar Belakang, **Rumusan Masalah**, Batasan Masalah, Tujuan Penelitian, Manfaat Penelitian |
| **Bab 2** | Penelitian Terkait | State of the art, literatur review |
| **Bab 3** | Metode dan Rancangan Penelitian | Deskripsi umum, metodologi, bagan alir, perancangan sistem |
| **Bab 4** | Jadwal Penelitian | Gantt Chart berbasis bulan |

### Bagian Akhir
| Elemen | Ada? |
|--------|------|
| Glosarium | ⚠️ Opsional — hanya jika ada jargon teknis yang membingungkan |
| Daftar Pustaka | ✅ |

### Yang TIDAK ADA di Proposal
- ❌ Halaman Pernyataan (Declaration)
- ❌ Motto
- ❌ Persembahan (Acknowledgment)
- ❌ Prakata (Preface)
- ❌ Daftar Tabel
- ❌ Daftar Gambar
- ❌ Daftar Lambang/Simbol
- ❌ Lampiran

---

## Struktur SKRIPSI (`skripsi/`)

> Class: `\documentclass[skripsi,indonesia]{ugmskripsi}`

### Bagian Awal
| Elemen | Ada? | Keterangan |
|--------|------|-----------|
| Halaman Sampul | ✅ | "SKRIPSI" |
| Halaman Pengesahan | ✅ | Muncul di Daftar Isi |
| Halaman Pernyataan | ✅ | Muncul di Daftar Isi |
| Motto | ✅ | Muncul di Daftar Isi |
| Persembahan | ✅ | Muncul di Daftar Isi |
| Prakata | ✅ | Muncul di Daftar Isi |
| Daftar Isi | ✅ | |
| Daftar Tabel | ✅ | |
| Daftar Gambar | ✅ | |
| Daftar Simbol | ✅ | Via `\lambang` |
| Intisari | ✅ | Bahasa Indonesia |
| Abstract | ✅ | Bahasa Inggris |

### Bagian Utama (Skripsi Ilmiah Akademik)
| Bab | Judul | Isi |
|-----|-------|-----|
| **Bab 1** | Pendahuluan | Latar Belakang, **Perumusan Masalah**, Batasan Penelitian, Tujuan, Manfaat |
| **Bab 2** | Kajian Pustaka dan Penelitian Terkait | Landasan teori, penelitian terdahulu, dan posisi penelitian |
| **Bab 3** | Metodologi Penelitian | Data, model, desain eksperimen, metrik, kontrol, dan analisis |
| **Bab 4** | Implementasi dan Hasil Penelitian | Pipeline, hasil eksperimen, analisis kualitas, kesalahan, dan efisiensi |
| **Bab 5** | Pembahasan | Interpretasi hasil, keterbatasan, implikasi, dan perbandingan dengan penelitian terkait |
| **Bab 6** | Kesimpulan dan Saran | Jawaban atas rumusan masalah dan arah penelitian lanjutan |

Catatan: berkas `template/skripsi/chapters/` masih merupakan scaffold lama berbasis inovasi produk. Jangan menjadikannya acuan struktur ilmiah akademik sebelum disesuaikan pada tahap penulisan skripsi.

### Bagian Akhir
| Elemen | Ada? |
|--------|------|
| Daftar Pustaka | ✅ |
| Lampiran | ✅ | Kode, konfigurasi, data primer |

---

## Perbedaan Kunci: Proposal vs Skripsi

| Aspek | Proposal | Skripsi |
|-------|----------|---------|
| Class option | `[proposal]` | `[skripsi]` |
| Cover text | "PROPOSAL TUGAS AKHIR" | "SKRIPSI" |
| Judul Bab 1 | Rumusan **Masalah** | Perumusan Masalah |
| Bab 2 | Penelitian Terkait | Kajian Pustaka dan Penelitian Terkait |
| Bab 3 | Metode dan Rancangan | Metodologi Penelitian |
| Bab 4 | Jadwal Penelitian | Implementasi dan Hasil Penelitian |
| Bab 5 | ❌ Tidak ada | Pembahasan |
| Bab 6 | ❌ Tidak ada | Kesimpulan dan Saran |
| Preliminary pages | Minimal | Lengkap |
| Lampiran | ❌ Tidak ada | ✅ Ada |

---

## Panduan Penulisan Bahasa

- Gunakan **bahasa Indonesia** (`[indonesia]`)
- Bahasa Inggris hanya untuk: judul, abstract, istilah teknis
- Istilah teknis boleh dalam bahasa Inggris dengan penjelasan Indonesia pada pertama kali disebut
- Gunakan Glosarium untuk jargon yang membingungkan

---

## Panduan Diagram dan Flowchart

- **Bagan Alir Metodologi** (Bab 3 Proposal / Bab 3-4 Skripsi): Wajib ada, visualisasi tahapan
- **Arsitektur Sistem** (Bab 3-4): Diagram komponen dan hubungannya
- **ERD / Skema Database** (jika relevan): Diagram relasi entitas
- **UI/UX Wireframe atau Mockup** (jika ada antarmuka): Rancangan tampilan
- **Gantt Chart** (Bab 4 Proposal): Jadwal penelitian berbasis bulan
- Semua diagram menggunakan environment `figure` dengan caption dan label

---

## Referensi Cepat LaTeX

### Citasi
```latex
\citep{key}   % (Author, Year)
\citet{key}   % Author (Year)
```

### Gambar
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/nama-file}
  \caption{Deskripsi gambar}
  \label{fig:label}
\end{figure}
```

### Tabel
```latex
\begin{table}[H]
  \centering
  \caption{Judul tabel}
  \begin{tabular}{|l|c|r|}
    \hline
    Kolom 1 & Kolom 2 & Kolom 3 \\
    \hline
    Data & Data & Data \\
    \hline
  \end{tabular}
  \label{tab:label}
\end{table}
```

### Kode / Listing
```latex
\begin{lstlisting}[language=yaml, caption={Judul}]
# kode di sini
\end{lstlisting}
```

---

## Kompilasi

```bash
export PATH="/Library/TeX/texbin:$PATH"
cd proposal/  # atau cd skripsi/
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

---

## Catatan Penting

- Jangan lupa mengisi metadata (nama, NIM, dosen pembimbing, dosen penguji) di `main.tex`
- Ganti `figures/logougm.pdf` dengan logo UGM resmi
- Untuk proposal: fokus pada **perencanaan**, bukan hasil
- Untuk skripsi: setiap bab harus terstruktur dan merujuk ke pedoman
- Gunakan `\bibliography{references}` untuk daftar pustaka
- Pastikan semua `\citep` / `\citet` ada di `references.bib`
