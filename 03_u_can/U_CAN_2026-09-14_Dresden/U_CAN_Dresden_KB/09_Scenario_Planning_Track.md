# 09 — The Scenario Planning Track (U_CAN Task T5.5)

Durable knowledge about the Exploratory Scenario Planning strand that runs through the Khmelnytskyi
Adaptive Traffic Management pilot and culminates in the Dresden workshop on 14 September 2026.

> **For the workshop preparation itself** — prepared answers, technical annex, team roles, printable
> cheatsheet — see the dedicated folder `03_u_can/U_CAN_2026-09-14_Scenario-Stress-Testing/`.

---

## 1 · What T5.5 is

**Task 5.5 — Citizen engagement in local climate governance**, delivered through
**Exploratory Scenario Planning (XSP)**, a methodology for navigating uncertainty in the six U_CAN
Ukrainian pilot cities: **Khmelnytskyi, Kyiv, Lviv, Vinnytsia, Zhytomyr, Ivano-Frankivsk**.

**Owner:** Swati Kulashri, TU Dresden, WISSENSARCHITEKTUR – Laboratory of Knowledge Architecture.
**Work package:** WP5.

XSP does not predict one future; it prepares for several. Its design principles: plausible futures,
uncertainty-first, participatory, action-oriented, iterative. The rationale for using it in Ukraine is
compounding uncertainty — armed conflict, dual-transition pressure (post-war recovery plus EU climate
integration), climate uncertainty, and a citizen-engagement gap where traditional participation breaks
down but buy-in is essential.

---

## 2 · The three stages, and Khmelnytskyi's progress

| Stage | Purpose | Khmelnytskyi date | Output |
|---|---|---|---|
| **01 Scenario Mapping** | Map uncertainties, vulnerable groups, stakeholders; assess readiness; define 2×2 axes | **1 April 2026**, 12:00–13:30 CET, Zoom + Miro | Shared scenario matrix |
| **02 Scenario Building** | Construct 4 plausible future narratives | **L'Aquila Consortium Meeting, 6–8 July 2026**, in person, A0 sheets | 4 narrative scenarios |
| **03 Scenario Testing** | Stress-test plans against all futures | **14 September 2026, Dresden, BZW Wing B, 15:00–16:30** | Robustness matrix and recommendations |

Stakeholder engagement is embedded in all three stages as a core design feature, not an add-on.

---

## 3 · The 2×2 that everything now hangs on

Selected at Stage I, used to build the scenarios at Stage II, stress-tested at Stage III.

- **Uncertainty 1 — AI Infrastructure Affordability:** affordable AI systems and infrastructure deployment **vs.** high implementation and infrastructure costs.
  *Rationale:* the workshop identified the high cost of AI systems, computing infrastructure and local data storage as a major barrier to implementing and scaling AI-enabled municipal services.
- **Uncertainty 2 — Long-term Funding Security:** stable long-term funding and investment **vs.** dependence on short-term external funding.
  *Rationale:* scaling the pilot depends on securing sustainable funding beyond externally funded projects and grants.

|  | **Strong funding security** | **Weak funding security** |
|---|---|---|
| **High affordability** | **Scenario A** | **Scenario B** |
| **Low affordability** | **Scenario C** | **Scenario D** |

**Three questions asked of each scenario at Stage II:**
1. *What does this future look like for the pilot?* — future conditions and implications
2. *What would be needed to make this successful?* — implementation and institutionalisation
3. *What should the city start doing today?* — preparation and immediate actions

**Three questions asked of each scenario at Stage III (the shock round):**
1. *What breaks?* 2. *What still works?* 3. *What should we change now?*

**The Stage III shock:** *Can adaptive traffic systems continue if AI/digital technologies become
unavailable, unaffordable, or technically unreliable?*

---

## 4 · The URI assessment frame

Cross-scenario reflection is scored against seven **Urban Readiness Index** dimensions:

