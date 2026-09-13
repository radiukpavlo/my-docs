# 08 — Asset Index

What is in this repository, what stayed on Google Drive, and why.

**Drive root** (`$G` below) = `G:\My Drive\Work\Work_RnD\RnD_U_CAN`
(1 232 entries, 15 top-level folders, ~1.5 GB).

## Selection rule

The repository keeps what you need to **produce** something — templates, reference
PDFs, plain text, playbooks. Drive keeps what you need to **re-master** something —
PPTX originals with embedded media, EPS/AI print files, raw photo and video archives.
Where a PPTX and its PDF rendition carry the same content, the repository keeps the
PDF: for the twenty-two candidate source files this was **16.6 MB instead of 141 MB**.

## `Reference/` — read-only PDFs (21 MB)

| File | What it is | Drive original |
|---|---|---|
| `2026-07-06_WP4_Status_LAquila.pdf` | **Most current WP4 status**, all six pilots, L'Aquila consortium meeting | `$G/U_CAN_2026-07-06_LAquila/U_CAN_LAquila_Pres/U_CAN_WP4(06.07.2026).pptx` (42 MB) |
| `WP4_Partners_Introduction.pdf` | WP4 tasks and deliverables explained partner by partner | `$G/U_CAN_Presentation_Core/4_U_CAN_Partners_Introduction.pptx` (20 MB) |
| `U_CAN_Technical_Report_B.pdf` | U_CAN technical report (46 pp) | `$G/U_CAN_Presentation_Core/8_U_CAN_1_Tech-report_B.pdf` |
| `U_CAN_1st_Periodic_Report_WP4.pdf` | WP4 slides for the 1st Review Meeting, M1–M18 | `$G/U_CAN_Presentation_Core/8_U_CAN_2_1st-periodic-report.pdf` |
| `U_CAN_WP_Overview.pdf` | One-page WP overview | `$G/U_CAN_Timesheets/U_CAN_WPs.pdf` |
| `2026-04-24_MS6_Agenda_EN.pdf` | MS6 conference agenda (EN; UA version on Drive) | `$G/U_CAN_2026-04-24_MS6/` |
| `2026-04-24_MS6_Radiuk_Presentation_UA.pdf` | Radiuk's MS6 talk (Ukrainian) | `…/MS6_Pres-Radiuk/16_Презентація_Радюк.pptx` (24 MB) |
| `2026-03-31_Consortium_Slides.pdf` | March 2026 consortium progress slides | `$G/U_CAN_2026-03-31_U_CAN-Consortium-Meeting/` |
| `2026-05-12_Monthly_Slides.pdf` | May 2026 monthly meeting slides | `$G/U_CAN_2026-05-12_Monthly-Meeting/` |
| `2026-04-01_SMW_Khmelnytskyi_Pilot_EN.pdf` | Smart Mobility Week pilot deck (EN) | `$G/U_CAN_2026-04-01_U_CAN-SMW/` |

## `Editable/` — files you actually open and change (7.7 MB)

| File | Use it for |
|---|---|
| `U_CAN_WP_Template.pptx` | **The design base for any WP deck.** Referenced by both slide playbooks. |
| `Template_Presentation_QRcode.potx` | Presentation template with QR-code slide |
| `2026-07-06_LAquila_Speech_Script.docx` | Model 5-minute speech script — copy its rhythm |
| `KhNU_Monthly_Progress_Tracker.xlsx` | Monthly progress tracker, May 2025 → June 2026 |
| `MS6_Speakers_Bio.docx` | 20 speaker biographies — reuse for future events |
| `Khmelnytskyi_Pilot_Scenario.docx` | Full pilot scenario narrative |
| `Khmelnytskyi_Pilot_QA.docx` | Anticipated questions and answers — **read before any Q&A session** |

More templates in `../U_CAN_Design/`: `Template_Presentation.potx`,
`Template_Report.docx`, `Template_Deliverable.docx`.

## `Source_Text/` — plain-text extracts (1.1 MB) — **search here first**

`GrantAgreement_101148374_full.txt` (583 KB, 178 pp) ·
`ConsortiumAgreement_full.txt` (89 KB, 57 pp) ·
`U_CAN_Technical_Report_B.txt` · `U_CAN_1st_Periodic_Report_WP4.txt` ·
`2026-07-06_WP4_Status_LAquila_slides.txt` · `WP4_Partners_Introduction_slides.txt` ·
`KhNU_Annual_Pilot_Report_2025-2026.txt` · `KhNU_Monthly_Progress_Tracker.txt` ·
`MS6_Conference_Report.txt` · `MS6_Speakers_Bio.txt` ·
`Khmelnytskyi_Pilot_Scenario.txt` · `Khmelnytskyi_Pilot_QA.txt` ·
and four speech scripts (`Speech_2026-03-31_Consortium`, `Speech_2026-04-01_SMW_EN`,
`Speech_2026-05-12_Monthly`, `Speech_2026-07-06_LAquila`).

