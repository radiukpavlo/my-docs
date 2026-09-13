# 04 — The KhNU Pilot (Task 4.5 / D4.5)

**Official pilot title:**
*Khmelnytskyi Pilot — Adaptive traffic management with emphasis on transport-related
CO₂ reduction.*

KhNU is **beneficiary 18**, lead of **Deliverable D4.5** and of **Milestone MS6**,
working with Khmelnytskyi City Council (KhCC) and, inside Task 4.5, with LYKUML,
OMB, ENV and LHD.

## Mandate, verbatim from the Grant Agreement

> Task 4.5: Climate-neutral pilot activities in Khmelnytskyi — M13–M42; KhNU
> (LYKUML, OMB, ENV, LHD). KhNU and LYKUML along with the Khmelnytskyi City Council
> will conduct two activities in the city of Khmelnytskyi. The first is concerned
> with dissemination activities for knowledge sharing related to CO₂ emissions
> reduction in cities that are working towards climate neutrality including a
> conference (M06) to bring together multiple Ukrainian cities and key stakeholders
> involved in the transport sector; and one dedicated workshop to discuss efficient
> urban traffic systems. The second is the development of a centre for the support
> of local policies in the field of climate-neutral construction and energy.

**D4.5 — Implementation Plan Khmelnytskyi.** Lead 18 — KhNU. Type: R — Document,
report. Dissemination level: **PU — Public**. Due **Month 39** (July 2027). WP4.

> **Note on "(M06)"** in the GA text: this is the *task-internal* numbering for the
> conference, and it maps to project **Milestone MS6**, due M24. The conference was
> held on **24 April 2026**, which is M24. Do not read "(M06)" as month 6.

## The two strands

**Strand A — KhNU: adaptive traffic management.**
Responds to static traffic-light control, peak-hour congestion, inefficient flow,
idling and the associated emissions. Supports the city in understanding the
technical, organisational, data and policy prerequisites for future adaptive traffic
management.

**Strand B — LYKUML: Centre for Support of Local Policies in the Field of Developing
Climate Neutrality and Energy.** Opened **24 October 2026**. Workshops delivered:
"The Role of Green Innovations…" (29–30 Jan 2026); "Climate-Neutral Waste Management…"
with the eco-startup *Trash → Cash* and a Gufi Center excursion (25–27 Feb 2026);
"Energy Efficiency in Martial Law" (21 May 2026). Partners: Energy Management
Department and Department for Ecology of Khmelnytskyi City Council, Office "Smart
Environment". Public channel: the **"Ecopulse"** Facebook page.

## Objectives of Task 4.5 (as reported)

1. Define the technical and data prerequisites for adaptive traffic management in Khmelnytskyi.
2. Scientifically validate traffic-pattern recognition and adaptive signal-control approaches using simulation and local-context data.
3. Consolidate the climate and transport indicators needed to assess future impacts on CO₂ emissions, traffic queues, idling time and trip duration.
4. Support knowledge exchange between KhNU, municipal authorities and mobility-planning stakeholders.
5. Deliver the dissemination activities of Task 4.5, including the MS6 conference.
6. Build a robust evidence base for D4.5, including implementation scenarios and scale-up recommendations.

## Results achieved (reporting period May 2025 – June 2026)

### Scientific validation
- **Gold Open Access Q2 article** on adaptive machine learning for sustainable traffic
  planning — HDBSCAN + k-means for high-fidelity traffic-pattern recognition.
  Validated on a **Khmelnytskyi transport-network simulation**;
  **scenario-identification accuracy ≈ 92.8–95.0 %**.
  <https://doi.org/10.3390/futuretransp5040152>
- **Gold Open Access Q2 article** on topography-aware deep reinforcement learning with
  contextual reward engineering, SUMO-based signal control.
  Simulated **CO₂ reduction potential up to 8.6 %** vs a Max-Pressure baseline and
  **4.7 %** vs standard DQN. <https://doi.org/10.3390/futuretransp6020082>
- Technical-deck simulation indicators: **14 800 vehicles**, **9-hour horizon**,
  **20 % heavy-vehicle share**, **72.09 s** mean trip duration, **1.31** queue length.

### Municipal cooperation, data and modelling capacity
- Ongoing cooperation with Khmelnytskyi City Council on communication, climate
  indicators, transport-data needs and future integration into sustainable mobility policy.
- Collected and processed climate and transport indicators for Khmelnytskyi, including
  public-transport speed, electric-transport share and vehicle-idling indicators.
- **PTV Visum training cycle, 20–22 January 2026**, with Khmelnytskyi City Council:
  network construction, four-step demand modelling, calibration, validation,
  visualisation, scenario planning, O-D and cost matrices, TFlowFuzzy, GEH statistic.

### Dissemination and reporting
- Delivered **MS6**: International Conference *"Reducing CO₂ Emissions in Ukrainian
  Cities: Pathways to Climate Neutrality"*, KhNU, **24 April 2026**, hybrid
  (in person at KhNU + Zoom).
- Prepared the MS6 evidence package and report by June 2026.
- Participated in WP4 and consortium meetings, the Standardization Workshop, USRA
  thematic workshops, CEEC XIX (Bratislava), EIT Urban Mobility activities, the
  Scenario Mapping Workshop, Clotex D-FEST and "Energy Efficiency in Martial Law".

### MS6 evidence base (auditable figures)
Approved bilingual agenda · public conference website · KhNU public news post ·
**44 registration records** · **25 feedback responses** collected 7 May – 4 June 2026 ·
**20 named speaker records** · photographs · QR-code materials · local video files.
Conference report **v1.0, 08/06/2026**.

## Status and risks

- **D4.5 is not submitted.** Correct phrasing: *"the implementation-plan evidence base
  was established; final D4.5 is scheduled for Month 39."*
- Main difficulty in the period: the time needed to obtain and consolidate
  transport data held across different municipal departments — additional
  coordination was occasionally required.
- **As of June 2026 there are no confirmed missed deadlines.** Minor data-collection
  delays did not affect the overall schedule.

## ⚠️ The one claim you must never make

All CO₂ figures from KhNU are **simulation-based potential** under a validated
modelling framework. **Do not state that real-world CO₂ emissions in Khmelnytskyi
have been reduced.** Use: *"estimated potential CO₂ reduction of up to 8.6 % under
the validated simulation framework"*. This constraint is written into the U_CAN
slide-generation playbooks and must survive into every derived slide, script or pitch.

## KhNU people

Department of Computer Science, Khmelnytskyi National University,
11 Instytutska Street, 29016 Khmelnytskyi, Ukraine.

| Person | Role / e-mail |
|---|---|
| **Pavlo Radiuk** | Corresponding author; presenter at consortium meetings — radiukp@khmnu.edu.ua, tel. +380-97-854-9146 |
| **Oleksander Barmak** | Co-author — barmako@khmnu.edu.ua |
| **Eduard Manziuk** | Co-author; Dresden delegation — manziuk.e@khmnu.edu.ua |
| **Oleksander Ryzhanskyi** | Lead author, topography-aware DRL — oryzhanskyi@khmnu.edu.ua |
| **Iurii Krak** | Co-author — Taras Shevchenko National University of Kyiv / V.M. Glushkov Institute of Cybernetics |
| **Kateryna Skyba** | Team member (timesheet records 2025) |

Related: KhNU also appears as co-lead of **MS5** (Indicators for climate neutrality
in pilot activities, M18) together with OMB and CIL.
