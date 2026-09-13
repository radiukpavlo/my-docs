# Asset manifest

Provenance for every file in `assets/`: where it came from, what licence governs
it, and what it may be used for. Task H10.

**Rule:** nothing enters `assets/` without a row here. An asset whose origin
nobody can state is an asset nobody can safely publish.

---

## Summary

| Tree | Files | Size | Source | Licence |
|---|---|---|---|---|
| `assets/logos/eu/` | 28 | 768K | EU brand portal, via project folder | EU visual identity — **never modify** |
| `assets/logos/cities-mission/` | 10 | 552K | EU Missions brand pack | EU visual identity — **never modify** |
| `assets/logos/lhd/` | 11 | 388K | `LHD/` supplied by Landeshauptstadt Düsseldorf | Partner/funder mark — **never modify** |
| `assets/logos/u-can/` | 8 | 1.2M | `Logos/U_CAN_V3_final.ai` + `.._Black-White.ai` | Project-owned |
| `assets/brand/` | 4 | 2.0M | Project source folder | Project-owned |
| `assets/fonts/manrope/` | 17 | 272K | Google Fonts / github.com/sharanda/manrope | **SIL OFL 1.1** — redistributable |
| **`assets/imagery/cities/`** | **24** | **8.8M** | WP7 communications library — see below | Project-owned |
| **`assets/imagery/project/`** | **2** | **0.5M** | WP7 communications library — see below | Project-owned |
| **`assets/maps/`** | **5** | **1.6M** | WP7 communications library — see below | Project-owned |
| `assets/illustrations/` | 5 | — | Project source + WP7 social templates | Project-owned |
| `assets/banners/` | 8 | — | Carried over from the previous extraction | Project-owned |

---

## Imagery — added 13 September 2026

Both project Drive folders were searched in full — `RnD_U_CAN` (1 049 files) and
`Saved_U_CAN` (2 270 files), 2 152 of them images. **Effectively all usable
imagery lives in one place** and it should be treated as canonical:

```
Saved_U_CAN/U_CAN_Sources/WP7_Communication, dissemination, exploitation/
```

### `assets/imagery/cities/` — pilot-city photography

`<city>-hero-16x9.jpg`, `-card-8x5.jpg`, `-square-1x1.jpg` for each of the six
pilot cities, centre-cropped from the largest original in `WP7…/Pictures/<City>/`.
**Never upscaled** — the delivered size is capped by the source.

| City | Source file | Original pixels | Hero delivered |
|---|---|---|---|
| Ivano-Frankivsk | `Ivano-Frankivsk1.jpg` | **5184 × 3349** | 1600 × 900 |
| Vinnytsia | `Vinnytsia .jpg` | 2000 × 1500 | 1600 × 900 |
| Khmelnytskyi | `Khmelnytskyi .jpg` | 1850 × 1434 | 1600 × 900 |
| Kyiv | `Kyiv6.jpg` | 1280 × 856 | 1280 × 720 |
| Zhytomyr | `Zhytomyr.JPG` | 1280 × 720 | 1280 × 720 |
| Lviv | `Lviv.jpg` | 1024 × 653 | 1024 × 576 |

All six are aerial or street cityscapes with **no identifiable individuals**.
**Lviv is the constraint:** exactly one photograph of Lviv exists in the whole
archive. Do not use its hero full-bleed above 1024 px.

`<city>-banner-16x9.png` — six official WP7 banners, 1440 × 810, from
`WP7…/Communication materials/Banners/Digital banner_<City>.png`. Reversed mark
with a circular city photograph masked into the wordmark, city name, pilot
objective, white EU emblem, per-city background.

The backgrounds are the brand palette, and they amount to a real per-city
colour coding — but **three of the six set white text on a ground that cannot
carry it**:

| City | Background | Token | White text | Verdict |
|---|---|---|---|---|
| Kyiv | `#00305E` | `--ucan-navy` | 13.25:1 | ✅ AAA |
| Lviv | `#0463CD` | `--ucan-blue` | 5.72:1 | ✅ AA |
| Zhytomyr | `#3B9139` | `--ucan-logo-green-deep` | 3.97:1 | ⚠️ large text only |
| Ivano-Frankivsk | `#EF7D00` | **not in the palette** | 2.76:1 | ❌ fails |
| Khmelnytskyi | `#75B23C` | `--ucan-green` | 2.56:1 | ❌ fails |
| Vinnytsia | `#FFCC00` | `--ucan-yellow` | **1.51:1** | ❌ fails badly |

The Vinnytsia banner is the exact pairing `tokens/colors.css` lists as
forbidden. **Use the banners as artwork, not as accessible text:** set the city
name and objective as real HTML over or beside the image, and for the three
failing cities do not reuse their baked-in caption at all. The clean fix is to
ask WP7 to reissue those three with `--ucan-navy` text — navy on yellow is
8.77:1, navy on the green 5.17:1.

