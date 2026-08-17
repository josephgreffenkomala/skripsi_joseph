# Ringkasan Grilling — IndoAgentBench

Date: 2026-07-20
Target: proposal
Status: STORED — ide disimpan dulu, belum di-accept. Kebaruan diverifikasi dan tidak 100% baru (lihat `literature-comparison-2026-07-20.md`); topik ini kandidat sementara yang menunggu keputusan akhir.

## Konteks

Sesi grilling dengan `/grilling` + `/domain-modeling` skill pada 20 Juli 2026 untuk menentukan topik proposal skripsi. 17 pertanyaan diajukan satu per satu, semuanya menghasilkan keputusan sementara. Hasil diturunkan dari 6 catatan eksplorasi di `notes/exploration/`, terutama `indonesian-prompt-coding-agent-topic-2026-06-08.md` (catatan B). Setelah verifikasi literatur mandiri, klaim kebaruan asli catatan B gugur sebagian — lihat `literature-comparison-2026-07-20.md`. Keputusan di bawah adalah snapshot saat grilling, **belum final**, dan dapat berubah saat topik diputuskan.

## Produk

**IndoAgentBench** — self-service benchmark harness yang mengukur apakah bahasa natural instruksi (Bahasa Indonesia vs Bahasa Inggris) menyebabkan perbedaan kemampuan coding agent repository-level menyelesaikan issue. Skripsi berjenis Inovasi Produk; produk utama adalah benchmark, bukan middleware mitigasi.

## Judul Proposal (Bahasa Indonesia)

IndoAgentBench: Benchmark Berbasis Pasangan Issue Indonesia–Inggris untuk Mengukur Kesenjangan Bahasa pada Coding Agent Repository-Level

## Posisi Ilmiah (setelah verifikasi literatur 2026-07-20)

Topik adalah **ekstensi terkontrol** dari Ren et al. (2026, arXiv:2604.14210) yang sudah menguji efek bahasa Cina pada coding agent di SWE-bench Lite. Klaim "pertama menguji efek bahasa natural pada coding agent repository-level" GUGUR. Lihat `literature-comparison-2026-07-20.md` untuk detail pembanding.

Klaim kebaruan yang defensible (4 diferensiasi):
1. Bahasa Indonesia low-resource non-CJK — belum diuji pada coding agent repository-level
2. Translate-then-act sebagai kondisi ketiga — tidak ada di paper Ren et al.
3. Failure taxonomy + audit ekuivalensi bilingual dengan rubrik + kappa — kontribusi metodologis
4. Transformasi task (6C) anti-kontaminasi — paper Ren et al. tidak melakukan ini

Klaim yang GUGUR (jangan dipakai):
- "Pertama menguji efek bahasa natural pada coding agent repository-level"
- "Belum ada benchmark bahasa natural untuk coding agent"
- "Belum ada yang menguji multilingual NL pada SWE-bench"

## Pohon Keputusan

| # | Dimensi | Keputusan | Catatan |
|---|---|---|---|
| 1 | Ranah masalah | SE / coding agent | Paling matang metodologinya |
| 2 | Jenis produk | Benchmark (bukan CV/XAI) | Produk developer-facing |
| 3 | Scope produk | 3A-kuat: self-service benchmark harness | No language bridge produk |
| 4 | Bentuk 3A | Self-service yang dapat dipakai ulang | Dengan CLI, dokumentasi, laporan |
| 5 | Sumber task | 5A: subset SWE-bench existing | Lisensi dicek ulang |
| 6 | Mitigasi 5A | 6C: transformasi task + audit ekuivalensi | Mitigasi kontaminasi + kritik 'tidak ada kontribusi data' |
| 7 | Agent harness | OpenHands | Harness baseline kredibel |
| 8 | Kondisi bahasa | 8B: 3 kondisi (EN, ID direct, translate-then-act) | Membedakan bahasa vs kualitas terjemahan |
| 9 | Metrik utama | 9B: resolution rate + failure taxonomy | Cost metrics sebagai sekunder |
| 10 | Statistik | McNemar + Wilson CI | Paired binary outcome |
| 11 | Failure taxonomy | 10B: 4 kategori a priori + 1-2 emergent | 2 annotator, Cohen's kappa |
| 12 | Protokol audit | 12B: rubrik multi-dimensi + 2 annotator teman SE | Kontribusi metodologis |
| 13 | Nama produk | IndoAgentBench | Framing 'mengukur' |
| 14 | Durasi | 6 bulan setelah proposal disetujui | 6 fase paralel |
| 15 | Anggaran | $0 | Tidak ada dana |
| 16 | Model LLM | 16A: Gemini 2.0 Flash + Llama-3.3-70B via free tier | Revisi dari Claude 3.5 + DeepSeek-Coder; 1 run |
| 17 | Batasan masalah | 13 batasan | Lihat list di bawah |

