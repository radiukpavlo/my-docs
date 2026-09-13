# U_CAN Design System — Finalization Task List

**Audit date:** 13 September 2026
**Audited state:** 11 components · 37 cards · 2 templates · 131 tokens · 0 registered fonts · 0 starting points
**Purpose:** this file is both a checklist and a *runnable prompt*. Hand any section to an agent
verbatim; each task states the deliverable, the file(s) it touches, and the condition that closes it.

---

## How to use this document

1. Work top-down. Section A gates everything visual; Section B gates everything structural.
2. After every section, run `check_design_system` and fix what it reports before moving on.
3A task is **closed** only when its *Done when* line is objectively true — not when a file exists.
4. Tasks marked 🔴 **need the user**; everything else the agent can complete unaided.
5. Tasks marked 🟡 **were previously believed blocked but are now self-serviceable** from the
   attached `my-docs/` folder. Do these first — they are free wins.

---

## Status correction — three claims in earlier notes are wrong

Fix these in `readme.md` and `SKILL.md` before anything else, because downstream docs repeat them.

| Claimed earlier | Actual |
|---|---|
| 21 components | **21 exports, but only 11 are reusable components** (`components/core/`, flat). The other 10 are UI-kit screens and chrome (`HomeScreen`, `OverviewScreen`, `PilotsScreen`, `NewsScreen`, `WebsiteHeader`, `WebsiteFooter`, `SectionHead`, `DocPage`, `DocumentCover`, `DocumentBodyPage`, `DocumentDetailsPage`) — compositions, not library primitives |
| `ui_kits/templates/` exists | **Does not exist.** Only `website/` and `documents/` |
| Fonts unavailable | Font archives **are** present in `my-docs/03_u_can/U_CAN_Design/` |

**A0.** Draw the line between *library components* and *kit compositions* in `readme.md` and
`SKILL.md`: state 11 components + 10 kit surfaces rather than a flat "21", correct the UI-kit
inventory, and correct the font status.
**Done when:** no document in the project states a count or a path that `list_files` contradicts.

---

## Section A — Typography: close the font gap

The system currently ships **zero** `@font-face` rules (`check_design_system` → `Fonts: (none)`).
`--font-sans` and `--font-claim` resolve to Google Fonts fallbacks loaded over the network.

**A1.** 🟡 Extract `my-docs/03_u_can/U_CAN_Design/avenir-next-similar-fonts.zip` and
`Bahnschrift-Font-Family.zip`. Inventory every face inside: family name, weight, style, format,
and the actual licence file if the archive carries one.
**Done when:** an inventory table exists in `guidelines/` or `readme.md` naming each usable face.

**A2.** 🔴 **Licence decision — the single most important open question in the project.**
Bahnschrift is a Windows-bundled font and Avenir Next is a commercial Linotype face; neither is
generally web-licensable, and a "similar fonts" archive is by definition *not* Avenir Next.
Ask the user to choose one of three paths and record the answer:
- **(a) Real licence:** they hold a webfont licence → they supply `.woff2` for Regular 400 + Bold 700.
- **(b) Sanctioned substitute:** name the face their comms team uses (Nunito Sans, Mulish, Figtree,
  Barlow, Archivo, DIN Next) → it becomes the *declared* brand font, not a silent fallback.
- **(c) Status quo:** keep the fallback stack and document it as a known deviation.
**Done when:** `tokens/fonts.css` names the decision in a comment and `readme.md` has a
"Typography licence" section stating which path was taken and by whom.

**A3.** Self-host whatever A2 selects. Create `assets/fonts/`, write `@font-face` rules into
`tokens/fonts.css` with `font-display: swap`, correct `unicode-range`, and `format("woff2")`.
The Google Fonts `@import` and the Nunito Sans / Barlow Semi Condensed substitutes have already
been removed — the tokens now declare the real families and fall through to the platform stack.
**Done when:** `check_design_system` reports the fonts (it currently reports `Fonts: (none)`, and
the two font notices it raises are upload prompts that clear only when binaries land).

