> ## ⛔ SUPERSEDED — historical record, 13 September 2026
>
> Written before this machine had design-system access, and superseded the same
> day by **v0.2.0** (project `a2b22667-6793-404e-821b-d5219760fa3b`) and by
> [`DESIGN-TASKS-REMAINING.md`](DESIGN-TASKS-REMAINING.md).
>
> **What it got right:** the yellow (`#FFCC00`), the SVG extraction from the
> `.ai` files, the Metropolis/Bahnschrift licence-vs-Cyrillic bind, and the
> deck-corpus analysis — that last was independently re-derived and matched exactly.
>
> **What it got wrong — one error, corrected below:** its logo colour inventory
> reported *fills* that were in fact a mix of fills and strokes, so both green
> counts were doubled and a stroke colour was reported as a fill.
>
> **Corrected logo inventory** (re-derived 13 Sep 2026 from
> `Logos/U_CAN_V3_final.ai`, separating fill from stroke, and cross-checked by a
> pixel census of a 6× render):
>
> | colour | fills | strokes | share of opaque pixels |
> |---|---|---|---|
> | `#FFFFFF` | 68 | — | 1.7 % |
> | `#FFCC00` | 50 | — | 12.5 % |
> | `#75B23C` | 17 | 17 | 2.2 % |
> | `#3B9139` | 17 | 17 | 2.5 % |
> | `#003399` | 6 | — | 3.9 % |
> | `#0057B7` | 4 | — | **59.1 %** |
> | `#00305E` | **0** | **44** | 2.8 % |
>
> Two things follow, and they cut in opposite directions. The earlier count of
> "44 navy fills" was wrong — navy carries **no** fill in this artwork. But the
> correction recorded in the live `tokens/colors.css`, that "there is no #00305E
> anywhere in the artwork", is an **over**-correction: navy is the stroke colour
> on 44 paths and accounts for ~47 000 rendered pixels. It is in the artwork; it
> is an outline colour, not a fill colour.
>
> Its nine-blocker list is also out of date — six are resolved. Use
> `DESIGN-TASKS-REMAINING.md`.

# U_CAN Design System — findings against `DESIGN-TASKS.md`

**Date:** 13 September 2026
**Worked from:** `my-docs/03_u_can/` only.
**Output:** [`U_CAN_Design/_derived/`](U_CAN_Design/_derived/)

---

## 1. What could and could not be done, and why

`DESIGN-TASKS.md` is written for an agent working *inside* the Claude Design
system project — the one that owns `tokens/`, `components/`, `templates/`,
`ui_kits/`, `slides/`, `guidelines/`, `readme.md` and `SKILL.md`, with
`my-docs/` attached to it as a folder. **This session is on the other side of
that boundary: it has `my-docs/`, not the design system.**

Concretely:

- No copy of the design system exists anywhere on this machine — no `tokens/`,
  no `components/core/`, no `*.dc.html`, no `_ds_bundle.js`.
- `DesignSync` — the only route to that project — reports it needs
  design-system authorization, and `/design-login` cannot run in a
  non-interactive session.
- So `check_design_system`, `list_files` and `dc_write` are all unavailable.
  Nearly every *Done when* line in the task list is defined against one of
  them.

**To unblock the rest:** run `/design-login` once in an interactive `claude`
terminal on this machine, then re-run this task. Headless and SDK runs reuse
that authorization afterwards.

What follows is everything that could be completed **without** it — which
turned out to be more than the audit assumed, because three tasks it marked as
needing the user are answerable from the files already in the repo.

---

## 2. Three blockers closed by evidence

### 🟢 B1 — the yellow: `#FFCC00`, settled

`Logos/U_CAN_V3_final.ai` is a PDF-1.5 file and parses cleanly. Its 180 vector
drawings use **`#FFCC00` for all 50 star fills; `#FFC000` appears nowhere in
the logo.** Across `Template_Presentation.potx`, `#FFCC00` outnumbers `#FFC000`
8 to 2.

The audit's premise also needs a correction: it said slide 5 uses `#FFCC00` and
slide 4 uses `#FFC000`. In fact **both values appear on both slides** — a
within-slide picker slip, not a second brand tone. Nothing is lost by deleting
one. `#FFCC00` is additionally the exact EU emblem yellow.

→ Actioned in [`tokens/colors.css`](U_CAN_Design/_derived/tokens/colors.css).
`--ucan-yellow-legacy` is retained but marked deprecated. **This no longer
needs your decision.**

### 🟢 H5 — the SVG logo master: extracted, not requested

The audit says the `.ai` files "cannot be parsed here — ask for an SVG export".
They can. Both are **PDF-1.5** — Illustrator's PDF-compatible save — with no
raster content at all. Converted to true vector SVG (281 paths) and verified by
rendering in Chrome:

- `assets/logos/u-can/u-can-logo-colour.svg` — 91 KB
- `assets/logos/u-can/u-can-logo-bw.svg` — 88 KB

