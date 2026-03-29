> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> HDP Sniper has evolved into the **S3 Sniper** system in v8.0, now enhanced with Monte Carlo simulation support. See [System Overview](../SYSTEM_OVERVIEW.md).

---

# Strategy Module: HDP Sniper

## Core Philosophy
**HDP Sniper** is a momentum-based strategy engineered exclusively for **Asian Handicap (HDP)** markets. It identifies "Positive Asymmetry" where a favorite is statistically dominating the match but the scoreboard (and thus the odds) has not yet adjusted.

## Operational Logic
* **Trigger Condition:**
    * Scoreline: Draw or Favorite trailing by 1 goal.
    * **Pressure Index:** > 75 (High Spatial Dominance).
    * **Market Trend:** Odds drifting upwards (market assuming the favorite is struggling).
* **Execution Target:** Asian Handicap (e.g., -0.25, -0.5, -0.75).
* **Risk Profile:** Medium-High Volatility / High Alpha.

## Technical Moat
This module utilizes a **"Goal Imminence"** vector. It differentiates between "sterile possession" (passing at the back) and "penetrative possession" (touches inside the box).
