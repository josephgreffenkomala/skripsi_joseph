# Repo Thesis Map

## Repository Layout

- `AGENTS.md`: highest-level local guidance for UGM proposal and skripsi structure.
- `examples/pedoman_ta.pdf`: official guide and highest authority.
- `examples/contoh_proposal.pdf`: visual/format reference only.
- `examples/contoh_skripsi.pdf`: visual/format reference only.
- `template/proposal/`: proposal LaTeX source.
- `template/skripsi/`: skripsi LaTeX source.
- `notes/exploration/`: durable notes from topic exploration, internet research, source review, evaluation planning, diagram planning, and writing handoffs.
- `Makefile`: local and Docker build commands.

## Proposal Structure

Class option: `\documentclass[proposal,indonesia]{ugmskripsi}`.

Main chapters:

1. `chapters/bab1-pendahuluan.tex`: Latar Belakang, Rumusan Masalah, Batasan Masalah, Tujuan Penelitian, Manfaat Penelitian.
2. `chapters/bab2-penelitian-terkait.tex`: state of the art and literature review.
3. `chapters/bab3-metodologi.tex`: methodology, design, architecture, flowchart, testing plan.
4. `chapters/bab4-jadwal-penelitian.tex`: month-based Gantt chart.

Proposal should focus on planning, not completed results.

## Skripsi Structure

Class option: `\documentclass[skripsi,indonesia]{ugmskripsi}`.

Main chapters:

1. `chapters/bab1-pendahuluan.tex`: Latar Belakang, Perumusan Produk, Batasan Produk, Tujuan Penelitian, Manfaat Penelitian.
2. `chapters/bab2-identifikasi-masalah.tex`: real problem identification and innovative idea.
3. `chapters/bab3-kajian-ilmiah.tex`: scientific basis, technology, methods, related work.
4. `chapters/bab4-perancangan.tex`: architecture, technical design, UI/UX or database design if relevant.
5. `chapters/bab5-pembuatan.tex`: implementation and component integration.
6. `chapters/bab6-pengujian.tex`: testing, evaluation, conclusion, and suggestions.

## Product Topic Framing Guidelines

Topics for UGM Skripsi Inovasi Produk should align with the student's area of interest and field of study.

Possible product framing elements:

- A reproducible, declarative software/infrastructure system or prototype.
- An automated workflow, algorithm, or platform that solves a practical institutional or domain problem.
- A prototype that improves performance, security, maintainability, auditability, or user experience.

Possible evaluation metrics:

- Success rate / accuracy / precision / throughput.
- Latency / operational completion time / recovery time.
- Resource consumption, error rate, configuration drift reconciliation, or user satisfaction.

Possible diagrams:

- Research methodology flowchart.
- System architecture & component interaction diagram.
- Sequence / data flow / state transition diagram.
- Entity-Relationship Diagram (ERD) or schema design.

## Exploration Output Structure

Outputs are stored in `notes/exploration/`:

- `notes/exploration/topic-catalog.md` (Master catalog & comparative matrix for all explored topics)
- `notes/exploration/topic-01-[slug].md`, `topic-02-[slug].md` (Individual detailed topic breakdown per topic)
- `notes/exploration/source-notes.md` (Internet literature research & BibTeX candidate notes)


