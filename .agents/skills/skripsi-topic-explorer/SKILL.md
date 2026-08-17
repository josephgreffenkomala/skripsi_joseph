---
name: skripsi-topic-explorer
description: Explore, sharpen, compare, and validate thesis topic ideas, research questions, product scope, novelty, internet sources, and evaluation plans for UGM proposal or skripsi projects. Use when the user asks to brainstorm topic ideas, compare multiple thesis/product titles, evaluate novelty, research literature online, or build structured topic exploration notes before writing LaTeX content.
---

# Skripsi Topic Explorer

Use this skill to explore, brainstorm, evaluate, and sharpen proposal or skripsi topics without assuming any hardcoded default topic. It handles both single-topic deep dives and multi-topic exploration, producing standardized, user-friendly, and novelty-focused documentation.

## Core References

Start by reading these local files when relevant:

- `AGENTS.md` for official repo rules, proposal-vs-skripsi chapter structures, and priority order.
- `README.md` for repository layout and build workflow.
- `template/proposal/main.tex` and `template/skripsi/main.tex` when target structure needs verification.
- `references/repo-thesis-map.md` in this skill for generic thesis topic framing and structure maps.
- `notes/exploration/` for reading or saving topic catalogs, source notes, and detailed topic breakdowns.

Use `examples/pedoman_ta.pdf` as the highest authority when guidance details differ.

## Core Rules & Principles

1. **No Default Topic Lock**: Never force or assume a specific default topic (e.g., InvenioRDM, GitOps, AI, etc.) unless the user specifies it or the existing project files explicitly demand it. Always discover or clarify the user's domain/interest.
2. **Multi-Topic Ready**: Be ready to generate, analyze, and compare multiple topic candidates in parallel.
3. **Novelty First**: Every topic candidate must explicitly state its novelty (kebaruan / state-of-the-art difference) compared to existing literature or existing software solutions.
4. **User-Friendly Clarity**: Include plain-language, jargon-free explanations ("Penjelasan Sederhana") for every topic so the user quickly understands the core value and practical application.
5. **Standardized Dual-Layer Output**:
   - **Layer 1 (1 Catalog File)**: `notes/exploration/topic-catalog.md` — High-level summary catalog comparing all topics.
   - **Layer 2 (Detailed Topic Files)**: `notes/exploration/topic-01-[slug].md`, `notes/exploration/topic-02-[slug].md` — In-depth breakdown per topic.

---

## Output Architecture

When performing topic exploration (especially for multiple topics), produce the following standardized artifacts in `notes/exploration/`:

### 1. Catalog File: `notes/exploration/topic-catalog.md`

Serves as the master index and comparative decision matrix.

```markdown
# Katalog Eksplorasi Topik Skripsi / Proposal

Tanggal: YYYY-MM-DD
Target Document: Proposal | Skripsi | Both
Bidang Utama: [Domain/Subject Area]

## Executive Summary
[Ringkasan singkat mengenai arah eksplorasi dan rekomendasi utama]

## Tabel Perbandingan Topik

| No | Judul Topik (Bahasa Indonesia) | Ringkasan Kebaruan (Novelty) | Tingkat Kesulitan | Kelayakan (Feasibility) | Rekomendasi |
|---|---|---|---|---|---|
| 01 | [Judul 1] | [Kebaruan utama] | Sedang/Tinggi | Tinggi | ⭐⭐⭐⭐⭐ |
| 02 | [Judul 2] | [Kebaruan utama] | Sedang | Sedang | ⭐⭐⭐ |

## Ringkasan Singkat & Penjelasan Sederhana

### Topik 01: [Judul 1]
- **Penjelasan Sederhana**: [Penjelasan ringkas tanpa istilah rumit]
- **Kebaruan Utama**: [Point-by-point novelty vs existing work]
- **File Detail**: [`topic-01-slug.md`](topic-01-slug.md)

### Topik 02: [Judul 2]
- **Penjelasan Sederhana**: [Penjelasan ringkas tanpa istilah rumit]
- **Kebaruan Utama**: [Point-by-point novelty vs existing work]
- **File Detail**: [`topic-02-slug.md`](topic-02-slug.md)

## Panduan Pemilihan untuk Mahasiswa
[Saran konkret untuk memilih topik berdasarkan minat, ketersediaan data/infrastruktur, dan waktu]
```

### 2. Detailed Topic Files: `notes/exploration/topic-01-[slug].md`, `topic-02-[slug].md`