| # | Dimension | Covers |
|---|---|---|
| 1 | **Vision & Strategic** | vision, political commitment, EU alignment, environmental policy, pilot readiness |
| 2 | **Regulatory & Planning** | climate legislation, master planning, zoning, transport planning, waste systems |
| 3 | **Institutional & Technical** | institutions, risk assessment, project delivery, digital systems, research partnerships |
| 4 | **Financial & Economic** | municipal finance, EU funding track record, diverse green economy, industry transition, PPPs for climate |
| 5 | **Innovation & Infrastructure** | infrastructure base, renewables, efficiency/retrofit programmes, circular systems, innovation ecosystems |
| 6 | **Civic & Stakeholder** | citizen engagement, public awareness, participation tools, education/skills, NGOs |
| 7 | **Conflict Impact & Recovery** | conflict exposure, damage assessment, recovery planning, adaptation strategy, heritage protection |

---

## 5 · Stage I findings (the evidence base)

**Critical uncertainties:** availability of financial resources · prioritisation of mobility vs recovery
needs · data infrastructure and system integration · long-term operational feasibility of AI systems.

**Structural barrier:** lack of an integrated data-governance system (a *"one umbrella system"*) and
coordination across municipal departments; data access requires manual coordination; responsibility
allocation between departments is unclear.

**Regulatory position:** AI systems are not yet embedded in formal policy frameworks; current effort
focuses on data *collection* (GPS, e-ticketing) rather than AI *control*.

**Social and security:** public acceptance is generally positive (2024 surveys and consultations) but
conditional on trust in data use and prior consultation. New concerns: privacy and surveillance; data
security during wartime; city-level vulnerability to data misuse by hostile actors; security risks from
camera data.

**Financial:** heavy reliance on external funding (EBRD, EU), not structurally embedded. Major gaps in
secure data centres, AI system costs (software + hardware), and operational expertise and staffing.
**Critical insight recorded from the City side: the city budget is redirected to military priorities.**
Stated requirement for **secure/local data storage — not cloud-based abroad**.

**Enablers:** strong existing mobility planning (SUMP, modelling tools) · transport simulation used before
implementation · active EBRD funding and international cooperation · data-driven policy ambition ·
positioning Khmelnytskyi as a knowledge hub for sustainable transport in Ukraine.

**Priority stakeholders:** KhNU (lead research and technical development) · Khmelnytskyi City Council and
municipal transport departments · local NGOs and citizen associations · community groups including daily
commuters and local business · smart technology companies and AI providers · national and regional
transport and environmental authorities · Ministry of Transport of Ukraine · big business and SMEs ·
large logistics companies · consulting firms developing transport models · international financial
institutions (EBRD) · security services influencing data governance.

**Vulnerable groups:** veterans, elderly people, people with disabilities · IDPs · daily commuters
dependent on affordable and efficient mobility · war-affected communities · privacy-sensitive groups
affected by surveillance · residents appearing on video · residents of high-traffic zones exposed to air
pollution and noise · youth and students · small business.

---

## 6 · The pilot being tested

**Khmelnytskyi Adaptive Traffic Management** — 267,891 residents, 20.6 km².

**Problem:** static traffic management does not respond to real road conditions, ignores terrain, and does
not optimise flows in real time — causing congestion and elevated CO₂.

**Current state:** fixed signal cycles, no real-time sensors, no integration between control nodes,
cameras present but software not integrated, terrain not accounted for. AI integration is impossible
without replacing hardware.

**Required for AI control:** controllers with open API · sensors and cameras at intersections ·
communication network between nodes · real-time data processing platform · topographic module.

**Research foundation** (both validated on a SUMO digital twin — 15 intersections, 45.7 km):
- *Future Transportation* **2025** — HDBSCAN + k-means adaptive ML for traffic pattern recognition:
  V-measure **0.79–0.82**, identification accuracy **95 %**, temporal coherence **0.94**
