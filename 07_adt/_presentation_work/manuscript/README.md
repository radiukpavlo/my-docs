# Cardiac MRI audit CEUR LaTeX bundle -- v0.6

This bundle contains the revised CEUR LaTeX manuscript *Auditing Deep Learning for Cardiac MRI Through Semantic Transitions and Conflict-Aware Production Rules*.

## Main files

- `main.tex` -- submission-ready CEUR manuscript source.
- `references.bib` -- revised BibTeX database, including the four 2022--2024 independent references added in the latest pass.
- `main.bbl` -- generated bibliography for reproducible builds.
- `main.pdf` -- compiled 15-page preview.
- `my_revision.md` and `revision_report.md` -- detailed revision log.
- `figures/` -- manuscript figures.
- `ceurart.cls`, license files, and CEUR logo files -- template assets.

## Compilation

Run:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

If a TeX installation exposes only `bibtex8`, it can be used as a fallback.
