# U_CAN Design System — remaining work to finalisation

**Written:** 13 September 2026
**Against:** design system v0.2.0 (`a2b22667-6793-404e-821b-d5219760fa3b`)
**Supersedes the open items in:** `DESIGN-TASKS.md`, `DESIGN-FINDINGS.md`, `TODO-for-you.md`

---

## How to use this document

This is both a checklist and a **runnable prompt**. Hand any section to an agent
verbatim. Every task states what to do and the condition that closes it.

1. **Section V first.** It is verification that has never been run. Until it
   passes, every claim below it is unconfirmed — including the claim that the
   system currently works at all.
2. **Section R second.** These are regressions and risks introduced by the
   v0.2.0 pass itself. They are cheap to check and expensive to discover later.
3. Then work A → L in any order that suits.
4. A task is **closed** only when its *Done when* line is objectively true — not
   when a file exists.
5. 🔴 = needs the user. 🟠 = risk or suspected defect. 🟢 = agent can complete unaided.

### What changed in v0.2.0, in one paragraph

42 library components across six concern directories; 10 templates; 12 token
files; Manrope self-hosted for Latin + Cyrillic; Lucide sanctioned; semantic
state colours; a measured contrast matrix; the EU/LHD/Cities-Mission logo trees;
vector logo masters plus a derived reversed lockup. Four brand decisions were
taken by the project owner. Seven real accessibility defects were fixed. The
full record is in `CHANGELOG.md`.

### The honest headline

**Nothing in v0.2.0 has been visually verified.** No browser was available in the
session that built it, `check_design_system` was not reachable, and the templates
were written through `write_files` rather than `dc_write`. The work is
internally consistent and every numeric claim in it was machine-checked — but
"it renders" is currently an assumption, not a finding.

---

## Section V — Verification that has never been run

**This section gates everything else.** Do it first.

**V1.** 🟢 Run `check_design_system`. Fix everything it reports.
**Done when:** it returns zero issues, or the only remaining ones are on a written
accepted-deviations list in `readme.md`.

**V2.** 🟠 **Confirm the bundle recompiled after the D1 restructure.** Five
components moved out of `components/core/` into `layout/` and `content/`, and
three moved out of `ui_kits/website/WebsiteChrome.jsx` into
`components/navigation/`. If the compiler has not re-run, `_ds_bundle.js` still
points at deleted files and **every card and kit page will fail to render.**
**Done when:** all 42 components resolve on `window.UCANDesignSystem_a2b226`, and
`qa/kitchen-sink.html` shows no "Not exported from the bundle" banner.

**V3.** 🟢 Open **every** card in `guidelines/` and `components/*/`. Confirm each
renders with no console error and no missing asset.
**Done when:** every card renders; any card referencing a not-yet-supplied asset
shows a labelled placeholder, never a broken image.

**V4.** 🟢 Confirm no card loads a raw `.jsx`/`.tsx` via `<script src>`. Cards
must load `_ds_bundle.js` and read from the namespace.
**Done when:** a grep for `script src=.*\.jsx` across the project returns nothing.

**V5.** 🟠 **Open all 10 templates in the editor.** The eight new ones were
written with `write_files`, not `dc_write`, so the Design Component runtime has
never validated them. Check the `<x-dc>` wrapper, the `@template` comment on line
1 of the template body, and the `<helmet>` block.
**Done when:** each of the 10 previews correctly styled, and each is editable.

**V6.** 🟢 **Print-test at A4 and Letter:** `report`, `deliverable`,
`pilot-report`, `conference-report`, `speakers-bio`, and `timesheet` (which is
**landscape** A4 — verify it does not silently rotate or clip).
**Done when:** no content is clipped at either size, running headers and page
numbers land correctly, and `@page :left`/`:right` margins alternate as intended.

**V7.** 🟢 **Consume the system from a scratch project.** Copy `templates/deck/`,
point the single `base` line in `ds-base.js` at the bound `_ds/` tree, and confirm
it renders fully styled with no other edit. Repeat for `templates/deliverable/`.
**Done when:** both render correctly with exactly one line changed. *This is the
only test that proves the system works for its actual audience.*

**V8.** 🟢 **Kitchen-sink baseline.** Screenshot `qa/kitchen-sink.html` at 1280px
and at 400px. Then tab through the entire page.
**Done when:** a baseline screenshot pair is committed for future diffing; nothing
overflows horizontally at 400px; **every** interactive element shows a visible
focus ring; the error bar at the foot of the page stays hidden.

