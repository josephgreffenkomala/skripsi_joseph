---
cssclasses:
  - full-width
---
# Prompt Next Session — Eksplorasi Topik Alternatif Skripsi

> Copy blok di bawah ini ke sesi baru. Gunakan untuk eksplorasi topik **alternatif** (bukan IndoAgentBench).

---

## Prompt (copy mulai dari sini)

Aku mau eksplorasi topik proposal skripsi yang **alternatif** — bukan IndoAgentBench (kandidat bahasa-coding-agent yang sudah disimpan, belum di-accept). Pakai skill `/grill-me` (atau `/grilling` + `/domain-modeling` jika lebih cocok) untuk menginterogasi ide-ide baru satu per satu.

### Konteks yang HARUS kamu baca dulu

1. `AGENTS.md` — pedoman UGM Skripsi (WAJIB ikuti).
2. `CONTEXT.md` — status: EKSPLORASI, belum ada topik di-accept; general lintas-topik, hanya constraint + terminologi umum. Glossary kandidat spesifik (mis. `indoagentbench-glossary.md`) berlaku hanya jika kandidat bersangkutan dipilih.
3. `notes/exploration/grilling-decisions-2026-07-20.md` — snapshot grilling 17 pertanyaan untuk IndoAgentBench (status STORED).
4. `notes/exploration/literature-comparison-2026-07-20.md` — pembanding literatur coding agent (Ren et al. 2026 sudah menguji efek bahasa Cina di SWE-bench).
5. `notes/exploration/indoagentbench-glossary.md` — glossary khusus IndoAgentBench (hanya berlaku jika topik itu dipilih).
6. `notes/exploration/indonesian-prompt-coding-agent-topic-2026-06-08.md` — catatan B (IndoAgentBench), ada disclaimer kebaruan.
7. `notes/exploration/ai-topic-options-2026-06-08.md` — gelombang 1 (RAG, NLP, hate-speech, bahasa daerah, PM2.5, food, legal).
8. `notes/exploration/ai-topic-options-wave2-2026-06-08.md` — gelombang 2 (debugging tutor, coding agent, ASR, multimodal, AI tutor, cybersecurity, memory, synthetic data).
9. `notes/exploration/computer-vision-xai-topic-options.md` — XAI audit toolkit (penyakit tanaman, CXR, jalan).
10. `notes/exploration/xai-toolkit-website-topic.md` — website XAI audit.

### Constraint KERAS (tidak bisa berubah)

- **Anggaran: $0.** Hanya API free tier (Google AI Studio, Groq, OpenRouter free) atau data/model lokal yang ringan.
- **Hardware: AMD Ryzen 3 5300U, 9GB RAM, TIDAK ada GPU, 8.5GB disk kosong.** Tidak bisa training/fine-tuning model besar. Tidak bisa inference model 7B+ lokal.
- **Durasi: 6 bulan** setelah proposal disetujui.
- **Jenis TA: mengikuti topik.** User belum memilih Inovasi Produk vs Ilmiah Akademik — jenis TA akan ditentukan oleh topik yang akhirnya dipilih, bukan di depan. Jangan jadikan jenis TA sebagai pertanyaan grilling awal. Jika topik menghasilkan produk/prototipe yang jelas → Inovasi Produk. Jika topik berupa eksperimen/analisis tanpa produk → Ilmiah Akademik. Struktur bab mengikuti jenis TA masing-masing (Inovasi Produk: Bab 4 Perancangan Produk, Bab 5 Pembuatan, Bab 6 Pengujian Produk; Ilmiah Akademik: Bab 4-6 metodologi, hasil, evaluasi).
- **Bahasa: Indonesia** untuk proposal/skripsi; abstract Inggris.
- **Tingkat: S1 UGM.**

### Pelajaran dari sesi sebelumnya (WAJIB diterapkan)

1. **Verifikasi kebaruan MANDIRI sebelum meng-accept topik.** Catatan B mengklaim "belum ada benchmark bahasa natural coding agent" — ternyata Ren et al. (2026, arXiv:2604.14210) sudah menguji Cina di SWE-bench. Cek arXiv, Google Scholar, Semantic Scholar, ACL Anthology untuk setiap klaim "pertama" atau "belum ada".
2. **Jangan trust catatan eksplorasi lama mentah-mentah.** Catatan 2026-06-08 belum tahu paper April-Juni 2026. Cek ulang tanggal dan paper terbaru.
3. **Grilling satu pertanyaan per kali, beri rekomendasi untuk setiap pertanyaan.** Jangan batch pertanyaan.
4. **Update `CONTEXT.md` saat istilah kristal, `docs/adr/` saat keputusan hard-to-reverse.** Tapi semua berstatus `stored` / `pending` sampai topik benar-benar di-accept.
5. **Cek constraint $0 + hardware di awal**, jangan di akhir setelah grilling 17 pertanyaan (sesi sebelumnya kena ini di pertanyaan 15).
6. **Klaim kebaruan harus spesifik dan dapat dipertahankan.** Hindari "pertama menguji X" tanpa verifikasi; lebih baik "ekstensi terkontrol dari Y dengan diferensiasi Z".

