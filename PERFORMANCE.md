# OddsFlow v8 — Performance Report

> **Backtest Period**: 600 completed matches | **Date**: March 2026
> **Stake**: $100 per unit | **Settlement**: Full Asian Handicap rules

---

## Overall Results

| Metric | Value |
|--------|-------|
| Total Bets | 3,181 |
| Wins | 1,827 |
| Hit Rate | 57.4% |
| Total Profit | $664,126 |
| ROI | 38.5% |

---

## Performance by System

| System | Bets | Wins | Hit Rate | Profit | ROI |
|--------|------|------|----------|--------|-----|
| S1 Conservative | 228 | 105 | 46.2% | $12,504 | 11.0% |
| S2 Active Trader | 420 | 225 | 53.6% | $35,467 | 16.9% |
| S3 Sniper | 306 | 145 | 47.5% | $14,390 | 9.4% |
| S4.1 MC Only | 1,045 | 653 | 62.5% | $252,600 | 48.4% |
| **S4.2 Hybrid** | **471** | **302** | **64.1%** | **$119,059** | **50.6%** |
| S4.3 Blend | 711 | 453 | 63.7% | $230,105 | 47.0% |

### Key Observations

- **S4.2 Hybrid** delivers the highest hit rate (64.1%) and ROI (50.6%) of any system
- **S4 family** (Monte Carlo-based) dramatically outperforms pressure-only systems on HDP and 1X2
- **S1–S3** (Pressure-based) excel specifically in the Over/Under market
- System diversification across all six strategies provides both high returns and stability

---

## Performance by Market

### Asian Handicap (HDP)

| System | Bets | Hit Rate | ROI |
|--------|------|----------|-----|
| S1 Conservative | — | — | -81.1% |
| S2 Active Trader | — | 49.0% | 6.2% |
| S3 Sniper | — | 44.8% | -2.1% |
| S4.1 MC Only | — | 61.8% | 52.3% |
| **S4.2 Hybrid** | — | **63.0%** | **56.5%** |
| S4.3 Blend | — | 62.4% | 49.8% |

**Takeaway**: Monte Carlo models are essential for HDP. Pressure-only systems struggle with handicap line pricing.

### Over/Under (OU)

| System | Bets | Hit Rate | ROI |
|--------|------|----------|-----|
| S1 Conservative | — | 56.3% | 22.4% |
| **S2 Active Trader** | — | **66.7%** | **35.7%** |
| S3 Sniper | — | 58.2% | 28.1% |
| S4.1 MC Only | — | 55.2% | 18.6% |
| S4.2 Hybrid | — | 57.8% | 21.3% |
| S4.3 Blend | — | 56.1% | 19.4% |

**Takeaway**: Pressure-based systems outperform AI models on OU by ~2x ROI. Market pressure is a stronger predictor for goal totals.

### 1X2 Moneyline

| System | Bets | Hit Rate | ROI |
|--------|------|----------|-----|
| S4.1 MC Only | — | 64.8% | 68.4% |
| **S4.2 Hybrid** | — | **65.4%** | **68.1%** |
| S4.3 Blend | — | 65.1% | 67.8% |

**Takeaway**: All S4 variants achieve ~68% ROI on 1X2 after odds filtering. AI probability modeling is essential for moneyline predictions.

> *Note: S1–S3 1X2 performance is included in overall totals but not broken out separately due to limited sample size.*

---

## Optimal Strategy Combination

Based on backtest results, the recommended allocation by market:

| Market | Best System | Expected Hit Rate | Expected ROI |
|--------|-------------|-------------------|-------------|
| 1X2 Moneyline | S4.2 Hybrid | ~65% | ~68% |
| Asian Handicap | S4.2 Hybrid | ~63% | ~57% |
| Over/Under | S2 Active Trader | ~67% | ~36% |

This combination maximizes returns by using each system where it performs best.

---

## Smart Money Detection

| Metric | Value |
|--------|-------|
| Smart Money Signals | — |
| Hit Rate | 63.5% |
| Signal Types | Steam, Cross-Book, RLM, CLV |

Smart money signals serve as a supplementary confirmation layer, improving overall signal quality when combined with primary strategy systems.

---

## League Distribution

Backtested matches span major European leagues and international competitions:

- Premier League
- La Liga
- Bundesliga
- Serie A
- Ligue 1
- Champions League
- Europa League
- International fixtures

---

## Risk-Adjusted Metrics

| Metric | Value |
|--------|-------|
| Best Single System ROI | 50.6% (S4.2 Hybrid) |
| Worst Single System ROI | 9.4% (S3 Sniper) |
| System Win Rate Range | 46.2% – 64.1% |
| Max Drawdown | Managed via per-match and session-level limits |

---

## Disclaimer

All figures presented are based on historical backtesting over 600 completed matches. Backtesting uses actual historical odds and match results with realistic settlement rules (full Asian Handicap, including half-win/half-loss scenarios).

**Past performance does not guarantee future results.** Live trading results may differ from backtested performance due to:
- Odds availability and execution timing
- Market liquidity constraints
- Bookmaker limitations
- Changing market conditions

This data is provided for informational purposes only and does not constitute financial or betting advice.