**V9.** 🟠 **Verify the SVG logo masters render in a browser** — not in a
converter preview. There is a recorded precedent here: an earlier conversion
produced a 660 KB file that Chrome refused to load at all while the converter's
own preview showed it as fine. Check `u-can-logo-colour.svg`,
`u-can-logo-bw.svg` and `u-can-logo-reversed.svg`.
**Done when:** all three render correctly in Chrome **and** Firefox, at 110 px
wide and at 600 px wide.

**V10.** 🟠 **Verify Manrope's Cyrillic at glyph level, not at declared range.**
The shipped subsets *declare* U+0490–0491 and U+2116 in their `unicode-range`;
the glyph tables inside the compressed `.woff2` were never inspected because no
tooling was available.
**Done when:** `Ґ ґ І і Ї ї Є є №` all render in Manrope — not in a fallback face —
verified with the browser's font inspector on
`guidelines/type-cyrillic.card.html`.

---

## Section R — Regressions and risks introduced by v0.2.0

**R1.** 🟠 **`Radio` is exported twice.** `components/forms/Checkbox.jsx` exports
both `Checkbox` and `Radio`; `components/forms/Radio.jsx` re-exports `Radio` from
it. If the bundler collects named exports from every `.jsx`, the same name is
registered from two modules.
**Fix:** either delete `Radio.jsx` and document that `Radio` lives in
`Checkbox.jsx`, or move the implementation into `Radio.jsx` and have `Checkbox.jsx`
re-export nothing.
**Done when:** each exported component name originates from exactly one module.

**R2.** 🟠 **`components/forms/_field.jsx` is not a component.** It exports
`fieldBase`, `fieldState` and `useFieldState` — a shared style contract. If the
compiler treats every `.jsx` under `components/` as a component, it will try to
register three non-components.
**Fix:** confirm the underscore prefix excludes it; if not, move it to a
non-scanned location.
**Done when:** `_field` does not appear in the namespace or in any card.

**R3.** 🟠 **Cross-screen import in the website kit.** `PilotsScreen.jsx` and
`NewsScreen.jsx` both import `ImageSlot` from `HomeScreen.jsx`. That makes
`HomeScreen` a dependency of screens that have nothing to do with it.
**Fix:** promote `ImageSlot` to `components/content/` as a proper three-file
component — it is a real, reusable placeholder pattern and other kits will want it.
**Done when:** no kit screen imports from another kit screen.

**R4.** 🟢 **`support.js` is duplicated 10 times** — roughly 69 KB per template
folder, ~690 KB total. This is the shipped pattern, so it may be intentional.
**Done when:** either a note in `guidelines/contributing.md` records that the
duplication is deliberate and why, or the templates share one copy.

**R5.** 🟠 **Audit every reference to the five deleted component paths.**
`components/core/{Card,Panel,MetaTable,ObjectiveItem,BandHeading}.*` were removed.
The five kit files were repointed, but `slides/*.html`, `templates/deck/`,
`templates/report/` and the 28 legacy guideline cards were **not** checked.
**Done when:** a project-wide grep for `components/core/(Card|Panel|MetaTable|ObjectiveItem|BandHeading)` returns nothing.

**R6.** 🟠 **`assets/imagery/` is now empty.** `corridor-bw.jpg` was deleted.
**Done when:** no file in the project requests anything from `assets/imagery/`,
and no card shows a broken image.

**R7.** 🟠 **`--ucan-yellow-alt` is deprecated but may still be in use.**
**Done when:** a project-wide grep finds it only in `tokens/colors.css`.

**R8.** 🟠 **`--ucan-grey` is now non-text-only.** Confirm nothing sets it as a
text colour anywhere — especially anything rendering the EU funding disclaimer,
which is legally required to be legible.
**Done when:** no `color:` declaration resolves to `--ucan-grey` or `#808080`.
*Known offenders are listed as E4 and F4 below.*

**R9.** 🟢 **`--ds-version` was added to `tokens/base.css` but nothing reads it.**
**Done when:** it is surfaced somewhere a consumer can see it — the readme
inventory, the thumbnail, or `check_design_system` output.

**R10.** 🟢 **Duplicate LHD assets.** `assets/logos/partners/` holds four files
that duplicate two of the eleven in `assets/logos/lhd/`. They were kept because
`guidelines/brand-partners.card.html` still points at them.
**Done when:** that card points at `assets/logos/lhd/` and `assets/logos/partners/`
is deleted.