- *Future Transportation* **2026** — topography-aware deep learning (DRL + CSRD):
  **−8.6 % CO₂** vs Max-Pressure, **−4.7 % CO₂** vs standard DQN

**Phases:** 0 Now (technical specifications) → 1 Platform (unified digital platform, connectivity
standards, control centre, secured network) → 2 Data (cameras and counters; database of intensity, flow
composition, peak hours) → 3 Pilot (algorithms at 3–5 intersections; measure CO₂ and trip duration) →
4 Scale (all intersections + Management Centre; model for other Ukrainian and EU cities).

**Governing principle:** with any replacement or repair, install AI-compatible equipment; **new
controllers only with open API**. Embed into the City Transport Plan, the Recovery Plan and municipal
Procurement Standards, with **KhNU as a permanent technical partner**.

---

## 7 · Pavlo Radiuk's role in this track

- Presented the pilot introduction at the **Scenario Mapping workshop** (1 April 2026) and circulated the deck afterwards.
- Participated in the **Scenario Building workshop** at L'Aquila with the **Deputy Mayor of Khmelnytskyi** — the pair who actually produced the four futures.
- Named in the Dresden FINAL agenda as owner of the Day-02 topic *U_CAN pilot project on Adaptive Traffic Management*.
- Principal technical respondent at the **Scenario Stress-Testing workshop** on 14 September 2026.

---

## 8 · Known gaps and cautions

| Item | Status |
|---|---|
| **Filled-in Stage II scenario narratives** | **Not circulated by e-mail.** They exist on the L'Aquila A0 sheets and in Swati's records. Swati will re-summarise them at the start of the Dresden session. Any scenario text we hold is reconstruction from the axes + Stage I evidence, not quotation. |
| Header error in the Stage I synthesis | `Khmelnytskyi_Scenario_Mapping_Summary.docx` is headed *"Exploratory Scenario Planning with Ivano-Frankivsk"* — a template copy-paste slip. Content is entirely Khmelnytskyi. |
| Miro boards | Two links are in circulation: `uXjVGsbe0zk` (main) and `uXjVGukeh5g`. Swati added Zoom-transcription points in **pink** after the session. |
| Interpretation | The Dresden session is **not** marked `[DE-UA]` in the agenda — it runs in English, unlike most other programme items. |

---

## 9 · Source trail

| Date | Source | Content |
|---|---|---|
| 2026-03-09 | Thread `19cd448203d19d5e` | *U_CAN — Next step for pilot scenario planning (Task 5.5)* |
| 2026-03-25 → 03-31 | Threads `19d25eabe020bb2d`, `19d2e94e250bade0` | Scheduling of the Scenario Mapping workshop; Radka confirms LYKUML is **not** invited as the topic is transport-pilot specific |
| 2026-03-31 | Thread `19d4588616bae2ae` | Swati's reminder with Zoom + Miro links; Kateryna Skyba confirms Transport Department participation and an interpreter; Pavlo has the deck ready |
| 2026-04-01 | Pavlo → all, same thread | Thank-you note + `SMW_Khmelnytskyi_Pilot_UCAN_EN.pptx` |
| 2026-04-07 | Swati → all, same thread | **Stage I synthesis** + Miro export; announces Stage II at L'Aquila |
| 2026-06-30 | Thread `19f176d2a3692617` | Swati sends the **six A0 Scenario Building templates** (one per pilot city) for printing; Kateryna forwards to Pavlo and Eduard |
| 2026-07-06/08 | L'Aquila Consortium Meeting | **Scenario Building workshop** — Pavlo + Deputy Mayor produce the four futures |
| 2026-09-09 | Thread `1a0827a57cbba97d` | **Swati's stress-testing briefing** — the shock, the three questions, the tri-partner framing, the end goal |

**Local materials:** `G:\My Drive\Work\Work_RnD\RnD_U_CAN\U_CAN_2026-04-01_U_CAN-SMW` — copies staged in
`03_u_can/U_CAN_2026-09-14_Scenario-Stress-Testing/Source_Files/`.
