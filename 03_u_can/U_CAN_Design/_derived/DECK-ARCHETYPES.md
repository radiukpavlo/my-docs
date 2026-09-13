> ## ✅ Still current
>
> Re-verified against source on **13 September 2026**. The deck-corpus analysis in
> this file was independently re-derived and **matched exactly** (126 slides,
> 7 decks, bullets on 1 slide in 126).

# How U_CAN actually presents — evidence for the deck template

**Task F2.** Ten PDFs in `U_CAN_Knowledge-base/Reference/` were parsed page by
page with PyMuPDF: text, font sizes, bullet glyphs, ruled lines, real table
structure, and the on-page area of every raster image. Two of the ten are A4
documents (`MS6_Agenda_EN`, `Technical_Report_B`) and are excluded. The
remaining eight are decks; seven are 16:9 and are the corpus below.
`U_CAN_WP_Overview.pdf` is 2.25:1 — a poster-shaped export, not a deck — and is
excluded from the counts.

**Corpus: 7 decks, 126 slides.**

---

## The finding that matters most

**U_CAN slides are graphic-led, not bullet-led — and most of that graphic
content is pasted raster imagery that the design system could render natively.**

Bullets appear on **1 slide in 126**. Ruled tables on **4**. Native vector
charts: **zero**. Meanwhile **94% of slides give at least 12% of their area to
pasted images.**

Manual review of a sample shows what those images actually are, and it is not
mostly photography:

| what the pasted image really is | what it should be | component |
|---|---|---|
| a "14,800 vehicles" / "20%" figure block | a stat tile | `Stat`/`KPI` (D5) |
| a 2 → 3 → 4 March dot-and-line chain | a milestone timeline | `Timeline` (D5) |
| a three-up photo strip with caption bars | a figure grid | `Figure` + `Caption` (D5) |
| a green or blue rounded callout box | a tinted panel | `Alert` / `Panel` (D3, B2) |
| a two-column problem/solution card pair | a comparison layout | `Grid` + `Card` (D6) |

Every one of these is on the Section D build list already. The evidence says
those components are not speculative additions — they are **the things U_CAN
is currently drawing by hand in PowerPoint and pasting in as pictures.**
That is also why the decks are heavy (a 35-slide status deck is 4.3 MB) and why
none of this content is selectable, searchable, translatable or accessible.

---

## Archetype frequency

Classification is heuristic — it counts pixels and glyphs, so a pasted diagram
and a photograph both read as "image". Treat the shape of the distribution as
reliable and the individual labels as indicative.

| archetype | slides | share |
|---|---|---|
| multi-image grid | 51 | 40% |
| image + text | 38 | 30% |
| full-bleed image | 12 | 10% |
| cover / title | 7 | 6% |
| thank-you / Q&A | 5 | 4% |
| statement / plain text | 5 | 4% |
| ruled table | 4 | 3% |
| agenda / contents | 3 | 2% |
| bulleted content | 1 | 1% |

## Standard slides — is there one of each?


Read across: **a thank-you / Q&A closing slide is the one near-universal
convention** (5 of 7, and it is always the final slide). An agenda appears in
4 of 7. "Next steps" is explicit in only 2 of 7 — it is usually folded into the
last content slide rather than given its own.

---

## The house layout that already exists

`2026-05-12_Monthly_Slides.pdf` is the most developed of the seven and uses a
consistent, repeating structure that the deck template should adopt more or
less verbatim. Slides 4 and 5 are the same layout with different content:

```
┌──────────────────────────────────────────────────────────────┐
│ [EU emblem]  Timeline step 3                    [U_CAN mark] │  header band
│──────────────────────────────────────────────────────────────│
│ 24 Apr  ──── European participation and online inputs        │  date + kicker rule
│                                                              │
│ Hybrid access connected European practice                    │  navy headline
│                                                              │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                     │  3-up media
│ │  image   │  │  image   │  │  image   │                     │
│ ├──────────┤  ├──────────┤  ├──────────┤                     │  caption bar,
│ │ caption  │  │ caption  │  │ caption  │                     │  green or navy
│ └──────────┘  └──────────┘  └──────────┘                     │
│                                                              │
│ ▎ The KhNU team connected in-room participants with …        │  tinted callout
│                                                              │
│ ●────●────●────○────○                                        │  progress dots
│ Source: …                        U_CAN | Ukraine towards …   │  source + footer
└──────────────────────────────────────────────────────────────┘
```

Note the **progress-dot rail**: a five-step tracker repeated on every slide with
the current step filled. That is a real U_CAN device and the deck template has
no equivalent.

---

## Task F3 — archetypes to add, ranked by evidence

| priority | layout | evidence |
|---|---|---|
| 1 | **Media grid** (2-up / 3-up with caption bars) | the single most common content shape |
| 2 | **Stat / figure block** | recurring, currently pasted as pictures |
| 3 | **Milestone timeline** + progress-dot rail | recurring; project runs on MS/deliverable dates |
| 4 | **Tinted callout / takeaway** | on most content slides in the developed deck |
| 5 | **Thank-you / Q&A closer** | closes 5 of 7 decks |
| 6 | **Agenda / contents** | 4 of 7 decks |
| 7 | **Section break** | used, but usually carries a background image |
| 8 | **Partner-logo wall** | consortium and WP decks both need it |
| 9 | **Ruled table** | only 3% — build it, but do not lead with it |
| 10 | **Two-column comparison** | problem/solution pairs seen in the consortium deck |

**Charts (Section G) are genuinely greenfield.** Not one native chart object
exists in 126 slides — every chart in these decks arrived as a screenshot. So
G1's question is not "what are your chart conventions"; it is closer to "there
are none yet, here is a proposal". That reframing is worth putting to the user.

---

## Task F1 — `slides/` vs `templates/deck/`

The evidence supports making **`templates/deck/` the single source** and the
`slides/01-title … 06-closing` files *specimens generated from its layouts*.
Reason: the six standalone slides were extracted from `Template_Presentation.potx`,
and this analysis shows that template is **not** how U_CAN actually presents —
its six layouts cover cover / two content / two accent / closing, while the real
corpus is dominated by media grids, stat blocks and timelines that the `.potx`
does not contain. Keeping two copies would preserve a layout set the evidence
has just contradicted.

## Task F4 — speaker notes

None of the seven decks carries speaker notes in the exported PDF. The four
`Speech_*.txt` files in the knowledge base are maintained as **separate
documents**, not as slide notes. The deck template should therefore *not*
pretend to carry notes; the honest convention is a sibling speech script, which
is what task E4 (`templates/speech-script/`) builds.