> **These banners are also evidence for task H4.** In all six, the stars knock
> out to **white** along with the buildings, wordmark and underscore. The
> system's `u-can-logo-reversed.svg` was derived mechanically and **keeps the
> stars yellow**, because yellow on navy measures 8.77:1 and the rule spared it.
> If the banners are authoritative, that file is wrong and should be regenerated.

### `assets/imagery/project/` — project photography, and why there are only two

Ten photographs were shortlisted from the two curated `Selected/` folders
(CEEC 2025 conference; Zhytomyr urban-gardening / LHD visit, Sept 2025).
Originals run from 4000 × 3000 to **7008 × 4672** and stay on Drive for print.

**Only two contain no identifiable people, and only those two are here:**

| File | What it shows | Source |
|---|---|---|
| `project-05-ceec-room.jpg` | SFPA "with Ukraine" banner, empty conference room | `Conferences/2025_11_CEEC 2025/Photos/Selected/SON06421.jpg` |
| `project-10-zhy-board.jpg` | Workshop results board, no people | `Materials for posting/25-09-24…_ZHY-visit LHD_UrbanGardening/Pictures/Selected/DSC_1475.JPG` |

The other eight show faces at close range — conference panels, a posed
delegation line-up, briefing and reception tables, a presenter. **They are
deliberately not in `assets/`.** They stay out until a release is on file for
every person shown; a public event does not imply consent for marketing use.
They are staged outside the system with per-photo notes in
`my-docs/03_u_can/U_CAN_Design/_derived_media/MEDIA-MANIFEST.csv`.

**This leaves task H1 half open.** The pilot-city half is complete; the
"6–10 project photographs" half stands at two.

### `assets/maps/` — the pilot-cities map

Five colourways, 1024 × 537 PNG, from `WP7…/Communication materials/Maps/`.
Ukraine in grey, the six pilot oblasts filled, yellow dots on the pilot cities.
Only `light-blue-with-names` carries labels.

**No vector master exists** — searched exhaustively; the only SVGs in either
Drive folder are the eleven LHD logos. At 1024 px the map is ~124 dpi at A4, so
it is usable on screen and **not** in print. See
`guidelines/charts-map.card.html` for the rebuild contract and the two routes
out.

### `assets/illustrations/ucan-spot-illustrations.png`

2354 × 408 strip of nine flat spot illustrations on U_CAN light green — tree,
sensor mast, lightbulb, gear, leaf document, handshake, traffic light, bench,
lamppost. From `WP7…/Social media/Templates/250612_U_CAN_Social-Templates[Illustrations_for_Canva].png`.

**This bears on task H9.** The system records that "the source materials contain
zero icons" and proposes sanctioning Lucide. That is no longer accurate — a real
U_CAN illustration set exists. It is spot illustration rather than a UI icon
system, so Lucide may still be right for interface icons, but these should be
the sanctioned choice for editorial and slide artwork.

---

## The U_CAN logo masters — corrections on the record

The two `.ai` files were previously reported as unparseable and an SVG export was
requested from the project. **That was wrong.** Both are PDF-1.5 — Illustrator's
PDF-compatible save — with no raster content at all, and they convert to true
vector SVG (281 paths each). No export was needed.

Three things were then found wrong *in the conversion*, and fixed:

1. **Eight opaque full-canvas white `<rect>` backgrounds.** An artefact of the
   PDF-compatible save: one per clip group. They made the "transparent" master
   opaque, so it could not be placed on the navy title slide — which is the
   exact problem the reversed lockup was supposed to solve. Stripped.
2. **24 paths carried no `fill` attribute.** Given an explicit `#00305E` — but
   see the caution below, which corrects the reasoning that was recorded here.
3. **The recorded fill inventory was wrong.** Recounted — twice. The second
   recount separated fill from stroke, which the first did not:

| Colour | Fills | Strokes | Share of rendered pixels | What it is |
|---|---|---|---|---|
| `#FFFFFF` | 68 | — | 1.7 % | counters, window highlights |
| `#FFCC00` | 50 | — | 12.5 % | star field |
| `#75B23C` | 17 | 17 | 2.2 % | light leaf green |
| `#3B9139` | 17 | 17 | 2.5 % | dark leaf green |
| `#003399` | 6 | — | 3.9 % | EU flag blue |
| `#0057B7` | 4 | — | **59.1 %** | the "CAN" wordmark and the skyline |
| `#00305E` | **0** | **44** | 2.8 % | outlines |

Two earlier claims both need correcting, and they err in opposite directions:

- The **first** inventory reported "44 navy fills, 34 + 34 greens, 4 blues". It
  summed fills and strokes, so the greens were doubled and a stroke colour was
  reported as a fill.
- The **second** correction — recorded here as "`#00305E` … is not in the
  artwork at all" — over-corrected. Navy is the **stroke** colour on 44 paths
  and accounts for roughly 47 000 rendered pixels. It is in the artwork; it is
  an outline colour, not a fill colour.

