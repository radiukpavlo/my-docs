> ## ✅ Uploaded to design system v0.2.0 — 13 September 2026
>
> 35 files written to project `a2b22667-6793-404e-821b-d5219760fa3b`:
> `assets/imagery/cities/` (24), `assets/imagery/project/` (**2** only — see
> consent below), `assets/maps/` (5), `assets/illustrations/` (1), plus rewritten
> `guidelines/imagery.card.html`, `guidelines/charts-map.card.html` and
> `guidelines/asset-manifest.md`. Both cards were render-tested in Chrome and
> every image path was checked against the live file list. **Task R6 is closed —
> `assets/imagery/` is no longer empty.**
>
> **Correction to the consent table below.** It originally labelled three project
> photos low-risk. Checking them at full size, only **two** are face-free:
> `project-05-ceec-room` (empty room with an SFPA banner) and
> `project-10-zhy-board` (workshop results board). The greenhouse and briefing
> shots both show identifiable faces. Only the two face-free photos were
> uploaded; the other eight remain here, outside the system. Two files were also
> renamed for accuracy: `project-07-zhy-garden` → `-briefing`,
> `project-08-zhy-sitevisit` → `-reception`.
>
> **New finding — the official banners have a contrast problem.** Their
> backgrounds are the brand palette, but three of six set white text on a ground
> that cannot carry it: Khmelnytskyi 2.56:1, Ivano-Frankivsk 2.76:1 (on an orange
> `#EF7D00` that is not in the token set), and **Vinnytsia 1.51:1 — the exact
> white-on-yellow pairing `tokens/colors.css` forbids.** Use them as artwork and
> set captions as real HTML; ask WP7 to reissue those three with navy text.

# U_CAN media — H1, H2, H3

**Date:** 13 September 2026
**Searched:** `G:\My Drive\Work\Work_RnD\RnD_U_CAN` (1 049 files) and
`G:\My Drive\Saved\Saved_U_CAN` (2 270 files) — 3 319 files, of which **2 152 are
images**, every subfolder walked.
**Staged here:** 40 files, 10.9 MB, ready to copy into the design system's `assets/`.

Almost everything usable came from one place:
`Saved_U_CAN/U_CAN_Sources/WP7_Communication, dissemination, exploitation/`.
That is the consortium's communications library and it should be treated as the
canonical source for project imagery.

---

## H1 — Photography ✅ delivered

### Pilot-city heroes

All six pilot cities have photography, in
`WP7…/Pictures/{Lviv,Kyiv,Zhytomyr,Khmelnytskyi,Ivano-Frankivsk,Vinnytsia}/`.
They are **aerial and street cityscapes with no identifiable individuals**, so
they carry no consent burden and can go live immediately.

Each is supplied in the three crops the task asks for — 16:9 hero, 8:5 card,
1:1 square — centre-cropped from the largest available original, never upscaled:

| city | source | true source pixels | hero delivered |
|---|---|---|---|
| Ivano-Frankivsk | `Ivano-Frankivsk1.jpg` | **5184 × 3349** | 1600 × 900 |
| Vinnytsia | `Vinnytsia .jpg` | 2000 × 1500 | 1600 × 900 |
| Khmelnytskyi | `Khmelnytskyi .jpg` | 1850 × 1434 | 1600 × 900 |
| Kyiv | `Kyiv6.jpg` | 1280 × 856 | 1280 × 720 |
| Zhytomyr | `Zhytomyr.JPG` | 1280 × 720 | 1280 × 720 |
| Lviv | `Lviv.jpg` | 1024 × 653 | 1024 × 576 |

**Lviv and Kyiv are the thin ones.** Lviv has exactly one photograph in the whole
archive, and its 1024 px hero is below a 1440 px full-bleed. Both are fine at
card and square sizes. If a full-bleed Lviv hero is needed, it has to be
sourced — nothing larger exists in either Drive folder.

> A note on the numbers: reading these files with a PDF library reports
> dimensions in **points**, not pixels, which understates them by 25 %. The
> table above is true pixels. Ivano-Frankivsk in particular is print-quality.

### Official pilot-city banners — better than the raw photos for most uses

`WP7…/Communication materials/Banners/Digital banner_<City>.png` — six banners,
**1440 × 810, exactly 16:9**, one per pilot city. Each carries the reversed
U_CAN mark with a circular city photograph masked into the wordmark, the city
name, the pilot's one-line objective, and the white "Funded by the European
Union" emblem, on a per-city background colour.

