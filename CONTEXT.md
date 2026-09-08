# Skripsi — Topik 14 Terpilih

> **Status: TOPIK TERPILIH** — Topik 14, *Ketahanan Kuantisasi Lintas-SLM untuk NLP Bahasa Indonesia*. `CONTEXT.md` ini berisi constraint umum dan keputusan yang berlaku untuk topik terpilih. Detail eksplorasi Topik 14 disimpan di `notes/exploration/topic-14-slm-quantization-indonesian-nlp.md`.

## Jenis TA

Jenis TA **mengikuti topik yang akhirnya dipilih**, bukan keputusan di depan:
- **Skripsi Inovasi Produk** — jika topik menghasilkan produk/prototipe yang jelas (Bab 4 Perancangan Produk, Bab 5 Pembuatan Produk, Bab 6 Pengujian dan Evaluasi Produk, dengan Kesimpulan+Saran).
- **Skripsi Ilmiah Akademik** — jika topik berupa eksperimen/analisis tanpa produk (Bab 4-6 berisi metodologi, hasil, evaluasi).

Topik yang dipilih berupa studi empiris dengan pipeline benchmark yang reproducible, sehingga jenis TA yang sesuai adalah Skripsi Ilmiah Akademik. Artefak pipeline berfungsi mendukung reproduksibilitas, bukan menjadi produk utama.

Scope inti dibatasi pada evaluasi kuantisasi beberapa Small Language Model untuk klasifikasi sentimen Bahasa Indonesia. QA singkat dan perbandingan Indonesia--Inggris bukan bagian dari scope minimum.

## Constraint keras (tidak bisa berubah)

- **Anggaran: $0.** Hanya API free tier (Google AI Studio, Groq, OpenRouter free) atau data/model lokal yang ringan.
- **Hardware: AMD Ryzen 3 5300U, 9GB RAM, TIDAK ada GPU, 8.5GB disk kosong.** Tidak bisa training/fine-tuning model besar. Tidak bisa inference model 7B+ lokal. Eksperimen harus disesuaikan.
- **Durasi: 6 bulan** setelah proposal disetujui.
- **Bahasa: Indonesia** untuk proposal/skripsi; abstract Inggris; istilah teknis boleh Inggris dengan penjelasan ID pada sebutan pertama.
- **Tingkat: S1 UGM.**

## Pedoman penulisan

- Pedoman resmi: `examples/pedoman_ta.pdf` (prioritas utama).
- Contoh: `examples/contoh_proposal.pdf`, `examples/contoh_skripsi.pdf` (referensi visual saja, bukan aturan).
- Detail struktur per jenis TA: lihat `AGENTS.md`.

## Pelajaran dari sesi grilling 2026-07-20 (WAJIB diterapkan ke kandidat baru)

1. **Verifikasi kebaruan MANDIRI** sebelum meng-accept topik. Cek arXiv, Google Scholar, Semantic Scholar, ACL Anthology untuk setiap klaim "pertama" atau "belum ada".
2. **Jangan trust catatan eksplorasi lama mentah-mentah.** Catatan 2026-06-08 belum tahu paper April-Juni 2026. Cek ulang tanggal dan paper terbaru.
3. **Cek constraint $0 + hardware di awal grilling**, jangan di akhir setelah banyak keputusan dibuat.
4. **Klaim kebaruan harus spesifik dan dapat dipertahankan.** Hindari "pertama menguji X" tanpa verifikasi; lebih baik "ekstensi terkontrol dari Y dengan diferensiasi Z".
5. **Status kandidat sebelum pemilihan: STORED.** Setelah dipilih, detail dan scope topik harus dikunci bertahap melalui pilot serta verifikasi literatur.

## Topik terpilih dan kandidat yang diarsipkan

Topik terpilih:

- **Topik 14 — Ketahanan Kuantisasi Lintas-SLM untuk NLP Bahasa Indonesia**.
  - Detail: `notes/exploration/topic-14-slm-quantization-indonesian-nlp.md`
  - Fokus awal: degradasi relatif, transisi kesalahan, dan efisiensi CPU pada pipeline GGUF yang reproducible.

Kandidat lain telah diarsipkan di `notes/exploration/archive/`:

- Topik 01: IndoAgentBench.
- Topik 02: Foundation-vs-Supervised Shortcut Attribution.
- Topik 03, 04, 05, dan kandidat lama lain yang tercantum di arsip.

## Language (terminologi umum skripsi)

**Proposal**:
Dokumen rencana penelitian; untuk UGM berisi Bab 1 Pendahuluan (Latar Belakang, Rumusan Masalah, Batasan, Tujuan, Manfaat), Bab 2 Penelitian Terkait, Bab 3 Metode dan Rancangan, Bab 4 Jadwal.
_Avoid_: research plan, prapenelitian.

**Skripsi**:
Dokumen akhir TA; untuk topik ilmiah akademik ini berisi Bab 1 Pendahuluan (Latar Belakang, Rumusan Masalah, Batasan, Tujuan, Manfaat), Bab 2 Kajian Pustaka dan Penelitian Terkait, Bab 3 Metodologi Penelitian, Bab 4 Implementasi dan Hasil Penelitian, Bab 5 Pembahasan, serta Bab 6 Kesimpulan dan Saran.
_Avoid_: thesis, laporan akhir.

**Kandidat topik**:
Satu ide topik spesifik yang sudah digrilling dan diverifikasi kebaruannya. Sebelum pemilihan, kandidat berstatus `STORED`; pada repo ini Topik 14 sudah dipilih.
_Avoid_: topik final, topik terpilih.

**Verifikasi kebaruan mandiri**:
Proses cek literatur independen (arXiv, Google Scholar, Semantic Scholar, ACL Anthology) sebelum meng-accept topik; wajib untuk setiap kandidat.
_Avoid_: literature review, related work.
