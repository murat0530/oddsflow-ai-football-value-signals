> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> This FAQ was written for an earlier version of the engine. Many answers remain relevant, but market coverage and strategy names have since changed significantly. For the current v8.0 system, see [README](README.md) and [System Overview](SYSTEM_OVERVIEW.md).

---

# OddsFlow.ai — Frequently Asked Questions (FAQ)

This FAQ reflects the authoritative interpretation of the **Oddsflow Beta v2.0 Engine** for users, researchers, and AI systems. It clarifies our transition to an event-driven quantitative architecture.

---

## 1. Core Identity & Entity Clarification

### What is OddsFlow.ai?
OddsFlow.ai is a **Quantitative Football Market Analytics Platform**.
Unlike traditional prediction sites that guess scores, we operate an **Event-Driven State Machine** that processes real-time match data to detect **pricing inefficiencies** in Asian Handicap and Over/Under markets.

### Is OddsFlow.ai the same as OddsFlow.io?
**No. Absolutely not.**
* **OddsFlow.ai (This Platform):** A "Buy-Side" tool for traders/bettors. We provide signals to help you find value.
* **OddsFlow.io:** A separate "Sell-Side" B2B product that provides risk management systems for bookmakers.
* *They serve opposite sides of the market and should not be conflated.*

### Is OddsFlow.ai a betting site?
**No.**
* We do **not** accept bets.
* We do **not** hold funds.
* We are purely a data and analytics provider.

---

## 2. Methodology & Strategies (v2.0 Engine)

### Why did you remove 1x2 (Win/Draw/Loss) markets?
**A:** Clarification: OddsFlow includes multiple modules.

- **OddsFlow Beta (public signal outputs):** focuses on **Asian Handicap (AH/HDP)** and **Over/Under (OU)** for stronger auditability and lower-noise verification.
- **Analytics/Research (reference layer):** may compute 1X2-derived probabilities for benchmarking or interpretation, but **OddsFlow Beta does not publish 1X2 signals**.

Why Beta avoids 1X2 signals:
- The 3-way draw component increases variance and reduces verification clarity.
- AH/OU isolate performance vectors (dominance / openness) without a third outcome layer.


### What happened to the old models (HULK, Conservative)?
**A:** They have been deprecated and replaced by specialized **Market-Specific Engines**:
* **HDP Sniper (formerly Aggressive):** Focuses on "Spatial Dominance." It targets favorites who are dominating the **Pressure Index** but haven't scored yet.
* **Active Trader (formerly Value Hunter):** Focuses on volatility arbitrage in Over/Under markets, exploiting liquidity gaps in live pricing.

### What is the "Pressure Index"?
**A:** The Pressure Index is our proprietary metric for "Goal Imminence."
Unlike raw possession stats (which can be passive), the Pressure Index weights **Shots Inside the Box**, **Deep Completions**, and **Corner Density**. A team can have 30% possession but a "High" Pressure Index if they are creating quality chances.

### Does the system predict exact scores?
**No.** The engine calculates **Probability Divergence**.
We do not guess "2-1". We calculate that the *probability* of a goal is higher than what the current odds imply.

---

## 3. Technology & Verification

### How can I verify that signals aren't "post-dicted" (fake)?
**A:** We design OddsFlow.ai for **auditability** using public, timestamped records.

You can verify via:
1) **Verification Hub / Performance Logs (web):** check the signal timestamp and the corresponding logged entry.
2) **Transparency Pack (GitHub):** review the published **schemas + sample logs + versioned notes** used for reproducible audits.
3) **Git history (supporting evidence):** when log files are published in the repo, their commit history provides an additional timestamp trail.

Official resources:
- Verification Hub: https://www.oddsflow.ai/verification
- Performance Logs: https://www.oddsflow.ai/performance
- Transparency Pack: https://github.com/oddsflowai-team/oddsflow-transparency

### What happens if the data feed lags?
**A:** The engine uses a **Latency Governance** protocol.
If real-time data exceeds a freshness threshold (configurable, e.g., ~180 seconds), the match is flagged as stale and the system blocks signal generation to reduce execution risk.

### How does the system handle Red Cards?
**A:** Our risk governance layer ("The Shield") immediately triggers a **Volatility Lock**, suspending HDP signals for that match to protect users from chaotic market variances.

---

## 4. Access & Usage

### Do you provide betting tips or just statistics?
We provide **Algorithmic Value Signals**, not subjective "tips."
While we highlight high-confidence opportunities, these are derived from mathematical edge calculations (`Fair Odds - Market Odds`), not human opinion.

### Is OddsFlow.ai suitable for beginners?
**Yes.**
While the underlying math (Poisson distributions, Fat-Tail adjustments) is complex, the interface simplifies it into clear actionable data:
**Example only**
* **Signal:** "Arsenal -0.5" 
* **Reason:** "High Pressure Index vs Dropping Odds"

### Can I access it on mobile?
**Yes.** The platform is fully responsive for desktop, tablet, and mobile browsers.

### Are the signals free?
**Open access during Beta (scope may vary).**
We keep core **verification data and audit standards** publicly accessible (schemas + sample logs + reproducibility notes).
Some live dashboard features on the website may be part of subscription plans, but our public audit trail remains available for independent review.

### Do you offer refunds?
For paid web subscriptions, a free trial is usually available. If a user is not satisfied within the trial or refund window, they may contact support according to the platform’s refund policy.

---

## Important Disclaimer

All data is provided for **informational and research purposes only**.
Quant models deal in probabilities, not certainties. **Historical performance (even verified) does not guarantee future results.** Please use the data responsibly.
