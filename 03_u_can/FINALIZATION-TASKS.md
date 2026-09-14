# U_CAN Design System — finalization record

**Status: finalized at v0.3.1, 14 September 2026.**

This document began as a ~70-task plan written against v0.2.x. Every section of that
plan is now closed. It is rewritten here as a record of what was decided, plus the
short list of what genuinely remains — all of which needs either a file only you can
supply or a click only you can make.

`check_design_system` reports **no issues**. Every card, component, template and
token compiles; all three declared families are self-hosted; every asset reference
in all 142 source files resolves.

---

## What the system contains

| | Count |
|---|---|
| Library components | **57** — `.jsx` + `.d.ts` + `.prompt.md`, seven concern directories |
| Design System cards | **53** — Brand 12, Colors 8, Type 8, Spacing 6, Slides 6, Components 6, Charts 4, Layout 1, Documents 1, Website 1 |
| Templates | **10** — deck, wp-status, report, deliverable, pilot-report, conference-report, speech-script, speakers-bio, invitation-email, timesheet |
| Tokens | **247** across 12 files, all imported through `styles.css` |
| Self-hosted fonts | **7 `@font-face` rules**, 2 variable families, nothing over the network |
| Guideline documents | 38 cards + 4 reference documents |
| Verification tools | 2 — `tools/_contrast.mjs`, `tools/_link-check.mjs` |

---

## Sections A–K: closed

**A — Typography.** Manrope (body) and Roboto Condensed (claim), both SIL OFL, both
self-hosted, both with full Ukrainian Cyrillic. Seven `@font-face` rules rather than
sixteen, because both families are variable and one file per subset carries the whole
weight axis. Bahnschrift is out of the web stack entirely (0.3.1) and is deliberately
not tokenised at all; the `.potx`/`.docx` divergence is documented with a review date.

**B — Colour.** `#FFCC00` canonical, `--ucan-yellow-alt` deprecated with a removal
release named. Four semantic states with foreground, background tint and border. Every
permitted pairing measured; every forbidden pairing recorded with a compliant
alternative named. Link colours defined for default, visited, hover and focus-visible,
on light and on dark. Light-only by design, with the on-dark convention documented.

**C — Tokens.** Breakpoints, container widths, z-index ladder, opacity/scrim scale,
table tokens and print tokens all exist and are carded.

**D — Components.** 57 across core, layout, content, forms, feedback, navigation and
charts. Every interactive component defines hover, active, focus-visible, disabled and
where applicable loading; 44px minimum hit targets; `prefers-reduced-motion` honoured
globally.

**E — Templates.** All ten built as Design Components with `@template` markers and a
sibling `ds-base.js`. The QR-code deck is a Tweak on `templates/deck/`, not a
separate template.

**F — Slides.** The `slides/` ↔ `templates/deck/` relationship is resolved and recorded
in `slides/README.md`.

**G — Charts.** Conventions carded and enforced in code: zero baseline mandatory,
horizontal gridlines only, direct labels by default, never colour alone, a
visually-hidden data table on every chart, and a series ramp asserted monotonic in
luminance by `tools/_contrast.mjs`. Map convention carded with five rendered variants.

**H — Assets.** EU logo trees (EN/UA × horizontal/vertical × seven treatments), LHD
Förderlogo and Stadtverwaltung sets with the funder/partner rule stated, Cities Mission
banners, U_CAN SVG masters including the reversed lockup, five pilot-city map
renderings, 24 city photographs, favicon set and social card. Third-party stock
removed. Provenance in `guidelines/asset-manifest.md`.

**I — UI kits.** Website and documents kits built. `ui_kits/templates/` confirmed as
never having existed, and every reference to it removed. The website kit's README
states plainly that it is an interpretation and names what would make it exact.

**J — System.** Contribution guide, usage-obligations document, voice-and-language
rules, asset manifest, changelog, adherence config, kitchen-sink QA surface, project
thumbnail.

**K — Verification.** All 142 source files scanned: every `src`, `href` and `url()`
resolves to a file that exists. No card loads a raw `.jsx` via `<script src>`. The
kitchen sink renders with no console error.

---

## What actually remains

### F1 · Register three starting points — app-side, one click each

`check_design_system` reports `Starting points: (none)` because registration happens in
the Design System app, not in a file. Approved 14 September 2026: `templates/deck/`,
`templates/report/`, `ui_kits/website/`.

### F2 · Consume the system once from a scratch project

The only test that proves the system works for its audience: copy `templates/deck/`
into a fresh project, point the `base` line in its `ds-base.js` at the bound `_ds/`
tree, and confirm it renders styled with no other edit. Everything is in place for this
to pass; it has not been run.

---

## What 1.0.0 requires

0.3.1 is **complete and internally consistent**. That is not the same as 1.0. A 1.0
design system is one that has been *used* — the remaining gap is almost entirely
between "the code is right" and "we have watched it work". Eleven items, in the order
they should be done.

### Blocking — a 1.0 cannot honestly ship without these

**V1 · Nobody has ever consumed this system.** Not once. Every claim about the
consumer contract — that a template folder copies cleanly, that one `base` line is
the only edit, that `_ds_bundle.js` resolves from a bound `_ds/` tree — is
reasoning, not observation. Copy `templates/deck/` into a scratch project, change
the one line, and render it.
*Done when:* it renders fully styled with no second edit, and the steps are written
into `readme.md` as verified rather than intended.

