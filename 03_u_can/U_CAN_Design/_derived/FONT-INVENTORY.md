> ## ⛔ SUPERSEDED — do not use as a source of truth
>
> Superseded on **13 September 2026** by design system **v0.2.0**
> (project `a2b22667-6793-404e-821b-d5219760fa3b`). Kept as a working record only.
>
> The **decision** recorded here is superseded: the project adopted **Manrope**
> (OFL, Latin + Cyrillic) rather than Metropolis. The *facts* in this file remain
> accurate and are still the reason Metropolis was rejected — it has **zero**
> Cyrillic glyphs, and Bahnschrift, which has full Cyrillic, is not
> web-redistributable. Re-verified 13 Sep 2026.

# Font inventory — U_CAN

**Task A1.** Every face inside the two archives in `U_CAN_Design/`, read from the
font binaries themselves with fontTools (name table, `OS/2`, `fvar`, `cmap`).

---

## Headline finding

The two archives are **complementary but individually insufficient**:

| | licence allows webfont use | Cyrillic coverage |
|---|---|---|
| `avenir-next-similar-fonts.zip` → **Metropolis** | ✅ SIL OFL 1.1 | ❌ **zero glyphs** |
| `Bahnschrift-Font-Family.zip` → **Bahnschrift** | ❌ Microsoft-supplied | ✅ **complete (256 cp)** |

U_CAN publishes in Ukrainian. Neither archive alone can serve the system, which
is why task A2 cannot be closed by picking one of them. See
[`tokens/fonts.css`](tokens/fonts.css) for the interim stack and the decision block.

---

## Archive 1 — `avenir-next-similar-fonts.zip` (323 KB)

**It is not Avenir Next.** It contains **Metropolis** by Chris Simpson (2015),
a geometric sans in the Avenir/Futura tradition. The archive ships its own
licence file, copied to [`assets/fonts/metropolis/OFL.txt`](assets/fonts/metropolis/OFL.txt):

> Copyright (c) 2015, Chris Simpson, with Reserved Font Name: "Metropolis".
> This Font Software is licensed under the SIL Open Font License, Version 1.1.

OFL 1.1 permits embedding, self-hosting, redistribution and modification, so
this family may be used on the website and in the design system without cost or
negotiation. The Reserved Font Name clause means a *modified* build must be
renamed; the unmodified faces below may keep the name.

18 faces, all `.otf` (CFF outlines), 300 glyphs each, ~22–24 KB each.
Character coverage is identical across every face: **256 Latin codepoints,
0 Greek, 0 Cyrillic.**

| face | file | CSS `font-weight` | style | shipped as WOFF2 |
|---|---|---|---|---|
| Thin | `Metropolis-Thin.otf` | 100 | normal | — |
| Thin Italic | `Metropolis-ThinItalic.otf` | 100 | italic | — |
| Extra Light | `Metropolis-ExtraLight.otf` | 200 | normal | — |
| Extra Light Italic | `Metropolis-ExtraLightItalic.otf` | 200 | italic | — |
| Light | `Metropolis-Light.otf` | 300 | normal | — |
| Light Italic | `Metropolis-LightItalic.otf` | 300 | italic | — |
| **Regular** | `Metropolis-Regular.otf` | **400** | normal | ✅ 15 KB |
| **Regular Italic** | `Metropolis-RegularItalic.otf` | **400** | italic | ✅ 16 KB |
| **Medium** | `Metropolis-Medium.otf` | **500** | normal | ✅ 15 KB |
| Medium Italic | `Metropolis-MediumItalic.otf` | 500 | italic | — |
| **Semi Bold** | `Metropolis-SemiBold.otf` | **600** | normal | ✅ 15 KB |
| Semi Bold Italic | `Metropolis-SemiBoldItalic.otf` | 600 | italic | — |
| **Bold** | `Metropolis-Bold.otf` | **700** | normal | ✅ 15 KB |
| **Bold Italic** | `Metropolis-BoldItalic.otf` | **700** | italic | ✅ 16 KB |
| **Extra Bold** | `Metropolis-ExtraBold.otf` | **800** | normal | ✅ 15 KB |
| Extra Bold Italic | `Metropolis-ExtraBoldItalic.otf` | 800 | italic | — |
| **Black** | `Metropolis-Black.otf` | **900** | normal | ✅ 15 KB |
| Black Italic | `Metropolis-BlackItalic.otf` | 900 | italic | — |

