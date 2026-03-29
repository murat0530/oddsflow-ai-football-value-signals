> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> This document describes the methodology of an earlier version of the engine. It is preserved to show how our quantitative approach has evolved. For the current v8.0 system, see [System Overview](SYSTEM_OVERVIEW.md) and [Performance](PERFORMANCE.md).

---

# Oddsflow Beta: Quantitative Methodology & Alpha Generation

# Oddsflow Beta: Quantitative Methodology & Alpha Generation

## 1. Quantitative Philosophy
Oddsflow Beta moves beyond traditional “outcome prediction” (e.g., who will win) to focus on **probability divergence** between:

- **Market-implied probability** (derived from current odds), and
- **Model-estimated probability** (derived from live, event-driven match context)

The core hypothesis is that **market prices can lag** when in-play dynamics shift the true probability distribution.

$$\text{Edge} = P(\text{Model}) - P(\text{Market})$$

Where $P(\text{Model})$ is derived from our proprietary event-driven state machine.

---


## 2. The Math Engine: Beyond Standard Poisson

Standard betting models rely on basic Poisson distribution, which assumes goals are random events distributed evenly over time. Oddsflow Beta corrects two critical flaws in this approach:

### A. The "Fat-Tail" Adjustment
Football matches exhibit **non-linear volatility**, especially in the final 15 minutes ("Fergie Time").
* **Standard Model:** Underestimates the probability of late goals.
* **Oddsflow Beta:** Applies a **Time-Decay Correction Coefficient** to the Lambda ($\lambda$) value, increasing probability density for late-game events based on the "Desperation Index" of the losing team.

### B. The Pressure Index (Goal Imminence)
We utilize a proprietary metric called the **Pressure Index** to quantify "Spatial Dominance."
Unlike raw possession stats (which are often passive), the Pressure Index measures the **quality of threat**:

* **Input Vectors:** `Shots_Inside_Box` (High Weight), `Deep_Completions` (Medium Weight), `Corner_Density` (Low Weight).
* **Logic:** A team with 30% possession but 4 shots inside the box has a higher $xG_{live}$ (Live Expected Goals) than a team with 70% possession and 0 shots inside the box.

---

## 3. Strategy Logic (The "Why")

The engine executes two distinct methodologies based on market conditions:

### Strategy 1: HDP Sniper (Asian Handicap)
* **The Setup:** A strong favorite is dominating the Pressure Index but the score remains 0-0 or 0-1.
* **The Inefficiency:** The market odds for the favorite drift upwards (becoming "cheaper") due to time decay.
* **The Edge:** Oddsflow Beta detects that the **Goal Imminence** is rising while the price is dropping. This creates a **Positive Asymmetry** opportunity.

### Strategy 2: Active Trader (Over/Under)
* **The Setup:** An open, end-to-end game with high combined Shot Volume.
* **The Inefficiency:** The market's automatic "Under" decay algorithm does not account for the chaotic nature of the specific match matchup.
* **The Edge:** The engine projects a **Liquidity Breakout** (a goal) before the market price adjusts.

---

## 4. Risk Governance ("The Shield")

A signal is only as good as its executability. Oddsflow Beta includes a governance layer that can **suppress or block** signals when auditability or execution quality is compromised.

- **Variance control (Beta public outputs):** Oddsflow Beta **does not publish 1X2 (Win/Draw/Loss) signals**. Beta public signals focus on **Asian Handicap (AH/HDP)** and **Over/Under (OU)** to reduce draw-driven noise and improve verification clarity.
- **Liquidity / executability checks:** Signals can be suppressed in leagues or moments where price formation is unreliable (e.g., thin markets, high slippage risk).
- **Volatility locks (threshold-based):**
  - **Red card protocol:** suspension of HDP-related outputs during instability windows.
  - **Post-goal cooldown:** a configurable cooldown period after major events (e.g., goals) to allow market equilibrium to reset.

*(Note: Exact thresholds and coefficients are implementation details and may evolve across versions.)*

---

## 5. Verification Standards

Oddsflow Beta is designed around **“Proof of Process”** — verifying what was published, when, and under what market conditions.

Public verification focuses on **signal-quality metrics**, such as:
1. **Timestamp integrity:** signals are logged with `updated_at_utc` (UTC).
2. **Edge transparency:** book odds vs fair odds at publish time, plus derived `edge_pct`.
3. **Price movement / CLV-style evaluation:** whether the market price moved after the signal (a standard way to evaluate signal quality independent of match outcomes).
4. **Reproducibility:** schemas, sample logs, and versioned notes are published to support independent audits.

Important clarification:
- **User PnL depends on execution** (timing, liquidity, stake sizing, limits). For that reason, realized PnL is **not** the primary object of public verification in this repository.

For the exact audit checklist and recommended citation wording, see `VERIFICATION.md`.

---

## Disclaimer
This methodology describes the **high-level framework** of the Oddsflow Beta engine.
Specific coefficients for the Pressure Index and tail-risk adjustments are proprietary and not disclosed in this repository.

All content is provided for **research and informational purposes only**.
OddsFlow.ai does not provide betting tips or guaranteed outcomes.
