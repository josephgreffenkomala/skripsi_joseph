# Pembanding Literatur — Efek Bahasa Natural pada Coding Agent

Date: 2026-07-20
Target: proposal (Bab 2 Penelitian Terkait)
Status: VERIFIED — verifikasi literatur mandiri selesai. Hasil ini mengikat sebagai pembanding Bab 2 **jika** topik IndoAgentBench dipilih; jika topik lain dipilih, file ini tetap sebagai referensi umum tentang landscape coding agent.

## Konteks

Setelah grilling 17 pertanyaan, user menanyakan "memang ini baru?". Verifikasi independen ke arXiv menemukan paper yang sudah mengisi gap inti catatan B. File ini mencatat pembanding yang wajib masuk Bab 2 proposal dan reframing klaim kebaruan.

## Pembanding Utama (wajib di Bab 2)

### Ren et al. (2026) — "Chinese Language Is Not More Efficient Than English in Vibe Coding"

arXiv:2604.14210, submitted 6 April 2026, cs.SE.

Inti:
- Menggunakan SWE-bench Lite untuk menguji apakah prompt Bahasa Cina lebih token-efficient dan lebih sukses dibanding Bahasa Inggris pada coding agent.
- Temuan: token cost model-dependent (MiniMax-2.7 1.28x lebih mahal untuk Cina, GLM-5 lebih murah), tetapi success rate Cina secara konsisten lebih rendah dari Inggris di semua model.
- Mengukur cost efficiency sebagai expected cost per successful task.

Implikasi pada klaim kebaruan kita:
- SUDAH menguji efek bahasa natural instruksi pada coding agent repository-level.
- SUDAH menggunakan SWE-bench sebagai infrastruktur.
- Persis struktur yang direncanakan catatan B, hanya beda bahasa (Cina bukan Indonesia).
- Karena itu klaim "pertama menguji efek bahasa natural pada coding agent repository-level" GUGUR.

Yang TIDAK dikerjakan paper ini (kebaruan kita yang masih defensible):
- Bahasa Indonesia (low-resource, non-CJK) — belum diuji
- Kondisi translate-then-act — tidak ada
- Failure taxonomy (4 kategori a priori + emergent) — tidak ada
- Audit ekuivalensi bilingual dengan rubrik + Cohen's kappa — tidak ada
- Transformasi task untuk mitigasi kontaminasi (6C) — tidak ada
- 2 keluarga model berbeda (Gemini + Llama) — paper Cina pakai MiniMax + GLM, tidak overlap

Posisi kita setelah pembanding ini:
- Ekstensi paper Ren et al. (2026) ke Bahasa Indonesia + kondisi ketiga + analisis kegagalan + audit ekuivalensi.
- Bukan "pertama menguji efek bahasa", tapi "pertama untuk Bahasa Indonesia dengan analisis mode kegagalan dan audit ekuivalensi terkontrol".

## Pembanding Pendukung

### Claw-SWE-Bench (Juni 2026, arXiv:2606.12344)

"Multilingual SWE-bench-style benchmark and adapter protocol" — sumbernya SWE-bench-Multilingual (= Multi-SWE-bench, bahasa pemrograman) + SWE-bench-Verified-Mini. Tidak menguji bahasa natural instruksi. Kontribusi pada adapter harness. Tidak tumpang tindih dengan kita.

### DeepSWE (Juli 2026, arXiv:2607.07946)

Benchmark 113 task original untuk mitigasi kontaminasi training data. Konsep sama dengan 6C kita (transformasi task untuk anti-kontaminasi), tapi DeepSWE menulis task dari nol; kita transformasi subset SWE-bench. Bisa dirujuk sebagai pembanding validitas anti-kontaminasi.

### mHumanEval (Raihan et al., NAACL 2025)

Function-level, single-turn, 200+ NL termasuk Bahasa Indonesia (expert translation 15 NL). Sudah ada Bahasa Indonesia, tapi hanya function-level, bukan repository-level, dan bukan coding agent. Dirujuk sebagai bukti bahwa Bahasa Indonesia sudah diuji di level sederhana, sehingga kontribusi kita adalah naik ke level repository agent.

### HumanEval-XL (Peng et al., LREC-COLING 2024)

Function-level, 23 NL x 12 PL. Sama dengan mHumanEval — function-level, bukan repository agent. Dirujuk sebagai literatur multilingual code generation.

### Multi-SWE-bench (Zan et al., Apr 2025)

"Multilingual" = bahasa pemrograman (Java/TS/JS/Go/Rust/C/C++), bukan bahasa natural. Repository-level + agent. Dirujuk untuk membedakan "multilingual = PL" vs "multilingual = NL" (inti gap yang kita isi).

### SWE-PolyBench (Rashid et al., Apr 2025)

"Multi-language" = bahasa pemrograman (Java/JS/TS/Python). Sama dengan Multi-SWE-bench. Repository-level + agent. Dirujuk sebagai pembanding bench repository-level.

## Klaim Kebaruan yang Defensible (setelah reframing)

1. **Bahasa Indonesia (low-resource, non-CJK)**: belum diuji pada coding agent repository-level. mHumanEval sudah ada ID tapi hanya function-level.
2. **Kondisi translate-then-act**: tidak ada di paper Ren et al. (hanya EN vs Cina, tidak ada mitigasi ringan).
3. **Failure taxonomy 4 kategori a priori + 1-2 emergent dengan 2 annotator + Cohen's kappa**: tidak ada di paper pembanding. Kontribusi metodologis.
4. **Audit ekuivalensi bilingual dengan rubrik multi-dimensi**: kontribusi metodologis yang dapat dikutip.
5. **Transformasi task (6C) untuk mitigasi kontaminasi**: paper Ren et al. tidak melakukan ini; DeepSWE menulis task baru, kita transformasi subset existing — pendekatan berbeda.

## Klaim yang GUGUR (jangan digunakan)

- "Pertama menguji efek bahasa natural pada coding agent repository-level" — sudah didahului Ren et al. (2026).
- "Belum ada benchmark bahasa natural untuk coding agent" — mHumanEval sudah ada (function-level), Ren et al. sudah ada (repository-level Cina).
- "Belum ada yang menguji multilingual NL pada SWE-bench" — Ren et al. sudah melakukannya untuk Cina.

## Posisi Ilmiah Akhir

Topik ini adalah **ekstensi terkontrol** dari Ren et al. (2026) dengan empat diferensiasi:
1. Bahasa Indonesia (low-resource, non-CJK) — generalisasi bahasa
2. Translate-then-act sebagai kondisi ketiga — intervensi mitigasi ringan
3. Failure taxonomy + audit ekuivalensi — kontribusi metodologis anotasi
4. Transformasi task anti-kontaminasi — validitas eksperimen

Framing ini jujur, defensible, dan tetap layak untuk Skripsi Inovasi Produk. Paper Ren et al. menjadi pembanding utama yang MEMPERKUAT (bukan menggugurkan) topik kita — keberadaannya menunjukkan fenomena ini nyata dan layak dieksplorasi lintas bahasa.