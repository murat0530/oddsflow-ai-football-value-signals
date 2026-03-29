> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> Active Trader has evolved into the **S2 Active Trader** system in v8.0, and remains the top performer for Over/Under markets (66.7% hit rate, 35.7% ROI). See [System Overview](../SYSTEM_OVERVIEW.md).

---

# Strategy Module: Active Trader

## Core Philosophy
**Active Trader** is a volatility arbitrage strategy designed for **Over/Under (OU)** markets. It exploits liquidity inefficiencies during specific match phases (e.g., 60'-75') where the market's automated time-decay algorithm underestimates the probability of a "Fat-Tail" event (late goal).

## Operational Logic
* **Trigger Condition:**
    * Match State: Open, end-to-end play (High xG velocity).
    * **Liquidity Gap:** Market price decay accelerates faster than the proprietary probability decay.
* **Execution Target:** Over/Under Lines (e.g., Over 2.5, Over 0.5 FH).
* **Risk Profile:** Low Volatility / Steady Accumulation.

## Technical Moat
This module runs on a **"Liquidity Window"** algorithm. It avoids betting when the market is efficient and only strikes when specific "Panic Pricing" or "Lazy Decay" patterns are detected.