> ⚠️ **Caution on fix (2).** The 24 fill-less paths were described as rendering
> "pure black". Paths that carry no fill but *do* carry a `#00305E` stroke were
> never black — they were navy outlines. Before relying on that fix, compare
> `u-can-logo-colour.svg` against a fresh render of the `.ai` and confirm no
> shape that was meant to stay open has been filled in.

### Files

| File | What it is |
|---|---|
| `u-can-logo-colour.svg` | Positive master. Transparent, explicit navy. Use on white and light tints. |
| `u-can-logo-reversed.svg` | **Derived** — dark shapes and both blues knocked out to white; yellow and greens kept. ⚠️ **The six WP7 city banners knock the stars to white too.** Needs brand sign-off — `guidelines/brand-logo-reversed.card.html`. |
| `u-can-logo-bw.svg` | Single-colour master, same two fixes applied. |
| `u-can-logo-*.png` | Raster fallbacks, retained for Office documents which cannot place SVG reliably. |
| `u-can-logo-legacy.png` | Superseded mark. **Provenance only — do not use in new work.** |

---

## Duplication, and what was left in place

`assets/logos/partners/` holds four LHD files (`lhd-duesseldorf-city-admin` and
`lhd-duesseldorf-funding-en`, each `.png` + `.svg`). These duplicate two of the
eleven files now in `assets/logos/lhd/`.

**They were kept, not deleted.** They are not orphans — `guidelines/brand-partners.card.html`
references them, and removing them would break a working card to save 4 files.
`assets/logos/lhd/` is the canonical, complete set (8 Förderlogo variants + 3
Stadtverwaltung); `assets/logos/partners/` is a legacy two-file subset. New work
uses `assets/logos/lhd/`.

---

## Removed

| File | Why |
|---|---|
| `assets/imagery/corridor-bw.jpg` | Third-party stock from an unrelated WM Studio deck template, standing in for **every** U_CAN news and event image. Components render a labelled placeholder instead — see `guidelines/imagery.card.html`. **`assets/imagery/` is no longer empty:** real pilot-city photography now fills it. |

---

## Not carried over

| Item | Why |
|---|---|
| Metropolis `.woff2` (8 faces, 124 KB) | Built during the font investigation, then superseded when Manrope was chosen. Metropolis has **no Cyrillic**, which is why it was not adopted. |
| `Bahnschrift-Font-Family.zip` | **Not redistributable** — "Microsoft supplied font". Office claim face by local install only, never in a web build. |
| ~~`map_eng_2.png`~~ | **Superseded.** The real artwork was found and is in `assets/maps/` — raster only; the vector is still outstanding. |
| `1_Монтажная область 1.png` (objectives artwork) | **Not present in either project Drive folder.** The name is Illustrator's default Russian-locale artboard export, so it has no searchable keyword. Likeliest explanation: it is already in `assets/illustrations/` under a better name and the task text is stale. Confirm before hunting further. |
| Eight project photographs showing identifiable faces | Consent not on file. See `assets/imagery/project/` above. |

---

## Fonts

`assets/fonts/manrope/` holds 16 `.woff2` files — four weights (400, 500, 700,
800) × four subsets (latin, latin-ext, cyrillic, cyrillic-ext) — plus `OFL.txt`.

**Verified 13 September 2026, and there is a saving here.** Manrope is a
**variable font**: each file carries `fvar wght 200 → 800` with all seven named
instances, and Google Fonts serves the **same bytes** for every weight.
`manrope-400-cyrillic.woff2` and `manrope-700-cyrillic.woff2` are byte-identical
(md5 `e58febde317b69ce`, 14 500 bytes each), and both match Google's file for
weights 200, 400 and 700. **So the sixteen files are four distinct files stored
four times over.**

Splitting by **subset** is right and must stay — a single combined file would
push every English reader to download the full Cyrillic glyph set on first paint.
Splitting by **weight** is pure duplication. Four `@font-face` rules, one per
subset, each declaring `font-weight: 200 800` instead of a point value, would
replace all sixteen and cut the tree by 75 %.

Cyrillic coverage was verified at glyph level, not at declared range:
`Ґ ґ І і Ї ї Є є №` are all present in `manrope-400-cyrillic.woff2` with real
outlines (98 Cyrillic codepoints, 165 glyphs). Note they live in Google's
**`cyrillic`** subset, not `cyrillic-ext` — checking `-ext` first shows all nine
missing and looks like a failure.

---

## Naming

All filenames are kebab-case. German and Ukrainian source names were
transliterated on copy — `Foerderlogo LHD schmal engl auf Farbe.pdf` became
`foerderlogo-schmal-engl-auf-farbe.svg` — because mixed-case names with spaces
and umlauts break on case-sensitive build servers and in URL paths.
