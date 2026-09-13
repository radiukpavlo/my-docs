> ## ⛔ SUPERSEDED — do not use as a source of truth
>
> Superseded on **13 September 2026** by design system **v0.2.0**
> (project `a2b22667-6793-404e-821b-d5219760fa3b`). Kept as a working record only.
>
> The `tokens/` directory here is **actively hazardous** — see the banner inside
> each file. `assets/` was already ingested into the live system. `ASSET-MANIFEST.md`
> and `DECK-ARCHETYPES.md` remain accurate.

# `_derived/` — generated design-system input

Everything here was produced from the files already in `U_CAN_Design/`, by
parsing the source binaries rather than re-keying values by eye. It is staged
so it can be copied into the Claude Design system project without further
editing.

| path | task | what it is |
|---|---|---|
| `assets/` | H1 H2 H4 H5 | 60 files, kebab-cased, ready to become the system's `assets/` tree |
| `tokens/` | A3 B1 B2 B4 C1–C6 | seven CSS token files |
| `FONT-INVENTORY.md` | A1 | every face in both archives, with licence and coverage |
| `CONTRAST-AUDIT.md` | B1 B3 B5 | measured palette + full WCAG matrix |
| `DECK-ARCHETYPES.md` | F1–F4 | what 126 real slides actually contain |
| `DECK-ARCHETYPES-per-slide.md` | F2 | the per-slide working behind it |
| `ASSET-MANIFEST.md` / `.csv` | H10 H11 | provenance, duplicates, what was left behind |
| `logo-render-proof.png` | H5 H6 | the extracted SVG rendered in Chrome at four sizes |

## Copy order

1. `assets/**` → `assets/`
2. `tokens/*.css` → `tokens/`, then import each from `styles.css`
3. run `check_design_system` and fix what it reports

## How the numbers were obtained

- **Fonts** — fontTools over the `name`, `OS/2`, `fvar` and `cmap` tables.
- **Palette** — PyMuPDF over `U_CAN_V3_final.ai`, which is a PDF-1.5 file;
  the fills are the artwork's own, counted by frequency.
- **Yellow** — regex over every XML part of `Template_Presentation.potx`.
- **Contrast** — WCAG 2.1 relative luminance; state colours solved in OKLCH
  with hue held exactly and chroma reduced to fit sRGB.
- **Slides** — PyMuPDF per page: words, span sizes, bullet glyphs, ruled-line
  geometry, table structure, and image area with the footer band excluded.