These are official WP7 artwork, already on-brand, already the right aspect, and
already captioned. **For the website kit's pilot cards they are a better default
than the raw photographs.** Both are staged so you can choose per surface.

### Project photography

Ten photographs from the two curated `Selected/` folders, downscaled to 1600 px
long edge. Originals are 4000 × 3000 to **7008 × 4672** — genuinely
professional, and the full-resolution files remain on Drive for print.

- **CEEC 2025** (`WP7…/Conferences/2025_11_CEEC 2025/Photos/Selected/`) — panel,
  audience, speaker, delegation, room.
- **Zhytomyr urban-gardening / LHD visit, Sept 2025**
  (`WP7…/Materials for posting/25-09-24 bis 27_ZHY-visit LHD_UrbanGardening/Pictures/Selected/`)
  — greenhouse, garden, site visit, workshop, results board.

### ⚠️ Consent — read before publishing any project photo

The task requires consent on file for every identifiable person. **I cannot
verify consent from the filesystem**, so each staged photo is labelled in
`MEDIA-MANIFEST.csv` with what it shows:

| label | files | meaning |
|---|---|---|
| `low risk — no faces` / `no/distant people` | 3 | greenhouse, garden, results board — publishable now |
| `check — … identifiable` | 2 | one or two people, recognisable |
| `FACES — consent required` | 5 | conference panels, audience, group portraits |
| `cityscape — no identifiable individuals` | 18 | all city crops — publishable now |

**Publish the cityscapes and the three low-risk project shots now. Hold the
other seven until consent is confirmed.** The CEEC group portraits are the
highest risk — posed shots of named individuals at a public event still need a
release for marketing use under GDPR.

---

## H2 — Pilot-cities map ◐ partial: raster delivered, no vector exists

### What was found

`WP7…/Communication materials/Maps/` — the real pilot map: Ukraine in grey with
the six pilot oblasts filled, yellow dots on the six pilot cities, other cities
as navy dots. **Five colourways**, all 1024 × 537 PNG:

`ukraine-pilots-light-blue-with-names.png` (the only one with city labels),
plus `light-blue`, `light-green`, `dark-blue`, `dark-green`, all `no-names`.

### The vector does not exist in either folder — this is now settled

I searched both roots exhaustively. **The only SVG files anywhere in either
Drive folder are the 11 LHD partner logos**, which the design system already
has. There is no `.ai`, `.eps`, `.svg` or vector PDF of the Ukraine map.

Places checked and ruled out:

| candidate | why it is not the map |
|---|---|
| `Conferences/…_Oulu/260226_U_CAN_Map[Draft_4]vektor.pdf` | genuinely vector (4 035 paths, no raster) but it is an **"Ideas Wall"** city-scene illustration for a workshop, **not** the Ukraine map. See H3 below. |
| `Communication materials/Banners/U_CAN rolldown banner_{EN,UA}.pdf` | 19 MB each, but each is **one flat raster** — zero vector drawings |
| `Communication materials/Postcards/Pilot postcard_*.pdf` | rasters with a thin vector frame |
| `04_Deliverables/D2.1_U_CAN_Interactive map_v1.1.pdf` | a 26-page report *about* the interactive map; its figures are screenshots |

### What this means and what to do

1024 px is enough for a 1280 px slide but **not for A4 print** — at 210 mm wide
that is about 124 dpi, well under the 300 dpi print standard. The task's own
rationale ("the same graphic is printed at A4 and projected at 1280px") is
therefore not satisfiable from what exists.

Two ways forward, in order of preference:

1. **Ask WP7 comms for the Illustrator source.** Five clean colourways of one
   artwork is the signature of a single `.ai` with swapped swatches. Whoever
   produced these has it; it has simply never been shared into the archive.
   This is a one-email fix and it also gives D6 the oblast paths it needs.
2. **Rebuild it.** Ukraine's oblast boundaries are open geodata, so a
   `UkraineMap` component could be drawn from scratch with the six pilots as a
   data prop — which is what D6 actually wants. This is real work and needs a
   decision on the geodata source and its licence.

Until one of those lands, the staged PNGs at least remove the broken
`map_eng_2.png` placeholder.

---

## H3 — Objectives artwork ❌ not found in either folder

**`1_Монтажная область 1.png` is not in `RnD_U_CAN` or `Saved_U_CAN`.** The name
is Illustrator's default Russian-locale artboard export ("Артборд 1"), so it was
exported by someone with a Russian-language Illustrator and given no real name —
which also means it will not be findable by a meaningful keyword. I searched for
the literal name, for `artboard`, for `objectiv*`, for `ціл*`, and for every
numeric-prefixed `.png`/`.ai`/`.svg` in both trees. It is not there.

