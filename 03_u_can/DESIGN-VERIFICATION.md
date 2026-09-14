> ## SUPERSEDED — historical record, 14 September 2026
>
> Superseded by design system **v0.3.0** and by
> [`DESIGN-STATUS.md`](DESIGN-STATUS.md), which is the only current status
> document. Much of what follows is now closed; some of it was wrong.
>
> **Corrections this file got wrong**, recorded here so they are not re-made:
> Archivo Narrow, Barlow Condensed and Saira Condensed were recommended for the
> claim line on the basis that Archivo Narrow "has full Cyrillic" — **none of
> the three has any Cyrillic at all**. `--weight-medium: 600` was reported as
> synthesised — the shipped fonts are **variable**, so it never was.
>
---

# U_CAN Design System — verification run

**Date:** 13 September 2026
**Against:** v0.2.0 · project `a2b22667-6793-404e-821b-d5219760fa3b`
**Covers:** `DESIGN-TASKS-REMAINING.md` Sections V and R, plus A2/A3 and J3/J4

Design-system access is now working, so the project is readable and writable from
here. Everything below was **measured**, not inferred.

---

## 1. The gating finding — V2 fails

**`_ds_manifest.json` was never recompiled after the v0.2.0 pass.** It still
describes the pre-0.2.0 system, and it points at files that no longer exist.

| what the manifest says | what `list_files` says |
|---|---|
| 21 components | **42** components exist |
| `components/core/{Card,Panel,MetaTable,ObjectiveItem,BandHeading}.jsx` | **all five deleted** — moved to `content/` and `layout/` |
| `WebsiteHeader`, `WebsiteFooter`, `SectionHead` from `ui_kits/website/WebsiteChrome.jsx` | **that file no longer exists** — promoted to `components/navigation/` |
| 0 of the 42 new components registered | `TextField`, `Alert`, `Stat`, `Timeline`, `Grid`, … all present on disk |
| 2 templates (deck, report) | **10** templates exist |
| card `guidelines/brand-no-icons.card.html` | **deleted** — replaced by `icons.card.html` |
| new cards absent (`colors-states`, `charts-conventions`, `type-cyrillic`, the six directory cards) | all present on disk |
| `brandFonts`: Avenir Next + Bahnschrift, status `no-face` | **Manrope is shipped and self-hosted** |
| `--text-muted` = `var(--ucan-grey)` · `--text-legal` = `var(--ucan-grey)` | live `tokens/colors.css` sets **both to `var(--ucan-slate)`** |
| `startingPoints: []` | unchanged — **task J1 is still open** |

So the Design System pane is currently rendering the **old** system, and the
card index, the component namespace and the token table are all describing a
state that no longer exists on disk.

**This cannot be fixed from here.** `_ds_manifest.json` and `_ds_bundle.js` are
compiled by the Design System app's own self-check; hand-writing either would be
guesswork and would be overwritten. **Open the project once in Claude Design so
the self-check re-runs**, then re-check V2 and V3.

Until that happens, every card and kit page should be assumed broken, exactly as
R5 predicted — the bundle still points at the five deleted `components/core/`
paths.

---

## 2. Confirmed from the file listing — no reads needed

These are objectively true right now.

| task | status | evidence |
|---|---|---|
| **R6** — `assets/imagery/` empty | ✅ **worse: it does not exist at all.** No `assets/imagery` entry in the project. Any `src` pointing there is a broken image today. |
| **R10** — duplicate LHD assets | ✅ confirmed. `assets/logos/partners/` holds 4 files (`lhd-duesseldorf-city-admin.{png,svg}`, `lhd-duesseldorf-funding-en.{png,svg}`) duplicating 2 of the 11 in `assets/logos/lhd/`. |
| **E1** — templates without `.thumbnail` | ✅ confirmed. Only `templates/deck/.thumbnail` and `templates/report/.thumbnail` exist. **8 of 10 templates will show no preview.** |
| **H7** — legacy root assets | ✅ confirmed, **11 files**: `ucan-logo{,-compact,-square,-transparent,-watermark}.png`, `ucan-v3-{final,black-white}.png`, `eu-funded-{horizontal,square}.png`, `eu-funded-en-horizontal-{pos,neg}.png`. |
| **I4** — `ui_kits/templates/` references | ✅ the directory does not exist. `ui_kits/` contains only `documents/` and `website/`. Remaining work is removing the textual references. |
| **J1** — starting points | ✅ confirmed `"startingPoints": []`. Never created. |

### Inventory claims that check out

The v0.2.0 summary is accurate on counts. Verified against `list_files`:

