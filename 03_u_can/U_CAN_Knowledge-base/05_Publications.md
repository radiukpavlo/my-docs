# 05 — Publications and Manuscripts

The KhNU scientific output under Task 4.5. All of it belongs to one research line:
**pattern-aware, topography-aware adaptive traffic signal control for urban CO₂
reduction**, validated on Khmelnytskyi-derived SUMO/PTV Visum models.

## Published — cite these

**P1 · An Adaptive Machine Learning Approach to Sustainable Traffic Planning:
High-Fidelity Pattern Recognition in Smart Transportation Systems**
*Future Transportation* (MDPI) · Gold Open Access · Q2 · released October 2025
**DOI: [10.3390/futuretransp5040152](https://doi.org/10.3390/futuretransp5040152)**
HDBSCAN + k-means clustering for high-fidelity traffic-pattern recognition;
validated on a Khmelnytskyi transport-network simulation;
**scenario-identification accuracy ≈ 92.8–95.0 %**.
Source package: `../U_CAN_Papers_Published/U_CAN_Paper_01.zip` (LaTeX, 2025-10-04).

**P2 · Topography-Aware Deep Reinforcement Learning with Contextual Reward
Engineering for Sustainable and Efficient Urban Traffic Control**
*Future Transportation* (MDPI) · Gold Open Access · Q2
**DOI: [10.3390/futuretransp6020082](https://doi.org/10.3390/futuretransp6020082)**
Authors: Oleksander Ryzhanskyi, Oleksander Barmak, Eduard Manziuk,
**Pavlo Radiuk** (corresponding), Iurii Krak.
Context-Specific Reward Design penalising the energy cost of uphill stop-and-go
driving, which flat-world RL models ignore. Simulated
**CO₂ reduction up to 8.6 %** vs Max-Pressure and **4.7 %** vs standard DQN.
Source package: `../U_CAN_Papers_Published/U_CAN_Paper_02.zip` (LaTeX, 2026-04-02).

## Submitted / in production — check status before citing as published

**P3 · From Urban Video to Adaptive Traffic Signals: Digital Twin and Deep
Reinforcement Learning under Real-World Demand**
*IET Cyber-Systems and Robotics* · package dated 2026-08-13
`../U_CAN_Papers_Published/U_CAN_Paper_03.zip`

**P4 · Scenario-Oriented Optimization of Traffic Signal Control for CO₂ Emissions
Based on Traffic Patterns**
*CMES — Computer Modeling in Engineering & Sciences* (Tech Science Press) ·
package dated 2026-09-12
`../U_CAN_Papers_Published/U_CAN_Paper_04.zip`

> The folder is named `U_CAN_Papers_Published`, but P3 and P4 are recent submission
> packages. Confirm acceptance before describing them as published.

## Under review

**R1 · Adaptive Cascade Clustering for Pattern-Aware Traffic-Regime Identification
at Locally Constrained Urban Intersections**
Vitaliy Pavlyshyn, Eduard Manziuk, Pavlo Radiuk, Oleksander Barmak, Iurii Krak.
Microscopic SUMO model of a real constrained corridor + unsupervised regime
recognition; HDBSCAN → k-means cascade with a weighted-voting selector assigning each
time window to one of **five recurring regimes**.
**Adjusted Rand Index 0.73**, **V-measure 0.79**; aggregated per-lane descriptors beat
concatenated temporal vectors by **≈ 0.15 ARI**.
`../U_CAN_Papers_Review/Pavlyshyn_AdaptiveCascadeClustering.docx`

**R2 · Bridging the Sim-to-Real Gap in Topography-Aware Traffic Control using
Automated Video Analytics**
Oleksander Ryzhanskyi, Oleksander Barmak, Eduard Manziuk, Pavlo Radiuk, Iurii Krak.
Robustness of the P2 controller against stochastic sensor noise (heavy-vehicle
misclassification in CV pipelines). SUMO, **3.8° uphill approach**, **20 % heavy-vehicle
fleet**: at a **10 % misclassification rate** the topography-aware agent still achieves
**−7.1 % CO₂** vs MaxPressure and **−3.2 %** vs standard DQN, with only **1.62 %**
degradation against the ideal-data case.
`../U_CAN_Papers_Review/Ryzhanskyi_BridgingtheSim-to-RealGap.docx`

## The narrative arc (use this when pitching)

P1 establishes **that traffic regimes can be recognised** at high fidelity.
P2 shows **that terrain-aware reward design cuts modelled CO₂**.
R1 pushes recognition **down to a single intersection**, where control actually happens.
R2 proves the controller **survives noisy real-world vision input** — the sim-to-real step.
P3/P4 close the loop from **video → digital twin → scenario-optimised signal control**.
Together they form the evidence base for **D4.5**.

## ORCIDs

Pavlo Radiuk 0000-0003-3609-112X · Oleksander Barmak 0000-0003-0739-9678 ·
Eduard Manziuk 0000-0002-7310-2126 · Iurii Krak 0000-0002-8043-0785 ·
Oleksander Ryzhanskyi 0009-0000-4664-5195 · Vitaliy Pavlyshyn 0009-0003-0702-9359

## Acknowledgement to use in papers

> The U_CAN project has received funding from the European Union's Horizon Europe
> Framework Programme for Research and Innovation under grant agreement No. 101148374.

Budgeted open-access support for KhNU in Annex 2: **3 open-access publications × €2 000**.