## Research Questions

- **RQ1**: Apakah bahasa instruksi (ID direct vs EN) menyebabkan perbedaan resolution rate pada coding agent repository-level?
- **RQ2**: Apakah besar kesenjangan berbeda menurut model (Gemini 2.0 Flash vs Llama-3.3-70B) dan tingkat kesulitan task?
- **RQ3**: Pada tahap mana instruksi Indonesia paling sering menyebabkan kegagalan: pemahaman requirement, pencarian lokasi kode, implementasi, atau validasi?
- **RQ4-lite**: Apakah translate-then-act mengurangi kesenjangan tanpa menambah biaya berlebihan?

## Metrik

**Utama**:
- Resolution rate (paired McNemar + Wilson CI)
- Failure taxonomy (4 kategori a priori + emergent, Cohen's kappa)

**Sekunder**:
- Test pass rate, pass@k
- Jumlah langkah/tool calls, token, biaya, waktu
- Invalid patch rate, regression rate

## Eksperimen

- 40-60 task instance dari subset SWE-bench yang ditransformasi (6C)
- 3 kondisi bahasa: EN, ID direct, translate-then-act (8B)
- 2 model: Gemini 2.0 Flash (Google AI Studio free), Llama-3.3-70B (Groq free)
- 1 run per kondisi (keterbatasan free tier, catat di Bab 6)
- Total: 240-360 eksekusi (40-60 task × 3 kondisi × 2 model)

## Jadwal (Bab 4 Proposal, Gantt 6 bulan)

- Bulan 1: studi literatur + finalisasi desain + persiapan subset SWE-bench
- Bulan 2: transformasi task + terjemahan ID + audit ekuivalensi (12B)
- Bulan 3: implementasi harness (OpenHands integration, container, runner, trajectory logger, test exec, laporan)
- Bulan 4: pilot eksperimen + debugging + finalisasi harness
- Bulan 5: eksperimen penuh (3 kondisi × 2 model × task) + anotasi failure taxonomy
- Bulan 6: analisis statistik + penulisan Bab 5-6 + revisi + sidang

## 13 Batasan Masalah (Bab 1 Proposal)

1. Bahasa: hanya Bahasa Indonesia dan Inggris.
2. Bahasa pemrograman: hanya Python.
3. Agent harness: hanya OpenHands.
4. Model: hanya Gemini 2.0 Flash + Llama-3.3-70B.
5. Sumber task: subset SWE-bench yang ditransformasi.
6. Kondisi bahasa: 3 kondisi (EN, ID direct, translate-then-act).
7. Tidak ada language bridge produk terpisah.
8. Run: 1 run per kondisi (keterbatasan free tier).
9. Taksonomi kegagalan: 4 kategori a priori + 1-2 emergent.
10. Anotator: 2 annotator (penulis + teman SE).
11. Tidak ada evaluasi usability manusia.
12. Tidak ada fine-tuning model.
13. Tidak mengklaim generalisasi ke model selain 2 yang diuji.

## File Pendukung yang Dibuat

- `CONTEXT.md` — glossary domain (16 istilah)
- `docs/adr/0001-free-tier-llm-choice.md` — ADR pergeseran model dari Claude 3.5 + DeepSeek-Coder ke free tier

## Open Questions untuk Setelah Proposal

- Lisensi SWE-bench: verifikasi ulang sebelum Bulan 1 selesai.
- Apakah Groq free tier cukup stabil untuk 240-360 eksekusi dalam 1-2 bulan? Pilot di Bulan 4 akan validasi.
- Apakah 1 run cukup untuk McNemar? Pertimbangkan tambah run jika rate limit memungkinkan.
- Apakah teman SE sebagai annotator kedua sudah tersedia? Konfirmasi sebelum Bulan 2.

## Handoff ke Penulisan Proposal

Topik sudah siap diturunkan ke draft LaTeX proposal. Struktur proposal mengikuti AGENTS.md:

- Bab 1 (Pendahuluan): Latar Belakang, Rumusan Masalah (4 RQ), Batasan Masalah (13), Tujuan, Manfaat
- Bab 2 (Penelitian Terkait): state of the art SWE-bench, multilingual code generation, coding agent
- Bab 3 (Metode dan Rancangan): metodologi, bagan alir, perancangan harness + protokol audit
- Bab 4 (Jadwal): Gantt 6 bulan

Gunakan skill `skripsi-latex-writer` untuk menulis draft.