**A4.** 🔴 **Cyrillic coverage.** The source `.potx` falls back to `Noto Sans SC` — a *Chinese*
face — for non-Latin runs. This is certainly wrong, and U_CAN publishes in Ukrainian.
Establish the Cyrillic stack, add a `--font-sans-cyr` token if the Latin face lacks coverage, and
write a bilingual specimen card showing the same paragraph in EN and UA at three sizes.
**Done when:** `guidelines/type-cyrillic.card.html` exists and no Ukrainian string in the system
renders in a CJK face.

**A5.** Add the missing type specimens: tabular/lining numerals, small-caps or all-caps tracking
rule, long-form measure (characters per line) for the document kit, and a "type in the wild"
card showing a real paragraph from `U_CAN_Technical_Report_B.txt` at document scale.
**Done when:** the Type group has a specimen for every style the two templates actually use.

---

## Section B — Colour: resolve the ambiguity and fill the semantic holes

**B1.** 🔴 **The yellow.** `Template_Presentation.potx` uses `#FFCC00` on slide 5 and `#FFC000`
on slide 4 for the identical reversed-title role. Both are currently tokenised
(`--ucan-yellow`, `--ucan-yellow-alt`). One must win.
Recommend `#FFCC00` — it is the exact EU emblem yellow, so it keeps brand and funder aligned.
**Done when:** one token is canonical, the other is either deleted or explicitly documented as
"legacy, do not use in new work", and no card shows both as equal options.

**B2.** Add the **semantic state colours** the system entirely lacks: success, warning, error,
info — each with a foreground, a background tint, and a border value, all derived from the U_CAN
palette rather than invented (use `oklch()` to stay in family).
**Done when:** `tokens/colors.css` exposes the four states and a `colors-states.card.html` shows
each with its three roles.

**B3.** Run a **WCAG contrast audit** across every foreground/background pair the system permits —
in particular navy-on-teal, white-on-teal, navy-on-yellow, and white-on-yellow, which are the
combinations the deck template invites. Body text needs 4.5:1; headline-scale type may sit at 3:1.
**Done when:** `guidelines/colors-pairings.card.html` prints the measured ratio next to every
pair and flags the failing ones as forbidden, with a compliant alternative named.

**B4.** Define **link colours** — default, visited, hover, focus-visible — in `tokens/base.css`.
Currently undefined, so any link a user adds in the editor renders browser-default blue.
**Done when:** `a`, `a:hover`, `a:visited`, `a:focus-visible` are styled from palette tokens.

**B5.** Decide the **dark-mode question** explicitly: either implement a `prefers-color-scheme`
token layer, or document in `readme.md` that the system is light-only by design (defensible for a
print-and-deck-led identity). Do not leave it unanswered.
**Done when:** `readme.md` states the position and, if implemented, every card renders in both.

---

## Section C — Tokens: the scales that are missing

131 tokens exist, but several dimensions a consuming project will immediately reach for are absent.

**C1.** **Breakpoints.** The website kit is responsive in practice but tokenises no breakpoints.
Add `--bp-sm/md/lg/xl` and document the intended behaviour at each.

**C2.** **Container widths / measure.** Add max-width tokens for the text column, the wide content
column, and the full-bleed band used by the deck and website kits.

**C3.** **Z-index scale.** Add a named ladder (base, raised, sticky, overlay, modal, toast) so
consumers stop inventing `9999`.

**C4.** **Opacity / scrim scale.** The image-text slide and the website hero both need a legible
scrim over photography; no token governs it.

**C5.** **Table tokens.** `MetaTable` is a shipped component but table row height, zebra tint,
header weight, and border colour are hard-coded inside it.

**C6.** **Print tokens.** The document kit is print-led; add page margin, running-header height,
and a print-safe ink colour (pure navy, not a tinted mix).

**Done when (C1–C6):** each scale is in `tokens/`, imported through `styles.css`, and has a card
in the Spacing or a new Layout group. `check_design_system` token count rises accordingly.

---

## Section D — Components: the library is a third of the way built

Existing (11 library components): `BandHeading`, `Button`, `Card`, `FundingNotice`, `LeafRule`,
`LogoLockup`, `MetaTable`, `ObjectiveItem`, `Panel`, `Tag`, and one more in `components/core/`.
Every one follows a good three-file pattern (`.jsx` + `.d.ts` + `.prompt.md`) — **keep that pattern
for every addition below.** The 10 UI-kit exports are compositions and are covered in Section I.

