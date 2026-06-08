# LaTeX Writing Checklist

## File Targets

Proposal:

- `template/proposal/main.tex`
- `template/proposal/chapters/bab1-pendahuluan.tex`
- `template/proposal/chapters/bab2-penelitian-terkait.tex`
- `template/proposal/chapters/bab3-metodologi.tex`
- `template/proposal/chapters/bab4-jadwal-penelitian.tex`
- `template/proposal/references.bib`

Skripsi:

- `template/skripsi/main.tex`
- `template/skripsi/chapters/bab1-pendahuluan.tex`
- `template/skripsi/chapters/bab2-identifikasi-masalah.tex`
- `template/skripsi/chapters/bab3-kajian-ilmiah.tex`
- `template/skripsi/chapters/bab4-perancangan.tex`
- `template/skripsi/chapters/bab5-pembuatan.tex`
- `template/skripsi/chapters/bab6-pengujian.tex`
- `template/skripsi/lampiran/lampiran-a.tex`
- `template/skripsi/references.bib`

## Proposal Chapter Intent

- Bab 1: establish context, urgency, problem questions, boundaries, objectives, benefits.
- Bab 2: group related work and show the research/product gap.
- Bab 3: explain method, architecture, workflow, environment, and planned testing.
- Bab 4: schedule work by month with a Gantt-style table.

## Skripsi Chapter Intent

- Bab 1: introduce product formulation and boundaries.
- Bab 2: identify real problems and explain the innovative idea.
- Bab 3: build the scientific and technical basis.
- Bab 4: describe the prototype/product design.
- Bab 5: document implementation and integration.
- Bab 6: present testing, evaluation, conclusion, and suggestions.

## LaTeX Patterns

Citations:

```latex
\citep{key}
\citet{key}
```

Figures:

```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/nama-file}
  \caption{Deskripsi gambar}
  \label{fig:label}
\end{figure}
```

Tables:

```latex
\begin{table}[H]
  \centering
  \caption{Judul tabel}
  \begin{tabular}{|l|c|r|}
    \hline
    Kolom 1 & Kolom 2 & Kolom 3 \\
    \hline
    Data & Data & Data \\
    \hline
  \end{tabular}
  \label{tab:label}
\end{table}
```

Listings:

```latex
\begin{lstlisting}[language=yaml, caption={Judul}]
# kode di sini
\end{lstlisting}
```

## Verification Commands

Local:

```bash
make proposal
make skripsi
make all
```

Docker:

```bash
make proposal-docker
make skripsi-docker
make all-docker
```

Clean artifacts:

```bash
make clean
```

Expected PDFs:

- `template/proposal/main.pdf`
- `template/skripsi/main.pdf`

Compile only the changed target when possible. Compile both when editing shared class/configuration files, shared figures, or instructions that affect both proposal and skripsi.

## Draft Quality Checks

- Does every paragraph serve the section's purpose?
- Are technical terms introduced in Indonesian?
- Are all cited keys present in `references.bib`?
- Are all figures/tables/listings captioned and labeled?
- Are proposal statements future-oriented?
- Are skripsi result statements backed by actual results?
- Are TODOs specific enough for the user to fill later?
