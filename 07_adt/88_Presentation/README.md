# CMR audit presentation - editorial revision

Ten static Beamer frames in American English, 16:9, on a 240 by 135 mm canvas. The first version's navy/teal design, white background, rectangular cards, and supplied identities are preserved.

## Build

Run from `88_Presentation`:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

For a forced rebuild after moving the folder, add `-g`. The generated PDF and current compilation log are `build/main.pdf` and `build/main.log`; `presentation.pdf` is the delivery copy. Open `main.tex` in a LaTeX editor or upload the whole project to Overleaf with pdfLaTeX. A current MiKTeX or TeX Live installation with Beamer, Helvetica, Latin Modern, TikZ, amsmath, booktabs, tabularx, makecell, and textcomp is sufficient. No shell escape, network resources, or bibliography processor is required.

## Scientific content and numbering

The source is `../88_Submission/Radiuk_Auditing-Deep-Learning_revised.zip`. All numerical table entries, ten numbered equations, and 25 semantic label keys are retained. Displayed table numbers follow presentation order:

- Slide 1: title, authors, affiliations, CMR expansion, ADT-ISMDDC @ ICST-ODESA.
- Slide 2: Tables 1-2 (manuscript Tables 8-9), comparison context, highlight legend, full Bernard reference.
- Slide 3: Table 3 (manuscript Table 1), purpose, cohort names, and QC.
- Slide 4: original Figure 1, Algorithm 1, and explicit WEDD-versus-tertiles clarification.
- Slide 5: Equations 1-4, transition fitting and tertile states.
- Slide 6: Equations 5-7, production rules, guarded inference, and predicate alignment.
- Slide 7: Tables 4-5 (manuscript Tables 2-3), Figures 2-3, Equation 8, reconstruction errors and external shift.
- Slide 8: Tables 6-7 (manuscript Tables 4-5), Figure 4, comparator and selective rule results.
- Slide 9: Tables 8-9 (manuscript Tables 6-7), embedded Figure 5, Equations 9-10.
- Slide 10: conclusions, limitations, contacts, affiliations, and supplied supporting identities.

Abbreviations expanded in the slides include CMR, ACDC, M&Ms, WEDD, NRMSE, SD, MAE, BCa, CI, AUROC, ECE, QC, ED, pp, HCM, DCM, MI, and ARVC. Cross-validation is written out. The evaluated representation is deterministic image-mask descriptors, not a trained deep encoder. The evaluated discretizer substitutes training tertiles for the full WEDD block of the framework. Similarity is not clinician agreement; proxies support review rather than diagnosis. Domain shift, mixed-unit summaries, selective coverage, and incomplete clinical validation remain explicit.

## Typography and visual conventions

All ten numbered equations use one `mathsize` definition: 13.2 TeX pt with 15.6 pt leading. This intermediate size reconciles the previously mixed 14.5/12.4 pt equations. Equation 4 reserves the card's right padding; Equation 6 now ends with a period; Equation 7 wraps without scaling.

Actual body and card text uses 12.4 pt, selected by `small` at frame entry. Tables and the slide 4 sidebar use 11.5 pt; notes, captions, chart labels, and footers use 10.5 pt. Headings use 21.5 pt, the title 25.5 pt, and the title-slide author line 14.5 pt. The defined 14.5 pt `normalsize` is not the slide-body size. These are absolute TeX points on a 240 mm canvas. At the same relative size on a standard 13.333-inch-wide PowerPoint canvas, 12.4 pt is approximately 17.4 pt and 10.5 pt approximately 14.8 pt. Dense evidence notes therefore remain at the compact end of projection typography.

Numerals in tables, prose, captions, cards, and chart labels use the surrounding Helvetica text face. Mathematical terms such as r, n, x, y, and lambda retain mathematical notation; numerical constants within complete equations remain mathematical. Signed prose values and both degree signs on slide 9 use text-mode symbols. Tables and native chart labels are not downscaled.

Table highlights have one documented meaning: blue for reported results, amber for guarded abstention, rose for selected error/drift flags, and green for proxy evidence. Repeated accuracy and coverage values use the same blue shading. Figure 4 presents coverage and abstention as complementary segments of one 100% decision bar; its remaining bars show performance, not a second redundant abstention outcome.

## Figures, reading order, and provenance

Figure 1 embeds the supplied architecture PDF. Only its redundant baked-in top title is clipped at display time; the original file is unchanged. Its source typography is intentionally preserved to retain the manuscript figure. The caption explains that the evaluated release substitutes training tertiles for the weighted entropy-density discretization block. Native Helvetica slide elements frame the figure.

Figures 2-4 are editable TikZ charts. Table 8 explicitly says "Table 8 with embedded Figure 5." Its common-scale similarity bars are 22 by 2.8 mm, enlarged from 10 by 1.8 mm. Full unsupported-family names are retained in the adjacent note. All five original figure PDFs remain in `figures/`.

Table 2 uses individually labeled correlation and bias rows, ordered LVEDV, LVEF, RVEF, then mass, matching Table 1's shared indices. Removing stacked makecell values improves PDF text extraction. Extraction was checked for row-label/value order; PDF readers may still differ in how they paste tables.

Only `content/equations-9-10.tex` supplies Equations 9-10. The superseded individual files and unused hatB/pair macros are removed. Footer totals use `inserttotalframenumber`. A fresh build records the current `88_Presentation` path.

## Reference

O. Bernard et al. "Deep Learning Techniques for Automatic MRI Cardiac Multi-Structures Segmentation and Diagnosis: Is the Problem Solved?" *IEEE Transactions on Medical Imaging*, 37(11):2514-2525, 2018. [DOI: 10.1109/TMI.2018.2837502](https://doi.org/10.1109/TMI.2018.2837502). [Indexed article record](https://pubmed.ncbi.nlm.nih.gov/29994302/).

The M&Ms cohort name is consistent with the [challenge paper](https://pubmed.ncbi.nlm.nih.gov/34138702/). These sources support nomenclature and bibliographic details; they do not turn the deck's cross-protocol comparisons into controlled rankings.

## Theme and delivery

Adapted from `87_Pres_v0.1.zip`. The KhNU theme files and `theme-original/` preserve Michael Wiedau's notices and [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). ADT-ISMDDC appears on slides 2-10; CEUR-WS, CS, ICST, and KhNU identities appear beneath the affiliations on slide 10. All ten pages are static. TikZ's title-placement overlay is not an incremental Beamer overlay.

The delivery archive is `../88_Presentation.zip`. The pre-review project is preserved in `../_presentation_work/88-before-editorial-review.zip`. RTK was used for build orchestration; all task-created files remain under `07_adt`.