**D1.** **Restructure into concern-based directories.** All 11 library components sit flat in
`components/core/`, which is why the Components group renders a single lumped card. Split into
`components/core/`, `components/forms/`, `components/feedback/`, `components/navigation/`,
`components/layout/`, `components/content/`.
⚠️ Each directory needs its **own** `@dsCard`-tagged `.html` or it contributes no thumbnail.
**Done when:** `check_design_system` reports one card per component directory and the Components
group shows distinct thumbnails.

**D2.** **Forms** — none exist, and the website kit has a contact page. Build: `TextField`,
`Textarea`, `Select`, `Checkbox`, `Radio`, `FieldGroup` (label + hint + error), `Fieldset`.
Each needs rest / hover / focus-visible / disabled / invalid states.

**D3.** **Feedback** — build `Alert` (using the B2 state colours), `Badge`/`StatusPill`,
`ProgressBar` (WP completion is a recurring U_CAN visual), `EmptyState`, `Skeleton`.

**D4.** **Navigation** — `WebsiteHeader`, `WebsiteFooter` and `SectionHead` exist but live inside
`ui_kits/website/WebsiteChrome.jsx`, so they are kit-specific rather than library primitives.
Promote them into `components/navigation/` with proper `.d.ts` + `.prompt.md`, then build the
missing ones: `Breadcrumb`, `Pagination`, `TabBar`, `Anchor/SkipLink`.