The signed **Grant Agreement** and **Consortium Agreement** PDFs (5.2 MB + 5.5 MB)
stay on Drive at
`$G/U_CAN_2026-07-06_LAquila/U_CAN_LAquila_Pres/U_CAN_LAquila_Pres_Sources/` —
the text extracts above carry every operative fact and are greppable.

```bash
grep -n -i "milestone" U_CAN_Knowledge-base/Source_Text/GrantAgreement_101148374_full.txt
```

## `Playbooks/` — proven prompts (91 KB)

| File | Produces |
|---|---|
| `Prompt_Create-Deck_15slide_system.md` | A full 15-slide WP4/D4.5 deck from the source set. The most complete slide brief. |
| `Prompt_Create-Slides_WP4_system.md` | Three D4.5 slides matching an existing deck's design logic |
| `Prompt_Make-Speech-Script.txt` | A timed presentation script, 3–4 sentences per slide |
| `Prompt_Conference-Report_system.txt` | A full conference/milestone report |
| `Prompt_Travel-Docs_system.txt` | The Ukrainian travel paperwork set (подання, витяг, заява, службова, мета) |
| `Prompt_Annual-Pilot-Report.txt` | The annual pilot progress report |
| `Prompt_Timesheets.txt` | Horizon timesheet records |
| `Prompt_Speakers-Bio.txt` · `Prompt_Conference-Invitation-Email.txt` | Speaker bios; invitation e-mails |

Full prompt library (42 numbered prompts, 11 MB of .docx) stays at `$G/U_CAN_Prompts/`.

## Elsewhere in `03_u_can/`

| Folder | Contents |
|---|---|
| `U_CAN_Design/` | Brand assets — **19 MB, slimmed from 146 MB** (see below) |
| `U_CAN_Papers_Published/` | LaTeX submission packages P1–P4 (31 MB) |
| `U_CAN_Papers_Review/` | Two manuscripts under review (1.9 MB) |
| `U_CAN_2026-09-14_Dresden/` | Dresden trip: its own 9-file KB, source files, tickets, paperwork |

### What was removed from `U_CAN_Design/` and where it lives

`Logos/EU Emblem and Cities Mission banner/horizontal` and `/vertical` were
**byte-identical duplicates** (md5-verified) of `Logos/EU logos/EN_horizontal` and
`EN_vertical`. Also removed: all `.eps` print masters (75 MB), `.jpg` copies where a
`.png` or `.svg` of the same asset was retained (each verified present before
deletion), macOS `._*` and `.DS_Store` files, and
`LHD/Grafisches_Erscheinungsbild_LHD_2024.pdf` (24 MB Dresden brand manual).

All of it remains on Drive at
`$G/U_CAN_Presentation_Core/U_CAN_Templates-and-Logos/`.

Retained and sufficient for slides, posters and print: U_CAN logo (PNG + AI, colour
and black-and-white, transparent and square), EU "Funded by the EU" emblems in EN and
UA, horizontal and vertical, RGB PNG + CMYK JPEG, Cities Mission banners in five
sizes, the full LHD Förderlogo and Stadtverwaltung sets (PNG + SVG + AI + PDF),
FB banner, Zoom wallpaper, PPT footer graphics, fonts, and the four Office templates.

## Drive folders deliberately not mirrored

| Folder | Why it stays on Drive |
|---|---|
| `U_CAN_2025/` (414 files) | 2024–25 archive, superseded by the reports summarised here |
| `U_CAN_2026-04-24_MS6/` (196 files) | Full conference archive: 20 speaker decks, photos, videos, registration and feedback workbooks, invitation letters. The report and agenda are mirrored; the rest is bulk evidence. |
| `U_CAN_2026-07-06_LAquila/` (109 files) | Travel receipts, tickets, boarding passes, handbooks |
| `U_CAN_Timesheets/` (38 files) | Personal and financial records — `Prompt_Timesheets.txt` regenerates them |
| `U_CAN_Prompts/` (56 files) | The nine highest-value prompts are mirrored in `Playbooks/` |
| `*_Archived/`, `*_Screenshots/`, `*_Images/`, `*_Videos/` | Superseded drafts and raw media |