Proof render: [`logo-render-proof.png`](U_CAN_Design/_derived/logo-render-proof.png).

One process note worth keeping: `pdftocairo -svg` produced a 660 KB file that
**Chrome refuses to load at all**, while PyMuPDF's SVG export renders perfectly.
PyMuPDF's *own* rasteriser, confusingly, renders the good file badly. Only the
browser check separated them — so verify SVG conversions in a browser, not in
the converter's own preview.

→ `thumbnail.html` can now use the real mark instead of a type-set wordmark
(task J2).

### 🟡 G1 — chart conventions: the question changes

**Across 126 real slides there is not one native chart object.** Every chart in
the reference decks arrived as a pasted screenshot. So G1 is not "what are your
chart conventions" — there are none to document. It is "here is a proposal,
please approve it." That is a much cheaper question to answer.

---

## 3. Corrections — including to `DESIGN-TASKS.md` itself

Task A0 asks that no document state a count or path that `list_files`
contradicts. I cannot run `list_files`, but I can correct what is checkable
from here. **Two of the audit's three "status corrections" hold; a claim of its
own is wrong, and two more are imprecise.**

| claim | source | actual |
|---|---|---|
| Fonts unavailable | earlier notes | correct to flag — archives are present. But **neither is usable as-is**: see below |
| `avenir-next-similar-fonts.zip` is "by definition not Avenir Next" | A2 | **correct** — it is Metropolis, SIL OFL 1.1 |
| `.ai` files "cannot be parsed here" | H5 | **wrong** — both are PDF-1.5 and convert to clean SVG |
| slide 5 uses `#FFCC00`, slide 4 uses `#FFC000` | B1 | **imprecise** — both values are on both slides |
| LHD Förderlogo has "9 variants" | H2 | **8** variant sets (plus 3 Stadtverwaltung) |
| source `.potx` falls back to `Noto Sans SC` | A4 | **correct, and worse than stated** — 358 references, the single largest font reference in the file |

### The font situation, stated accurately

| archive | what it really is | webfont licence | Cyrillic |
|---|---|---|---|
| `avenir-next-similar-fonts.zip` | **Metropolis** (Chris Simpson, 2015) | ✅ SIL OFL 1.1 | ❌ **zero glyphs** |
| `Bahnschrift-Font-Family.zip` | **Bahnschrift**, variable (`wght` 300–700, `wdth` 75–100) — **15 byte-identical copies** of one 315 KB file | ❌ "Microsoft supplied font" | ✅ complete (256 cp) |

The licensable face has no Cyrillic; the Cyrillic face is not licensable. That
is why A2 cannot be closed by picking one of them, and it is the single most
important thing the archives tell us.

Also worth recording: the `.potx` theme font was never Avenir. `majorFont` and
`minorFont` are **Calibri** in themes 1–8 (Aptos in theme 9). Avenir Next
appears 23 times as a direct run override, and Bahnschrift only on the title
slide. So "Avenir" has always been an intention applied by hand, not a
configured default.

---

## 4. Delivered

All paths relative to [`U_CAN_Design/_derived/`](U_CAN_Design/_derived/).

| task | status | deliverable |
|---|---|---|
| **A1** | ✅ done | `FONT-INVENTORY.md` — every face, licence, coverage, plus the `usWeightClass` trap |
| **A3** | ✅ built | 8 × `.woff2` (124 KB total) + `tokens/fonts.css` with `font-display:swap` and `unicode-range` |
| **A4** | ◐ part | `--font-sans-cyr` added; `Noto Sans SC` never inherited; `:lang(uk)` rule. Specimen card needs the system |
| **B1** | ✅ done | resolved above; `tokens/colors.css` |
| **B2** | ✅ done | four states × fg/bg/border, OKLCH-derived, each ≥4.5:1 on its own tint |
| **B3** | ✅ done | `CONTRAST-AUDIT.md` — full 12 × 12 matrix, forbidden pairs, named alternatives |
| **B4** | ✅ done | `tokens/base.css` — default / visited / hover / focus-visible, plus on-dark inversion |
| **B5** | ✅ done | position taken: light-only by design, with an `.on-dark` navy-band convention |
| **C1–C6** | ✅ done | `layout.css`, `elevation.css`, `table.css`, `print.css` — breakpoints, containers, z-index, scrim, table, print |
| **F1** | ✅ decided | `templates/deck/` becomes the source; `slides/` become generated specimens — with the reason |
| **F2** | ✅ done | `DECK-ARCHETYPES.md` + per-slide working over 126 slides |
| **F3** | ✅ ranked | ten archetypes ordered by measured frequency |
| **F4** | ✅ answered | no deck carries notes; speeches are separate documents |
| **H1 H2 H4** | ✅ staged | 58 files copied and kebab-cased, incl. the UA and vertical EU sets and all 11 LHD SVGs |
| **H5** | ✅ done | resolved above |
| **H10** | ✅ done | `ASSET-MANIFEST.md` + `.csv` — provenance, 2 duplicate groups, what was left behind and why |
| **H11** | ✅ recommended | keep the four Office binaries as provenance-only |