**V2 · Print has never been tested.** Ten templates, six of them print-first
(deliverable, report, pilot-report, conference-report, timesheet, speakers-bio), and
not one has been through a print dialogue. The project is German- and
Ukrainian-facing, so **A4 is the real default and Letter is the fallback** — page
boxes, running headers, footer depth for the EU statement, and table splits across
pages are all unverified.
*Done when:* every print template is exported at A4 and Letter and visually checked
for overflow, orphaned headings and clipped running elements.

**V3 · Ukrainian exists as policy, not as a surface.**
`guidelines/voice-and-language.md` commits to full parallel website versions and
Ukrainian-first pilot-city material. **Zero Ukrainian screens or template variants
are built.** The same document warns that Ukrainian runs 10–15 % longer than English
— which means every fixed-width element in ten templates and two kits is an untested
assumption. This is the largest gap in the system.
*Done when:* Ukrainian variants of `templates/deck/`, `templates/pilot-report/` and
`templates/invitation-email/` exist, the website home renders in Ukrainian, and each
has been checked for wrapping and overflow at its real content length.

**V4 · Numbers are formatted `en-GB`, hard-coded.** `components/charts/chart-kit.jsx`
calls `toLocaleString("en-GB")`, so a Ukrainian chart renders `1,234` where the
convention is `1 234`. A bilingual project cannot ship a chart library with one
locale compiled in.
*Done when:* locale is a prop or a token, defaulting from `lang`, and the charts card
shows both renderings.

**V5 · The verification tools have never been executed.** `tools/_contrast.mjs` and
`tools/_link-check.mjs` are committed, documented and required before every release
— and no one has run them, because there is no Node in this environment. A guard that
has never fired is not yet a guard.
*Done when:* both have been run once against 0.3.1, their output recorded, and any
drift they find fixed.

**V6 · Accessibility is asserted, not observed.** Every claim in the readme is
code-level: focus rings are defined, targets are 44 px, contrast is computed. Nobody
has tabbed through a template, run a screen reader over a chart's hidden data table,
zoomed to 200 %, or opened a card in forced-colors mode.
*Done when:* a keyboard walk and a screen-reader pass are completed on
`qa/kitchen-sink.html` and two templates, with findings recorded.

### Required, lower risk

**V7 · Website kit is an interpretation of a Wix site.** Its README says so honestly,
which is the right interim position but not a 1.0 one. Either supply desktop and
mobile screenshots (or a Figma file) for Home, Overview, Pilot Cities, News, a single
news post and Contacts and rebuild against them — **or** formally accept the kit as
an original design and stop describing it as a recreation.

**V8 · Website kit is missing surfaces the site has.** Present: Home, Overview,
Pilots, News. Missing: single news post, Contacts (the form components now exist),
Consortium/Partners, Work Packages, Publications, Events, 404 and a search-results
state. No mobile or tablet rendering exists for any screen, and the site's real
traffic is mobile-heavy.

**V9 · The invitation email has never been sent.** HTML email fails in clients, not
in browsers, and Outlook's Word rendering engine is where table layouts break. One
send to Outlook, Gmail, Apple Mail and a phone client would settle it.

**V10 · Office templates still diverge.** `.potx`/`.docx` keep Bahnschrift and
Calibri while the web system uses Manrope and Roboto Condensed — both OFL and both
embeddable. A 1.0 should either regenerate the three Office files against the system
or state the freeze as permanent rather than as a review.

**V11 · Cascadia Mono is 167 KB for token labels.** Three times the entire body
family, for the least important role in the system. The options were measured: subset
to ~15 KB and rename the face (OFL clause 3), or drop the self-hosted file and let
`ui-monospace` carry it at zero. Both are defensible; carrying 167 KB indefinitely is
the one that isn't.

### Explicitly out of scope for 1.0

Dark mode (decided against, reviewed September 2027) · additional chart types beyond
the five · animation beyond hover and `prefers-reduced-motion` · a Figma library ·
automated visual regression · `--ucan-yellow-alt` deletion (already scheduled for
0.4.0).

### Suggested sequencing

| Phase | Items | Why first |
|---|---|---|
| 1 | V1, V5 | Both are single sessions and both can invalidate everything below |
| 2 | V2, V4, V6 | Correctness failures in shipped artefacts |
| 3 | V3 | The largest build, and it depends on V2's page geometry holding |
| 4 | V7, V8, V9 | Kit completeness; V7 gates V8 |
| 5 | V10, V11 | Cleanups that need a decision more than they need work |

**Of the eleven, four need only your time (V1, V5, V6, V9), two need a decision
(V10, V11), one needs material from you (V7), and four are build work (V2, V3, V4,
V8).**

---

## Standing reviews

| What | Why | When |
|---|---|---|
| Office templates keep Bahnschrift + Calibri | Re-flowing three binary templates is riskier than the gain | September 2027 |
| Light-only colour system | Print-and-deck-led identity; revisit if the site gains photo-led surfaces | September 2027 |
| `--ucan-yellow-alt` | Deprecated; nothing references it | Delete in v0.4.0 |
| Website kit is an interpretation | Live site is a Wix build with no accessible design source | When screenshots or Figma arrive |
| `source/` binaries | Kept as provenance for derived token claims | Reconsider if repo weight matters |

---

## Before every release

```bash
node tools/_contrast.mjs     # 43 pairings, re-derived from tokens/
node tools/_link-check.mjs   # every src/href/url() and every var() resolved
```

Then open `qa/kitchen-sink.html`, screenshot it, and diff against the previous release.
**Numbers in this system are recomputed, not inherited.**
