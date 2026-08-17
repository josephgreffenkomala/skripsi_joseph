# Skripsi — Topik Belum Diputuskan

> **Status: EKSPLORASI** — belum ada topik yang di-accept. `CONTEXT.md` ini bersifat general lintas-topik dan hanya berisi constraint + terminologi umum skripsi yang tidak bergantung topik spesifik. Glossary kandidat spesifik disimpan terpisah per-kandidat di `notes/exploration/` (mis. `indoagentbench-glossary.md`).

## Jenis TA

Jenis TA **mengikuti topik yang akhirnya dipilih**, bukan keputusan di depan:
- **Skripsi Inovasi Produk** — jika topik menghasilkan produk/prototipe yang jelas (Bab 4 Perancangan Produk, Bab 5 Pembuatan Produk, Bab 6 Pengujian dan Evaluasi Produk, dengan Kesimpulan+Saran).
- **Skripsi Ilmiah Akademik** — jika topik berupa eksperimen/analisis tanpa produk (Bab 4-6 berisi metodologi, hasil, evaluasi).

User belum tahu arah topik dan butuh bantuan memetakan pilihan. Jangan jadikan jenis TA sebagai pertanyaan awal — biarkan muncul alami dari topik yang dipilih.

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
5. **Status kandidat: STORED, bukan accepted.** Putusan akhir tetap milik user.

## Kandidat topik yang sudah dieksplorasi

Setiap kandidat punya artefak tersendiri di `notes/exploration/`. Status kandidat berikut kandidat tersimpan, bukan accepted:

- **IndoAgentBench** (grilling 2026-07-20) — benchmark kesenjangan bahasa pada coding agent.
  - Grilling: `grilling-decisions-2026-07-20.md` (status STORED)
  - Verifikasi literatur: `literature-comparison-2026-07-20.md` (klaim kebaruan utama gugur sebagian — Ren et al. 2026 sudah menguji Cina di SWE-bench)
  - Glossary: `indoagentbench-glossary.md` (berlaku hanya jika topik ini dipilih)
  - ADR: `docs/adr/0001-free-tier-llm-choice.md` (berlaku hanya jika topik ini dipilih)

## Language (terminologi umum skripsi)

**Proposal**:
Dokumen rencana penelitian; untuk UGM berisi Bab 1 Pendahuluan (Latar Belakang, Rumusan Masalah, Batasan, Tujuan, Manfaat), Bab 2 Penelitian Terkait, Bab 3 Metode dan Rancangan, Bab 4 Jadwal.
_Avoid_: research plan, prapenelitian.

**Skripsi**:
Dokumen akhir TA; untuk Inovasi Produk berisi Bab 1 Pendahuluan (Latar Belakang, Perumusan Produk, Batasan, Tujuan, Manfaat), Bab 2 Identifikasi Masalah dan Ide Inovatif, Bab 3 Kajian Ilmiah, Bab 4 Perancangan Prototipe/Produk, Bab 5 Proses Pembuatan Produk, Bab 6 Pengujian dan Evaluasi Produk + Kesimpulan+Saran.
_Avoid_: thesis, laporan akhir.

**Kandidat topik**:
Satu ide topik spesifik yang sudah digrilling dan diverifikasi kebaruannya; status `STORED` (belum di-accept). Bisa ada lebih dari satu kandidat secara paralel.
_Avoid_: topik final, topik terpilih.

**Verifikasi kebaruan mandiri**:
Proses cek literatur independen (arXiv, Google Scholar, Semantic Scholar, ACL Anthology) sebelum meng-accept topik; wajib untuk setiap kandidat.
_Avoid_: literature review, related work.