---

## Section A — Typography, remaining

**A1.** 🔴 **The claim line loses its character off Windows.** `--font-claim` is
`Bahnschrift → DIN Next → Segoe UI Variable → Manrope`. Bahnschrift is not
web-licensable and both DIN fallbacks are commercial, so on macOS, Linux, Android
and iOS the claim line — *"Ukraine towards Carbon Neutrality"*, the most-repeated
string in the brand — silently renders in Manrope and loses the condensed DIN
look entirely.
**Decide:** adopt a licensable condensed/DIN-adjacent face for web (Archivo
Narrow, Barlow Condensed, Saira Condensed — all OFL), or accept that the claim
line is Manrope everywhere except Office and say so.
**Done when:** `tokens/fonts.css` names the decision in a comment and
`guidelines/type-claim-face.card.html` shows the real rendering on a non-Windows
machine.

**A2.** 🟢 **`--weight-medium: 600` is synthesised.** Manrope ships 400/500/700/800;
600 is interpolated by the browser. It is currently used for table headers.
**Fix:** either ship the real Manrope 600 subset files, or repoint
`--weight-medium` at 500 (`--weight-label`) or 700.
**Done when:** no token resolves to a weight the shipped files do not contain.

**A3.** 🟢 **Confirm Manrope 800 is used.** Four weights were shipped; 800 may be
dead weight (64 KB across four subsets).
**Done when:** either something uses it, or the four 800 files are removed and
`tokens/fonts.css` updated.

**A4.** 🟢 **Finish task A5 from the original list.** Specimens exist for
numerals, all-caps tracking, measure and weights. What was never done is the
*audit*: enumerate every run style actually used in `Template_Presentation.potx`
and `Template_Report.docx`, and confirm the Type group has a specimen for each.
**Done when:** a table in `guidelines/type-specimens.card.html` maps every source
run style to its specimen, with no gaps.

**A5.** 🔴 **The Office templates and the web system now use different fonts.**
The `.potx`/`.docx` keep Bahnschrift + Calibri; the web system is Manrope. That is
defensible (licensing), but it means a deck and a web page for the same event do
not match.
**Decide:** update the Office templates to Manrope (it is OFL — it can be
installed and embedded), or document the divergence as accepted.
**Done when:** `readme.md` states the position under "Typography licence".

**A6.** 🟢 **Bilingual specimen at deck scale.** `type-cyrillic.card.html` shows
EN/UA at document scale only. Ukrainian runs 10–15% longer, which bites hardest
on a 32px slide title inside a fixed-width 587px band.
**Done when:** the card shows a slide-scale EN/UA pair in the real band geometry,
demonstrating what happens when the Ukrainian title overflows.

---

## Section B — Colour, remaining

**B1.** 🟠 **Audit the 28 legacy guideline cards against the new palette.** Cards
like `colors-neutral`, `colors-primary`, `colors-accent`, `colors-field-tints`
and `colors-eu` were written before `--ucan-slate` existed and before the
forbidden-pairings list. Some may still present `--ucan-grey` as a text colour or
show pairings now known to fail.
**Done when:** no card contradicts `guidelines/colors-pairings.card.html`, and any
card showing a failing pair labels it as forbidden.

**B2.** 🟢 **Audit the `.on-dark` / `data-surface="dark"` convention** across all
42 components. `Panel`, `Band`, `BandHeading`, `PageHeader` and `CoverBlock` set
it. Others that can legitimately sit on a navy band may not.
**Done when:** every component that can appear on a dark surface either sets the
attribute or documents that it must be wrapped in one that does.

**B3.** 🟢 **Set a removal date for `--ucan-yellow-alt`.**
**Done when:** the deprecation comment names the version it will be deleted in.

**B4.** 🟢 **Document that `--ucan-yellow` and `--eu-yellow` are intentionally the
same value.** Both are `#FFCC00`. A future maintainer will otherwise "de-duplicate"
them and break the EU emblem alignment.
**Done when:** `tokens/colors.css` says so explicitly.

**B5.** 🟢 **Re-affirm or revisit the light-only position** once real photography
lands, since photo-led surfaces are where dark mode usually starts to matter.
**Done when:** `readme.md`'s dark-mode section carries a review date.

---

