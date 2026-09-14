> ## SUPERSEDED — historical record
>
> This described v0.3.0. The system is now **v1.0.0**; the current record is
> [`FINALIZATION-TASKS.md`](FINALIZATION-TASKS.md), and print exports are in
> [`U_CAN_Design/_derived_print/`](U_CAN_Design/_derived_print/).

---

# U_CAN Design System — status after v0.3.0

**Date:** 14 September 2026
**Project:** `a2b22667-6793-404e-821b-d5219760fa3b` ("U_CAN Design System")
**Supersedes the open items in:** `DESIGN-TASKS.md`, `DESIGN-FINDINGS.md`,
`DESIGN-TASKS-REMAINING.md`, `DESIGN-VERIFICATION.md`

88 files written, 16 deleted. This file is the only current status document.

---

## What changed in one paragraph

v0.2.0's own honest headline was that **nothing in it had been visually
verified** — no browser was available to the session that built it. This pass
put a real browser (Chrome 153) and the real font binaries under the claims,
fixed what that turned up, added the surface area the kits and templates were
about to need, and **committed the verification as two dependency-free tools**
so it cannot rot again.

---

## Verified by measurement, not assumed

| Was | Now |
|---|---|
| "The SVG masters probably render" (V9) | **Verified in Chrome** at 110px and 600px, on white, navy and brand blue. Also found: they are *not* pure vector — each carries 33 embedded PNG soft-masks, 26 % of the file. For large-format print use the `.ai`. |
| "Manrope declares Cyrillic in its unicode-range" (V10) | **Verified at glyph level.** The `cyrillic` subset was decompressed and its `cmap` read: Є І Ї є і ї Ґ ґ № all present with real outlines. |
| "`--weight-medium: 600` is synthesised" (A2) | **Wrong.** `fvar` + `gvar` on every shipped file — these are variable fonts and 600 is a real instance. Nothing was ever faux-bolded. |
| "Manrope 800 may be dead weight" (A3) | The 16 files were **4 distinct files stored 4 times over**. Now 4 files declaring the axis. 75 % smaller, no rendering change. |
| "Archivo Narrow is OFL and has full Cyrillic" (A1) | **It has no Cyrillic at all.** Nor do Barlow Condensed or Saira Condensed. All three would have fixed the English claim line and re-broken the Ukrainian one. |

---

## Defects found and fixed

- **`Tag tone="grey"` failed WCAG AA at 3.50:1** — and it is the tone the
  templates use for the dissemination level on the cover of every deliverable.
- **The invitation email could not have worked in an inbox**: it referenced an
  SVG (Outlook renders none), used project-relative image paths a mail client
  cannot resolve, had no plain-text part and no preheader, and set 11px footer
  links in yellow-on-blue at 3.78:1 — the system's own rule says small text on
  the band is white.
- **The deck's closing disclaimer and the report's were `#808080`** — 3.95:1 on
  text the grant agreement requires to be legible.
- **`LeafRule` ignored the `base` prop convention**, which is exactly why both
  document templates drew the leaf rule by hand instead of using the component.
- **`--ucan-navy` IS in the logo artwork.** v0.2.0 over-corrected an earlier
  error and recorded that it was not. It is the *stroke* colour on 44 paths,
  ~47 000 rendered pixels. Left standing, a maintainer would have dropped the
  token as unfounded.

---

## Added

- **`components/charts/`** — BarChart, StackedBarChart, LineChart, DonutChart,
  WPProgressGroup. Zero baseline, horizontal gridlines, direct labels, a
  finding-stating `aria-label` and a visually-hidden data table, all enforced in
  code rather than left to the author.
- **`UkraineMap`** — names set as real HTML over the no-names artwork. The
  coordinates are the **measured centroids of the artwork's own yellow markers**,
  found by isolating yellow pixels and flood-filling. An equirectangular
  estimate from latitude and longitude was good in x and ~1.5 % high in y, which
  read on screen as every label floating above its dot.
- `ImageSlot`, `Dialog`, `Toast`, `Tooltip`, `Menu`/`LanguageSwitch`, `Avatar`,
  `Divider`, `Stepper`, `FileUpload` — each with the full three-file contract.
