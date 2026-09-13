# 07 — Boilerplate: copy-paste blocks

Everything here is either verbatim from an approved U_CAN document or composed
strictly from verified facts in [01](01_Project_Facts.md)–[05](05_Publications.md).

## Mandatory EU statements

**Funding statement (slides, posters, reports) — CINEA variant, used on WP decks:**
> Funded under HORIZON-MISS-2023-CIT-02 call, GA 101148374. Views and opinions
> expressed are however those of the author(s) only and do not necessarily reflect
> those of the European Union or CINEA. Neither the European Union nor the granting
> authority can be held responsible for them.

**Disclaimer — European Commission variant, used on deliverables and reports:**
> Funded by the European Union. Views and opinions expressed are, however, those of
> the author(s) only and do not necessarily reflect those of the European Union or
> European Commission. Neither the European Union nor the European Commission can be
> held responsible for them.

**Acknowledgement (journal papers):**
> The U_CAN project has received funding from the European Union's Horizon Europe
> Framework Programme for Research and Innovation under grant agreement No. 101148374.

**Copyright notice (deliverables and reports):**
> © 2026 U_CAN Consortium. All rights reserved. No copying or distributing in any
> form or by any means is allowed without the prior written agreement. In addition to
> such written permission, the source must be clearly referenced.

**Liability clause (deliverables):**
> All U_CAN Consortium members are also committed to publish accurate and up to date
> information and take the greatest care to do so. However, the Consortium members
> cannot accept liability for any direct, indirect, special, consequential or other
> losses or damages of any kind arising out of the use of this information.

The EU emblem must appear with the funding statement. Assets:
`../U_CAN_Design/Logos/EU logos/` (EN and UA, horizontal and vertical, RGB PNG) and
the Cities Mission banner in
`../U_CAN_Design/Logos/EU Emblem and Cities Mission banner/`.

## Pitches

**One line.**
> U_CAN is a €5 million Horizon Europe mission project helping eight Ukrainian cities
> build practical, standards-aligned pathways to climate neutrality — with Dresden as
> their EU Mission City partner.

**Thirty seconds.**
> U_CAN — Ukraine towards Carbon Neutrality — is a Horizon Europe Coordination and
> Support Action running from May 2024 to April 2028 under grant agreement 101148374.
> Twenty-one partners across ten countries, coordinated by TU Dresden, work with a
> core group of eight Ukrainian cities on a bottom-up route to climate neutrality:
> vision workshops, road mapping and stakeholder co-creation, twinning with European
> Mission Cities, and then real pilot implementation in six of them — Lviv, Kyiv,
> Zhytomyr, Khmelnytskyi, Ivano-Frankivsk and Vinnytsia. In wartime conditions,
> co-creation and Citizen Science keep the work needs-oriented rather than top-down.

**Two minutes — KhNU's own story.**
> Khmelnytskyi National University leads the Khmelnytskyi pilot in Work Package 4.
> Our theme is adaptive traffic management with emphasis on transport-related CO₂
> reduction. The city runs static traffic-light control: fixed timings, peak-hour
> congestion, long queues, a great deal of idling — and idling is where urban
> transport emissions quietly accumulate.
>
> Our approach was to earn the right to recommend a change before recommending it.
> First we asked whether the city's traffic even has recognisable recurring regimes.
> It does: using HDBSCAN and k-means on a Khmelnytskyi network simulation, we
> identify the active scenario with 92.8 to 95 per cent accuracy — that is our first
> Q2 Gold Open Access paper. Then we asked what a controller should optimise. Most
> reinforcement-learning models silently assume flat terrain, which hides the energy
> penalty of heavy vehicles restarting uphill. Our topography-aware framework with
> contextual reward design closes that gap, and in simulation yields up to 8.6 per
> cent lower CO₂ than a max-pressure baseline and 4.7 per cent lower than a standard
> DQN — the second Q2 paper.
>
> Alongside the science we built municipal capacity: a three-day PTV Visum modelling
> cycle in January 2026 with the City Council, covering demand modelling, calibration
> and scenario planning, and a continuing working relationship with the Department of
> Transport Infrastructure. In April 2026 we delivered Milestone 6 for the whole
> consortium — an international hybrid conference on reducing CO₂ emissions in
> Ukrainian cities, twenty speakers, forty-four registrations, fully documented.
>
> These results are simulation-based potential, not emissions already avoided. That
> distinction matters, and it is exactly why the next step is the sim-to-real work:
> proving the controller holds up against noisy computer-vision input from real street
> cameras. All of it feeds Deliverable 4.5, the Implementation Plan for Khmelnytskyi,
> due in July 2027.

## Speaker bio — Pavlo Radiuk

> **Pavlo Radiuk** is a researcher at the Department of Computer Science,
> Khmelnytskyi National University, and a member of the U_CAN project team
> (Horizon Europe, GA 101148374), where KhNU leads Task 4.5 and Deliverable 4.5 —
> the Implementation Plan for Khmelnytskyi. His work applies machine learning and
> deep reinforcement learning to adaptive urban traffic signal control for
> transport-related CO₂ reduction, published in *Future Transportation* (Gold Open
> Access, Q2). He coordinated Milestone MS6, the international conference "Reducing
> CO₂ Emissions in Ukrainian Cities: Pathways to Climate Neutrality" (KhNU, April
> 2026). ORCID 0000-0003-3609-112X · radiukp@khmnu.edu.ua

## House style

| Rule | Value |
|---|---|
| Language | **English (British)** — modelling, organisation, programme, optimisation, prioritisation, standardisation, mobilisation |
| Font | **Avenir** family throughout (substitutes: `../U_CAN_Design/avenir-next-similar-fonts.zip`; Bahnschrift also supplied) |
| Slide format | 16:9 widescreen |
| Palette | U_CAN blue / green / yellow |
| Slide layout | Left: white area with U_CAN identity, city or evidence imagery. Top-left: blue title band with **yellow** title text. Right: pale green content panel with **blue** body text. Green leaf decoration where appropriate. |
| Density | Concise bullets, short labels, compact evidence blocks. Never overcrowd. |
| Images | Real visuals from source files only. Never invent photographs, icons, metrics or results. Crop carefully; never stretch. |
| Closing slide | Funding statement + disclaimer (CINEA variant above) |

## Naming conventions in this project

- Events: `U_CAN_YYYY-MM-DD_EventName/`
- Documents: `U_CAN_<Event>_<NN>_<YYYY-MM-DD>_<Type>.<ext>`
- Superseded work goes into a sibling `*_Archived/` folder, never deleted
- Prompts: `U_CAN_Prompt_<NN>_<Topic>_<vN-basic|vN-system>.docx`
- Ukrainian internal paperwork keeps Ukrainian names: Подання, Витяг, Заява,
  Службова, Мета, Наказ, Дозвіл, Резерв+

## Phrases to get right

| Say | Not |
|---|---|
| "estimated potential CO₂ reduction under the validated simulation framework" | "we reduced CO₂ in Khmelnytskyi" |
| "the D4.5 evidence base was established / advanced" | "D4.5 was delivered" |
| "six WP4 pilot cities" / "a core group of eight Ukrainian cities" | mixing the two counts |
| "Khmelnytskyi National University (KhNU), beneficiary 18" | "partner 18" |
| "MS6, delivered 24 April 2026" | "the M06 conference" |