Every contrast figure quoted in the token comments was machine-verified. One
was wrong on first writing — the visited-link colour is 8.48:1 on white, not
7.21:1 — and is corrected in the file.

---

## 5. Not attempted, and why

**Sections D (components), E (templates), I (UI kits), J (system docs), K
(verification) were not attempted.** This is a deliberate stop, not an
omission.

Those tasks require writing files into an API I cannot see. D2–D6 alone is
~30 components that must match a three-file pattern (`.jsx` + `.d.ts` +
`.prompt.md`) whose conventions live in the 11 existing components — which I
cannot read. E1–E8 are Design Components that must be written with `dc_write`
under an inline-styles-only contract, against a `.dc.html` structure I have no
example of. Writing ~40 files by guessing at an unseen API would produce
something that looks complete, cannot be verified, and would most likely have
to be thrown away.

Tokens and assets were safe to write because CSS custom properties and image
files have no project-specific contract to guess at. Components and templates
do.

**Also blocked, for the same reason:** A5 (needs to know which styles the two
templates use), G2/G3 (follow from G1), I1–I6, J1–J10, K1–K6.

---

## 6. What still needs you

The audit listed nine. **B1 is closed, H5 is closed, G1 is reframed** — leaving
these, plus one new one.

**0. 🔑 New — design-system access.** Run `/design-login` once in an
interactive `claude` terminal. Without it nothing in Sections D, E, I, J or K
can proceed, and none of the work in `_derived/` can be uploaded.

**1. Font licence path (A2).** Now a sharper question, because the archives
cannot answer it:

- **(a)** you hold an Avenir Next webfont licence → supply `.woff2` for 400 + 700;
- **(b)** ⭐ *recommended* → adopt **one** OFL family covering Latin **and**
  Cyrillic, so the EN and UA editions of a document share letterforms.
  Candidates: Manrope, Montserrat, Nunito Sans, Mulish. Metropolis is
  licence-clean and already in hand but has **no Cyrillic**, so it cannot be
  the whole answer for a project that publishes in Ukrainian;
- **(c)** accept the platform fallback and record it as a known deviation.

Either way: **Bahnschrift stays for the Office templates** — it is on every
Windows install, and using an installed font is permitted; only redistribution
is not.

**2. Cyrillic face (A4).** Folds into (1) if you take path (b). If you take (a)
or (c), it needs a separate answer — the current `--font-sans-cyr` falls back
to the platform UI face, which is correct but unbranded.

**3. LHD: funder or partner (H3)?** Both sets are staged
(`logos/lhd/foerderlogo-*` = funder, `logos/lhd/stadtverwaltung-*` = partner).
Only the rule is missing.

**4. Reversed and stacked lockups (H6).** Now evidenced rather than asserted:
row 2 of `logo-render-proof.png` shows the colour mark on `#00305E` — the navy
buildings and the blue "CAN" all but disappear. The deck's navy title slide
genuinely has nowhere to put this logo. With the SVG master in hand a reversed
version is quick to produce, but *which* elements knock out to white is a brand
decision, not a mechanical one.

**5. Icon set (H9).** The source materials contain zero icons. Name a set, or
say the word and Lucide becomes the sanctioned choice.

**6. Map, objectives artwork, photography (H7, H8).** `map_eng_2.png` and
`1_Монтажная область 1.png` are not in `U_CAN_Design/`. Nor are project photos —
and the reference decks show U_CAN uses photography heavily, so the gap is real.

**7. Co-branding rules (J8).** Which logos on which surfaces; TU Dresden + U_CAN
footer band or plain U_CAN; whether the Ukrainian-language emblem is required.
Note the UA emblem set has no monochrome variant — if you need one it must come
from the EU brand portal.

**8. Website design source (I1).** Screenshots or Figma, or accept the kit as a
declared interpretation.

---

## 7. One finding worth acting on beyond the task list

The reference decks show U_CAN hand-drawing layout in PowerPoint and pasting it
in as pictures — stat blocks, milestone timelines, captioned photo strips,
callout boxes. **That is why the decks are heavy and why none of that content is
selectable, searchable, translatable or accessible.**

Every one of those shapes is already on the Section D build list
(`Stat`/`KPI`, `Timeline`, `Figure`+`Caption`, `Alert`/`Panel`). The evidence
says they are not speculative additions — they are the highest-value components
in the whole list, because each one replaces a recurring manual paste. Building
those five before the other twenty-five would return the most.

Details: [`DECK-ARCHETYPES.md`](U_CAN_Design/_derived/DECK-ARCHETYPES.md).
