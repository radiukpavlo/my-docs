# Technical Annex — Pavlo's backup material

Everything here is for the moment someone asks *"but what actually happens when the AI stops working?"*
Keep it in reserve; lead with the degradation ladder.

---

## 1 · Degradation modes — how the system actually fails

| # | Failure mode | Trigger | Effect on the pilot |
|---|---|---|---|
| **M1** | **Detection loss** | Camera down, power cut, blackout, shelling, lens obscured | Adaptive control loses its inputs; controller must not "freeze" on a stale plan |
| **M2** | **Communication partition** | Fibre cut, LTE outage, jamming | Junctions isolated from the centre; coordination (green waves) is lost, local control must continue |
| **M3** | **Central platform unavailable** | Data-centre hit, cloud unreachable, licence lapse, sanctions | No central optimisation, no dashboards, no logging |
| **M4** | **Model degradation / distribution shift** | Traffic patterns change after curfew, evacuation, road closure, bridge loss | The model is *confidently wrong* — the most dangerous mode, because nothing looks broken |
| **M5** | **Licence / subscription lapse** | Funding gap, vendor withdrawal from the market, FX shock | Software stops legally or technically; support disappears |
| **M6** | **Cyber / adversarial** | Compromised camera feed, data poisoning, hostile reconnaissance use of video | Both a control-integrity and a national-security problem |
| **M7** | **Skills loss** | Mobilisation, emigration, contract end | Nobody can operate, retrain or repair the system |

> **The point to make:** M4 and M7 are the ones people forget. A model that is confidently wrong is worse than a model that is off, and a system nobody can operate is already broken.

---

## 2 · The degradation ladder (the core proposal)

Each level must be reachable **automatically and locally**, and each controller must hold the next level down **in its own memory**, not on a server.

| Level | Mode | Needs | Survives |
|---|---|---|---|
| **L4** | **Full adaptive AI** — DRL + topography-aware control, centrally coordinated | Live detection + comms + central compute + valid model | Normal operation |
| **L3** | **Frozen-model adaptive** — inference only, no retraining, last validated model | Live detection + local compute | M3, M5 (central platform / licence gone) |
| **L2** | **Actuated control** — local vehicle detection, min/max green, gap-out | Local detector + controller logic only | M2, M3, M4, M5 (no network, no AI) |
| **L1** | **Time-of-day fixed-time plans** — 3–4 offline-optimised plans (AM peak, interpeak, PM peak, night) | A clock only | M1, M2, M3, M4, M5 — everything except power |
| **L0** | **Flashing amber / manual police control** | Nothing | Total failure; safety fallback |

**Design rules to state out loud:**
1. **Fail *down* the ladder, never off it.** Loss of a level triggers automatic fallback, not a dark junction.
2. **Fallback plans live in the controller**, refreshed periodically from the centre — so a comms cut is a degradation, not an outage.
3. **Watchdog on plausibility, not just liveness.** Detector health and traffic-state sanity checks must demote L4→L2 when inputs become implausible (this is the defence against M4).
4. **Every level must be tested**, including annual "AI-off" drills. Untested fallbacks are not fallbacks.

---

## 3 · Non-AI fallbacks — what they actually deliver

### Time-of-day fixed-time plans (L1)
- Derived **offline** from historical counts using the **SUMO digital twin** (15 intersections, 45.7 km, already built and validated).
- Needs no live data, no sensors, no network — only a synchronised clock.
- Can be re-optimised whenever traffic patterns change, at effectively zero marginal cost.
- **This is the pilot's insurance policy, and it already exists.**

### Actuated control (L2)
- Inductive loops or radar at the stop line, plus local controller logic (minimum green, extension, gap-out, maximum green).
- Cheap, extremely robust, decades of field-proven practice, no central dependency.
- Handles demand variability that fixed-time plans cannot — captures a meaningful share of the adaptive benefit with none of the AI fragility.

### Coordinated green waves without AI
- Fixed offsets along arterials, synchronised by GPS / NTP with local holdover.
- Delivers corridor-level progression with no central optimiser in the loop.

### Honest framing of what the AI layer is worth
From our own published results (*Future Transportation*, 2026, DRL + CSRD, validated on the Khmelnytskyi digital twin):
- **−8.6 % CO₂** versus Max-Pressure control
- **−4.7 % CO₂** versus standard DQN

> **Say this plainly:** the AI layer is worth roughly **8.6 % CO₂** over a strong non-AI baseline. That is a real, publishable benefit and worth pursuing — **but it is an increment on top of a working system, not the system itself.** Losing it costs us that increment. Losing the platform and data layers costs us everything. That asymmetry is the whole argument for building in this order.

---

## 4 · Cheap and replaceable vs. locked-in

### Cheap, commodity, low switching cost — *build the pilot out of these*

| Component | Notes |
|---|---|
| Edge compute | Industrial mini-PC or Jetson-class, inference only; interchangeable |
| Detection | Inductive loops, radar/lidar counters, generic **ONVIF** IP cameras |
| Software stack | **SUMO**, Python/PyTorch, HDBSCAN + k-means, PostgreSQL/TimescaleDB, MQTT — all open-source |
| Connectivity | Fibre, LTE modems, PoE switches, UPS |
| **Our own assets** | Trained models, the digital twin, data schemas — **KhNU intellectual property** |

### Locked-in, high switching cost — *the real risk surface*

