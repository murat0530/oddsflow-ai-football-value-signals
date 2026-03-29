# OddsFlow v8 — AI-Powered Football Betting Signal Engine

OddsFlow is a real-time football betting signal engine that combines statistical modeling, machine learning, and market microstructure analysis to generate high-value betting opportunities across Asian Handicap, Over/Under, and Moneyline markets.

## System Performance at a Glance

| Metric | Value |
|--------|-------|
| Total Bets | 3,181 |
| Win Rate | 57.4% |
| ROI | 38.5% |
| Profit (@ $100/unit) | $664,126 |
| Markets | HDP / OU / 1X2 |
| Sample | 600 matches |

## How It Works — The 3-Phase Signal Pipeline

OddsFlow doesn't start when the whistle blows. It starts with the players.

### Phase 1: Player-Level Foundation (OddsFlow Score)

Every player in every match is assigned an **OddsFlow Score** — a proprietary composite rating derived from both **publicly available statistics** and **institutional-grade professional data sources**. The exact parameters and weighting of the OddsFlow Score are not disclosed.

This score quantifies each player's expected impact on match dynamics, and serves as the foundational input layer for all downstream modeling.

### Phase 2: Pre-Match Simulation (10,000 Sandbox Runs)

Before kickoff, the engine operates in two stages:

1. **Pre-Lineup AI Analysis** — Initial match modeling using expected squad compositions, historical matchup data, and OddsFlow Scores to establish baseline probability distributions.

2. **Post-Lineup Confirmation** — Once official lineups are confirmed, the engine executes **10,000 Monte Carlo simulations** incorporating the actual confirmed players. Every realistic scenario — scorelines, timing of goals, momentum shifts, substitution impacts — is computed and mapped into a complete probability foundation.

This foundation represents **all plausible match outcomes and their associated probabilities** before a single ball is kicked.

### Phase 3: Live Execution (Real-Time Edge Detection)

During the match, the engine compares **real-time match state** against the pre-computed 10,000-run simulation foundation:

- As events unfold (goals, cards, substitutions, momentum shifts), the system identifies **where the live match trajectory diverges from what the market is pricing**.
- When the divergence exceeds threshold — meaning the bookmaker odds lag behind what the simulation foundation already mapped — a value signal is generated.

> **In short:** OddsFlow knows all 10,000 versions of how the match could play out. It watches one version unfold in real time, and strikes when the market hasn't caught up.

---

## Version Evolution — Beta v2.0 vs v8.0

| Capability | Beta v2.0 (Jan 2026) | v8.0 (Mar 2026) |
|---|---|---|
| **Strategy Systems** | 2 (HDP Sniper, Active Trader) | 6 (S1–S4.3, including Monte Carlo family) |
| **Markets** | AH/HDP + OU only | AH/HDP + OU + 1X2 Moneyline |
| **Signal Engine** | Pressure Index only | Pressure Index + Monte Carlo Simulation + Hybrid AI fusion |
| **Smart Money Detection** | None | 4 signal types (Steam, Cross-Book, RLM, CLV) — 63.5% hit rate |
| **Risk Management** | Basic "The Shield" filter | Multi-layer: position sizing, anomaly detection, drawdown protection, time-based locks |
| **Backtesting** | None | Full engine with batch testing, debug mode, automated reporting |
| **Concurrent Matches** | Limited | Perpetual mode — 20-30 simultaneous matches |
| **Settlement** | Manual | Automated with full AH quarter-line split-stake rules |
| **Best System ROI** | N/A (no backtest) | **50.6%** (S4.2 Hybrid) |
| **Best System Hit Rate** | N/A | **64.1%** (S4.2 Hybrid) |
| **1X2 ROI** | Not supported | **~68%** (S4 family) |
| **Tech Stack** | Supabase + basic ETL | Node.js/TypeScript + PostgreSQL + Monte Carlo + real-time multi-source feeds |

## Strategy Systems

OddsFlow runs **six independent strategy systems**, each targeting different market conditions:

| System | Approach | Best Market | Hit Rate | ROI |
|--------|----------|-------------|----------|-----|
| **S1** Conservative | High-threshold pressure signals | OU | 46.2% | 11.0% |
| **S2** Active Trader | Early-entry momentum capture | OU | 53.6% | 16.9% |
| **S3** Sniper | Selective handicap targeting | OU | 47.5% | 9.4% |
| **S4.1** MC Only | Pure Monte Carlo simulation | 1X2 | 62.5% | 48.4% |
| **S4.2** Hybrid | AI + Pressure dual confirmation | 1X2 | **64.1%** | **50.6%** |
| **S4.3** Blend | AI-Pressure weighted fusion | 1X2 | 63.7% | 47.0% |

### Top Performer: S4.2 HYBRID

The Hybrid system achieves the highest signal quality by requiring **both** AI model confirmation and market pressure validation before generating a signal. This dual-gate approach filters out false positives and produces the best risk-adjusted returns.

- **64.1% hit rate** across all markets
- **50.6% ROI** overall
- **68.1% ROI** on 1X2 Moneyline

### Coming Next: OddsFlow Core Strategy

> A next-generation strategy model is currently under internal testing within the **OddsFlow Core Strategy** framework. Details will be released when validation is complete. Stay tuned.

---

## Supported Markets

- **Asian Handicap (HDP)** — Quarter-line and half-line support with split-stake settlement
- **Over/Under (OU)** — Goal totals with dynamic threshold adjustment
- **1X2 Moneyline** — Match result prediction with probability calibration

## Smart Money Detection

Built-in detection of professional money flow across four signal types, achieving a **63.5% hit rate** on smart money indicators.

## Documentation

| Document | Description |
|----------|-------------|
| [System Overview](SYSTEM_OVERVIEW.md) | Detailed architecture and strategy breakdown |
| [Performance](PERFORMANCE.md) | Full backtest results with system and market analysis |
| [Changelog](CHANGELOG.md) | v8 system updates and improvements |

---

## Official Links

| Channel | URL |
|---------|-----|
| Website | https://www.oddsflow.ai/ |
| Verification Hub | https://www.oddsflow.ai/verification |
| Performance Logs | https://www.oddsflow.ai/performance |
| GitHub Org | https://github.com/oddsflowai-team |
| Transparency Pack | https://github.com/oddsflowai-team/oddsflow-transparency |
| Hugging Face | https://huggingface.co/Oddsflowai-team/oddsflow-transparency |
| Medium | https://medium.com/@oddsflow.ai |
| Substack | https://substack.com/@oddsflowai |
| Kaggle | https://www.kaggle.com/oddsflow |
| X | https://x.com/Oddsflow_Nat |
| YouTube | https://www.youtube.com/@OddsflowAIPrediction |
| Instagram | https://www.instagram.com/oddsflow.ai |

## Entity Clarification

**OddsFlow.ai is NOT affiliated with OddsFlow.io.**

- **OddsFlow.ai** — AI-powered football market analytics for traders and researchers (buy-side).
- **OddsFlow.io** — A separate sell-side B2B product providing pricing/risk systems for bookmakers.

---

> **Disclaimer**: All performance figures are based on historical backtesting over 600 matches. Past performance does not guarantee future results. Betting involves risk of loss.
