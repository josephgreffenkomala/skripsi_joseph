---
name: skripsi-topic-explorer
description: Explore and sharpen topic ideas, research questions, product scope, internet/source needs, datasets, evaluation plans, diagrams, saved research notes, and writing material for this UGM Inovasi Produk proposal/skripsi repo. Use when the user asks to brainstorm, research online, compare, validate, outline, or gather anything needed before writing proposal or skripsi content about the GitOps deployment system for InvenioRDM on Kubernetes.
---

# Skripsi Topic Explorer

Use this skill to turn vague thesis/proposal ideas into usable writing material for this repository. The default subject is a Skripsi Inovasi Produk: a GitOps deployment system for InvenioRDM on Kubernetes.

## Core References

Start by reading these local files when relevant:

- `AGENTS.md` for the official repo rules, proposal-vs-skripsi structure, and priority order.
- `README.md` for repository layout and build workflow.
- `template/proposal/main.tex` and `template/proposal/chapters/*.tex` when the work targets the proposal.
- `template/skripsi/main.tex` and `template/skripsi/chapters/*.tex` when the work targets the skripsi.
- `references/repo-thesis-map.md` in this skill for a compact topic and writing map.
- `notes/exploration/` for saved findings, source notes, topic comparisons, and writing handoffs produced during exploration.

Use `examples/pedoman_ta.pdf` as the highest authority when a detail is uncertain. If examples and the guide differ, follow `pedoman_ta.pdf`.

## First Move

Identify which output the user needs:

- Topic exploration: several possible angles, novelty claims, feasibility notes.
- Source/data discovery: papers, docs, standards, datasets, operational data, benchmark data, or product references.
- Chapter planning: section-by-section material for proposal or skripsi.
- Research design: methodology, architecture, test scenarios, metrics, Gantt plan.
- Writing handoff: a concise brief ready for the LaTeX writing skill.

Internet exploration is part of this skill. If the user asks for current literature, software behavior, product versions, standards, security practices, examples, deployment practices, or Kubernetes/InvenioRDM/GitOps details that may have changed, browse or otherwise verify from primary sources when possible. Prefer official documentation, academic papers, standards, and project repositories over blogs.

## Exploration Workflow

1. Read repo context before suggesting structure.
2. State whether the target is `proposal/`, `skripsi/`, or both.
3. Frame the product problem in UGM Inovasi Produk terms:
   - real problem,
   - proposed product,
   - innovative idea,
   - scientific/technical basis,
   - prototype design,
   - implementation,
   - evaluation.
4. Separate claims into:
   - confirmed from repo/local sources,
   - confirmed from external sources,
   - reasonable inference,
   - needs user confirmation.
5. Convert exploration into concrete assets:
   - candidate titles in Indonesian and English,
   - problem statements or product formulation,
   - scope boundaries,
   - related-work buckets,
   - methodology steps,
   - diagram inventory,
   - evaluation metrics,
   - BibTeX/source TODOs.
6. Save durable exploration findings in `notes/exploration/` when the work produces reusable research notes, source lists, topic comparisons, or a handoff for writing.

## Internet Research Workflow

Use internet research proactively when the task benefits from current or citable information. This matters for InvenioRDM, Kubernetes, GitOps tools, Helm/Kustomize, security practices, and recent academic literature because versions and recommended practices change.

When researching online:

1. Start with source categories:
   - official docs for technologies,
   - peer-reviewed papers or proceedings for academic claims,
   - official repositories or release notes for implementation details,
   - standards or institutional documents for research data management context.
2. Capture bibliographic details as you go:
   - title,
   - author or organization,
   - year or access date,
   - URL/DOI,
   - why the source matters for the proposal/skripsi.
3. Separate source notes from thesis claims. A source may justify background, design choice, evaluation metric, limitation, or related work; label that role clearly.
4. Prefer concise paraphrase. Do not paste long copyrighted passages.
5. End with citation TODOs or candidate BibTeX keys if the LaTeX writer will draft from the findings.

## Saving Findings

Use `notes/exploration/` for reusable exploration outputs. Create the folder if it does not exist.