Each topic gets its own standalone detailed analysis file.

```markdown
# Detail Topik 01: [Judul Utama Topik]

Date: YYYY-MM-DD
Catalog Reference: [`topic-catalog.md`](topic-catalog.md)

## 1. Opsi Judul (Title Candidates)
- **Bahasa Indonesia**: [Judul formal Indonesia]
- **English**: [Formal English Title]

## 2. Penjelasan Sederhana (Easy-to-Understand Breakdown)
[Penjelasan konsep produk/penelitian dengan bahasa yang mudah dipahami oleh siapapun, menjelaskan apa masalahnya, apa yang dibuat, dan mengapa penting.]

## 3. Analisis Kebaruan (Novelty & State-of-the-Art)
- **Kondisi Saat Ini (Existing State/Literature)**: [Apa yang sudah ada di jurnal/tools saat ini]
- **Keterbatasan / Gap**: [Apa kelemahan atau hal yang belum diselesaikan oleh solusi existing]
- **Kebaruan Solusi Ini (Novelty Contribution)**: [Nilai kebaruan spesifik yang ditawarkan produk/penelitian ini]
- **Matriks Perbandingan Novelty**:
  | Fitur / Parameter | Solusi Conventional / Existing | Topik Ini (Proposed) |
  |---|---|---|
  | ... | ... | ... |

## 4. Perumusan Produk & Masalah (UGM Inovasi Produk)
- **Masalah Nyata**: [Problem statemen konkret]
- **Solusi / Produk Inovatif**: [Bentuk produk/prototipe yang dikembangkan]
- **Batasan Masalah/Produk**: [Scope boundaries]

## 5. Landasan Teknik & Ilmiah (Technical & Scientific Basis)
- **Teknologi / Framework**: [Daftar stack dan tools]
- **Metode / Algoritma / Arsitektur**: [Dasar ilmiah atau mekanisme kerja]

## 6. Rencana Pengujian & Parameter Ukur (Evaluation Plan)
- **Metode Pengujian**: [Eksperimen, benchmark, user evaluation, etc.]
- **Metrik Evaluasi**: [Daftar metrik kuantitatif/kualitatif, e.g. latency, success rate, drift, recovery time]

## 7. Pemetaan ke Bab Skripsi/Proposal (Chapter Mapping)
- **Bab 1**: [Point-point isi Pendahuluan]
- **Bab 2**: [Point-point Penelitian Terkait / Ide Inovatif]
- **Bab 3-4**: [Point-point Metode & Perancangan]

## 8. Catatan Sumber & Literatur (Source Notes & Citation Checklist)
- [ ] Source 1: Title, Authors, Year, URL/DOI - Role: (Background/Novelty Baseline)
- [ ] Source 2: Documentation / Standard - Role: (Technical Basis)

## 9. Penyerahan ke Penulisan LaTeX (Draft Handoff)
- **Target File**: `proposal/chapters/...` or `skripsi/chapters/...`
- **Kebutuhan Gambar/Diagram**: [Daftar flowchart, arsitektur, diagram]
- **Pertanyaan ke Pengguna**: [Hal yang perlu dikonfirmasi pengguna]
```

---

## Exploration & Internet Research Workflow

When requested to brainstorm or explore topics:

1. **Discover Domain & User Intent**:
   - Check user prompt and existing repo context for domain guidelines.
   - If no domain is specified, ask or suggest 2–3 relevant domains based on the user's field, or ask what area they prefer.

2. **Conduct Internet / Literature Verification**:
   - Perform search for existing literature, repositories, or tools related to the candidate topics.
   - Verify that proposed novelty claims are valid and not already standard baseline practice.

3. **Generate Standardized Output**:
   - Always create/update `notes/exploration/topic-catalog.md`.
   - Create individual `notes/exploration/topic-01-[slug].md` files for each candidate topic.
   - Ensure every topic includes clear Indonesian/English titles, plain-language explanation, novelty evaluation, technical basis, and evaluation metrics.

4. **Present Clean Summary to User**:
   - In chat response, provide a brief overview of the topics explored, point to the generated Catalog file (`topic-catalog.md`), and highlight the top recommended topic.

---

## Asking for Confirmation

Keep questions short and non-blocking. Ask when clarification is needed on:
- Preferred domain/field if vague.
- Target document type (`proposal` vs `skripsi`).
- Selected topic candidate to proceed into LaTeX drafting.