| Component | Risk | Mitigation |
|---|---|---|
| Traffic controller firmware and proprietary protocols | The deepest lock-in; determines everything downstream | **Open API mandatory in procurement**; prefer NTCIP 1202 / OCIT / UTMC-class standards |
| Central ATMS/UTC platform SaaS licences | Recurring cost, vendor dependence | Open interfaces; source-code escrow; data portability clause |
| Cloud GPU / inference subscriptions | FX, sanctions, export control, recurring opex | Keep inference **at the edge**; on-premise capability |
| Foreign cloud storage | Cost **and** wartime security exposure | **Secure local storage** — explicitly flagged in Stage I |
| Proprietary camera analytics SDKs | Ties detection to one vendor | ONVIF-compliant hardware; our own analytics |
| Single-supplier maintenance contracts | No competition at renewal | Multi-vendor compatibility as a tender requirement |

**The strategy in one line:** *keep the interfaces open and the data local; treat algorithms as replaceable; never let the plan depend on one vendor's cloud.*

---

## 5 · Institutional measures at KhNU that would harden the pilot

| # | Measure | What it protects against |
|---|---|---|
| 1 | **Formalise KhNU as permanent technical partner** — a standing agreement with named roles, not project-bound (already in the pilot strategy as *"University as a permanent technical partner"*) | Funding gaps, political turnover |
| 2 | **Asset escrow and mirroring** — digital twin, code, trained models, data schemas in a KhNU repository, with an **off-site copy held by TU Dresden** | M7 skills loss; physical destruction; funding collapse |
| 3 | **Open-API / AI-compatibility clause embedded in municipal procurement standards** — a Phase 0 deliverable, costs nothing now | Foreclosure of the future by like-for-like replacement |
| 4 | **Two people per critical role**, and train **municipal engineers** as well as researchers; MSc/PhD pipeline on the pilot | Mobilisation, emigration, contract end |
| 5 | **Publish the method** — two papers already out; keep publishing | Knowledge being lost or held hostage; also strengthens replication and funding cases |
| 6 | **Help the city build the "one umbrella system"** — a cross-departmental data-sharing protocol with local secure storage, retention limits, anonymisation/blurring, and a wartime data-security policy | The #1 structural barrier identified in Stage I; privacy and surveillance concerns; M6 |
| 7 | **Publish an explicit TCO per intersection, with and without the AI layer** | Lets the city make an informed stop/go decision at each phase instead of an all-or-nothing one |
| 8 | **Route replication through LYKUML's dissemination centre**, and leverage the Dresden–Stuttgart–Khmelnytskyi partnership for grant access | Isolation; loss of the replication argument |

---

## 6 · Pilot facts — have these numbers ready

| Fact | Value |
|---|---|
| City | Khmelnytskyi — **267,891 residents**, **20.6 km²** |
| Digital twin | **SUMO**, **15 intersections**, **45.7 km** of network |
| Paper 1 (*Future Transportation*, 2025) | Adaptive ML traffic pattern recognition, **HDBSCAN + k-means** — V-measure **0.79–0.82**, identification accuracy **95 %**, temporal coherence **0.94** |
| Paper 2 (*Future Transportation*, 2026) | Topography-aware deep learning, **DRL + CSRD** — **−8.6 % CO₂** vs Max-Pressure, **−4.7 % CO₂** vs standard DQN |
| Current state | Fixed signal cycles, no real-time sensors, no integration between control nodes, cameras exist but software not integrated, terrain not accounted for |
| Needed for AI | Controllers with **open API**; sensors/cameras at intersections; communication network between nodes; real-time data processing platform; **topographic module** |
| Phase 0 · Now | Document current state, define problem, write technical specifications → *Technical Specifications* |
| Phase 1 · Platform | Unified digital platform, connectivity standards, control centre, secured network → *Future-proof Foundation* |
| Phase 2 · Data | Cameras and counters at key intersections; database of intensity, flow composition, peak hours → *Real Database* |
| Phase 3 · Pilot | Algorithms at **3–5 intersections**; measure actual CO₂ reduction and trip duration → *First Real Results* |
| Phase 4 · Scale | All intersections + Management Centre; model for other Ukrainian and EU cities → *Full AI System* |
| Governing principle | *With any replacement or repair — install AI-compatible equipment.* New controllers **only with open API**. |
| Embedding targets | City Transport Plan · Recovery Plan · Procurement Standards · KhNU–Council partnership |

---

## 7 · Anticipated hard questions, and answers

**"If fixed-time plans are nearly as good, why fund the AI at all?"**
> They are not nearly as good — they are a floor, not a ceiling. Our measured delta is 8.6 % CO₂ over a strong baseline, and fixed-time plans degrade as traffic patterns drift while adaptive control tracks them. The argument is about *sequencing*, not about abandoning AI: build the layers that work without AI first, so that the AI layer is an upgrade rather than a single point of failure.

**"Isn't a digital twin useless without real data?"**
> The twin is calibrated on the real network geometry and historical counts, and both papers were validated on it. It is not a substitute for Phase 2 data — it is what lets us design, test fallbacks and re-optimise plans *before* and *without* live data. When Phase 2 data arrives the algorithms get significantly more accurate; until then the twin is the only place we can safely fail.

**"Can you run AI at all under blackouts?"**
> Not reliably, and we should not pretend otherwise. That is exactly why the ladder exists: under blackout conditions the honest answer is L1/L0 with UPS at priority junctions. Designing for that is more useful than promising uptime we cannot deliver.

**"Who owns the data, and is video legal and safe in wartime?"**
> The city owns it, and it must be stored locally — not in a cloud based abroad. Stage I flagged both the privacy/surveillance concern and the risk of camera data being misused by hostile actors. Our position: minimise retention, anonymise or blur at the edge wherever possible, count vehicles rather than identify them, and write this into the data-governance protocol before deployment, not after.

**"What happens if KhNU's key people leave?"**
> That is failure mode M7 and we treat it as a design constraint: two people per critical role, escrowed code and models with an off-site copy, published methods, and municipal engineers trained alongside us so the capability is not only ours.