## Section C — Tokens, remaining

**C1.** 🟠 **Raw hex is pervasive in the templates and slides.** `Deck.dc.html`
alone hard-codes `#00305E`, `#75B23C`, `#0463CD`, `#FFCC00`, `#BAD99E` and
`#808080`. `Report.dc.html` and the six `slides/*.html` are the same.
**Fix:** replace with `var(--token, #fallback)` — the fallback matters, because
`.dc.html` files must still render if the stylesheet has not loaded.
**Done when:** no `.dc.html` or slide file contains a bare hex value except as a
`var()` fallback.

**C2.** 🟢 **Confirm `_adherence.oxlintrc.json` forbids what matters** (original
task J3 — never done). It is auto-generated and was never inspected.
**Done when:** it demonstrably flags: raw hex outside `tokens/`, hard-coded px
where a spacing token exists, and non-token font families. Verify by introducing
each violation deliberately and confirming it is caught.

**C3.** 🟢 **Verify the token count** reported by `check_design_system` matches
the twelve files, and that `@kind` annotations are present on every non-colour
token.
**Done when:** the reported count is explained in `readme.md`.

---

## Section D — Components, remaining

**D1.** 🟠 **Four original components were never audited.** The D7 pass covered
`Button`, `Card`, `Panel`, `BandHeading`, `ObjectiveItem` and `MetaTable`.
**`Tag`, `LogoLockup`, `FundingNotice` and `LeafRule` were not opened.**
Check each for: hard-coded values that should be tokens, missing focus-visible,
props declared in `.d.ts` but never read, and `--ucan-grey` used as text.
**Done when:** all four have been read and either fixed or confirmed clean in
writing.

**D2.** 🟠 **`FundingNotice` is the highest-risk of those four.** It renders the
legally required EU disclaimer. If it sets `--ucan-grey`, the disclaimer is at
3.95:1 and fails WCAG AA.
**Done when:** it uses `--text-legal`, and the card proves the ratio.

**D3.** 🟢 **Finish the D8 interaction-state pass.**
`guidelines/motion-hover.card.html` still covers hover only.
**Done when:** it covers hover, active, focus-visible, disabled and loading, and
demonstrates the `prefers-reduced-motion` behaviour.

**D4.** 🟢 **Build the components the kits will hit next.** Not speculative — each
is implied by a screen already listed as outstanding:
`Dialog`/`Modal` (cookie consent, newsletter), `Tooltip` (chart affordances),
`Toast` (form submission), `Menu`/`Dropdown` (language switch),
`Avatar` (partner and speaker lists), `Divider`, `Stepper` (pilot progress),
`FileUpload` (deliverable submission).
**Done when:** each has `.jsx` + `.d.ts` + `.prompt.md`, appears in its directory
card, and is added to `qa/kitchen-sink.html`.

**D5.** 🟠 **Chart components do not exist.** `guidelines/charts-conventions.card.html`
specifies a series ramp, gridline policy and labelling rules — but the only
chart-shaped component in the system is `ProgressBar`. Everything else is a
document.
**Build (after G1 approval):** `BarChart`, `StackedBarChart`, `LineChart`,
`DonutChart`, `WPProgressGroup`.
**Done when:** each reads its colours from `tokens/charts.css`, renders
`role="img"` with a finding-stating `aria-label`, direct-labels by default, and
is demonstrated in a card.

**D6.** 🔴 **`UkraineMap` component.** Blocked on the artwork (H2).
**Done when:** it renders the six pilot cities from a data prop, meets every rule
in `guidelines/charts-map.card.html`, and degrades to a labelled placeholder when
no geometry is supplied.

**D7.** 🟢 **`ImageSlot` promotion.** See R3.
**Done when:** `ImageSlot` is a three-file component under `components/content/`, shown in the content card, and no kit screen imports from another kit screen.

---

## Section E — Templates, remaining

**E1.** 🟠 **The eight new templates have no `.thumbnail`.** `templates/deck/` and
`templates/report/` each have one; the new folders do not, so they will show no
preview.
**Done when:** all 10 template folders have a `.thumbnail`.

**E2.** 🟠 **`templates/report/Report.dc.html` was never updated.** Known defects,
read directly from the file: the funding disclaimer is set in `#808080`
(**3.95:1 — fails AA on legally required text**); it points at the legacy asset
path `assets/logos/eu-funded-horizontal.png`; every colour is raw hex; body copy
is described in a comment as "11 pt Avenir Next", which is no longer true.
**Done when:** disclaimer uses `--text-legal`, assets point at `assets/logos/eu/`,
colours are tokens, and the comment names Manrope.

