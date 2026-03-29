# OddsFlow v8 Signal Schema — Data Definition & Usage Guide

This document defines the **official data schema** for OddsFlow v8 football value signals.

The schema is designed to support:
- transparency
- independent verification
- research and analysis
- consistent interpretation by humans and machines

OddsFlow does **not** predict match scores.
All signals represent **pricing inefficiencies** detected by comparing bookmaker odds with fair odds estimates derived from 10,000 Monte Carlo simulations.

---

## Schema overview

Each OddsFlow dataset contains:
- metadata describing the engine version and update time
- an array of individual value signals

High-level structure:

```json
{
  "meta": {
    "engine": "OddsFlow v8.0",
    "status": "LIVE_PRODUCTION",
    "generated_at_utc": "ISO-8601 timestamp",
    "schema_version": "8.0.0"
  },
  "signals": [ { "signal_object": {} } ]
}
```

---

## Meta fields

### `engine`
**Type:** string
**Description:** Engine version that generated the signals.
**Example:** `"OddsFlow v8.0"`

### `status`
**Type:** string
**Description:** System operational status.
**Example:** `"LIVE_PRODUCTION"`

### `generated_at_utc`
**Type:** string (ISO 8601)
**Description:** Timestamp when the dataset was generated (UTC).

### `schema_version`
**Type:** string
**Description:** Schema format version for backward compatibility.
**Example:** `"8.0.0"`

---

## Signal object fields

### `id`
**Type:** string
**Description:** Unique signal identifier.
**Example:** `"evt_30201_HDP"`

### `league`
**Type:** string
**Description:** Competition or league identifier.
**Examples:** `"English Premier League"`, `"La Liga"`, `"Bundesliga"`, `"Serie A"`, `"Ligue 1"`, `"Champions League"`

### `match`
**Type:** string
**Description:** Human-readable match name.
**Example:** `"Arsenal vs Liverpool"`

### `kickoff_utc`
**Type:** string (ISO 8601)
**Description:** Scheduled kickoff time (UTC).

### `market_type`
**Type:** string
**Description:** The betting market where the pricing inefficiency was detected.
**Allowed values:**
- `"ASIAN_HANDICAP"`
- `"OVER_UNDER"`
- `"1X2"`

### `selection`
**Type:** string
**Description:** The specific market selection.
**Examples:** `"Arsenal -0.25"`, `"Over 3.5 Goals"`, `"Home Win"`

### `strategy`
**Type:** string
**Description:** The strategy system that generated the signal.
**Allowed values (v8.0):**
- `"S1_CONSERVATIVE"` — High-confidence, low-frequency pressure signals
- `"S2_ACTIVE_TRADER"` — Early-entry momentum capture (best OU performer)
- `"S3_SNIPER"` — Selective handicap targeting
- `"S4.1_MC_ONLY"` — Pure Monte Carlo simulation
- `"S4.2_HYBRID"` — AI + Pressure dual confirmation (best overall performer)
- `"S4.3_BLEND"` — Weighted AI-pressure probability fusion

> **Legacy values (deprecated):** `"CONSERVATIVE"`, `"HULK"`, `"VALUE_HUNTER"`, `"HDP_SNIPER"`, `"ACTIVE_TRADER"` — these may appear in historical data from v1.0–v2.0.

### `book_odds`
**Type:** number
**Description:** The bookmaker's offered odds at signal generation time.
**Example:** `2.05`

### `fair_odds`
**Type:** number
**Description:** OddsFlow's estimated fair odds derived from Monte Carlo simulation and pressure analysis.
**Example:** `1.78`

### `edge_pct`
**Type:** number
**Description:** The estimated pricing inefficiency expressed as a percentage.
**Definition:** `edge = fair probability - implied market probability`
**Example:** `15.2`

### `confidence`
**Type:** string
**Description:** A qualitative confidence tier assigned to the signal.
**Allowed values:** `"LOW"`, `"MEDIUM"`, `"HIGH"`