- **42 library components** — content 10, core 6, feedback 5, forms 7, layout 7, navigation 7. ✓
- **10 templates** ✓ · **12 token files** ✓ · six concern directories each with their own `*.card.html` ✓

### C3 — a false alarm

`_ds_manifest.json` lists only 9 `globalCssPaths`, omitting `charts.css`,
`layout.css`, `print.css` and `table.css`. That looks like four dead token files
— but `styles.css` **does** `@import` all twelve, and `styles.css` is itself in
the list. **No functional gap.** The short list is one more symptom of the stale
manifest, not a separate defect.

---

## 3. V10 — Cyrillic verified at glyph level. It passes.

The task list flagged this as unverifiable because "no tooling was available".
It is verifiable, and the answer is good.

`assets/fonts/manrope/manrope-400-cyrillic.woff2`, decompressed and read from its
`cmap` and `glyf` tables:

| codepoint | char | in cmap | glyph | outline |
|---|---|---|---|---|
| U+0404 | Є | yes | `uni0404` | 1 contour |
| U+0406 | І | yes | `uni0406` | composite |
| U+0407 | Ї | yes | `uni0407` | composite |
| U+0454 | є | yes | `uni0454` | 1 contour |
| U+0456 | і | yes | `uni0456` | composite |
| U+0457 | ї | yes | `uni0457` | 3 contours |
| U+0490 | Ґ | yes | `uni0490` | 1 contour |
| U+0491 | ґ | yes | `uni0491` | 1 contour |
| U+2116 | № | yes | `uni2116` | composite |

**All nine present with real outlines.** 98 Cyrillic codepoints, 165 glyphs.
Ukrainian renders in Manrope, not in a fallback face.

One note for whoever re-runs this: all nine live in Google's **`cyrillic`**
subset (`U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116`), **not** in
`cyrillic-ext`. Checking the `-ext` file first shows all nine missing and looks
like a failure; it is not.

---

## 4. A2 and A3 — both claims in the task list are wrong

**A2 says `--weight-medium: 600` is synthesised because "Manrope ships
400/500/700/800".** It does not ship static weights at all.

The shipped files are **variable fonts**:

```
fvar  axis wght: 200 → 200 → 800
named instances: ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold
gvar ✓  HVAR ✓  STAT ✓
```

600 (SemiBold) is a **real named instance on the axis**. Nothing is interpolated
or faux-bolded, and no token resolves to a weight the files cannot produce.
**A2 needs no fix.**

**A3 asks whether Manrope 800 is "dead weight — 64 KB across four subsets".**
It is not dead, and it costs nothing extra, because:

> `manrope-400-cyrillic.woff2` and `manrope-700-cyrillic.woff2` are
> **byte-identical**, and both are byte-identical to what Google Fonts serves
> for weights 200, 400 **and** 700 — md5 `e58febde317b69ce`, 14 500 bytes, all
> three. One file carries the whole axis.

So the 16 shipped files are **4 distinct files** (latin, latin-ext, cyrillic,
cyrillic-ext), each stored 4 times.

**The real A3 finding — a 75 % saving:** replace the sixteen `@font-face` rules
with four, one per subset, each declaring the range rather than a point weight:

```css
@font-face{
  font-family:"Manrope";
  font-style:normal;
  font-weight:200 800;          /* the axis, not a single instance */
  font-display:swap;
  src:url("../assets/fonts/manrope/manrope-cyrillic.woff2") format("woff2");
  unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;
}
```

As shipped, a page using 400 and 700 downloads the same 14.5 KB file twice under
two names. Correct, but wasteful.

---

## 5. R1 — narrower than feared

`components/forms/Radio.jsx` is four lines:

```js
export { Radio } from "./Checkbox.jsx";
```

A **re-export**, not a second implementation — so the two can never drift, which
was the stated worry. The residual risk is only that the name `Radio` is
reachable from two module paths, so a compiler that harvests named exports from
every `.jsx` would register it twice. R1's second option (move the
implementation into `Radio.jsx`, leave `Checkbox.jsx` exporting only `Checkbox`)
removes that cleanly. Low severity; worth doing while the file is open.

---

## 6. The palette question in "A note on trust"

Re-derived from `Logos/U_CAN_V3_final.ai`, separating fill from stroke and
cross-checking against a pixel census of a 6× render:

| colour | fills | strokes | share of opaque pixels |
|---|---|---|---|
| `#FFFFFF` | 68 | — | 1.7 % |
| `#FFCC00` | 50 | — | 12.5 % |
| `#75B23C` | 17 | 17 | 2.2 % |
| `#3B9139` | 17 | 17 | 2.5 % |
| `#003399` | 6 | — | 3.9 % |
| `#0057B7` | 4 | — | **59.1 %** |
| `#00305E` | **0** | **44** | 2.8 % |