**E3.** 🟠 **`templates/deck/Deck.dc.html` was never updated.** Same class of
issues: the closing slide's disclaimer is `#808080`; it uses five legacy asset
paths (`eu-funded-horizontal.png`, `eu-funded-square.png`, `ucan-logo-compact.png`,
`ucan-logo-watermark.png`, `eu-missions-cities-square.png`); all colour is raw hex.
**Done when:** as E2.

**E4.** 🟠 **The invitation email will break in Outlook.** Two concrete bugs:
- It references `u-can-logo-colour.svg`. **Outlook does not render SVG.** Swap to
  a PNG at 2× intended size.
- Image `src` values are project-relative (`../../assets/...`). A sent email
  cannot resolve those — they must be absolute `https://` URLs or CID attachments.

Also missing: a plain-text alternative part, and a preheader.
**Done when:** the template renders correctly in Outlook (Windows), Gmail (web and
Android) and Apple Mail, with images blocked *and* unblocked.

**E5.** 🔴 **E9 — poster / one-pager.** Never built; the original task asked for
confirmation of need first. Note the Dresden materials contain two real one-pagers
(`04_OnePager_KhNU_*`, `05_OnePager_City_*`), which suggests the need is real.
**Done when:** the user confirms, and `templates/one-pager/` exists — or the task
is recorded as declined.

**E6.** 🟢 **E10 — the QR-code deck variant is completely untouched.**
`Template_Presentation_QRcode.potx` is a distinct source template that has never
been processed. The intended resolution was "a Tweak on `templates/deck/`", but
that was never written down or implemented.
**Done when:** the `.potx` has been examined, and the variant is either implemented
as a deck Tweak or as its own template, with the reason recorded.

**E7.** 🔴 **Ukrainian-language template variants.** Every template is
English-only. `guidelines/voice-and-language.md` says pilot-city material is
"Ukrainian first" — but there is no Ukrainian template to write it in.
**Done when:** at minimum `pilot-report` and `invitation-email` have UA variants,
or the policy is amended to say English-only templates are intentional.

**E8.** 🟢 **Cross-reference the speaker-notes convention.** `templates/deck/` and
`templates/wp-status/` should both point at `templates/speech-script/`, per the F4
decision.
**Done when:** both carry the pointer in their `@template` description or a comment.

---

## Section F — Deck and slides

**F1.** 🟠 **The F1 decision was recorded but never executed.** `slides/README.md`
now declares that `templates/deck/Deck.dc.html` is the source and the six
`slides/*.html` are *generated specimens*. **They were not regenerated** — they
are the same six files as before, and nothing guarantees they match the template.
**Done when:** each of the six specimens is demonstrably derived from the
corresponding deck layout, or the README's claim is corrected.

**F2.** 🟠 **The deck leads with its rarest layout.** Slide 02 of `Deck.dc.html`
is a four-bullet content slide. The evidence says **bullets appear on 1 slide in
126.** Meanwhile the three most common archetypes — multi-image grid (40%),
image + text (30%), full-bleed image (10%) — have either one layout or none.
**Done when:** the deck's layout order reflects measured frequency, and the
bulleted layout is present but not the default content slide.

**F3.** 🟢 **Add the missing archetypes to the deck** (original task F3, never
done). Ranked by evidence in `slides/README.md`: image grid (2/3/4-up, captioned),
full-bleed image with scrim, agenda/contents, table, stat row, milestone timeline,
thank-you/Q&A *(a closing slide exists — confirm it covers Q&A)*.
**Done when:** the deck's layout set matches the ranked list, and each new layout
uses the relevant component rather than hand-drawn shapes.

**F4.** 🟠 **The deck and slides do not use any components.** Every shape is drawn
inline. That is the exact practice the system was built to replace — `Stat`,
`Timeline`, `Figure`, `Alert` and `Grid`+`Card` exist specifically for these.
**Done when:** at least the stat, timeline and figure-grid layouts are built from
components.

---

## Section G — Data visualisation

