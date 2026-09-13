# Prepared Answers — 4 Scenarios × 3 Questions

**The shock:** AI/digital technologies become **unavailable** (sanctions, supply chain, destroyed infrastructure), **unaffordable** (licence/subscription/FX costs, budget redirected to defence) or **technically unreliable** (model drift, sensor and comms loss, cyber compromise).

> **Framing sentence that works in every scenario — say it early:**
> *"The pilot has four layers — platform, data, algorithms, scale. The shock removes the algorithm layer only. Everything we are asking the city to build in Phases 1 and 2 keeps its value without AI. That is why we designed it in this order."*

Each block below is written so it can be read out, or transcribed onto sticky notes almost verbatim.

---

## Scenario A — High Affordability + Strong Funding Security
### *"Full Deployment"*

**1 · What breaks?**
- **Design complacency.** With money and cheap technology, the city procures an AI-first architecture and *skips the fallback layer*. When the shock hits there is no L2/L1 mode to fall back to — the failure is total rather than graceful.
- **Depth of stack dependency.** Full deployment across all intersections means one central platform, one vendor cloud, one model family. A single unavailability event takes down the whole city, not one junction.
- **Political exposure.** A flagship, highly visible, publicly communicated system failing is far more damaging than a quiet pilot failing. Public acceptance — currently positive per the 2024 consultations — is spent quickly.
- **Over-scaling before validation.** Abundant funding tempts the city to scale to all intersections before Phase 3 has produced measured CO₂ results on real (not simulated) data.
- **Skills concentration.** Money buys a vendor, so the municipality never builds in-house competence; when the vendor withdraws, no one can operate the system.

**2 · What still works?**
- **Phases 1 and 2 in full.** The unified digital platform, connectivity standards, secured network, control centre, cameras, counters and the traffic database are **all AI-independent**. They keep every bit of their value.
- **Fixed-time and actuated control** on the new controllers — the hardware is better than what the city has today even with the AI switched off.
- **The SUMO digital twin** (15 intersections, 45.7 km) — still generates optimised time-of-day plans offline, no live data and no AI required.
- **Institutional assets:** the KhNU–City Council partnership, staff trained during deployment, the data-governance structure, the procurement standards.
- **The funding relationship itself** — strong funding security means the shock is survivable as a *re-scoping*, not a cancellation.

**3 · What should we change now?**
- **Write the degradation ladder into the technical specification** (L4 → L0, see [03_Technical_Annex.md](03_Technical_Annex.md)) and make "system operates correctly in fixed-time and actuated mode with the central platform disconnected" a **contractual acceptance criterion**.
- **Mandate open API and local data storage** in every procurement lot — no exceptions, regardless of how affordable the closed option looks.
- **Spend a slice of the abundant funding on resilience, not only on coverage:** UPS at junctions, spare controllers, local storage, redundant communications.
- **Train municipal engineers alongside the vendor** — contractually require knowledge transfer and documentation in Ukrainian.
- **Keep a non-AI control group** of intersections so the AI benefit stays measurable and defensible.
- **Stage the roll-out anyway:** 3–5 intersections → measure → expand, even when money would allow going faster.

---

## Scenario B — High Affordability + Weak Funding Security
### *"Cheap Tech, Fragile Money"*

**1 · What breaks?**
- **Operations, not capital.** Capex is affordable; **opex is not funded**. Subscriptions, licences, cloud inference, maintenance contracts and staff salaries are the first things to lapse.
- **The pilot becomes an orphaned demo.** 3–5 intersections work, scaling stops, and after the grant ends nobody owns the system.
- **Staff attrition.** Short-term project contracts mean key people leave, are mobilised or emigrate — and the knowledge goes with them.
- **Replacement cycle.** Cheap hardware still fails; with no capital line a dead controller stays dead and the pilot silently shrinks.
- **Data continuity.** Storage costs are recurring — the traffic database from Phase 2 is at risk of simply being deleted.

**2 · What still works?**
- **The open-source, low-cost edge stack** — SUMO, Python, HDBSCAN/k-means, PostgreSQL/TimescaleDB, MQTT, commodity edge compute. No licences to lapse.
- **Locally autonomous junctions.** If each controller holds its own plans, the pilot zone keeps running with the central platform switched off and nobody paying a cloud bill.
- **KhNU as operator.** The university can host the platform and maintain it as **research infrastructure** between grants — a cost the city does not carry.
- **Already-paid-for assets:** two published papers, the digital twin, the trained models, the 2024 public-consultation goodwill.
- **The replication argument** — a cheap, working, documented pilot is exactly what attracts the next EBRD/EU/donor round. Weak funding is not zero funding.

