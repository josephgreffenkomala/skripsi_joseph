---
name: skripsi-latex-writer
description: Write, revise, and debug LaTeX proposal/skripsi text in this UGM thesis repo, including Indonesian academic drafting, citation/BibTeX hygiene, figure/table/listing insertion, pdflatex/bibtex error fixes, and focused git commits after meaningful writing or draft changes unless the user asks to leave changes uncommitted.
---

# Skripsi LaTeX Writer

Use this skill when the user wants actual writing or LaTeX editing in this repository. It covers drafting, revising, fixing compile errors, cleaning citations, adding figures/tables/listings, and committing completed text changes.

## Core References

Read these before editing:

- `AGENTS.md` for official proposal/skripsi structure and priority rules.
- `README.md` and `Makefile` for build commands.
- `template/proposal/main.tex` and `template/proposal/chapters/*.tex` for proposal work.
- `template/skripsi/main.tex` and `template/skripsi/chapters/*.tex` for skripsi work.
- `references/latex-writing-checklist.md` in this skill for repo-specific writing and compile checks.

Use `examples/pedoman_ta.pdf` as the highest authority when a formatting or structure issue is uncertain.

## Editing Workflow

1. Determine target:
   - proposal or skripsi,
   - exact chapter/section,
   - whether this is drafting, revision, compile fixing, or citation work.
2. Inspect the current `.tex` and `.bib` files before editing.
3. Preserve the repo's existing LaTeX style:
   - `\chapter`, `\section`, `\subsection`,
   - `\citep{...}` and `\citet{...}`,
   - `figure`, `table`, and `lstlisting` examples from `AGENTS.md`,
   - Indonesian prose with English only for abstract, title, and technical terms.
4. Replace placeholder text only in the requested scope unless the user asks for broader cleanup.
5. Keep claims defensible. Use TODO markers for missing data, measurements, names, or citations instead of inventing.
6. Compile the target LaTeX document to PDF, or run the smallest useful verification if a full build is not feasible.
7. For meaningful writing or draft changes, create a focused git commit after verification unless the user explicitly asks to leave changes uncommitted. For tiny exploratory edits or failed compile-debug attempts, report the state and ask before committing.

## Proposal vs Skripsi Guardrails

Proposal:

- Uses `\documentclass[proposal,indonesia]{ugmskripsi}`.
- Bab 1 uses `Rumusan Masalah`, not `Perumusan Produk`.
- Has Bab 1-4 only.
- Focus on plan, method, design, schedule, and expected evaluation.
- Do not add declaration, motto, acknowledgments, preface, lists of tables/figures, symbols, or appendices.

Skripsi:

- Uses `\documentclass[skripsi,indonesia]{ugmskripsi}`.
- Bab 1 uses `Perumusan Produk` and `Batasan Produk`.
- Has Bab 1-6 plus appendices.
- May include implementation details, results, evaluation, conclusion, and suggestions.

## Writing Style

Write in formal Indonesian academic prose:

- Prefer clear topic sentences and paragraphs that build a chain of reasoning.
- Define English technical terms at first mention, for example: GitOps, yaitu pendekatan operasional berbasis repositori Git sebagai sumber kebenaran deklaratif.
- Use active, precise wording when possible.
- Avoid unverified absolute claims such as "paling baik", "selalu", or "terbukti" unless supported by data or citation.
- Keep proposal wording future-oriented: "akan dikembangkan", "dirancang", "direncanakan".
- Keep skripsi result wording evidence-oriented: "hasil pengujian menunjukkan" only when results exist.

## Citation and Bibliography Rules

- Before adding `\citep{key}` or `\citet{key}`, check the relevant `references.bib`.
- If a needed source is missing, ask whether to add a BibTeX entry or add a clear `% TODO: tambahkan sitasi ...` marker.
- Prefer source-specific citation keys such as `argocdDocs2026`, `kubernetesDocs2026`, or `smith2024gitops` over placeholder keys.
- Do not leave broken citations after editing.

## Compile to PDF

Use the README and Makefile workflow as the default way to produce PDFs.

From the repository root:

```bash
make proposal
make skripsi
```

Expected outputs:

- `template/proposal/main.pdf` for proposal builds.
- `template/skripsi/main.pdf` for skripsi builds.

If the user only changed one target, compile only that target. Use `make all` when edits affect shared files or both documents.

If local TeX Live is unavailable, use Docker:

```bash
make proposal-docker
make skripsi-docker
make all-docker
```

Use `make clean` when the PDF does not update, auxiliary files look stale, or citation/list outputs appear inconsistent.

## Compile and Fix Loop

Use local build commands first:

```bash
make proposal
make skripsi
```

For targeted debugging:

```bash
cd template/proposal && pdflatex -interaction=nonstopmode main.tex
cd template/skripsi && pdflatex -interaction=nonstopmode main.tex
```

If local LaTeX is unavailable and Docker is available, use:

```bash
make proposal-docker
make skripsi-docker
```

When a build fails:

1. Read the first real LaTeX error in the `.log`, not only the final fatal message.
2. Fix the smallest relevant source file.
3. Re-run the target build.
4. Repeat until the requested target compiles or the blocker is external.

Common checks:

- unmatched braces,
- unescaped `%`, `_`, `&`, `#`,
- missing `\end{...}`,
- missing image file,
- broken citation key,
- table too wide,
- `lstlisting` language mismatch,
- accidental Unicode punctuation if the file style is ASCII.

## Git Commit Behavior

When the user asks to write draft text or revise thesis/proposal prose:

1. Run `git status --short` before editing and after editing.
2. Do not stage or commit unrelated user changes.
3. Verify the target document if feasible.
4. Review the diff for only the files touched.
5. Commit with a focused Indonesian or conventional message, for example:
   - `docs(proposal): draft bab 1 latar belakang`
   - `docs(skripsi): revise bab 4 architecture design`
   - `fix(latex): resolve proposal bibliography build`

If the user explicitly says not to commit, mention that the changes are ready and leave them uncommitted.

## Output Summary

After writing or fixing, report:

- files changed,
- sections drafted or errors fixed,
- PDF compile command and result, including output path when successful,
- commit hash if a commit was made,
- any TODOs needing user data or source confirmation.