**G1.** 🔴 **Approve the chart conventions.** `guidelines/charts-conventions.card.html`
is a proposal, not a record — there were no existing conventions to document,
because across 126 reference slides there is **not one native chart object.**
Review: the six-colour luminance-ordered series ramp, horizontal-gridlines-only,
direct labels over legends, mandatory zero baseline, and the exclusion of
`--ucan-green` and `--ucan-yellow` as series fills.
**Done when:** approved, amended, or rejected in writing. **This blocks D5 and G2.**

**G2.** 🟢 **Build the chart specimen set** once G1 lands. See D5.
**Done when:** `guidelines/charts-*.card.html` shows real rendered bar, stacked
bar, line, donut and WP-progress charts — not described, drawn.

**G3.** 🟢 **Prove the greyscale claim.** The series ramp's whole justification is
that it survives greyscale printing.
**Done when:** a card shows the same chart in colour and desaturated, side by side.

---

## Section H — Assets

**H1.** 🔴 **Real photography — the largest remaining gap.** Send 6–10 project
photographs plus one hero per pilot city (Lviv, Kyiv, Zhytomyr, Khmelnytskyi,
Ivano-Frankivsk, Vinnytsia). Crops: 16:9 hero, 8:5 card, 1:1 portrait. Consent on
file for every identifiable person.
**Done when:** no labelled placeholder remains in the website kit, and
`guidelines/imagery.card.html` shows real examples.

**H2.** 🔴 **The pilot-cities map.** Vector strongly preferred — the same graphic
is printed at A4 and projected at 1280px. Specification already written in
`guidelines/charts-map.card.html`.
**Done when:** the artwork is in `assets/` as SVG, D6 renders it, and no placeholder
referring to `map_eng_2.png` remains in the website kit or on the Pilots screen.

**H3.** 🔴 **The objectives artwork** (`1_Монтажная область 1.png`).
**Done when:** it is in `assets/illustrations/` under a kebab-case name, recorded
in the asset manifest, and used on the website kit Home screen.

**H4.** 🔴 **Sign off the reversed lockup.** `u-can-logo-reversed.svg` was derived
mechanically: anything under 3:1 against navy was knocked to white, anything above
kept. Which elements *should* knock out is a brand judgement.
**Done when:** approved or amended. See `guidelines/brand-logo-reversed.card.html`.

**H5.** 🔴 **The vertical / stacked lockup still does not exist.** The original
task H6 asked for *both* a reversed and a stacked lockup. Only reversed was
delivered.
**Done when:** a vertical lockup exists as SVG, or the brand confirms there is none.

**H6.** 🔴 **Monochrome Ukrainian EU emblem.** The UA set has no mono variant. If
one is needed it must come from the EU brand portal — it may **not** be made by
desaturating the colour file.
**Done when:** supplied, or recorded as not needed.

**H7.** 🟠 **Migrate the legacy root assets.** `assets/logos/` still holds
`ucan-logo.png`, `ucan-logo-compact.png`, `ucan-logo-square.png`,
`ucan-logo-transparent.png`, `ucan-logo-watermark.png`, `ucan-v3-final.png`,
`ucan-v3-black-white.png`, `eu-funded-horizontal.png`, `eu-funded-square.png`,
`eu-funded-en-horizontal-{pos,neg}.png`. These predate `assets/logos/u-can/` and
`assets/logos/eu/` and duplicate several of them. They are still referenced by
`LogoLockup`, `FundingNotice`, `Deck.dc.html` and `Report.dc.html`.
**Done when:** referrers point at the new trees and the legacy files are deleted —
or each is documented in `guidelines/asset-manifest.md` as intentionally distinct.

**H8.** 🟢 **Favicon and app icons do not exist.** Never raised in the original
audit, but any consuming web project needs them.
**Done when:** `favicon.ico`, a 512px maskable PNG and an SVG mark exist, with
sizes documented.

**H9.** 🟢 **Open Graph / social share image.** Also missing. `brand-social.card.html`
documents banner sizes but the project has no default share card.
**Done when:** a 1200×630 OG image exists and the website kit references it.

**H10.** 🟢 **Optimise.** `assets/brand/` is 2.0 MB across four PNGs; the SVG
masters are ~93 KB each and carry Illustrator cruft (clip paths, `<use>` elements,
a `-32768` bounding path).
**Done when:** run through an optimiser, verified visually unchanged per V9, and
total asset weight recorded in the manifest.

**H11.** 🟢 **Finish the H10 orphan sweep.** The manifest documents provenance but
the "confirm every file in `assets/` is referenced somewhere, delete orphans" half
was only partially done.
**Done when:** every file in `assets/` is either referenced or explicitly listed as
a supplied-variant kept for future use.