**3 · What should we change now?**
- **Design for zero-opex survival:** no mandatory subscriptions anywhere on the critical path; open-source first; hardware chosen for long spare-part availability.
- **Move maintenance from the project line into the municipal budget line** — a small permanent line beats a large temporary one.
- **Sign a KhNU service agreement** to operate and maintain the system between funding rounds, with a nominal or in-kind fee.
- **Front-load what is funded now.** Complete Phase 1 (standards, platform, network) and Phase 2 (data) while money exists — these retain value indefinitely; Phase 3 can wait.
- **Build the benefits-evidence pack from day one** — before/after CO₂ and delay at the pilot junctions — because that document *is* the next grant application.
- **Archive everything** (code, twin, models, schemas, data) in a KhNU repository with an off-site copy, so a funding gap never becomes data loss.

---

## Scenario C — Low Affordability + Strong Funding Security
### *"Expensive Tech, Stable Money"*

**1 · What breaks?**
- **Coverage and value for money.** High cost per intersection means city-wide deployment is unaffordable *even with stable funding*. The pilot stays a pilot.
- **Vendor lock-in becomes attractive.** With money available, a turnkey proprietary ATMS looks like the easy answer — and the city loses control of its data, its interfaces and its future costs in one signature.
- **Import exposure.** Expensive foreign hardware and GPU/cloud capacity are hostage to FX movements, sanctions, export controls and wartime logistics.
- **Procurement latency.** Large, expensive tenders take longer, and under war conditions the requirement may change before delivery.
- **The AI layer crowds out the durable layer.** Money spent on licences is money not spent on controllers, fibre and secure local storage.

**2 · What still works?**
- **Stable funding can buy exactly what the city is missing** — open-API controllers, detection, communications, a control centre and *secure local data-centre capacity*. None of that is AI.
- **KhNU's in-house algorithms substitute for expensive vendor AI.** This converts a cost problem into a research contribution: our HDBSCAN/k-means and DRL+CSRD work already exists and is published.
- **Institutional and governance work is cheap and unaffected** — the "one umbrella system" for data governance, departmental responsibility allocation, procurement standards.
- **EBRD / EU alignment continues** — stable funding relationships are precisely the asset that survives a technology shock.
- **The digital twin** replaces expensive live-data experimentation with simulation.

**3 · What should we change now?**
- **Split the tender in two:** (i) open infrastructure — controllers, detection, network, storage; (ii) algorithms/software. The expensive AI layer then becomes **optional and swappable** rather than structural.
- **Set a cost ceiling per intersection** and a minimum open-standards requirement (NTCIP/OCIT-class protocols, ONVIF cameras, documented API).
- **Use the KhNU stack as the reference implementation** to benchmark vendor pricing — a credible in-house alternative is the strongest negotiating position the city has.
- **Prioritise by benefit, not by uniformity.** Let the twin identify the 3–5 highest-benefit junctions and equip those properly instead of thin coverage everywhere.
- **Invest in local data-centre capacity rather than foreign cloud** — simultaneously a cost decision, a resilience decision and a wartime security decision.
- **Contract for source-code escrow and data portability** on anything proprietary that is bought.

---

## Scenario D — Low Affordability + Weak Funding Security
### *"Survival Mode"*

**1 · What breaks?**
- **The entire AI layer.** No procurement, no subscriptions, no new hardware. Phases 3 and 4 are off the table.
- **The city budget is redirected to military priorities** — flagged in Stage I as the *critical insight*, and the defining feature of this quadrant.
- **Formal closure risk.** The pilot is quietly dropped from work plans, the team disperses, and institutional memory evaporates.
- **Existing infrastructure degrades further.** Today's controllers are already obsolete; with no capital line they keep failing and are replaced like-for-like with non-AI-compatible equipment — **permanently foreclosing the future**.
- **Donor attention moves on** if there is no visible activity to point at.

