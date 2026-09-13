# Briefing — background to the Scenario Stress-Testing Workshop

Read once. Everything here is evidenced from the mailbox and from
`G:\My Drive\Work\Work_RnD\RnD_U_CAN\U_CAN_2026-04-01_U_CAN-SMW`.

---

## 1 · Where this workshop sits

This is **Stage III of Exploratory Scenario Planning (XSP)** under U_CAN **Task T5.5**
(*Citizen engagement in local climate governance*), applied to the Khmelnytskyi pilot
**Adaptive Traffic Management System**.

| Stage | What it does | When, for Khmelnytskyi | Output |
|---|---|---|---|
| **01 · Scenario Mapping** | Map key uncertainties, vulnerable groups and stakeholders; assess city readiness; define the 2×2 axes | **1 April 2026**, 12:00–13:30 CET, Zoom + Miro | Shared scenario matrix |
| **02 · Scenario Building** | Construct 4 plausible future narratives | **L'Aquila Consortium Meeting, 6–8 July 2026**, in person, A0 sheets | 4 narrative scenarios |
| **03 · Scenario Testing** | Stress-test plans against all futures | **14 September 2026, Dresden** ← *this session* | Robustness matrix and recommendations |

XSP principles, from Swati's methodology deck: plausible futures rather than one forecast ·
uncertainty-first · participatory · action-oriented · iterative. The same three-step method runs
across all six U_CAN pilot cities (Khmelnytskyi, Kyiv, Lviv, Vinnytsia, Zhytomyr, Ivano-Frankivsk).

---

## 2 · The pilot in brief

**Problem.** Static traffic management systems do not respond to real road conditions, do not account
for city terrain, and do not optimise flows in real time — causing congestion and elevated CO₂.

**Approach.** Smart sensors and cameras for real-time data · AI for pattern recognition and adaptive
control · flow optimisation for fewer stops and lower emissions.

**Current state (the honest starting point).** Khmelnytskyi's traffic management system is technically
obsolete: fixed signal cycles with no adaptation, no real-time sensors and problematic data collection,
no integration between control nodes, terrain not taken into account. Cameras exist but their software
is not integrated with traffic management. Integrating AI is impossible without replacing hardware.

**What is needed for AI control:** controllers with open API · sensors and cameras at intersections ·
a communication network between nodes · a real-time data processing platform · a topographic module.

**Scientific foundation (both validated on the SUMO digital twin of Khmelnytskyi — 15 intersections, 45.7 km):**
- *Future Transportation*, **2025** — adaptive ML for traffic pattern recognition (HDBSCAN + k-means): V-measure **0.79–0.82**, identification accuracy **95 %**, temporal coherence **0.94**
- *Future Transportation*, **2026** — topography-aware deep learning (DRL + CSRD): **−8.6 % CO₂** vs Max-Pressure, **−4.7 % CO₂** vs standard DQN

**Phased roadmap — foundation first, then the building:**

| Phase | What we do | Outcome |
|---|---|---|
| **0 · Now** | Document current state, define the problem, write technical specifications | Technical Specifications |
| **1 · Platform** | Unified digital platform, connectivity standards, control centre, secured network | Future-proof Foundation |
| **2 · Data** | Cameras and counters at key intersections; database of traffic intensity, flow composition, peak hours | Real Database |
| **3 · Pilot** | Algorithms at 3–5 intersections; measure actual CO₂ reduction and trip duration | First Real Results |
| **4 · Scale** | Expansion to all intersections + Management Centre; model for other Ukrainian and EU cities | Full AI System |

**Governing principle:** *with any replacement or repair, install AI-compatible equipment* — not all at
once, but right from the start. **New controllers only with open API.** Embed into the City Transport
Plan, the Recovery Plan and municipal Procurement Standards, with KhNU as a permanent technical partner.

> **This phased structure is the strongest card in the workshop.** The pilot was already designed so that
> the AI layer sits on top of layers that hold their value without AI. The stress test does not invalidate
> the plan — it validates the sequencing.

---