---

## Section I — UI kits

**I1.** 🟢 **Four website screens remain unbuilt:** Consortium/Partners, Work
Packages, Publications, Events. `PersonCard`, `DataTable`, `Timeline` and
`Pagination` now exist, so none is blocked.
**Done when:** each exists and is reachable from `ui_kits/website/index.html`.

**I2.** 🟢 **Responsive proof per screen.** `WebsiteHeader` has a `compact` mode
and `Grid` is container-responsive, but no screen has a mobile or tablet
rendering, and the site's real traffic is mobile-heavy.
**Done when:** every screen has a 390px and a 768px rendering in the kit.

**I3.** 🟢 **Per-screen accessibility audit.** Landmarks, skip link and hit targets
are in place. Not yet checked per screen: heading order (no skipped levels), real
alt text on every image slot, and `lang` on every Ukrainian string.
**Done when:** each screen passes an automated audit (axe or equivalent) with zero
violations, plus a manual heading-order check.

**I4.** 🟠 **Confirm every `ui_kits/templates/` reference is gone.** `readme.md`
claims the references were removed. `FINALIZATION-TASKS.md` still mentions it.
**Done when:** a project-wide grep returns nothing outside a historical note.

**I5.** 🔴 *(optional)* **Website exactness.** The kit is a declared interpretation
by agreement. To upgrade it: desktop (1440px) and mobile (390px) full-page
screenshots for Home, Overview, Pilots, News, a post and Contacts — or a Figma file.
**Done when:** either the kit matches supplied references and the interpretation
notice is removed from `ui_kits/website/README.md`, or the notice stays and this
task is recorded as declined.

---

## Section J — System level

**J1.** 🟠 **Starting points were never created.** `check_design_system` reports
`Starting points: (none)` and that has not changed. `readme.md` gained a
"Starting points" *table*, but that is documentation, not registration — a
consuming project still has no blank surface to begin from.
**Done when:** at minimum a blank deck, a blank report and a blank web page are
registered as actual starting points, and `check_design_system` lists them.

