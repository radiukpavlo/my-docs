# U_CAN Design System — finalization record

**Status: v1.0.0, 14 September 2026.**

The eleven items this document listed as required for 1.0 are closed, except one
which is deferred with a reason and one which can only be done in the app. All
five verification tools run green.

This file is now a record. The live status is `readme.md` and `CHANGELOG.md`.

---

## What 1.0 turned out to mean

0.3.1 was complete and internally consistent. It had also never been *used* —
never consumed from another project, never printed, never sent, never tabbed
through, and its two verification tools had never been executed because there was
no Node in the environment that wrote them.

Doing all of that found **eleven real defects**. Not one was visible on screen.
That is the whole argument for the distinction between a system that compiles and
a system that has been watched working.

| | Found by |
|---|---|
| Every image 404s when a template is copied into a consuming project | V1 |
| `_ds_bundle.js` throws on a static template (React not present) | V1 |
| The timesheet prints with ~330px cut off — a signed financial record | V2 |
| The deck prints two cropped slides to a portrait sheet | V2 |
| The deliverable spills a blank page carrying the EU disclaimer | V2 |
| The report does the same | V2 |
| Charts have `en-GB` compiled in; Ukrainian renders `1,234` not `1 234` | V4 |
| `--text-muted` on `--surface-field` is 3.77:1 — 14 nodes on one deck | V6 |
| Every template is missing `<title>` | V6 |
| The English deck is missing `lang` | V6 |
| The deck's image-grid slide overflows the stage by 63px | V3 tooling |

The last one is worth singling out: it was found by the tool built to protect
*Ukrainian*, and the slide it broke was the **English** one. It had been wrong
since the layout was written, and every review had looked straight past it.

---

## The eleven — disposition

| | Item | Status |
|---|---|---|
| **V1** | Consume the system from a scratch project | **Closed.** Done, failed, fixed, re-run green. Steps recorded in `readme.md` as verified. |
| **V2** | Print has never been tested | **Closed.** Named pages in `tokens/print.css`; `tools/_print-check.mjs` asserts an artboard equals a sheet. PDFs exported at A4, Letter and the CSS sizes. |
| **V3** | Ukrainian exists as policy, not as a surface | **Closed.** `deck-uk`, `pilot-report-uk`, `invitation-email-uk`, each overflow-checked at real content length. |
| **V4** | Numbers formatted `en-GB`, hard-coded | **Closed.** `locale` prop on all four numeric charts, defaulting from document `lang`; both renderings shown on the charts card. |
| **V5** | The verification tools have never been executed | **Closed.** Both run, plus three new ones. See the correction below. |
| **V6** | Accessibility is asserted, not observed | **Closed.** axe WCAG 2.2 A/AA, keyboard walk, 200 % zoom, forced-colors. 0 serious violations, 0 focus stops without an indicator. |
| **V7** | Website kit is an interpretation of a Wix site | **Closed by decision, 14 Sep 2026.** Accepted as an **original design**. The live site predates this system; rebuilding the kit to match it would mean the design system's own web kit copying a site that does not follow the design system. |
| **V8** | Website kit is missing surfaces the site has | **DEFERRED — the one open build item.** See below. |
| **V9** | The invitation email has never been sent | **Sent**, both editions, 14 Sep 2026. Awaiting the client-by-client check — see below. |
| **V10** | Office templates still diverge | **Closed by decision.** The freeze is permanent, not a review. `readme.md` carries the per-document procedure for anyone who wants matching Office output. |
| **V11** | Cascadia Mono is 167 KB for token labels | **Closed.** Replaced by JetBrains Mono: 52 KB, variable 400–700, WOFF2, full Cyrillic, no Reserved Font Name obstacle. |

### The correction V5 produced, which matters more than V5

`_contrast.mjs` ran and reported **43 pairings green** — while the deck had
**fourteen** contrast failures. The tool was not wrong. Its *list* was
incomplete: `--text-muted` on `--surface-field` had never been added, and the
green field is the ground the deck uses for two-thirds of every slide.

A guard that has never fired is not yet a guard. A guard that fires green on an
incomplete list is worse, because it buys confidence it has not earned.

**When you add a surface, add its pairings.** That rule is now in `readme.md`,
`tools/README.md` and the tool's own header.

---

## What remains

### 1 · Register three starting points — app-side, one click each

`check_design_system` reports `Starting points: (none)` because registration
happens in the Design System app, not in a file. Approved: `templates/deck/`,
`templates/report/`, `ui_kits/website/`.