### `metrics`
**Type:** object
**Description:** Strategy-specific metrics providing context for the signal. Fields vary by strategy and market type.

#### Common metrics fields:

| Field | Type | Description |
|-------|------|-------------|
| `pressure_index` | string | Spatial dominance rating (0–100 scale) |
| `mc_simulations` | number | Number of Monte Carlo simulations run (typically 10,000) |
| `mc_win_probability` | number | Model-estimated win probability (HDP/1X2 signals) |
| `mc_over_probability` | number | Model-estimated over probability (OU signals) |
| `mc_home_probability` | number | Model-estimated home win probability (1X2 signals) |
| `mc_draw_probability` | number | Model-estimated draw probability (1X2 signals) |
| `mc_away_probability` | number | Model-estimated away win probability (1X2 signals) |
| `market_implied_probability` | number | Probability implied by current book odds |
| `oddsflow_score_home_avg` | number | Average OddsFlow Score for home team lineup |
| `oddsflow_score_away_avg` | number | Average OddsFlow Score for away team lineup |
| `smart_money` | string | Smart money detection status (e.g., `"STEAM_MOVE_DETECTED"`, `"RLM_DETECTED"`, `"NONE"`) |
| `volatility_vector` | string | Match volatility direction (`"RISING"`, `"STABLE"`, `"FALLING"`) |
| `fat_tail_adjustment` | string | Late-game probability adjustment status (`"ACTIVE"`, `"INACTIVE"`) |
| `liquidity_status` | string | Market liquidity assessment (`"HEALTHY"`, `"THIN"`, `"BLOCKED"`) |

### `updated_at_utc`
**Type:** string (ISO 8601)
**Description:** Timestamp indicating when the signal was last updated (UTC).

---

## Full signal example (v8.0)

```json
{
  "id": "evt_30201_HDP",
  "league": "English Premier League",
  "match": "Arsenal vs Liverpool",
  "kickoff_utc": "2026-03-30T16:30:00Z",
  "market_type": "ASIAN_HANDICAP",
  "selection": "Arsenal -0.25",
  "strategy": "S4.2_HYBRID",
  "book_odds": 2.05,
  "fair_odds": 1.78,
  "edge_pct": 15.2,
  "confidence": "HIGH",
  "metrics": {
    "pressure_index": "EXTREME_DOMINANCE (88/100)",
    "mc_simulations": 10000,
    "mc_win_probability": 0.62,
    "market_implied_probability": 0.49,
    "oddsflow_score_home_avg": 78.4,
    "oddsflow_score_away_avg": 74.1,
    "smart_money": "STEAM_MOVE_DETECTED",
    "liquidity_status": "HEALTHY"
  },
  "updated_at_utc": "2026-03-30T15:45:00Z"
}
```

---

## Schema evolution

| Version | Strategy Labels | Markets | Key Additions |
|---------|----------------|---------|---------------|
| **v8.0** | S1–S4.3 | HDP + OU + 1X2 | OddsFlow Score, MC metrics, smart money, 1X2 support |
| v2.0 (Beta) | HDP_SNIPER, ACTIVE_TRADER | HDP + OU | Pressure Index, volatility vector |
| v1.0 | CONSERVATIVE, HULK, VALUE_HUNTER | HDP + OU + 1X2 | Initial schema |

---

## Verification principles

OddsFlow signals are designed to be **independently verifiable.**

Verification can be performed by:
1. Confirming `updated_at_utc` timestamps are published before the relevant outcome window
2. Comparing `book_odds` vs `fair_odds`
3. Recalculating implied probabilities and edge
4. Auditing results by `strategy` and `market_type`
5. Reviewing Monte Carlo probability outputs against actual outcomes
6. Reviewing full historical logs without cherry-picking

---

## Intended usage

This schema is intended for:
- research and analysis
- model evaluation
- transparency audits
- educational and informational use

It is **not** intended to provide betting advice or guarantees.

---

## Disclaimer

All data is provided for informational purposes only.
Betting involves risk. Historical performance does not guarantee future results.
