# OddsFlow v8 — Changelog

## Next — OddsFlow Core Strategy (In Development)

> A new algorithmic model is currently being validated inside the **OddsFlow Core Strategy** framework. This represents the next evolution of the engine beyond the S1–S4.3 system family. Further details will be published upon completion of internal testing.

---

## v8.0.0 — Major System Upgrade

*Released: March 2026*

### New: S4 Monte Carlo Strategy Family

Introduced three new AI-driven strategy systems powered by Monte Carlo simulation:

- **S4.1 MC Only** — Pure model-driven signal generation using probabilistic match simulation
- **S4.2 Hybrid** — Dual-confirmation system combining AI modeling with market pressure validation (best overall performer at 64.1% hit rate, 50.6% ROI)
- **S4.3 Blend** — Weighted probability fusion of AI and pressure models for high-volume, stable output

The S4 family brings AI-powered probability estimation to complement the existing pressure-based systems (S1–S3), resulting in dramatically improved performance on Asian Handicap and Moneyline markets.

### New: 1X2 Moneyline Market

Added full support for 1X2 (match result) betting:

- Probability calibration for Home/Draw/Away outcomes
- Odds filtering and edge detection
- Integrated across S1, S4.1, S4.2, and S4.3 systems
- Achieves ~68% ROI in backtesting

### New: Smart Money Detection

Introduced professional money flow detection with four signal types:

- **Steam Moves** — Detects sudden, volume-driven odds shifts
- **Cross-Book Signals** — Identifies price discrepancies across bookmakers
- **Reverse Line Movement** — Flags odds moving against public sentiment
- **Closing Line Value** — Tracks entry quality against closing prices

Smart money signals achieve 63.5% hit rate and serve as a supplementary confirmation layer.

### Improved: Risk Management

Enhanced the multi-layer risk framework:

- Per-match exposure limits and position sizing controls
- Time-based entry windows and lockout periods
- Opponent pressure counter-signal detection
- Anomaly detection for unusual market behavior
- Session-level drawdown protection

### Improved: Data Pipeline

- Real-time odds ingestion from multiple sources
- Live score and match statistics integration
- Automated settlement with full Asian Handicap rules (quarter-line split-stake support)
- Match report generation (halftime and fulltime)

### Improved: Perpetual Mode

- Continuous operation monitoring multiple concurrent matches (20-30 simultaneous)
- Automatic match discovery and scheduling (48-hour lookahead)
- Auto-restart between match batches
- Halftime and fulltime automated reporting

### Improved: Backtesting Engine

- Support for individual match and batch backtesting
- Automated report generation and database storage
- Debug mode for detailed signal analysis
- CLI interface for rapid iteration

---

## Version Comparison — Beta v2.0 vs v8.0

| Feature | Beta v2.0 | v8.0 | Improvement |
|---|---|---|---|
| **Strategies** | 2 modules | 6 systems (S1–S4.3) | 3x strategy coverage |
| **Markets** | AH + OU | AH + OU + 1X2 | +1X2 Moneyline (~68% ROI) |
| **Core Engine** | Pressure Index (rule-based) | Pressure + Monte Carlo + Hybrid AI | From heuristic to probabilistic modeling |
| **Best Hit Rate** | Unverified | 64.1% (S4.2 Hybrid) | Backtested across 600 matches |
| **Best ROI** | Unverified | 50.6% (S4.2 Hybrid) | Verified with full AH settlement rules |
| **Smart Money** | Not available | 4 detection types, 63.5% hit rate | New capability |
| **Risk Layer** | Single filter ("The Shield") | 6-layer framework (position sizing, anomaly detection, drawdown limits, time locks, opponent analysis, exposure caps) | From binary pass/fail to dynamic risk scoring |
| **Backtesting** | None | Full engine (batch + debug + CLI + reporting) | New capability |
| **Data Pipeline** | Single-source polling | Multi-source real-time feeds + automated settlement | End-to-end automation |
| **Concurrency** | Sequential processing | 20-30 simultaneous matches (Perpetual Mode) | Production-grade throughput |
| **HDP Performance** | Pressure-only (weak on handicaps) | S4.2 Hybrid: 63.0% hit rate, 56.5% ROI | Monte Carlo essential for HDP |
| **OU Performance** | Pressure-based (strength) | S2 Active Trader: 66.7% hit rate, 35.7% ROI | Pressure systems remain best for OU |

### Key Insight

> **Pressure-based systems (S1–S3) excel at Over/Under.** Monte Carlo systems (S4) dominate Asian Handicap and 1X2. The v8.0 architecture combines both families, allowing each system to operate where it performs best — something impossible under the v2.0 single-engine design.

---

## Previous Versions

### v7.x — Pressure System Maturity

*2026 Q1*

- Pressure-based signal systems (S1 Conservative, S2 Active Trader, S3 Sniper) fully calibrated
- Asian Handicap and Over/Under markets with improved edge detection
- Risk management with opponent pressure analysis and time-based controls
- Perpetual mode prototype — multi-match concurrent monitoring

### v6.x — Automated Settlement & Reporting

*2026 Q1*

- Automated settlement engine with full Asian Handicap rules (quarter-line split-stake)
- Halftime and fulltime match report generation
- Database-backed result storage and audit trail
- Performance reporting by system, market, and league

### v5.x — Multi-League Expansion

*2025 Q4*

- Expanded coverage to 7+ major European leagues and international fixtures
- League-specific parameter tuning for pressure thresholds
- Improved data normalization across heterogeneous source formats
- Liquidity filtering to exclude thin markets

### v4.x — Risk Management Framework

*2025 Q4*

- Introduced multi-layer risk management (position sizing, exposure limits, drawdown protection)
- Anomaly detection for unusual market behavior
- Per-match and session-level capital controls
- Opponent threat counter-signal analysis

### v3.x — Real-Time Odds Pipeline

*2025 Q3*

- Built real-time odds ingestion from multiple data providers
- Market pressure detection algorithm (foundation for Pressure Index)
- Live score integration with sub-minute latency
- Staleness protocol — automatic signal suppression on stale data

### v2.0 (Beta) — Event-Driven Architecture

*January 2026*

- Transitioned from static dataset generation to event-driven state machine
- Introduced Pressure Index and "The Shield" risk governance
- Focused exclusively on Asian Handicap and Over/Under (1X2 excluded for variance control)
- First public release of open verifiable value signals
- See [ARCHITECTURE.md](ARCHITECTURE.md) and [METHODOLOGY.md](METHODOLOGY.md) for historical documentation

### v1.0 — Initial Release

*January 2026*

- Initial public release of open verifiable value signals
- Support for 1X2, Asian Handicap, and Over/Under
- Conservative, HULK, and Value Hunter model styles
