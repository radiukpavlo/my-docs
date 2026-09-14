# Print exports — U_CAN Design System v1.0.0

**Exported 14 September 2026** by `tools/_print-check.mjs --pdf`, through Chrome 153.

These exist to prove task **V2**: before v1.0.0 not one of the ten templates had
ever been through a print dialogue, and doing it for the first time found three
real failures. All three are fixed in `tokens/print.css` using named pages.

| File | Pages | Page box | Was
|---|---|---|---|
| `deck.pdf` | 12 | 1280 x 720 | 6 portrait A4 sheets, two cropped slides each |
| `deck-uk.pdf` | 12 | 1280 x 720 | did not exist |
| `timesheet.pdf` | 1 | landscape A4 | portrait A4 with ~330px cut off the right edge |
| `deliverable.pdf` | 5 | A4 | 5 sheets, the last one blank but for the EU disclaimer |
| `report.pdf` | 4 | A4 | 4 sheets, same blank-page fault |
| `pilot-report-uk.pdf` | 3 | A4 | did not exist |

## Regenerate these with the real artwork

```bash
node tools/_print-check.mjs --pdf print-out
```

**Read this before using the PDFs as final artwork.** They were exported from a
working mirror of the project on one machine, and that mirror carries only part
of `assets/`. Three decorative images in the deck — the footer band on the title
slide, the leaf rule, and the city-scene illustration on the split slide — are
LOCAL STAND-INS, not the real files. Everything that matters for the print
question is real: page geometry, type, colour, tables, the photography and the
EU emblems.

Running the command above inside the actual project regenerates every one of
these with the correct artwork. The geometry will be identical — that is the
part these files are evidence for.