- **Roboto Condensed**, self-hosted, so the claim line is condensed on every
  platform and in both languages.
- **`tools/contrast.mjs`** — 43 pairings, the forbidden list, the series-ramp
  monotonicity, and every `N.NN:1` quoted anywhere in the system re-derived from
  the tokens named on the same line. Currently **0 failures, 0 drifted**.
- **`tools/link-check.mjs`** — every `src`/`href`/`url()` and every `var()`.
- Favicon set and a 1200×630 Open Graph card.
- Deck reordered by measured frequency, and six archetypes added.

---

## Still open — and who can close it

### Only the Design System app can do these

1. **Recompile.** `_ds_manifest.json` still describes the pre-0.2.0 system — it
   lists 21 components at `components/core/` paths that were deleted two
   releases ago, and it does not know about any of the 15 added since.
   `_ds_bundle.js` is compiled at the same time, so every card that reads the
   namespace is rendering against a stale bundle.
   **Open the project once in Claude Design and let the self-check run.** This is
   one action and it unblocks V1, V2, V3 and V5.
2. **Register starting points.** `check_design_system` reports
   `Starting points: (none)`. `readme.md` has a table, but a table is
   documentation, not registration. A blank deck, a blank report and a blank web
   page need registering inside the app.

### Needs a decision or an asset from you

3. **Sign off the reversed lockup (H4).** Rendering the colour mark on navy was
   verified this pass and confirms the need — the blue "CAN" all but disappears.
   `u-can-logo-reversed.svg` was derived mechanically; *which* elements knock out
   to white is a brand judgement.
4. **Vertical / stacked lockup (H5)** — supply, or confirm none exists.
5. **Monochrome Ukrainian EU emblem (H6)** — needed or not? If needed it must
   come from the EU brand portal; it may not be made by desaturating.
6. **A vector pilot-cities map (H2).** The raster artwork works and is now
   correctly labelled, but the same graphic is printed at A4 and projected.
7. **Three official city banners have a contrast problem.** Khmelnytskyi 2.56:1,
   Ivano-Frankivsk 2.76:1, and Vinnytsia **1.51:1** — the exact white-on-yellow
   pairing the system forbids. Ask WP7 to reissue those three with navy text.

### Agent work remaining

8. **Four website screens** — Consortium/Partners, Work Packages, Publications,
   Events. `PersonCard`, `DataTable`, `Timeline`, `Pagination` and now `Menu` all
   exist, so none is blocked. *Not done in this pass.*
9. **Wire `LanguageSwitch` into `WebsiteHeader`** and give the Home screen a
   Ukrainian rendering. The component is built; the integration is not.
10. **Ukrainian variants of `pilot-report` and `invitation-email`.** The
    bilingual foundations are in (`FundingNotice` is bilingual, the map takes
    `lang`), but the template variants are not written.
11. **Delete the legacy flat assets.** Nothing in the four files that were
    keeping them alive points at them any more, but 28 legacy guideline cards and
    eight templates were not opened this pass. Run
    `node tools/link-check.mjs` over the whole project first — that is what it
    is for — then delete.
12. **`qa/kitchen-sink.html` under-reports.** Its `expected` array is a
    hard-coded list of 42 component names; there are now 57 modules.
13. **Eight templates still have no `.thumbnail`**, so they show no preview.
14. **`templates/deliverable/`, `pilot-report/`, `conference-report/`,
    `speakers-bio/`, `speech-script/`, `timesheet/`, `wp-status/`** were not
    opened this pass. Expect the same class of defect the deck and report had:
    raw hex, legacy asset paths, `#808080` on legal text.

---

## How to verify any of this yourself

```bash
node tools/contrast.mjs     # 43 pairings recomputed from tokens/
node tools/link-check.mjs   # every asset path and token reference
```

Both are dependency-free and live in the project. **Numbers in this system are
recomputed, not inherited** — that rule exists because two ratios were once
carried over from a different palette and made a failing colour look compliant.