## 3 · What Stage I (Scenario Mapping) established

From Swati's synthesis of 7 April 2026 and the Miro board.

**Critical uncertainties identified:**
- availability of financial resources
- prioritisation of mobility vs recovery needs
- data infrastructure and system integration
- long-term operational feasibility of AI systems

**System and governance challenges.** The key structural barrier is the **lack of integrated data
governance and coordination across municipal departments** ("one umbrella system"), limiting effective
use of real-time data. Data access requires manual coordination. Regulatory frameworks for AI-based
traffic systems are still emerging, with current effort focused on **data collection (GPS, e-ticketing)
rather than system-wide AI optimisation**. Responsibility allocation between departments is unclear.

**Social and security dimensions.** Public acceptance is generally positive, supported by previous
surveys and consultations (2024, with legitimate firms) — but it depends on **trust in data use and
prior consultation**. The pilot introduces new concerns: privacy and surveillance; data security during
wartime; city-level vulnerability to data misuse by hostile actors; security risks from camera data.

**Infrastructure and financial constraints.** Scaling requires significant investment in sensors and
monitoring, data infrastructure and storage, and traffic control centres. Major gaps in: secure data
centres · AI system costs (software + hardware) · operational expertise and staffing. Funding relies
heavily on external sources (EBRD, EU) and is **not yet structurally embedded**. A **critical insight
recorded from the City side: the city budget is redirected to military priorities.** There is a stated
need for **secure/local data storage — not cloud-based abroad** — and concern about the operational
complexity of AI systems (subscriptions, maintenance).

**Enablers already in place:** strong existing mobility planning (SUMP, modelling tools) · use of
transport simulation models before implementation · active EBRD funding and international cooperation ·
data-driven policy ambition · positioning Khmelnytskyi as a knowledge hub for sustainable transport.

**Priority stakeholders:** KhNU (lead research and technical development) · Khmelnytskyi City Council and
municipal transport departments · local NGOs and citizen associations · community groups including daily
commuters and local business · smart technology companies and AI providers · national and regional
transport and environmental authorities · Ministry of Transport of Ukraine · big business and SMEs ·
large logistics companies (Nova Post-type actors) · consulting firms developing transport models ·
international financial institutions (EBRD) · security services influencing data governance.

**Vulnerable groups to include:** veterans, elderly people (pensioners), people with disabilities · IDPs ·
daily commuters dependent on affordable and efficient mobility · war-affected communities relying on
resilient mobility · privacy-sensitive groups affected by surveillance systems · residents who can appear
on video · residents of high-traffic zones exposed to air pollution and noise · youth and students seeking
sustainable transport alternatives · small business.

**Conclusion of Stage I:** *the adaptive traffic system has strong potential, but its success depends on
aligning technological innovation with governance capacity, financial models and security considerations.*

---

## 4 · What Stage II (Scenario Building) produced

Held in person at the **L'Aquila Consortium Meeting, 6–8 July 2026**, with **Pavlo Radiuk and the
Deputy Mayor of Khmelnytskyi**. Swati distributed A0 templates, one per pilot city, on 30 June 2026.

**Objective (verbatim from the Khmelnytskyi template):**
> *To collaboratively identify the key factors and drivers shaping the future of Khmelnytskyi's AI-powered
> transport management pilot and co-create plausible future scenarios for scaling digital and climate-smart
> governance, grounded in local uncertainties around technology deployment and long-term financing.*

**The two axes selected from Stage I:**

| | Definition | Why it was chosen |
|---|---|---|
| **Uncertainty 1 — AI Infrastructure Affordability** | Affordable AI systems and infrastructure deployment **vs.** high implementation and infrastructure costs | The workshop identified the high cost of AI systems, computing infrastructure and local data storage as a major barrier to implementing and scaling AI-enabled municipal services |
| **Uncertainty 2 — Long-term Funding Security** | Stable long-term funding and investment **vs.** dependence on short-term external funding | The workshop highlighted that scaling the pilot depends on securing sustainable funding beyond externally funded projects and grants |