Recommended filenames:

- `notes/exploration/topic-options.md`
- `notes/exploration/source-notes.md`
- `notes/exploration/evaluation-plan.md`
- `notes/exploration/diagram-plan.md`
- `notes/exploration/draft-handoff-YYYY-MM-DD.md`

Use this shape for saved notes:

```markdown
# [Exploration Title]

Date: YYYY-MM-DD
Target: proposal|skripsi|both

## Summary

## Findings

## Sources

## Writing Handoff

## Open Questions
```

## Topic Heuristics

Good ideas for this repo usually connect at least three of these:

- InvenioRDM deployment complexity.
- Kubernetes-native operation.
- GitOps workflow, reproducibility, auditability, rollback, and declarative configuration.
- Institutional repository needs: reliability, preservation, metadata, access, and maintainability.
- Product innovation: a usable deployment system, not only an analysis.
- Evaluation: deployment success rate, recovery time, configuration drift, reproducibility, operational effort, and maintainability.

Avoid framing the work as a generic DevOps tutorial. Keep tying it back to a product/prototype and a real user or institution problem.

## Proposal Output Shape

For proposal exploration, produce material that can become:

- Bab 1: Latar Belakang, Rumusan Masalah, Batasan Masalah, Tujuan, Manfaat.
- Bab 2: Penelitian Terkait and state of the art.
- Bab 3: Metode dan Rancangan Penelitian, architecture, methodology flow, testing plan.
- Bab 4: Gantt chart by month.

Proposal content is planning-oriented. Do not invent results.

## Skripsi Output Shape

For skripsi exploration, produce material that can become:

- Bab 1: Latar Belakang, Perumusan Produk, Batasan Produk, Tujuan, Manfaat.
- Bab 2: Identifikasi Masalah dan Ide Inovatif.
- Bab 3: Kajian Ilmiah.
- Bab 4: Perancangan Prototipe/Produk.
- Bab 5: Proses Pembuatan Produk.
- Bab 6: Pengujian dan Evaluasi Produk, including Kesimpulan dan Saran.

Skripsi content may discuss implementation and results, but label unknown values as TODO until the user supplies data.

## Source and Data Checklist

When asked to find sources or data, look for:

- InvenioRDM official documentation and deployment docs.
- Kubernetes official documentation.
- Argo CD or Flux official documentation, depending on the selected GitOps tool.
- Helm, Kustomize, container registry, secrets management, and CI/CD docs when used.
- Academic literature on GitOps, continuous deployment, reproducible infrastructure, repository systems, and research data management.
- Evaluation data the user can collect locally: install duration, failed/successful deployments, rollback time, drift detection, resource usage, and operator steps.

For each source, capture the citation purpose: background, related work, technical basis, design decision, or evaluation method.

## Asking for Confirmation

Ask before making strong assumptions about:

- GitOps tool choice: Argo CD, Flux, or another tool.
- Deployment packaging: Helm chart, Kustomize overlays, plain manifests, or a hybrid.
- InvenioRDM environment: local cluster, cloud Kubernetes, campus infrastructure, or lab server.
- Evaluation metrics and target users.
- Whether to browse for current sources when the user has not already requested online research.
- Whether to save findings to `notes/exploration/` when exploration is quick or throwaway.
- Whether to pass a completed brief to the LaTeX writing skill for direct drafting.

Keep questions short. If the user wants momentum, proceed with clearly marked assumptions.

## Deliverable Formats

For brainstorming, use this compact format:

```markdown
**Arah Utama**
[1-2 paragraphs]

**Pilihan Topik**
1. [Title] - [novelty, feasibility, risks]

**Bahan Proposal/Skripsi**
- Bab ...

**Sumber/Data yang Dibutuhkan**
- ...

**Asumsi**
- ...
```

For a writing handoff, end with:

```markdown
**Draft Handoff**
Target: proposal|skripsi
Files: ...
Sections: ...
Key claims:
- ...
Citations needed:
- ...
Figures/tables needed:
- ...
User confirmations:
- ...
```