Eight faces were converted to WOFF2 into
[`assets/fonts/metropolis/`](assets/fonts/metropolis/) — **124 KB for the whole
shipped family.** The remaining ten are available in the archive if a weight is
later needed.

### ⚠️ Trap: this family's `OS/2 usWeightClass` is wrong

Eight of the eighteen faces misreport their own weight. A build that reads
`usWeightClass` — as most automated `@font-face` generators do — will produce a
broken weight ladder.

| face | declares | actually is |
|---|---|---|
| Thin / Thin Italic | 400 | 100 |
| Extra Light / Extra Light Italic | 400 | 200 |
| Light / Light Italic | 400 | 300 |
| Medium Italic | 700 | 500 |
| Semi Bold Italic | 700 | 600 |

`tokens/fonts.css` derives every `font-weight` from the **face name**, which is
correct throughout. Keep it that way.

---

## Archive 2 — `Bahnschrift-Font-Family.zip` (2.7 MB)

**15 files, all byte-identical** — md5 `b3483ec650bba4a4416d39c4d6030a99` for
every one of `BAHNSCHRIFT.TTF` and `BAHNSCHRIFT 1..14.TTF`. The archive is one
font duplicated fifteen times; ~2.5 MB of the 2.7 MB is pure redundancy.

The single real font is a **variable font**:

| property | value |
|---|---|
| family | Bahnschrift |
| outlines | TrueType (`glyf`) |
| variable axes | `wght` 300 → **400** → 700 · `wdth` 75 → **100** → 100 |
| glyphs | 836 |
| coverage | Latin 311 · Greek 135 · **Cyrillic 256 + 2 supplement** |
| size | 315 KB |
| `nameID 13` | "Microsoft supplied font. You may use this font to create, display, and print content as pe…" |
| `nameID 14` | http://www.microsoft.com/typography/fonts/ |

Bahnschrift is Microsoft's DIN 1451 interpretation, bundled with Windows 10 and
later. The licence permits *using* the installed font to create and display
content — which is exactly what `Template_Presentation.potx` does — but it does
**not** grant redistribution, so it cannot be shipped as a `.woff2`.

**Practical consequence:** Bahnschrift stays the display face for the Office
templates (`.potx`, `.docx`), where it resolves from the local Windows install.
It must not be copied into a web build. `--font-claim` declares it first and
falls through on non-Windows platforms.

---

## What the source template actually specifies

For completeness, `Template_Presentation.potx` was read directly. Its theme
fonts are **not** the brand fonts:

| slot | value |
|---|---|
| `majorFont` / `minorFont` (themes 1–8) | **Calibri** |
| theme 9 | Aptos / Aptos Display |
| `ea` / `cs` (East-Asian & complex-script) | **Noto Sans SC Regular** |

Run-level font references across the whole template:

| typeface | references |
|---|---|
| Noto Sans SC Regular | 358 |
| Calibri | 204 |
| Times New Roman | 190 |
| DejaVu Sans | 56 |
| Arial | 37 |
| **Avenir Next** | **23** |
| Estrangelo Edessa | 8 |
| Ebrima | 6 |
| Nirmala UI | 4 |

Two things follow:

1. **Avenir Next is a real brand intention** (23 direct run references, and
   `Bahnschrift` appears on the title slide) but it was never the theme font.
   The template's *default* text has always been Calibri.
2. **The `Noto Sans SC` problem is the single largest font reference in the
   file.** Every complex-script and East-Asian run in the template routes to a
   Chinese face. This is task A4, and the evidence is unambiguous.