**D5.** **Content** — build `Stat`/`KPI`, `Quote`/`Pullquote`, `Timeline` (the project runs on
milestones — MS6 etc.), `Accordion`/`FAQ` (the Khmelnytskyi Pilot QA is literally Q&A), `DataTable`,
`Figure` + `Caption` (reports are figure-heavy), `PersonCard` (speakers' bios are a recurring need).

**D6.** **Layout** — extract `Band`/`Section`, `Grid`, `Stack`, `PageHeader`, `CoverBlock` from the
patterns currently duplicated across the kits and slides.

**D7.** **Audit the 11 existing components** for API consistency: prop naming convention, whether
every prop in `.d.ts` is actually read, whether every hard-coded value should be a token, and
whether `as`/`className` escape hatches exist. Fix drift.

**D8.** **Interaction-state completeness pass.** Every interactive component must define hover,
active, focus-visible, disabled, and loading where applicable — plus honour
`prefers-reduced-motion`. `guidelines/motion-hover.card.html` covers hover only.

**Done when (D2–D6):** each new component has `.jsx` + `.d.ts` + `.prompt.md`, appears on
`window.UCANDesignSystem_a2b226`, and is demonstrated in its directory's card.

---

## Section E — Templates: two exist, the project needs eight

`templates/deck/` and `templates/report/` are solid and extracted verbatim from source. The
knowledge base shows what else U_CAN produces daily — each is a template-shaped hole.

**E1.** `templates/deliverable/` — from `source/Template_Deliverable.docx`. A formal EU deliverable
has a mandated cover (deliverable number, WP, lead beneficiary, dissemination level, due vs actual
date), a revision-history table, and an executive summary. None of this is in the report template.

**E2.** `templates/wp-status/` — from `U_CAN_WP_Template.pptx` and
`Prompt_Create-Slides_WP4_system.md`. The recurring WP status/monthly-progress deck.

**E3.** `templates/conference-report/` — from `Prompt_Conference-Report_system.txt` and
`MS6_Conference_Report.txt`.

**E4.** `templates/speech-script/` — from `Prompt_Make-Speech-Script.txt` and the four
`Speech_*.txt` files. A distinct typographic problem: large type, breath marks, timing cues.

**E5.** `templates/speakers-bio/` — from `MS6_Speakers_Bio.docx`. Uses the D5 `PersonCard`.

**E6.** `templates/invitation-email/` — from `Prompt_Conference-Invitation-Email.txt`.
Must be a send-ready single-file HTML email (table layout, inline styles, no webfonts).

**E7.** `templates/pilot-report/` — from `Prompt_Annual-Pilot-Report.txt` and
`KhNU_Annual_Pilot_Report_2025-2026.txt`.

**E8.** `templates/timesheet/` — from `Prompt_Timesheets.txt` and `KhNU_Monthly_Progress_Tracker.xlsx`.
A dense, print-first, form-shaped layout the system has no precedent for.

**E9.** `templates/poster/` or `templates/one-pager/` — a single-sheet project summary for
conferences. No precedent in source; confirm need with the user before building. 🔴

**Done when (E1–E8):** each is `templates/<slug>/<Slug>.dc.html` with the `@template` comment on
line 1 of the template body, a sibling `ds-base.js`, and it previews correctly styled.
**Rule:** templates are Design Components written with `dc_write`, inline styles only — never
`write_file` on a `.dc.html`, never a stylesheet or CSS class inside one.

**E10.** **QR-code variant.** `Template_Presentation_QRcode.potx` is a distinct source template
not yet processed — decide whether it is a deck variant (a Tweak on `templates/deck/`) or its own
template, then implement.

---

## Section F — Slides vs deck template: resolve the duplication

`slides/01-title` … `06-closing` are six standalone `@dsCard` HTML files. `templates/deck/Deck.dc.html`
is the copy-and-go deck. These overlap and can drift apart.

**F1.** Decide the relationship: either the `slides/` files become *specimens generated from* the
deck template's layouts, or the deck template's layouts are *authored from* the slides and the
duplication is documented as intentional. Pick one and make the code reflect it.

**F2.** **Mine the real decks for archetype frequency.** `U_CAN_Knowledge-base/Reference/` holds
ten real PDFs (consortium slides, monthly slides, WP4 status, MS6 presentation). Read them and
count: how often do section breaks appear, what is the real bullet density, how often do tables
and charts dominate, is there a standard agenda slide, a standard partner-logos slide, a standard
"next steps" slide?
**Done when:** the deck template's layout set matches how U_CAN actually presents, with the
evidence recorded in `slides/README.md`.

**F3.** Add the archetypes F2 reveals that are missing. Likely: agenda/contents, table-heavy,
chart-heavy, quote, two-column comparison, partner-logo wall, milestone timeline, thank-you +
contacts, Q&A.

**F4.** **Speaker-notes convention.** Real U_CAN decks are delivered as speeches (four speech
scripts in the source). Document whether the deck template carries notes and in what format.

---

## Section G — Data visualisation: completely undefined

**G1.** 🔴 Ask for U_CAN's chart conventions — which blues in series order, gridline policy,
whether axes are labelled, legend placement. The templates define none.

**G2.** Build the chart specimen set once G1 lands: bar, stacked bar, line, donut, and the
WP-progress bar the project uses constantly. Define a categorical series palette (5–7 steps,
contrast-checked against each other, not just against the background) and a sequential ramp.
**Done when:** `guidelines/charts-*.card.html` covers series colour, gridlines, labels, and
the accessibility rule (never colour alone — pattern or direct label).

**G3.** Add a **map** convention. Six pilot cities on a Ukraine map is the project's signature
graphic; the system should specify how it is drawn, not just reference a missing PNG.

---

## Section H — Assets: what is missing, and what can now be recovered

**H1.** 🟡 **Copy the EU logo trees that previously failed.** `my-docs/03_u_can/U_CAN_Design/Logos/EU logos/`
contains `EN_horizontal`, `EN_vertical`, `UA_horizontal`, `UA_vertical` — the Ukrainian and vertical
variants earlier reported as un-copyable are present. Copy them into `assets/logos/` and card them.

**H2.** 🟡 **Copy the partner logo trees.** `LHD/LHD Förderlogo/` (9 variants incl. negative and
narrow) and `LHD/LHD Logo Stadverwaltung/` (3 variants) are present locally.

**H3.** 🔴 **Resolve which LHD logo applies.** Is Landeshauptstadt Düsseldorf a **funder**
(→ Förderlogo) or a **partner** (→ Stadtverwaltung logo)? Both sets exist; the rule does not.

**H4.** 🟡 **Copy the remaining brand graphics:** `Footer graphics.png`, `Ppt footer.png`,
`Zoom wallpaper.png`, `U_CAN FB banner transparent.png`, `U_CAN Logo square.png`. Several are not
in `assets/` yet. The Zoom wallpaper and FB banner also imply a **social/virtual-presence** card
the system does not have.

**H5.** 🔴 **SVG logo master.** Only rasters are in `assets/logos/`. The `.ai` files
(`U_CAN_V3_final.ai`, `U_CAN_V3_final_Black-White.ai`) exist locally but cannot be parsed here —
ask for an **SVG export**. This is why `thumbnail.html` sets the wordmark in type instead of using
the mark.

**H6.** 🔴 **Reversed and stacked lockups.** No white-on-transparent version and no vertical
lockup exist. Both are needed — the deck's navy title slide has nowhere to put a dark logo.

**H7.** 🔴 **The pilot-cities map** (`map_eng_2.png`) and the **objectives artwork**
(`1_Монтажная область 1.png`). Both are bespoke graphics currently rendered as labelled blanks.

**H8.** 🔴 **Real photography.** The only photo in the system is `assets/imagery/corridor-bw.jpg`
— a black-and-white stock image from the third-party WM Studio deck template, now standing in for
*every* news and event thumbnail. Request 6–10 real project photos plus the six pilot-city heroes.
Until then, replace it with honest placeholders rather than misleading stock.
**Done when:** no third-party stock image appears anywhere in the system, and a
`guidelines/imagery.card.html` states the photographic style (warm/cool, candid/formal, colour/mono).

**H9.** 🔴 **Icon set.** The source materials contain **zero** icons. Either the user names an
existing set, or document Lucide as the sanctioned choice and build an icon card with sizes,
stroke weight, and alignment rules. `guidelines/brand-no-icons.card.html` records the absence but
does not resolve it.

**H10.** **Asset hygiene.** Cross-check against `U_CAN_Knowledge-base/08_Asset_Index.md`, confirm
every file in `assets/` is referenced somewhere, delete orphans, normalise filenames to
kebab-case, and record provenance (source file + licence) for each in a manifest.

**H11.** **Decide the fate of `source/`.** Four binaries (`.potx`, `.docx`×2, `.pptx`) sit in the
repo. Keep as provenance or remove for weight — either way, say so in `readme.md`.

---

## Section I — UI kits: one is honest, one is thin, one is missing

**I1.** 🔴 **The website kit is a recreation, not a match.** `ui_kits/website/` applies the deck
template's visual language to the real site's copy and navigation, because the live site is a Wix
build with no accessible design source. Request full-page screenshots (desktop **and** mobile) or a
Figma file for: Home, Project Overview, Pilot Cities, News, a single news post, Contacts — then
rebuild against them.
**Done when:** either the kit matches supplied references, or `ui_kits/website/README.md` states
plainly at the top that it is an interpretation and names what would be needed to make it exact.

**I2.** **Complete the website kit's screens.** Present: Home, Overview, Pilots, News. Missing:
single news post, Contacts (needs Section D2 forms), Consortium/Partners, Work Packages,
Publications, Events, plus a 404 and a search-results state.

**I3.** **Responsive proof.** Add mobile and tablet renderings for each screen. The kit currently
demonstrates desktop only, and the site's real traffic is mobile-heavy.

**I4.** **Thicken the documents kit.** `ui_kits/documents/` is one `.jsx` and one `index.html`.
It needs: deliverable cover, report cover, running header/footer with pagination, a table of
contents, a figure-and-caption spread, a table spread, an annex page, and the EU funding-disclaimer
placement on each.

**I5.** **Build `ui_kits/templates/` or stop claiming it.** It is referenced in project notes and
does not exist. Either build a template-picker surface showing all Section E templates, or remove
every reference.

**I6.** **Accessibility pass on both kits.** Landmark elements, heading order, skip link, visible
focus, alt-text policy, `lang` attributes on Ukrainian strings, 44px minimum hit targets.

---

## Section J — System-level completeness

**J1.** **Starting points.** `check_design_system` reports `Starting points: (none)`. Define them —
they are how a consuming project begins. At minimum: blank deck, blank report, blank web page.

**J2.** **Project thumbnail review.** `thumbnail.html` renders at ~72×48px. Verify it follows the
tile rules (brand colour main area + flush swatch strip, lightest→darkest, no neutrals, no
components) and swap the type-set wordmark for the real mark once H5 lands.

**J3.** **Adherence rules.** `_adherence.oxlintrc.json` is auto-generated. Confirm it actually
forbids what matters: raw hex outside `tokens/`, hard-coded px where a spacing token exists,
non-token font families.

**J4.** **A kitchen-sink QA page.** One page rendering every component in every state and every
token scale, so regressions are visible in a single screenshot. Not a card — a test surface.

**J5.** **Contribution + naming guide.** Document the three-file component pattern, the `@dsCard`
comment format, the template folder contract, the inline-styles-only rule for `.dc.html`, and the
token-naming convention. Anyone adding a component should not have to reverse-engineer it.

**J6.** **Versioning and changelog.** Add `CHANGELOG.md` and a version token. A design system
consumed by other projects needs a way to say what changed.

**J7.** **Usage-obligations doc.** Consolidate the non-negotiables: EU funding statement wording
and placement, logo clear space and minimum size, co-branding order, disclaimer text. These carry
legal weight under the grant agreement — they should be one authoritative page, not scattered cards.

**J8.** 🔴 **Co-branding rules.** Unresolved: which partner logos must appear and on what surfaces;
whether the TU Dresden + U_CAN footer band or the plain U_CAN band is default (both exist, no rule);
whether the Ukrainian-language "Funded by the EU" emblem is required.

**J9.** **Tone of voice, extended.** Guidelines cover tone; add the mechanical rules — how the
project name is written (`U_CAN`, never `UCan`/`U-CAN`), the claim line's exact wording and
capitalisation, date and number formats, how partner and city names are rendered in both languages.

**J10.** **Ukrainian/English bilingual policy.** Beyond type (A4): which surfaces are bilingual,
whether they are side-by-side or separate documents, and how language switching works on the site.

---

## Section K — Verification before hand-off

**K1.** Run `check_design_system` until the only remaining issues are ones the user has explicitly
accepted. Target: zero.

**K2.** Open every one of the cards and confirm each renders with no console error and no missing
asset. Cards that reference a not-yet-supplied asset must show a labelled placeholder, not a broken
image.

**K3.** Confirm no card loads a raw `.jsx`/`.tsx` via `<script src>` — cards must load
`_ds_bundle.js` and read from `window.UCANDesignSystem_a2b226`.

**K4.** Print-test both document templates and the deck at Letter **and** A4. The project is
German- and Ukrainian-facing, so A4 is the real default.

**K5.** Consume the system from a scratch project: copy `templates/deck/`, point `ds-base.js` at
the bound `_ds/` tree, and confirm it renders styled with no edits beyond that one line. This is
the only test that proves the system actually works for its audience.

**K6.** Regenerate `readme.md` so its inventory matches reality, and re-run A0's consistency check.

---

## Consolidated blocker list — what only the user can answer

Nine questions. Everything else in this document can proceed without them.

1. **Font licence path** (A2) — real licence, named substitute, or accept the fallback?
2. **The yellow** (B1) — `#FFCC00` or `#FFC000`?
3. **Cyrillic font** (A4) — what replaces the erroneous `Noto Sans SC` fallback?
4. **Icon set** (H9) — do you have one, or shall I sanction Lucide?
5. **Logo SVG + reversed + stacked lockups** (H5, H6).
6. **Map, objectives artwork, and real photography** (H7, H8).
7. **LHD: funder or partner?** (H3) — which of the two logo sets applies.
8. **Co-branding rules** (J8) — which logos, which surfaces, which footer band, UA emblem or not.
9. **Website design source** (I1) — screenshots or Figma, or accept the kit as an interpretation.

**Nice-to-have, sharpens everything:** one real finished deck and one real finished deliverable
(any WP, any version), plus your chart conventions (G1).

---

## Suggested order of work

| Phase | Sections | Rationale |
|---|---|---|
| 1 | A0, A1, H1, H2, H4 | Free wins from the attached folder; fixes false claims |
| 2 | Blocker list to user | Everything below partly depends on these answers |
| 3 | B, C | Tokens gate every component |
| 4 | D | Components gate every template and kit |
| 5 | E, F | Templates are the actual deliverable for most users |
| 6 | G, I | Charts and kits build on components |
| 7 | H remainder, J | Assets and system docs |
| 8 | K | Verification |

**Total: 9 user decisions, ~70 agent tasks.**
