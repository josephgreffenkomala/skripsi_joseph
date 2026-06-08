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

## Default Product Topic

GitOps deployment system for InvenioRDM on Kubernetes.

Possible product framing:

- A reproducible, declarative deployment package for InvenioRDM.
- A GitOps workflow that separates desired state from manual cluster operations.
- A prototype that improves auditability, repeatability, rollback, and operational maintainability.

Possible evaluation metrics:

- Successful deployment rate across repeated trials.
- Time from commit to synchronized deployment.
- Rollback time after a deliberately introduced configuration error.
- Configuration drift detection and reconciliation behavior.
- Number of manual steps needed compared with a manual deployment baseline.
- Resource usage of the deployed InvenioRDM components.

Possible diagrams:

- Research methodology flowchart.
- GitOps workflow diagram.
- Kubernetes component architecture.
- Deployment pipeline sequence diagram.
- Configuration repository structure.
- Optional ERD or data flow if the product changes data models.

## Exploration Notes Folder

Use `notes/exploration/` for outputs that should survive beyond the chat. Good candidates:

- topic alternatives and chosen direction,
- internet source notes with URLs/DOIs and citation purpose,
- comparison of Argo CD vs Flux or Helm vs Kustomize,
- evaluation metrics and test scenario plans,
- diagram inventories,
- draft handoffs for the LaTeX writer.