### Tujuan sesi ini

1. Pilih **1 topik alternatif** yang paling menarik untuk dieksplorasi (boleh dari catatan eksplorasi di atas, atau ide baru yang realistis di constraint ini).
2. Grilling topik tersebut secara mendalam sampai punya: rumusan masalah, produk, metrik, sumber data, jadwal, batasan.
3. **Verifikasi kebaruan via literatur** sebelum meng-accept. Catat di `notes/exploration/literature-comparison-<topik>-YYYY-MM-DD.md`.
4. Bandingkan kekuatan vs IndoAgentBench (yang STORED) secara jujur — mana yang lebih layak.
5. JANGAN langsung meng-accept. Simpan sebagai kandidat baru dengan status `STORED` di `CONTEXT.md` / `docs/adr/` kalau perlu. Putusan akhir tetap user punya.

### Output yang diharapkan

- File `notes/exploration/grilling-<topik-baru>-YYYY-MM-DD.md` — ringkasan grilling kandidat baru.
- File `notes/exploration/literature-comparison-<topik-baru>-YYYY-MM-DD.md` — verifikasi kebaruan mandiri.
- Update `CONTEXT.md` HANYA untuk terminologi umum lintas-topik; glossary spesifik kandidat baru simpan di file tersendiri (mis. `notes/exploration/<topik-baru>-glossary.md`), tidak dicampur ke `CONTEXT.md`.
- Status kandidat baru: `STORED`, bukan `accepted`. Glossary kandidat berlaku hanya jika kandidat bersangkutan dipilih.
- Perbandingan singkat vs IndoAgentBench di akhir sesi.

### Pertanyaan pertama yang harus kamu jawab sebagai agent

User **belum tahu arah topik yang ingin dieksplorasi** dan butuh bantuan memetakan pilihan sebelum memilih. Jangan tanya "arah mana yang ingin dieksplorasi?" secara langsung — user belum bisa menjawab itu.

Sebagai gantinya, mulai sesi dengan **brainstorming terstruktur**, bukan grilling langsung:

1. **Pemetaan pilihan**: baca semua catatan eksplorasi di `notes/exploration/`, ringkas tiap kandidat dalam 2-3 kalimat (ide, kenapa menarik, risiko utama). Sajikan sebagai tabel atau list terurut supaya user bisa lihat semua opsi sekaligus.
2. **Filter awal berdasarkan constraint keras** ($0, hardware lemah, 6 bulan, S1): tandai kandidat mana yang mustahil di constraint ini (mis. ASR fine-tuning butuh GPU, NLP bencana butuh data besar), mana yang masih feasible. Jangan tanya user untuk kandidat yang sudah jelas tidak feasible.
3. **Rekomendasi arah**: berdasarkan feasibility + kebaruan potensial + kesesuaian dengan minat yang terbaca dari sesi sebelumnya, rekomendasikan **3-5 arah** paling menjanjikan untuk dieksplorasi. Jelaskan singkat kenapa.
4. **Tanya user**: "Dari 3-5 arah yang direkomendasikan, mana yang paling menarik untuk dieksplorasi lebih dalam? Atau ada arah lain yang belum tercakup?" Beri user ruang untuk pilih, modifikasi, atau usul sendiri.
5. **Grilling topik terpilih**: setelah user pilih satu arah, mulai grilling satu pertanyaan per kali, beri rekomendasi untuk setiap pertanyaan.

**Jenis TA jangan ditanya di awal.** Jenis TA mengikuti topik yang dipilih — jika topik menghasilkan produk/prototipe → Inovasi Produk; jika topik berupa eksperimen/analisis murni → Ilmiah Akademik. Keputusan jenis TA muncul alami di tengah grilling, bukan di awal.

Tunggu jawaban user di tiap langkah, baru lanjut.

---

## Catatan penggunaan

- Prompt ini disimpan di `notes/next-session-prompt-explore-different-idea.md`.
- Setelah sesi baru selesai, simpan artefak grilling + verifikasi literatur mengikuti pola file sebelumnya.
- Jangan pernah meng-accept topik tanpa verifikasi literatur mandiri — ini pelajaran utama dari sesi 2026-07-20.