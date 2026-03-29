> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> This directory contains strategy definitions from an earlier version. In v8.0, these strategies have evolved into the S1–S4.3 system family. For the current strategy breakdown, see [System Overview](../SYSTEM_OVERVIEW.md).

---

# Oddsflow Beta Engine: Strategy Definitions

## Overview
This directory documents the active quantitative strategies employed by the **Oddsflow Beta v2.0 Engine**.

> **⚠️ Deprecation Notice:**
> Legacy model styles defined in v1.0 (`HULK`, `Conservative`, `Value Hunter`) have been **deprecated** and removed from production. The engine now operates strictly on the event-driven modules listed below.

---

## Active Strategy Modules (v2.0)

### 1. [HDP Sniper](HDP_Sniper.md)
* **Market Focus:** Asian Handicap (HDP).
* **Role:** The "Alpha Generator." Targets favorites with high **Pressure Index** dominance but suppressed prices.
* **Key Metric:** Spatial Dominance vs. Price Lag.

### 2. [Active Trader](Active_Trader.md)
* **Market Focus:** Over/Under (OU).
* **Role:** The "Steady Accumulator." Exploits volatility mispricing and time-decay inefficiencies.
* **Key Metric:** Liquidity Gap Analysis.

---

## Selection Logic
The Oddsflow Beta engine automatically routes signals to the appropriate strategy module based on real-time **State Machine** data:
* If `Dominance_Vector` is High -> Trigger **HDP Sniper**.
* If `Volatility_Vector` is High -> Trigger **Active Trader**.
* If `Risk_Flags` (Red Card/VAR) are Active -> **The Shield** blocks all signals.
