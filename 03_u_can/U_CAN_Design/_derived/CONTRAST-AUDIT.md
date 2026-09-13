> ## ⛔ SUPERSEDED — do not use as a source of truth
>
> Superseded on **13 September 2026** by design system **v0.2.0**
> (project `a2b22667-6793-404e-821b-d5219760fa3b`). Kept as a working record only.
>
> **Every ratio in this file was computed against the wrong palette.** It uses the
> logo artwork's `#0057B7` / `#3B9139` as if they were the brand tokens. The live
> brand tokens are `--ucan-blue: #0463CD` and `--ucan-green: #75B23C`, taken from
> the Office templates. So the headline figures here are wrong for the live system:
> the 6.89:1 quoted for "blue on white" is the **logo** blue (live is **5.72:1**),
> and the 3.97:1 quoted for "green on white" is the **logo deep** green
> (live `--ucan-green` on white is **2.56:1** — a much worse failure).
> The live, correct matrix is `guidelines/colors-pairings.card.html`.
>
> The *method* here is still sound, and the state-colour derivation (B2) was
> carried into the live `tokens/colors.css` unchanged and verified.

# Colour audit — U_CAN

**Tasks B1 and B3.** Ratios are WCAG 2.1 relative-luminance contrast, computed
from the hex values, not estimated. Thresholds: **4.5:1** body text,
**3:1** large text (≥24 px, or ≥18.66 px bold).

---

## Where the palette comes from

`Logos/U_CAN_V3_final.ai` is a **PDF-1.5 file** — Illustrator's PDF-compatible
save. It parses cleanly: 180 vector drawing operations, one page, **no raster
content at all**. Every brand value below is one of the artwork's own fills.

| colour | fills in the logo | role in the mark |
|---|---|---|
| `#FFFFFF` | 68 | counters, window highlights |
| **`#FFCC00`** | **50** | the twelve EU stars |
| `#00305E` | 44 | deep navy — building bodies |
| `#75B23C` | 34 | light green — leaf highlights |
| `#3B9139` | 34 | dark green — leaf bodies |
| `#003399` | 6 | EU flag blue — star field |
| `#0057B7` | 4 | the "CAN" wordmark |

Two of these are exact flag colours, which is almost certainly deliberate:
`#003399` is the EU flag blue and `#0057B7` is the Ukrainian flag blue.

---

## Task B1 — the yellow, resolved

**`#FFCC00` is canonical. `#FFC000` is a picker slip.**

1. **The artwork settles it.** `#FFCC00` fills all 50 star shapes in the logo
   master. `#FFC000` does not appear anywhere in the logo.
2. **The deck template agrees, 8 to 2.** Across the whole of
   `Template_Presentation.potx`, `#FFCC00` occurs 8 times and `#FFC000` twice.
3. **The audit's premise needs a correction.** The earlier note said slide 5
   uses `#FFCC00` and slide 4 uses `#FFC000`. In fact **both values appear on
   both slide 4 and slide 5** — so this is inconsistency *within* a slide, not a
   deliberate second tone. Nothing is lost by deleting one.
4. **Brand and funder stay aligned.** `#FFCC00` is the exact EU emblem yellow,
   so a U_CAN yellow band and the EU emblem beside it are the same colour.

Action taken in `tokens/colors.css`: `--ucan-yellow: #FFCC00` is canonical;
`--ucan-yellow-legacy: #FFC000` is marked deprecated, retained only so existing
`.potx`-derived artwork remains traceable.

---

## Task B3 — contrast audit

The last four rows of the matrix are values inherited from the third-party
WM Studio deck template, not U_CAN brand colours. They are audited because the
deck template still exposes them.

### Full pairing matrix