**The four scenarios:**

| | Strong funding security | Weak funding security |
|---|---|---|
| **High affordability** | **A** | **B** |
| **Low affordability** | **C** | **D** |

**The three questions asked of each scenario in Stage II** (worth knowing — Swati will echo them):
1. **What does this future look like for the pilot?** — *Future conditions and implications:* how is the pilot functioning; is it expanding, stagnating, adapting, transforming; what opportunities and challenges emerge; key actors and most vulnerable groups.
2. **What would be needed to make this successful?** — *Implementation and institutionalisation:* what policies, technical capacities, financing mechanisms and governance arrangements are required.
3. **What should the city start doing today?** — *Preparation and immediate actions:* what actions should begin immediately; what capacities need strengthening; what partnerships should develop; what governance structures should be established.

**Part II of the template — Cross-Scenario Reflection:** which readiness gaps appear repeatedly? Which URI
dimensions remain weak regardless of future? What barriers repeatedly limit success? Assessed against the
**seven URI dimensions**: 1 Vision & Strategic · 2 Regulatory & Planning · 3 Institutional & Technical ·
4 Financial & Economic · 5 Innovation & Infrastructure · 6 Civic & Stakeholder · 7 Conflict Impact & Recovery.

> ⚠ **Known gap:** the **filled-in narratives** from the L'Aquila session were never circulated by e-mail.
> They exist on the A0 sheets and in Swati's records. Our preparation is therefore built from the **axes,
> the scenario definitions, the template questions and the Stage I evidence** — all of which are documented.
> Swati has said she will re-summarise the four futures at the start of the session, so treat our scenario
> descriptions as well-founded expectations to be adjusted live, not as quotations.

---

## 5 · Stage III — what Swati has asked for

From her e-mail of 9 September 2026 (thread `1a0827a57cbba97d`):

- She introduces a **Technology shock**: *can adaptive traffic systems continue if AI/digital technologies become unavailable, unaffordable, or technically unreliable?*
- The session explores how **three partners jointly support the pilot to withstand the shock**:
  - **KhNU** — technology expertise
  - **Khmelnytskyi City Council** — political and policy perspective, experience in green transport systems
  - **LYKUML** — through its dissemination centre
- **End goal:** *validated and resilient pathways for pilot implementation and replication.*
- **Three framing questions per scenario:** what breaks · what still works · what should we change now.
- She will summarise the four scenarios before the start "to have everyone on board".

---

## 6 · Source materials

| In `Source_Files/` | What it is |
|---|---|
| `01_XSP_Methodology_Overview.pdf` | Swati's Exploratory Scenario Planning methodology deck — the 3-step framework |
| `02_Pilot_Deck_EN_2026-04-01.pdf` / `.pptx` | Pavlo's pilot introduction presented at the Scenario Mapping workshop |
| `03_Pilot_Deck_UK_2026-04-01.pptx` | Ukrainian version of the same deck |
| `04_Pilot_Deck_Script_EN.docx` | Slide-by-slide speaking script for that deck |
| `05_Workshop1_ScenarioMapping_Board_UK.pdf` | Ukrainian A0 board of Workshop 1 outputs — uncertainties, stakeholders, vulnerable groups, URI indicators |
| `06_Workshop2_ScenarioBuilding_Template.pdf` | **The blank A0 scenario-building template** — axes, four quadrants, the three question blocks, Part II |
| `07_Scenario_Mapping_Summary_2026-04-07.docx` | Swati's official synthesis of Stage I |
| `08_Scenario_Mapping_Miro_Board.pdf` | Export of the Stage I Miro board (Swati added Zoom-transcription points in pink) |

**Miro boards (live):**
`https://miro.com/app/board/uXjVGsbe0zk=/` · `https://miro.com/app/board/uXjVGukeh5g=/`

**Note on document 07:** its header reads *"Task: Exploratory Scenario Planning with Ivano-Frankivsk"* —
a copy-paste slip in Swati's template. The content is entirely Khmelnytskyi. Not worth raising unless it
appears again in a deliverable.