### Two things that were found instead, both useful

**1. `illustrations/ucan-spot-illustrations.png`** — from
`WP7…/Social media/Templates/250612_U_CAN_Social-Templates[Illustrations_for_Canva].png`.
A 2354 × 408 strip of nine flat spot illustrations on U_CAN light green: tree,
sensor mast with signal arcs, lightbulb, gear, leaf document, handshake, traffic
light, bench, lamppost.

This is brand-sanctioned pictorial artwork, and it **changes task H9**. The
audit records that "the source materials contain zero icons" and proposes
sanctioning Lucide. That is no longer quite true — there is a real U_CAN
illustration set. It is a spot-illustration set rather than a UI icon system, so
Lucide may still be right for interface icons, but these should be the
sanctioned choice for editorial and slide illustration, and the decision should
be made knowing they exist.

**2. A vector city-scene illustration.** The Oulu "Ideas Wall" PDF is a genuine
vector drawing — 4 035 paths, no raster — of an urban decarbonisation scene
(factories, solar arrays, retrofitted blocks, green corridors, cycle paths).
The design system already ships `assets/illustrations/ucan-city-scene.png` and
`ucan-city-scene-with-lockup.png`; **this looks like the vector master for that
family.** I did not stage it: a direct conversion is 1.5 MB with 242 embedded
raster tiles, too heavy to ship as-is. It would need cleaning in Illustrator
first, and the source is at
`WP7…/Conferences/2026_03_Citizen Science Festival_Oulu/260226_U_CAN_Map[Draft_4]vektor.pdf`.

**To close H3 properly** the artwork has to be identified. The likeliest answer
is that it is one of the existing `assets/illustrations/` files already in the
system under a better name — in which case H3 is already done and the task text
is stale. Worth confirming before anyone hunts further.

---

## Beyond H1–H3 — three finds that affect other open tasks

**1. The official Corporate Design Guideline exists.**
`WP7…/Visual Guidelines/2024-06-23 CI VI_Guideline und Bericht-Vorlagen/` holds
`2024-06-23_U_CAN_Corporate Design Guideline_Rev.00.pdf` (original and minimized)
plus **16 `.ai` source pages** — logo structure, logo variants, inadmissible
use, font types, logo colour, greyscale logo, auxiliary colours, colours in
photos, design-area division, grid element, format specifics — and Deliverable,
Report and cover-sheet templates.

This is the authoritative brand document, and nothing in the design system
currently cites it. It very likely answers **H4** (reversed lockup), **H5**
(stacked lockup), **J8** (co-branding) and **A1** outright. It is the single
highest-value thing found in this search.

**2. Avenir Next is present as 14 desktop TTFs**, in the `Font/` folder of that
same CI kit — the consortium designer shipped them with the guideline. Note
carefully: **desktop TTFs are not a webfont licence.** Avenir Next is a
Monotype/Linotype commercial face and a CI-kit desktop licence normally excludes
web embedding. So this does **not** by itself resolve **A2** — but it does mean
the Office templates can legitimately use the real Avenir Next, and it is worth
checking the guideline's own licence page before deciding A2/A5.

**3. The reversed lockup is already settled by the banners — evidence for H4.**
Every one of the six pilot banners uses the U_CAN mark reversed on a colour
ground, and in all six **the stars knock out to white along with the buildings,
the wordmark and the underscore.**

The design system's `u-can-logo-reversed.svg` was derived mechanically by
knocking out anything under 3:1 against navy — which **keeps the yellow stars**,
because yellow on navy measures 8.77:1. The official treatment does not. If
these banners are authoritative, the derived reversed lockup is wrong and should
be regenerated with the stars white.

---

## Files staged here

```
cities/      <city>-hero-16x9.jpg · -card-8x5.jpg · -square-1x1.jpg   (6 × 3)
             <city>-banner-16x9.png                                   (6, official)
project/     project-01…10-*.jpg                                      (10, 1600 px)
map/         ukraine-pilots-<colourway>-<with|no>-names.png           (5)
illustrations/ucan-spot-illustrations.png                             (1)
MEDIA-MANIFEST.csv    every file: dimensions, bytes, consent status,
                      exact source path on Drive, and processing applied
```

Suggested destinations in the design system: `cities/` and `project/` →
`assets/imagery/` (which is currently **empty — it does not exist at all**, task
R6), `map/` → `assets/`, `illustrations/` → `assets/illustrations/`.

Nothing here has been uploaded. All originals remain untouched on Drive.