| foreground \ background | navy | blue | eu-blue | yellow | green | green-light | white | ink | yellow-alt (legacy) | teal (potx accent1) | mint (potx accent5) | slate-blue (potx layouts) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **navy** `#00305E` | — | ❌ 1.92 | ❌ 1.22 | ✅ 8.77 | ⚠️ 3.34 | ✅ 5.17 | ✅ 13.25 | ❌ 1.31 | ✅ 8.07 | ✅ 6.37 | ✅ 9.11 | ❌ 2.24 |
| **blue** `#0057B7` | ❌ 1.92 | — | ❌ 1.58 | ✅ 4.56 | ❌ 1.74 | ❌ 2.69 | ✅ 6.89 | ❌ 2.53 | ⚠️ 4.20 | ⚠️ 3.31 | ✅ 4.74 | ❌ 1.16 |
| **eu-blue** `#003399` | ❌ 1.22 | ❌ 1.58 | — | ✅ 7.18 | ❌ 2.74 | ⚠️ 4.24 | ✅ 10.86 | ❌ 1.60 | ✅ 6.62 | ✅ 5.22 | ✅ 7.47 | ❌ 1.83 |
| **yellow** `#FFCC00` | ✅ 8.77 | ✅ 4.56 | ✅ 7.18 | — | ❌ 2.62 | ❌ 1.70 | ❌ 1.51 | ✅ 11.51 | ❌ 1.09 | ❌ 1.38 | ❌ 1.04 | ⚠️ 3.92 |
| **green** `#3B9139` | ⚠️ 3.34 | ❌ 1.74 | ❌ 2.74 | ❌ 2.62 | — | ❌ 1.55 | ⚠️ 3.97 | ⚠️ 4.39 | ❌ 2.42 | ❌ 1.91 | ❌ 2.73 | ❌ 1.49 |
| **green-light** `#75B23C` | ✅ 5.17 | ❌ 2.69 | ⚠️ 4.24 | ❌ 1.70 | ❌ 1.55 | — | ❌ 2.56 | ✅ 6.79 | ❌ 1.56 | ❌ 1.23 | ❌ 1.76 | ❌ 2.31 |
| **white** `#FFFFFF` | ✅ 13.25 | ✅ 6.89 | ✅ 10.86 | ❌ 1.51 | ⚠️ 3.97 | ❌ 2.56 | — | ✅ 17.40 | ❌ 1.64 | ❌ 2.08 | ❌ 1.45 | ✅ 5.93 |
| **ink** `#1A1A1A` | ❌ 1.31 | ❌ 2.53 | ❌ 1.60 | ✅ 11.51 | ⚠️ 4.39 | ✅ 6.79 | ✅ 17.40 | — | ✅ 10.60 | ✅ 8.37 | ✅ 11.97 | ❌ 2.94 |
| **yellow-alt (legacy)** `#FFC000` | ✅ 8.07 | ⚠️ 4.20 | ✅ 6.62 | ❌ 1.09 | ❌ 2.42 | ❌ 1.56 | ❌ 1.64 | ✅ 10.60 | — | ❌ 1.27 | ❌ 1.13 | ⚠️ 3.61 |
| **teal (potx accent1)** `#00CC99` | ✅ 6.37 | ⚠️ 3.31 | ✅ 5.22 | ❌ 1.38 | ❌ 1.91 | ❌ 1.23 | ❌ 2.08 | ✅ 8.37 | ❌ 1.27 | — | ❌ 1.43 | ❌ 2.85 |
| **mint (potx accent5)** `#AAE2CA` | ✅ 9.11 | ✅ 4.74 | ✅ 7.47 | ❌ 1.04 | ❌ 2.73 | ❌ 1.76 | ❌ 1.45 | ✅ 11.97 | ❌ 1.13 | ❌ 1.43 | — | ⚠️ 4.08 |
| **slate-blue (potx layouts)** `#3465A4` | ❌ 2.24 | ❌ 1.16 | ❌ 1.83 | ⚠️ 3.92 | ❌ 1.49 | ❌ 2.31 | ✅ 5.93 | ❌ 2.94 | ⚠️ 3.61 | ❌ 2.85 | ⚠️ 4.08 | — |

### The pairings the deck template invites

| pair | ratio | body text ≥4.5 | headline ≥3.0 | verdict |
|---|---|---|---|---|
| navy on teal `#00305E` on `#00CC99` | **6.37:1** | ✅ | ✅ | AA |
| white on teal `#FFFFFF` on `#00CC99` | **2.08:1** | ❌ | ❌ | FAIL |
| navy on yellow `#00305E` on `#FFCC00` | **8.77:1** | ✅ | ✅ | AAA |
| white on yellow `#FFFFFF` on `#FFCC00` | **1.51:1** | ❌ | ❌ | FAIL |
| navy on white `#00305E` on `#FFFFFF` | **13.25:1** | ✅ | ✅ | AAA |
| white on navy `#FFFFFF` on `#00305E` | **13.25:1** | ✅ | ✅ | AAA |
| yellow on navy `#FFCC00` on `#00305E` | **8.77:1** | ✅ | ✅ | AAA |
| blue on white `#0057B7` on `#FFFFFF` | **6.89:1** | ✅ | ✅ | AA |
| white on blue `#FFFFFF` on `#0057B7` | **6.89:1** | ✅ | ✅ | AA |
| green on white `#3B9139` on `#FFFFFF` | **3.97:1** | ❌ | ✅ | AA large only |
| white on green `#FFFFFF` on `#3B9139` | **3.97:1** | ❌ | ✅ | AA large only |
| white on green-light `#FFFFFF` on `#75B23C` | **2.56:1** | ❌ | ❌ | FAIL |
| navy on green-light `#00305E` on `#75B23C` | **5.17:1** | ✅ | ✅ | AA |
| navy on yellow-alt `#00305E` on `#FFC000` | **8.07:1** | ✅ | ✅ | AAA |

