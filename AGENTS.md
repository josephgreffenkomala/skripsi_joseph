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

Topik tugas akhir masih **dalam tahap eksplorasi**. Belum ada judul, pertanyaan penelitian, jenis tugas akhir, model, dataset, metode, lingkungan eksperimen, atau klaim kontribusi yang dikunci.

Proposal aktif harus diperlakukan sebagai **template/scaffold awal**, bukan sebagai dokumen yang mewakili topik penelitian tertentu. Isi yang masih berupa lorem ipsum, placeholder, atau komentar `TODO` boleh dipertahankan sampai arah topik dipilih.

Aturan selama eksplorasi:

- Jangan menganggap isi proposal lama sebagai scope penelitian yang berlaku.
- Jangan mengunci model, dataset, metode, runtime, perangkat keras, metrik, jadwal, atau desain eksperimen tanpa keputusan eksplisit setelah eksplorasi.
- Jangan menyalin klaim kontribusi, hasil pilot, atau kesimpulan dari topik sebelumnya ke proposal baru.
- Jika menambahkan catatan eksplorasi, tandai sebagai hipotesis atau opsi yang masih perlu diverifikasi, bukan sebagai fakta atau keputusan final.
- Setelah topik dipilih, perbarui bagian ini terlebih dahulu sebelum mengembangkan isi proposal secara substantif.

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
