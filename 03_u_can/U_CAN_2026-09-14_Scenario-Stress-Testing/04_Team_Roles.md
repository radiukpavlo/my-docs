# Team Roles and Talking Points

Share this with the delegation **tonight**. One card per person — nobody needs to read anything else to contribute well.

**Session:** Monday 14 September, 15:00–16:30, TU Dresden BZW Wing B. Facilitator: Swati Kulashri.
**Working language: English.** This session is *not* marked `[DE-UA]` in the agenda, so no interpreter is guaranteed — see the note at the bottom.

---

## How to make the session work

- Swati wants **brainstormed input per scenario**, not presentations. Short, concrete points beat polished speeches.
- The three questions repeat for every scenario: **what breaks · what still works · what should change now**.
- If the room goes quiet, the most useful move is to name a **specific mechanism** ("the subscription lapses", "the controller keeps a stale plan"), not a general worry ("funding is difficult").
- Expect sticky notes on A0 sheets. Write in short phrases, one idea per note.

---

## Pavlo Radiuk — KhNU, Associate Professor, Computer Science
### *Technology owner. The main respondent in this session.*

**Own these:**
- The **four-layer framing** (platform → data → algorithms → scale) and why only layer 3 is at risk.
- The **degradation ladder** L4 → L0, and the rule that fallback plans live in the controller, not the server.
- **Non-AI fallbacks:** time-of-day fixed-time plans from the SUMO twin; actuated control; GPS-synchronised green waves.
- **What the AI layer is actually worth:** −8.6 % CO₂ vs Max-Pressure, −4.7 % vs standard DQN. Be honest that this is an increment, not the whole system — it makes every other claim more credible.
- **Cheap vs locked-in:** commodity edge compute and open-source stack vs controller firmware, ATMS licences, cloud GPU, foreign storage.
- **Failure mode M4 (model drift):** a model that is *confidently wrong* is worse than a model that is off.

**Your three asks for the room** (get these into the output):
1. Open-API / AI-compatibility clause in procurement standards — zero cost, all four futures.
2. The digital twin as a permanent, AI-independent municipal asset.
3. The degradation ladder written into the technical specification as an acceptance criterion.

---

## Oleg Kostenetskyi — Khmelnytskyi City Council, Deputy Head, Transport and Communications
### *Political and budgetary reality. The most important voice on "what should change now".*

**Own these:**
- What the department **can realistically commit to** in each funding scenario, and what it cannot.
- The **budget-redirected-to-military-priorities** insight — this came from the City side in Stage I and it is the defining constraint in Scenario D.
- Whether maintenance can move **from a project line into a permanent municipal budget line** (the single most valuable answer in Scenario B).
- How the pilot can be written into the **City Transport Plan** and the **Recovery Plan** so it survives without a new political decision.
- Existing green-transport initiatives and the SUMP — the city is not starting from nothing.

**One sentence worth saying:** *"We can protect the option cheaply — every controller we replace anyway can be an open-API one — but we cannot protect a recurring licence bill."*

---

## Mariia Lisitsyna — Khmelnytskyi City Council, Head of Road Infrastructure Safety Division
### *Safety of degraded modes. Junction selection.*

**Own these:**
- What each rung of the degradation ladder means **for road safety** — particularly the difference between fixed-time, flashing amber and manual control at busy junctions.
- Which intersections are **safety-critical** and therefore need UPS and priority treatment.
- Which of the 3–5 pilot junctions should be chosen, and on what criteria.
- Whether a "system off" state is acceptable anywhere, and what the fallback protocol with the police would be.

**One sentence worth saying:** *"A degraded signal is acceptable; a dark signal at these particular junctions is not — that tells us where the UPS budget goes first."*

---

## Eduard Manziuk — KhNU, Professor, Computer Science
### *Data and model robustness. Pavlo's technical second.*

**Own these:**
- **Model drift and distribution shift** — why retraining is needed when traffic patterns change after curfew, evacuation or road closures, and why plausibility checks must demote the system automatically.
- Data quality, sensor health monitoring, and what "technically unreliable" means in practice.
- The research pipeline and what can continue on near-zero budget.
- Link to the wider KhNU research portfolio (including the polymer waste-to-fuel project presented on Day 3) — the *decision-support-for-local-authorities* framing is common to both.

---

## Prof. Inna Shevchuk — LYKUML, Head of Scientific and Research Department
### *Dissemination and replication. Swati named LYKUML explicitly in her briefing.*

**Own these:**
- What the **LYKUML dissemination centre** can carry when money is short — replication guidance, training, policy briefs, public communication.
- The **Centre for Local Policy Support in Climate-Neutral Construction and Energy** as a channel for keeping the pilot visible.
- Public acceptance and consultation — how to protect the 2024 goodwill through a period of no visible progress.
- Replicability to other Ukrainian cities as a funding argument.

---

## Prof. Ivan Kostyashkin — LYKUML, Head of Department of Labour, Land and Economic Law
### *Legal and regulatory hardening.*

**Own these:**
- How to draft the **open-API / AI-compatibility requirement** so it is legally enforceable in municipal procurement.
- **Source-code escrow and data-portability clauses** in contracts with proprietary vendors.
- Data-protection and surveillance law as it applies to camera-based traffic monitoring, and wartime data-security obligations.
- The legal form of a standing **KhNU–City Council partnership agreement** that is not project-bound.

---

## Daria Arziantseva — LYKUML, Associate Professor, Management, Economics, Statistics and Digital Technologies
### *The economics of the shock.*

**Own these:**
- **TCO per intersection with and without the AI layer** — the number that lets the city make a phased stop/go decision.
- Capex vs **opex** distinction — the core insight of Scenario B.
- Cost-benefit of the 8.6 % CO₂ improvement against recurring AI costs.
- FX, import and sanctions exposure on expensive foreign hardware (Scenario C).

---

## Liudmyla Remishevska — KhNU, Head of International Relations Office
### *Institutional continuity and partnerships.*

**Own these:**
- The formal mechanics of a standing KhNU–City partnership and of **asset custody with TU Dresden** (off-site copy of code, twin and models).
- Grant and mobility instruments that could sustain the pilot between funding rounds.
- Continuity of the U_CAN relationship and the Dresden–Stuttgart–Khmelnytskyi partnership.

---

## Yevheniia Smoliienko — Smart Environment Office / KCE "Spetskomuntrans"
### *EBRD procurement precedent.*

**Own this:** the Khmelnytskyi Solid Waste Project (EBRD Operation No. 50729) is a live example of how the city has actually structured a large donor-funded infrastructure programme — phased delivery, retendering, grant-plus-loan blending. That precedent is directly relevant to how the traffic pilot should be financed and tendered. Worth one contribution in Scenario C.

---

## Language note

The agenda does not mark this session for German–Ukrainian interpretation, and it runs in English. Two practical consequences:

1. **Pavlo carries the technical load in English.** Plan for that.
2. For the City Council colleagues, agree in advance who paraphrases into Ukrainian if needed. Kateryna Fütterer interprets for the Deputy Mayor elsewhere in the programme but is not assigned here. If interpretation matters for Oleg Kostenetskyi's and Mariia Lisitsyna's contributions, **flag it to Swati or Radka tonight** — there is still time to arrange informal support, and their input is the most valuable part of the "what should we change now" round.

**Suggested pre-brief:** 20 minutes over breakfast on Monday, using [05_Cheatsheet_1page.md](05_Cheatsheet_1page.md). Agree who speaks first on each scenario so the room does not stall.
