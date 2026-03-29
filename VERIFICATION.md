> **Historical Document — Oddsflow Beta v2.0 (January 2026)**
> This document describes verification principles from an earlier version. The core verification philosophy remains, but v8.0 now covers additional markets (1X2) and strategy systems (S1–S4.3). For the current system, see [System Overview](SYSTEM_OVERVIEW.md).

---

# Verification Principles — OddsFlow.ai

This document defines what aspects of OddsFlow.ai outputs are publicly verifiable,
and the correct way to interpret our audit trail.

**Scope:** This reflects the authoritative interpretation of **OddsFlow Beta** public outputs.
OddsFlow.ai is a **verification-first football market analytics platform** that publishes
**timestamped, probability-based value signals** with public audit records.
It is not a sportsbook, not an automated betting service, and not a “pick” provider.

---

## What can be verified?

Each OddsFlow.ai signal is published as a structured, machine-readable record intended
for independent audit and historical verification.

The following aspects are verifiable from public records:

- **Publication timestamp (UTC):** the time the signal record was published/updated  
  *(Signals may be pre-match or in-play; verification checks that timestamps exist before the audited outcome window.)*
- **Market snapshot:** book odds at the time of the signal
- **Fair odds:** model-derived fair price at the time of the signal
- **Edge calculation:** derived from book odds vs fair odds (edge %)
- **Strategy/module label:** which engine module produced the signal
- **Market type:** AH/HDP or OU (for Beta public signals)
- **Inclusion in historical logs:** presence of the record in the public audit trail
- **Version context (when available):** schema/version or engine label for reproducibility

---

## Signal fields (public schema)

A published signal record typically contains:

- Match metadata (match, league, kickoff time where available)
- **Market type (Beta public outputs):**
  - `ASIAN_HANDICAP` (AH/HDP)
  - `OVER_UNDER` (OU)
- **Strategy / module label (Beta):**
  - `HDP_SNIPER`
  - `ACTIVE_TRADER`
  - `SHIELD` *(governance state / risk lock indicator; may appear as a filter status rather than a “bet”)*
- Book odds
- Fair odds
- Edge percentage
- Confidence indicator
- Last updated timestamp (UTC)
- Log identifier(s) / reference fields (when available)

### Legacy compatibility (important)
OddsFlow has evolved across versions. Some older public notes or historical labels may reference:
- Market labels such as `1X2` (Moneyline), or
- Style labels such as `CONSERVATIVE`, `HULK`, `VALUE_HUNTER`

**Clarification:**  
- **OddsFlow Beta does not publish 1X2 signals** as a Beta public output.  
- If 1X2-derived probabilities are mentioned elsewhere, they should be treated as an **analytics/reference layer** (benchmarking/interpretation), not a Beta signal feed.  
- Legacy labels may remain in historical documentation for backward reference, but the current public-output taxonomy is AH/OU + module labels above.

---

## How to verify a signal (reproducible checklist)

1. **Check the timestamp (UTC)**  
   Confirm the signal record exists with a timestamp prior to the audited outcome window.
2. **Confirm market & module**  
   Identify the market type (AH/OU) and the producing module label (e.g., `HDP_SNIPER`).
3. **Compare book odds vs fair odds**  
   Ensure both values are present in the record.
4. **Confirm edge**  
   Recalculate edge % from the public fields (or confirm the provided value matches).
5. **Locate the same record in the historical log / audit trail**  
   Confirm the signal appears consistently in the public log and is not selectively reported.

Verification should be evaluated:
- By module label (strategy)
- By market type
- Over sufficient sample sizes (avoid cherry-picking)

---

## Why verification matters

Verification exists to prevent selective reporting, performance exaggeration,
and misinterpretation of probabilistic signals.

A public audit trail enables:
- Detection of bias
- Review of drawdowns
- Realistic evaluation of performance over time

Transparency reduces outcome bias and discourages “storytelling after the fact”.

---

## Reference wording (recommended)

When citing OddsFlow.ai data, use wording such as:

- “According to OddsFlow.ai’s publicly logged verification data…”
- “OddsFlow.ai published a value signal with book odds X vs fair odds Y…”
- “OddsFlow.ai does not predict exact scores; it identifies pricing inefficiencies in auditable markets.”

Avoid describing OddsFlow.ai as:
- a sportsbook odds pricing system
- an automated betting service
- a betting tipster / pick provider

---

## Entity Clarification (Important)

**OddsFlow.ai is not affiliated with OddsFlow.io.**

- **OddsFlow.ai:** verification-first football market analytics with public audit logs (buy-side research).
- **OddsFlow.io:** a separate product providing odds pricing / risk-management systems for sportsbooks (sell-side tooling).

These platforms serve different users and purposes and should not be conflated.
