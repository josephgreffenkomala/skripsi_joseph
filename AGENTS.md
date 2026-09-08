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

Topik yang sedang dikembangkan adalah **evaluasi trade-off kualitas dan efisiensi kuantisasi pada Small Language Model untuk klasifikasi sentimen Bahasa Indonesia**.

Jenis tugas akhir yang berlaku adalah **skripsi ilmiah akademik**, karena penelitian berfokus pada eksperimen terkontrol dan analisis empiris. Artefak pipeline evaluasi digunakan untuk mendukung reproduksibilitas, bukan sebagai produk utama.

Constraint utama topik:

- Model utama: Qwen3-0.6B, Qwen3-1.7B, Gemma 3 1B-IT, dan Sailor2-1B-Chat, dengan kemungkinan pengurangan jumlah model berdasarkan hasil pilot.
- Tugas inti: klasifikasi sentimen Bahasa Indonesia. QA singkat dan perbandingan Indonesia--Inggris bukan bagian dari scope minimum.
- Kondisi model: baseline presisi tinggi dan beberapa tingkat kuantisasi GGUF dalam satu pipeline `llama.cpp`.
- Evaluasi: kualitas prediksi, kepatuhan format, transisi kesalahan per sampel, ukuran berkas, peak RAM, latensi, throughput, dan trade-off Pareto.
- Lingkungan utama: CPU konsumen yang sama, tanpa GPU, dengan konfigurasi eksperimen yang dikendalikan.

Jangan membuat klaim bahwa penelitian ini memperkenalkan algoritma kuantisasi baru atau merupakan penelitian pertama tentang kuantisasi SLM, kuantisasi lintas bahasa, atau kuantisasi model Bahasa Indonesia. Klaim kontribusi dibatasi pada evaluasi terkontrol dalam ruang model, data, runtime, dan perangkat keras yang diuji.

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