### 2 · Open the project once so the compiler re-runs

v1.0.0 was uploaded through the file API. `_ds_manifest.json` and
`_ds_bundle.js` are built by the app's own self-check, so the card index and the
component namespace stay at the previous compile until the project is opened.
Nothing is wrong with the files; the index simply has not caught up.

### 3 · V8 — the website kit is still missing surfaces

Present: Home, Overview, Pilots, News. Missing: a single news post, Contacts,
Consortium/Partners, Work Packages, Publications, Events, 404 and a
search-results state. No mobile or tablet rendering exists for any screen, and
the site's traffic is mobile-heavy.

**Deferred deliberately, not overlooked.** Building these means composing
`PersonCard`, `DataTable`, `Timeline`, `Pagination`, `WebsiteHeader` and
`WebsiteFooter` — and this pass could not render-verify those components, so the
screens would have been written without being watched working. That is precisely
the failure mode 1.0.0 exists to end. Six screens that compile and have never
been looked at would be a step backwards from a release whose entire claim is
that its surfaces have been observed.

It is the first item of v1.1.0, and it is unblocked: every component it needs
already exists.

### 4 · V9 — the email was sent; the client check is yours

Both editions went to `radiukp@khmnu.edu.ua` on 14 September 2026, each with its
HTML and plain-text parts. HTML email fails in clients, not in browsers, so the
remaining step cannot be automated: open both in **Outlook on Windows** (the
Word rendering engine is where table layouts break), Gmail web, Gmail mobile and
Apple Mail. Each message carries its own checklist in the text part.

Expected: the three images will not load. Their `src` values point at
`https://www.ucan-ukraine.eu/email-assets/`, which does not exist yet — which
also exercises the images-blocked path most clients default to. Upload them there
before any real send.

### 5 · The three new template folders need `support.js`

`templates/deck-uk/`, `templates/pilot-report-uk/` and
`templates/invitation-email-uk/` ship with their `.dc.html` and their
`ds-base.js`, but **not** `support.js` — that file is the Design Component
runtime, it is ~69 KB, and it is byte-identical in all ten existing template
folders. Copy it from any sibling:

```bash
cp templates/deck/support.js templates/deck-uk/support.js
cp templates/report/support.js templates/pilot-report-uk/support.js
cp templates/invitation-email/support.js templates/invitation-email-uk/support.js
```

Until then the three Ukrainian templates render correctly as HTML but are not
editable as Design Components.

### 6 · Legacy flat assets are still in the tree

`assets/logos/ucan-*.png`, `assets/logos/eu-funded-*.png` and
`assets/logos/partners/` were superseded in 0.3.0 and nothing in the system
points at them. 0.3.1 planned the deletion and it has not happened.
`node tools/_link-check.mjs` is the gate: it reports zero `LEGACY` hits today, so
the deletion is safe whenever someone wants the tidier tree.

---

## Standing reviews

| What | Why | When |
|---|---|---|
| Office templates keep Bahnschrift + Calibri | **Permanent as of 1.0.0.** Re-flowing three binary templates the consortium already uses risks more than it gains. Per-document procedure in `readme.md`. | Not scheduled |
| Light-only colour system | Print-and-deck-led identity; revisit if the site gains photo-led surfaces | September 2027 |
| `--ucan-yellow-alt` | Deprecated; nothing references it | Delete in v1.1.0 |
| Website kit surfaces (V8) | Six screens plus mobile renderings | v1.1.0 |
| `source/` binaries | Kept as provenance for derived token claims | Reconsider if repo weight matters |

---

## Explicitly out of scope for 1.0

Dark mode (decided against, reviewed September 2027) · chart types beyond the
five · animation beyond hover and `prefers-reduced-motion` · a Figma library ·
automated visual regression in CI.

---

## Before every release

```bash
node tools/_contrast.mjs        # 45 pairings, re-derived from tokens/
node tools/_link-check.mjs      # every src/href/url() and every var()
node tools/_print-check.mjs     # an artboard must equal one sheet
node tools/_overflow-check.mjs  # does the text fit the box it was given?
node tools/_a11y-check.mjs      # axe + keyboard + 200% zoom + forced-colors
```

Then open the project in Claude Design, look at `qa/kitchen-sink.html`, and diff
the screenshot against the previous release.

**Numbers in this system are recomputed, not inherited.**
