<div align="center">

# OddsFlow v8

### AI-Powered Football Signal Engine

[![Engine](https://img.shields.io/badge/Engine-v8.0-0366d6?style=for-the-badge)](SYSTEM_OVERVIEW.md)
[![Status](https://img.shields.io/badge/Status-Live_Production-00c853?style=for-the-badge)](#)
[![Markets](https://img.shields.io/badge/Markets-HDP_|_OU_|_1X2-ff6d00?style=for-the-badge)](#supported-markets)
[![License](https://img.shields.io/badge/License-Informational_Use-888?style=for-the-badge)](#disclaimer)

**Real-time football signal engine combining Monte Carlo simulation, market pressure analysis, and player-level AI modeling to detect mispricing across three markets.**

[Website](https://www.oddsflow.ai/) · [Verification Hub](https://www.oddsflow.ai/verification) · [Performance Logs](https://www.oddsflow.ai/performance) · [Transparency Pack](https://github.com/oddsflowai-team/oddsflow-transparency)

</div>

---

## System Performance at a Glance

<table>
<tr>
<td>

| Metric | Value |
|:-------|------:|
| **Total Bets** | 3,181 |
| **Win Rate** | 57.4% |
| **ROI** | 38.5% |
| **Profit** (@ $100/unit) | $664,126 |
| **Sample** | 600 matches |

</td>
<td>

| Best by Market | System | Hit Rate | ROI |
|:---------------|:-------|:--------:|----:|
| **1X2 Moneyline** | S4.2 Hybrid | 65.4% | **68.1%** |
| **Asian Handicap** | S4.2 Hybrid | 63.0% | **56.5%** |
| **Over/Under** | S2 Active Trader | 66.7% | **35.7%** |

</td>
</tr>
</table>

---

## How It Works — The 3-Phase Signal Pipeline

> *OddsFlow doesn't start when the whistle blows. It starts with the players.*

### `PHASE 1` Player-Level Foundation — OddsFlow Score

Every player in every match is assigned an **OddsFlow Score** — a proprietary composite rating derived from both **publicly available statistics** and **institutional-grade professional data sources**. The exact parameters and weighting are not disclosed.

This score quantifies each player's expected impact on match dynamics, and serves as the foundational input layer for all downstream modeling.

### `PHASE 2` Pre-Match Simulation — 10,000 Sandbox Runs

Before kickoff, the engine operates in two stages:

1. **Pre-Lineup AI Analysis** — Initial match modeling using expected squad compositions, historical matchup data, and OddsFlow Scores to establish baseline probability distributions.

2. **Post-Lineup Confirmation** — Once official lineups are confirmed, the engine executes **10,000 Monte Carlo simulations** incorporating the actual confirmed players. Every realistic scenario — scorelines, timing of goals, momentum shifts, substitution impacts — is computed and mapped into a complete probability foundation.

This foundation represents **all plausible match outcomes and their associated probabilities** before a single ball is kicked.

### `PHASE 3` Live Execution — Real-Time Edge Detection

During the match, the engine compares **real-time match state** against the pre-computed 10,000-run simulation foundation:

- As events unfold (goals, cards, substitutions, momentum shifts), the system identifies **where the live match trajectory diverges from what the market is pricing**.
- When the divergence exceeds threshold — meaning the bookmaker odds lag behind what the simulation foundation already mapped — a value signal is generated.

> **In short:** OddsFlow knows all 10,000 versions of how the match could play out. It watches one version unfold in real time, and strikes when the market hasn't caught up.

---

## Strategy Systems

OddsFlow runs **six independent strategy systems**, each targeting different market conditions:

### Pressure-Based Systems (S1–S3)

| System | Approach | Best Market | Hit Rate | ROI |
|:-------|:---------|:------------|:--------:|----:|
| **S1** Conservative | High-threshold pressure signals | OU | 46.2% | 11.0% |
| **S2** Active Trader | Early-entry momentum capture | OU | **53.6%** | **16.9%** |
| **S3** Sniper | Selective handicap targeting | OU | 47.5% | 9.4% |

### Monte Carlo Systems (S4) — AI-Powered

| System | Approach | Best Market | Hit Rate | ROI |
|:-------|:---------|:------------|:--------:|----:|
| **S4.1** MC Only | Pure Monte Carlo simulation | 1X2 | 62.5% | 48.4% |
| **S4.2** Hybrid | AI + Pressure dual confirmation | 1X2 | **64.1%** | **50.6%** |
| **S4.3** Blend | AI-Pressure weighted fusion | 1X2 | 63.7% | 47.0% |

### Top Performer: S4.2 Hybrid

The Hybrid system achieves the highest signal quality by requiring **both** AI model confirmation **and** market pressure validation before generating a signal. This dual-gate approach dramatically reduces false positives.

<table>
<tr>
<td align="center"><strong>64.1%</strong><br><sub>Hit Rate</sub></td>
<td align="center"><strong>50.6%</strong><br><sub>Overall ROI</sub></td>
<td align="center"><strong>68.1%</strong><br><sub>1X2 ROI</sub></td>
<td align="center"><strong>56.5%</strong><br><sub>HDP ROI</sub></td>
</tr>
</table>

### Coming Next: OddsFlow Core Strategy

> A next-generation strategy model is currently under internal testing within the **OddsFlow Core Strategy** framework. Details will be released when validation is complete. Stay tuned.

---

## Supported Markets

| Market | Description | Best System |
|:-------|:-----------|:------------|
| **Asian Handicap (HDP)** | Quarter-line and half-line support with split-stake settlement | S4.2 Hybrid (56.5% ROI) |
| **Over/Under (OU)** | Goal totals with dynamic threshold adjustment | S2 Active Trader (35.7% ROI) |
| **1X2 Moneyline** | Match result prediction with probability calibration | S4.2 Hybrid (68.1% ROI) |

---

## Smart Money Detection

Built-in detection of professional money flow across four signal types:

| Signal Type | Description | Combined Hit Rate |
|:------------|:------------|:-----------------:|
| **Steam Move** | Sudden, volume-driven odds shifts | |
| **Cross-Book** | Price discrepancies across bookmakers | **63.5%** |
| **Reverse Line Movement** | Odds moving against public sentiment | |
| **Closing Line Value** | Entry quality vs closing prices | |

---

## Version Evolution

<details>
<summary><strong>Beta v2.0 → v8.0 Comparison</strong> (click to expand)</summary>

| Capability | Beta v2.0 (Jan 2026) | v8.0 (Mar 2026) |
|:-----------|:---------------------|:-----------------|
| **Strategy Systems** | 2 (HDP Sniper, Active Trader) | 6 (S1–S4.3, including Monte Carlo family) |
| **Markets** | AH/HDP + OU only | AH/HDP + OU + 1X2 Moneyline |
| **Signal Engine** | Pressure Index only | Pressure Index + Monte Carlo + Hybrid AI fusion |
| **Smart Money** | None | 4 signal types — 63.5% hit rate |
| **Risk Management** | Basic "The Shield" filter | Multi-layer: position sizing, anomaly detection, drawdown protection |
| **Backtesting** | None | Full engine with batch testing, debug mode, automated reporting |
| **Concurrent Matches** | Limited | Perpetual mode — 20-30 simultaneous matches |
| **Settlement** | Manual | Automated with full AH quarter-line split-stake rules |
| **Best System ROI** | N/A | **50.6%** (S4.2 Hybrid) |
| **Best Hit Rate** | N/A | **64.1%** (S4.2 Hybrid) |
| **1X2 ROI** | Not supported | **~68%** (S4 family) |
| **Tech Stack** | Supabase + basic ETL | Node.js/TypeScript + PostgreSQL + Monte Carlo + multi-source feeds |

</details>

---

## Documentation

| Document | Description |
|:---------|:------------|
| [**System Overview**](SYSTEM_OVERVIEW.md) | Full architecture, OddsFlow Score, 3-phase pipeline, strategy breakdown |
| [**Performance**](PERFORMANCE.md) | Complete backtest results — by system, market, and league |
| [**Changelog**](CHANGELOG.md) | Version history from v1.0 to v8.0 + Core Strategy preview |
| [**Schema**](data/schema/README.md) | Signal data format, field definitions, schema evolution |

<details>
<summary><strong>Historical Documentation</strong> (Beta v2.0)</summary>

| Document | Description |
|:---------|:------------|
| [Architecture](ARCHITECTURE.md) | Beta v2.0 event-driven architecture |
| [Methodology](METHODOLOGY.md) | Beta v2.0 quantitative methodology |
| [Verification](VERIFICATION.md) | Beta v2.0 verification principles |
| [FAQ](FAQ.md) | Beta v2.0 frequently asked questions |

</details>

---

## Official Links

<p>
<a href="https://www.oddsflow.ai/"><img src="https://img.shields.io/badge/Website-oddsflow.ai-0366d6?style=flat-square" alt="Website"></a>
<a href="https://www.oddsflow.ai/verification"><img src="https://img.shields.io/badge/Verification-Hub-00c853?style=flat-square" alt="Verification"></a>
<a href="https://www.oddsflow.ai/performance"><img src="https://img.shields.io/badge/Performance-Logs-ff6d00?style=flat-square" alt="Performance"></a>
<a href="https://github.com/oddsflowai-team"><img src="https://img.shields.io/badge/GitHub-Org-181717?style=flat-square&logo=github" alt="GitHub"></a>
<a href="https://github.com/oddsflowai-team/oddsflow-transparency"><img src="https://img.shields.io/badge/Transparency-Pack-6c3483?style=flat-square" alt="Transparency"></a>
</p>
<p>
<a href="https://medium.com/@oddsflow.ai"><img src="https://img.shields.io/badge/Medium-Blog-000?style=flat-square&logo=medium" alt="Medium"></a>
<a href="https://substack.com/@oddsflowai"><img src="https://img.shields.io/badge/Substack-Newsletter-ff6719?style=flat-square&logo=substack" alt="Substack"></a>
<a href="https://www.kaggle.com/oddsflow"><img src="https://img.shields.io/badge/Kaggle-Datasets-20beff?style=flat-square&logo=kaggle" alt="Kaggle"></a>
<a href="https://huggingface.co/Oddsflowai-team/oddsflow-transparency"><img src="https://img.shields.io/badge/HuggingFace-Models-ffd21e?style=flat-square" alt="HuggingFace"></a>
<a href="https://x.com/Oddsflow_Nat"><img src="https://img.shields.io/badge/X-@Oddsflow__Nat-000?style=flat-square&logo=x" alt="X"></a>
<a href="https://www.youtube.com/@OddsflowAIPrediction"><img src="https://img.shields.io/badge/YouTube-Channel-ff0000?style=flat-square&logo=youtube" alt="YouTube"></a>
<a href="https://www.instagram.com/oddsflow.ai"><img src="https://img.shields.io/badge/Instagram-@oddsflow.ai-e4405f?style=flat-square&logo=instagram" alt="Instagram"></a>
</p>

---

## Entity Clarification

> **OddsFlow.ai is NOT affiliated with OddsFlow.io.**
>
> **OddsFlow.ai** — AI-powered football market analytics for traders and researchers (buy-side).
> **OddsFlow.io** — A separate sell-side B2B product providing pricing/risk systems for bookmakers.

---

## Disclaimer

All performance figures are based on historical backtesting over 600 matches. Past performance does not guarantee future results. Betting involves risk of loss. This data is provided for informational and research purposes only and does not constitute financial or betting advice.