**2 · What still works?**
- **Twin-based signal retiming — near-zero capex.** The SUMO digital twin plus historical counts can produce better fixed-time plans for existing junctions **today**, with no new hardware and no AI. This is the single highest-leverage surviving action.
- **The AI-compatibility procurement clause** — costs nothing, and is the difference between a recoverable future and a foreclosed one.
- **KhNU research capacity, publications and students.** Research output continues on almost no budget and keeps the method alive and citable.
- **Partnerships:** Dresden–Stuttgart–Khmelnytskyi Solidarity Partnership, the U_CAN consortium, LYKUML's dissemination centre.
- **Public goodwill** from the 2024 consultations — free, and perishable only through neglect.

**3 · What should we change now?**
- **Define a Minimum Viable Pilot** that costs almost nothing: twin-based retiming at a handful of junctions, with before/after delay and CO₂ measured from existing data. Deliver *something* measurable every year.
- **Keep the pilot formally alive** inside the **City Transport Plan** and the **Recovery Plan** so it can be reactivated without a new political decision.
- **Protect the assets:** code, digital twin, trained models, data schemas and the traffic database in a KhNU archive, with an off-site copy held by a partner (TU Dresden is the natural custodian).
- **Keep a costed, shovel-ready project file** — technical specification, bill of quantities, junction priority list — so that when *any* donor money appears the city can move in weeks rather than months.
- **Protect the option, not the project.** Every repair and replacement anywhere in the network must still install AI-compatible, open-API equipment. It is the cheapest resilience measure available.
- **Bank the value as knowledge** — publications, replication guidance through LYKUML, and a case study for other Ukrainian cities.

---

## Cross-Scenario Reflection (Part II of Swati's template)

The template asks: *which readiness gaps appear repeatedly? Which URI dimensions remain weak regardless of future?*

### The seven no-regret actions — robust in all four scenarios

| # | Action | Why it is robust |
|---|---|---|
| 1 | **Open-API / AI-compatibility clause in procurement standards** | Zero cost, preserves optionality in every future |
| 2 | **SUMO digital twin maintained as a permanent asset** | Produces value with no AI, no live data, no budget |
| 3 | **Degradation ladder (L4→L0) in the technical specification** | Turns "AI fails" into "system degrades", never "signals fail" |
| 4 | **Secure local data storage + the "one umbrella system" data governance** | Cost, resilience and wartime-security decision in one |
| 5 | **KhNU as permanent technical partner; code/model escrow; two people per critical role** | Survives funding gaps, mobilisation and emigration |
| 6 | **Pilot embedded in the City Transport Plan and Recovery Plan** | Institutional survival independent of any single budget |
| 7 | **Continuous benefits measurement and publication** | The evidence pack *is* the next funding application |

### URI dimensions that stay weak regardless of future

| Dimension | Assessment |
|---|---|
| **4 · Financial & Economic** | **Weakest.** Stressed in all four quadrants. Major gaps in data centres, AI software + hardware cost, and operational staffing. Funding is external (EBRD/EU) and not structurally embedded. |
| **3 · Institutional & Technical** | **Weak.** No integrated data-governance system; data access requires manual inter-departmental coordination; responsibility allocation between departments unclear; operational expertise and staffing gaps. |
| **7 · Conflict Impact & Recovery** | **Weak.** No redundancy or backup strategy yet; high infrastructure-destruction risk; data-security threats from camera feeds during wartime. |
| **2 · Regulatory & Planning** | **Medium.** AI systems not yet embedded in formal policy frameworks; current focus is data *collection* (GPS, e-ticketing) rather than AI *control*. |
| **5 · Innovation & Infrastructure** | **Medium-weak.** Must be built from scratch — sensors, cameras, control centres — and scaling depends entirely on future funding. |
| **1 · Governance & Vision** | **Strongest.** Clear municipal commitment, existing SUMP, transport modelling capacity, integration into local strategy. |
| **6 · Civic & Stakeholder** | **Strong but conditional.** Acceptance exists (2024 surveys) but depends on trust in data use and prior consultation; privacy and surveillance concerns remain critical. |

**The one-line conclusion to offer the room:**
> *"Across all four futures the binding constraints are the same three: money that is recurrent rather than one-off, data governance, and wartime resilience. The technology is not the fragile part — the institutions around it are. So the resilient pathway is to build the AI-independent layers first and keep the AI layer swappable."*
