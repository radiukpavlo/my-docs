# 09 — Contradictions Found, and What to Trust

Every discrepancy noticed while building this KB, with the resolution. Check here
before quoting any number that feels surprising.

## Resolved — use the right-hand column

### 1. Per-partner budgets in the Grant Agreement Data Sheet ⚠️ important

The Data Sheet table on page 9 (`GrantAgreement_101148374_full.txt`, ~line 410) has
three independently-offset column streams in the extracted text. Read naively, a
physical line pairs **KhNU** with the legal name *Politechnika Wrocławska* and the
amount *169 750.00* — both wrong.

**Resolution:** Annex 2 (~line 7440) gives each beneficiary its own cost row.
Because the funding rate is 100 %, the row's cost columns sum to that partner's
maximum grant amount. All 21 rows were summed independently; they total exactly
**€4 999 375.00**, and every value then matches the Data Sheet list once it is
aligned correctly. **KhNU = €138 250.00**, not €169 750.00 (which is OMB's).
[02_Consortium.md](02_Consortium.md) uses the verified figures.

### 2. "Eight Ukrainian cities" vs "six pilot cities"

The GA abstract says U_CAN "starts with a core group of 8 Ukrainian cities"; WP4 has
6 pilots. Both are correct at different scopes: the **6 WP4 pilot cities** are Lviv,
Kyiv, Zhytomyr, Khmelnytskyi, Ivano-Frankivsk, Vinnytsia; the **core city group** also
includes Kharkiv (OMB) and Kherson (RCSD), whose partners are beneficiaries but not
WP4 pilot leads. Never use the two counts interchangeably in one sentence.

### 3. A pilot-city list in the partner deck is missing Kyiv

`WP4_Partners_Introduction_slides.txt`, slide 3: *"6 pilot cities in Ukraine (Lviv,
Zhytomyr, Khmelnytskyi, Іvano-Frankivsk and Vinnytsia)"* — says six, lists five.
**Resolution:** a typo in that deck. The 1st Periodic Report and the 06.07.2026 WP4
deck both list all six including **Kyiv**. Do not copy that slide's list.

### 4. "Conference (M06)" in Task 4.5

The GA Task 4.5 text says the conference is at "(M06)". That is task-internal
numbering pointing at **Milestone MS6**, which is due **M24**. The conference took
place 24 April 2026 = M24. Reading it as project month 6 (October 2024) is wrong.

### 5. MS6 lead

The GA milestone table leaves MS6's lead cell visually ambiguous, but the amendment
record states: *"Change of lead of Milestone MS6 from LYKUML to KhNU."*
**MS6 is KhNU's milestone.**

### 6. Paper P2 — "submitted" or "published"?

The KhNU annual report (18 June 2026) says "Prepared and submitted" while quoting a
DOI; the 06.07.2026 WP4 deck presents it as a published Q2 Gold OA article with the
same DOI. A DOI of the form `futuretransp6020082` denotes a published article.
**Resolution:** treat P2 as published, but if it matters for a formal record, verify
at <https://doi.org/10.3390/futuretransp6020082> before citing.

### 7. Folder name `U_CAN_Papers_Published`

Contains four LaTeX packages, but P3 (2026-08-13, IET Cyber-Systems and Robotics) and
P4 (2026-09-12, CMES) are **recent submission packages**, not confirmed publications.
Confirm status before describing them as published. See [05](05_Publications.md).

### 8. Name transliterations

"Oleksander Barmak" and "Oleksander Ryzhanskyi" appear as printed in the published
papers; "Oleksandr" also occurs elsewhere. **Use the published spelling when citing a
paper**, and keep one spelling consistent within any single document.
Similarly: Khmelnytskyi (preferred) vs Khmelnitsky / Khmelnytsky — the GA legal name
is "KHMELNITSKY NATIONAL UNIVERSITY", so use that exact string only in legal or
financial contexts, and **Khmelnytskyi National University** everywhere else.

## Not resolvable from the files reviewed

| Item | Status |
|---|---|
| Whether D4.1's "submitted 02/02/2026" was subsequently **accepted** by the EC | Not stated in any reviewed source |
| RP1 periodic-report outcome and the interim payment amount | `U_CAN Funding Distribution_1st interim payment and remaining pre-financing.pdf` is on Drive at `$G/U_CAN_Timesheets/U_CAN_Timesheets_Funding/` — not mirrored (financial) |
| Publication status of P3 and P4 | See item 7 |
| Whether the "dedicated workshop on efficient urban traffic systems" required by Task 4.5 has been held | MS6 conference is documented; a separate dedicated workshop is not evidenced in the reviewed files. **Worth checking before writing D4.5.** |
| The three-year D4.5 scenario set and recommendations | Not yet drafted — that is the remaining work to M39 |

## Source quality ranking

When two sources disagree, prefer the higher entry:

1. **Grant Agreement Annex 2** — arithmetically verifiable, signed
2. **Grant Agreement Data Sheet / Annex 1** — signed, but watch the PDF column drift
3. **Consortium Agreement**
4. **MS6 Conference Report v1.0 (08.06.2026)** and the **KhNU annual report (18.06.2026)** — formal, dated, evidence-backed
5. **WP4 status deck 06.07.2026** — most current status, but presentation-grade
6. Monthly meeting decks and speech scripts — snapshots, drift quickly
7. **ucan-ukraine.eu** — public-facing, least detailed; good for partner slugs and news
8. Archived drafts in `*_Archived/` — superseded by definition

## Maintenance

This KB was compiled **2026-09-13**. Refresh after: each consortium meeting, each
periodic report, each new publication, and any GA amendment. The files most likely to
go stale first are [03](03_Work_Packages.md) (deliverable statuses),
[05](05_Publications.md) (publication statuses) and [06](06_Timeline.md).

## Note on the Dresden trip KB

`../U_CAN_2026-09-14_Dresden/U_CAN_Dresden_KB/01_Trip_Brief.md` calls the project
"U_CAN — Ukraine towards Carbon/Climate Neutrality". The Grant Agreement name is
**"Ukraine towards Carbon Neutrality"** — no "/Climate". The Grant Agreement number
quoted there (101148374) is correct. No other conflict exists between that trip KB
and this global KB; the two are complementary — it covers one visit in depth, this
one covers the project.