**J2.** 🟢 **`FINALIZATION-TASKS.md` is stale.** Its inventory line ("11 components
· 37 cards · 2 templates · 131 tokens · 0 registered fonts") describes the
pre-0.2.0 state. It is currently kept as a historical record with a dating note in
`TODO-for-you.md`.
**Done when:** it carries its own header stating it is superseded and dated, or it
is removed.

**J3.** 🟠 **`my-docs/03_u_can/U_CAN_Design/_derived/` contains superseded work.**
Its `tokens/colors.css` redefines the core palette with *different values* —
`--ucan-blue: #0057B7` instead of `#0463CD`, and a different green — and drops the
semantic alias layer entirely. **If anyone uploads that file it will silently
change the primary blue across the whole system and break every component that
reads `--surface-*` or `--text-*`.** Its contrast comments are also wrong for the
live palette (6.89:1 and 3.97:1 belong to the other blue and green).
**Done when:** `_derived/` is archived, deleted, or carries a prominent README
warning that it is a superseded working directory and must not be uploaded.

**J4.** 🟢 **`DESIGN-FINDINGS.md` is stale** in the same way — it describes the
pre-access session and lists nine open blockers, six of which are closed.
**Done when:** superseded-and-dated, or removed.

**J5.** 🟢 **Keep `qa/kitchen-sink.html` in sync.** Its `expected` array is a
hard-coded list of 42 component names. Every new component must be added in two
places or the page silently under-reports.
**Done when:** `guidelines/contributing.md`'s pre-PR checklist names this
explicitly *(it currently says "does the directory card show the new component?"
but not the kitchen sink)*.

**J6.** 🟢 **Write a consumer migration note for v0.2.0.** The D1 restructure
moved five components and changed `--text-muted`. `CHANGELOG.md` records it, but
no upgrade guide exists.
**Done when:** `CHANGELOG.md` carries a short "upgrading from 0.1.0" section with
the exact path and token substitutions.

**J7.** 🟢 **Release process.** There is a version token and a changelog but no
stated process — who bumps it, when, and what counts as breaking.
**Done when:** `guidelines/contributing.md` states it.

---

## Section K — Bilingual delivery

**K1.** 🔴 **The website kit is English-only.** `guidelines/voice-and-language.md`
commits to "full parallel versions, language switch in the header" — and the
header has no language switch.
**Done when:** the switch exists (a `Menu` component would serve — see D4) and at
least the Home screen has a Ukrainian rendering.

**K2.** 🟢 **Ukrainian overflow testing.** UA runs 10–15% longer. Nothing has been
tested against that.
**Done when:** every kit screen and every deck layout has been viewed with
Ukrainian strings and nothing clips, truncates or overlaps.

**K3.** 🟢 **Ukrainian in the kitchen sink.** It currently carries a few UA strings
incidentally.
**Done when:** it has a deliberate EN/UA parallel section so overflow regressions
are visible in the standard screenshot.

---

## Section L — Governance and infrastructure

**L1.** 🟢 **Visual regression.** V8 produces a baseline; nothing automates the
comparison.
**Done when:** a documented command screenshots the kitchen sink and every card and
diffs against committed baselines.

**L2.** 🟢 **Automate the contrast check.** Every ratio in this system was verified
with a throwaway script that no longer exists in the project.
**Done when:** a committed script recomputes every pairing in
`guidelines/colors-pairings.card.html` and fails if a documented figure drifts.

**L3.** 🟢 **Asset link checker.** Several tasks above exist because a referenced
asset path went stale.
**Done when:** a script resolves every `src`/`href` in the project against
`assets/` and reports misses.

**L4.** 🟢 **Review cadence.** Set a date to re-audit the accepted deviations,
the light-only decision (B5) and the declared-interpretation status (I5).
**Done when:** recorded in `readme.md`.

---

## Consolidated blocker list — only the user can answer these

| # | Task | Question |
|---|---|---|
| 1 | G1 | **Approve the chart conventions.** Blocks D5, G2, G3. |
| 2 | H1 | **Real photography** — 6–10 project photos + 6 city heroes. |
| 3 | H2 | **The pilot-cities map**, ideally vector. |
| 4 | H3 | **The objectives artwork.** |
| 5 | H4 | **Sign off the reversed lockup** — or say which elements should knock out. |
| 6 | H5 | **Vertical / stacked lockup** — supply, or confirm none exists. |
| 7 | H6 | **Monochrome UA emblem** — needed or not? |
| 8 | A1 | **The claim line off Windows** — adopt a licensable condensed face, or accept Manrope? |
| 9 | A5 | **Office vs web fonts** — update the `.potx`/`.docx` to Manrope, or accept the divergence? |
| 10 | E5 | **Poster / one-pager** — build it? (Two real one-pagers exist in the Dresden materials.) |
| 11 | E7 | **Ukrainian template variants** — which templates need them? |
| 12 | K1 | **Website language switch** — required for launch, or later? |
| 13 | I5 | *(optional)* Website screenshots or Figma, to make the kit exact. |

---

## Suggested order of work

| Phase | Sections | Rationale |
|---|---|---|
| **1** | **V** | Nothing below is trustworthy until the system is known to render. |
| **2** | **R** | Cheap checks for expensive-to-find breakage introduced by v0.2.0. |
| 3 | Blockers 1–7 to the user | The longest lead times; everything visual waits on them. |
| 4 | C, D1–D3, E1–E4, F | Correctness and consistency in what already exists. |
| 5 | A, B, J | Decisions and system docs. |
| 6 | D4–D7, G, I | New surface area, once the foundations are verified. |
| 7 | H, K | Assets and bilingual delivery. |
| 8 | L | Automate what was verified by hand, so it stays verified. |

**Totals: 86 tasks — 14 needing the user, 27 flagged as suspected defects or risks,
45 an agent can complete unaided.** The user-decision table above lists 13 of the
14; the fourteenth is I5, which is optional.

---

## A note on trust

Two things in this repository turned out to be confidently wrong, and both were
caught only by re-deriving them from source rather than reading them forward:

- The logo colour inventory in `_derived/` was **wrong on every line** — it
  recorded 44 navy fills in artwork that contains no navy at all, and doubled both
  green counts.
- Two contrast figures had been carried over from a *different* palette, making
  a failing colour look compliant.

Conversely, the deck-corpus analysis (126 slides, 7 decks, bullets on 1 slide in
126) **verified exactly** when re-derived independently.

The lesson is not that the earlier work was careless — most of it was sound. It
is that **numbers in this system should be recomputed, not inherited.** Task L2
exists to make that automatic.
