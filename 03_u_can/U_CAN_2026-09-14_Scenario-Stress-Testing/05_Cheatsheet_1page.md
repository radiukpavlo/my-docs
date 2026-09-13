# CHEATSHEET — Scenario Stress-Testing · Mon 14 Sep, 15:00–16:30 · BZW Wing B

**Shock:** *Can adaptive traffic systems continue if AI/digital tech becomes unavailable, unaffordable, or unreliable?*
**Per scenario, 3 questions:** what **breaks** · what **still works** · what to **change now**

|  | **Strong funding** | **Weak funding** |
|---|---|---|
| **AI affordable** | **A** Full Deployment | **B** Cheap Tech, Fragile Money |
| **AI expensive** | **C** Expensive Tech, Stable Money | **D** Survival Mode |

---

### OPENING LINE
> *"Four layers — platform, data, algorithms, scale. The shock removes only layer 3. Layers 1, 2 and 4 keep their value without AI. That is why we built it in this order."*

### DEGRADATION LADDER — the answer to everything
**L4** full adaptive AI → **L3** frozen model, inference only → **L2** actuated (local detector, no network) → **L1** time-of-day fixed-time plans (clock only) → **L0** flashing amber / manual
*Rules:* fail **down**, never off · fallback plans live **in the controller** · watchdog on **plausibility**, not just liveness · test every level annually.

### THE HONEST NUMBER
AI layer = **−8.6 % CO₂** vs Max-Pressure, **−4.7 %** vs standard DQN. *An increment on a working system, not the system.*

---

### A — Full Deployment
- **Breaks:** no fallback layer was ever built · single platform/vendor/model = city-wide failure · political exposure · over-scaling before real-data validation · no in-house skills
- **Works:** Phases 1–2 entirely · fixed-time + actuated on new hardware · digital twin · KhNU partnership · the funding relationship
- **Change now:** ladder as a **contractual acceptance criterion** · open API + local data, no exceptions · spend on redundancy not only coverage · knowledge transfer in Ukrainian · keep a non-AI control group

### B — Cheap Tech, Fragile Money
- **Breaks:** **opex, not capex** — subscriptions, licences, maintenance, salaries lapse first · orphaned demo · staff attrition · dead controllers stay dead · traffic database deleted
- **Works:** open-source stack, no licences · locally autonomous junctions · **KhNU hosts it as research infrastructure** · papers + twin already paid for · replication argument
- **Change now:** **zero-opex design** · maintenance into a **permanent municipal budget line** · KhNU service agreement · front-load Phases 1–2 · benefits-evidence pack from day one · archive everything off-site

### C — Expensive Tech, Stable Money
- **Breaks:** coverage unaffordable even with money · **vendor lock-in becomes attractive** · FX/sanctions/logistics on imports · slow tenders · licences crowd out durable infrastructure
- **Works:** stable money buys **exactly what is missing** — controllers, detection, network, control centre, **local data centre** · KhNU algorithms substitute for vendor AI · governance work · EBRD/EU alignment · the twin
- **Change now:** **split the tender** — open infrastructure vs algorithms · cost ceiling per junction + open standards (NTCIP/OCIT, ONVIF) · KhNU stack as price benchmark · prioritise by benefit · **local storage over foreign cloud** · escrow + portability clauses

### D — Survival Mode
- **Breaks:** whole AI layer · **budget redirected to military priorities** · formal closure, team disperses · obsolete controllers replaced like-for-like → **future foreclosed** · donors move on
- **Works:** **twin-based retiming at near-zero capex** · the procurement clause (free) · research, publications, students · Dresden/Stuttgart + LYKUML · 2024 public goodwill
- **Change now:** define a **Minimum Viable Pilot** · keep it in the **City Transport Plan + Recovery Plan** · archive assets with an off-site copy at TU Dresden · keep a **shovel-ready costed file** · AI-compatible equipment on every repair · bank the value as knowledge

---

### SEVEN NO-REGRET ACTIONS (robust in all four)
1. **Open-API / AI-compatibility clause in procurement** — free, preserves every future
2. **Digital twin as a permanent municipal asset**
3. **Degradation ladder in the technical specification**
4. **Secure local storage + "one umbrella system" data governance**
5. **KhNU as permanent partner · escrowed code/models · two people per role**
6. **Pilot embedded in City Transport Plan + Recovery Plan**
7. **Measure and publish benefits continuously**

### WEAKEST URI DIMENSIONS IN EVERY FUTURE
**4 Financial & Economic** (weakest) · **3 Institutional & Technical** (no data governance, unclear departmental responsibility, staffing) · **7 Conflict Impact & Recovery** (no redundancy/backup strategy)
*Strongest:* **1 Governance & Vision** · **6 Civic** (conditional on trust and consultation)

### CLOSING LINE
> *"Across all four futures the binding constraints are the same: recurrent money, data governance, wartime resilience. The technology is not the fragile part — the institutions around it are."*

---

### KEY NUMBERS
267,891 residents · 20.6 km² · SUMO twin: **15 intersections, 45.7 km** · Paper 1 (2025): HDBSCAN+k-means, V-measure 0.79–0.82, **95 %** accuracy, 0.94 temporal coherence · Paper 2 (2026): DRL+CSRD, **−8.6 %** / **−4.7 %** CO₂ · Phases: 0 specs → 1 platform → 2 data → 3 pilot at **3–5 intersections** → 4 scale

### FAILURE MODES
M1 detection loss · M2 comms partition · M3 central platform down · **M4 model drift — confidently wrong** · M5 licence lapse · M6 cyber/adversarial · **M7 skills loss**