**Both earlier accounts were partly wrong, in opposite directions.**

- The original audit's "44 navy fills, 34 + 34 greens" double-counted: it summed
  fills and strokes. The greens really are **17 fills each**, and navy really
  has **no fill**. That correction stands.
- But `tokens/colors.css` now records "there is no `#00305E` anywhere in the
  artwork". That is an **over**-correction. Navy is the stroke colour on 44
  paths and renders as roughly 47 000 pixels. It is in the artwork — as an
  outline colour, not a fill colour. The comment should say so, or a future
  maintainer may conclude `--ucan-navy` is unfounded and drop it.
- The note that 24 paths "carried NO fill … so they rendered as pure BLACK"
  needs the same care: paths with no fill but a `#00305E` stroke are not black,
  they are navy outlines. **Before any of those 24 were given an explicit
  `#00305E` fill, check that the change did not fill shapes that were meant to
  be open** — compare `assets/logos/u-can/u-can-logo-colour.svg` against a fresh
  render of the `.ai` (V9).

### And the primary blue is sound

`--ucan-blue: #0463CD` is **not** in the logo — but the comment claiming it comes
from the templates is correct, and I verified it:

| value | in `Template_Presentation.potx` | in `Template_Deliverable.docx` | in `Template_Report.docx` |
|---|---|---|---|
| `#0463CD` | 6 | **106** | — |
| `#00305E` | 6 | 11 | **133** |
| `#3465A4` | 82 | — | — |
| `#0057B7` | **0** | **0** | **0** |

The document blue and the logo blue are genuinely different colours from
genuinely different sources. Keeping `--ucan-blue` (`#0463CD`) separate from
`--ucan-logo-blue` (`#0057B7`) is the right call.

---

## 7. J3 and J4 — closed

**J3.** `my-docs/03_u_can/U_CAN_Design/_derived/` was, as the task list says, a
live hazard. Fixed:

- all seven `_derived/tokens/*.css` now open with a `⛔ SUPERSEDED — DO NOT
  UPLOAD` banner naming the exact token collisions and their consequences;
- `_derived/CONTRAST-AUDIT.md` carries a banner stating that its ratios were
  computed against the logo palette, with the live figures beside them
  (blue on white **5.72:1**, not 6.89:1; green on white **2.56:1**, not 3.97:1 —
  the live green is a *worse* failure than the superseded file implies);
- `_derived/FONT-INVENTORY.md` is marked superseded as a *decision* while noting
  its facts still stand and are why Metropolis was rejected;
- `_derived/DECK-ARCHETYPES.md` is marked **still current** — it re-derived exactly;
- `_derived/README.md` says which parts are hazardous and which are not.

**J4.** `DESIGN-FINDINGS.md` now opens with a superseded header carrying the
corrected logo inventory above, and a pointer to `DESIGN-TASKS-REMAINING.md`.

---

## 8. What still needs doing, and by whom

### Needs the Design System app (cannot be done over the file API)

| task | why |
|---|---|
| **V1** `check_design_system` | not exposed as a tool here |
| **V2** recompile | `_ds_manifest.json` / `_ds_bundle.js` are built by the app's self-check |
| **V3, V5** cards and templates render | must follow the recompile — checking now would only test the stale bundle |

**One action unblocks all of these: open the project once in Claude Design.**

### Ready to do over the file API, once V2 is green

R1 (Radio), R3 (promote `ImageSlot`), R5 (repoint the deleted paths), R7, R8,
R9, R10, E1 (thumbnails), E2/E3 (tokenise `Report.dc.html` / `Deck.dc.html`),
H7 (migrate legacy assets), plus the A3 font consolidation above.

### Still needs you

Unchanged from the task list's blocker table: **G1** (chart conventions),
**H1–H3** (photography, map, objectives artwork), **H4/H5** (reversed sign-off,
stacked lockup), **H6** (mono UA emblem), **A1/A5** (claim face off Windows;
Office vs web fonts), **E5/E7**, **K1**, **I5**.

Two are now cheaper to answer than the list suggests:

- **A1** — the claim line falls back to Manrope off Windows. Manrope has no
  condensed axis, so the DIN character is genuinely lost. If you want it kept,
  **Archivo Narrow** is OFL, has full Cyrillic, and is the closest of the three
  candidates to Bahnschrift's proportions.
- **A5** — Manrope is OFL, so it *can* be installed and embedded in the `.potx`
  and `.docx`. Updating the Office templates to Manrope is permitted and would
  make deck and web match. The only cost is re-flowing the templates.