---

### Forbidden pairings, and what to use instead

| ❌ forbidden | measured | why | ✅ use instead |
|---|---|---|---|
| white on `--ucan-yellow` | **1.51:1** | far below every threshold; effectively invisible | navy on yellow — **8.77:1**, AAA |
| white on teal `#00CC99` | **2.08:1** | fails even at headline scale | navy on teal — **6.37:1**, AA |
| white on `--ucan-green-light` | **2.56:1** | fails even at headline scale | navy on green-light — **5.17:1**, AA |
| `--ucan-green` on white | **3.97:1** | headline scale only; fails body text | navy on white — **13.25:1**, AAA |
| white on `--ucan-green` | **3.97:1** | headline scale only; fails body text | navy on green-light, or white on navy |
| `--ucan-blue` on `--ucan-navy` | **1.92:1** | two brand blues too close to separate | yellow on navy — **8.77:1**, AAA |

### The safe pairings — what the system should reach for by default

| pairing | ratio | grade |
|---|---|---|
| white on `--ucan-navy` | 13.25:1 | AAA |
| `--ucan-navy` on white | 13.25:1 | AAA |
| `--ucan-navy` on `--ucan-yellow` | 8.77:1 | AAA |
| `--ucan-yellow` on `--ucan-navy` | 8.77:1 | AAA |
| `--ucan-blue` on white | 6.89:1 | AA |
| white on `--ucan-blue` | 6.89:1 | AA |
| `--ucan-navy` on `--ucan-green-light` | 5.17:1 | AA |

**The pattern worth stating as a rule:** navy and white are the only two
foregrounds that work almost everywhere. Every U_CAN accent — yellow, both
greens, both blues — is a *background* colour that takes navy on top. The one
exception is `--ucan-blue`, which is dark enough to sit on white.

---

## Task B2 — semantic state colours

Derived in OKLCH so they stay in the brand's family rather than being imported
from a generic UI kit. `success` and `info` reuse the hues of `--ucan-green`
and `--ucan-blue` **exactly**; `warning` reuses `--ucan-yellow`'s hue, darkened
until it can carry text. Only `error` introduces a hue the brand lacks — there
is no red in the U_CAN palette and a danger signal cannot be green, blue or
yellow — and it keeps the palette's chroma discipline (C ≈ 0.16).

Each `-fg` was solved for the **lightest** lightness that still clears 4.5:1
against its own tint, so the states stay as vivid as accessibility permits.

| state | fg | bg tint | border | fg oklch | fg on its tint | fg on white |
|---|---|---|---|---|---|---|
| **success** | `#2A822A` | `#EBFBE9` | `#AFDEAB` | `oklch(0.536 0.150 143.0)` | **4.51:1** | 4.86:1 |
| **warning** | `#906B00` | `#FFF5E0` | `#E9CC8F` | `oklch(0.551 0.113 85.0)` | **4.52:1** | 4.90:1 |
| **error** | `#C34740` | `#FFF3F1` | `#FFBCB4` | `oklch(0.568 0.160 27.0)` | **4.50:1** | 4.89:1 |
| **info** | `#246FD2` | `#F0F6FF` | `#B2D2FF` | `oklch(0.552 0.168 257.0)` | **4.52:1** | 4.91:1 |

Gamut handling: where a hue could not hold the target chroma in sRGB, chroma was
reduced and **hue held exactly**, rather than clamping RGB channels — clamping
shifts hue and would have pulled `warning` toward orange and `info` toward cyan.
This is why `warning` lands at C = 0.113 rather than 0.150.

---

## Task B5 — dark mode

Recorded as a position rather than left open: **the system is light-only by
design.** It is a print-and-deck-led identity whose two primary outputs — A4
deliverables and 16:9 decks — are authored on white and printed on white. A
`prefers-color-scheme` layer would have to invent a second set of brand
relationships that no source material specifies.

What the system does have instead is a **dark-surface convention**: the navy
band. `tokens/base.css` defines `.on-dark` / `[data-surface="dark"]` so that
type and links invert correctly on navy without a whole second theme.
