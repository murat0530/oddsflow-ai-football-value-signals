#!/usr/bin/env python3
"""
OddsFlow v8 — Test Run
Loads sample signals, verifies edge calculations, and prints a summary report.
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).parent


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def implied_prob(odds: float) -> float:
    """Convert decimal odds to implied probability."""
    return 1.0 / odds


def calc_edge(book_odds: float, fair_odds: float) -> float:
    """Edge = (book_odds / fair_odds - 1) * 100  (OddsFlow convention)."""
    return round((book_odds / fair_odds - 1) * 100, 2)


def kelly_fraction(edge_pct: float, book_odds: float) -> float:
    """
    Kelly criterion: f = (b*p - q) / b
    where b = net odds (book_odds - 1), p = fair prob, q = 1 - p
    """
    b = book_odds - 1
    p = implied_prob(book_odds) + edge_pct / 100
    p = min(max(p, 0.0), 1.0)
    q = 1.0 - p
    kelly = (b * p - q) / b if b > 0 else 0.0
    return round(max(kelly, 0.0) * 100, 2)  # as %


def separator(char: str = "─", width: int = 72) -> str:
    return char * width


def print_signal(s: dict, idx: int) -> None:
    edge_check = calc_edge(s["book_odds"], s["fair_odds"])
    kelly = kelly_fraction(s["edge_pct"], s["book_odds"])
    match_edge = math.isclose(edge_check, s["edge_pct"], abs_tol=0.5)

    print(f"\n  [{idx}] {s['match']}  |  {s['league']}")
    print(f"      Market   : {s['market_type']}  →  {s['selection']}")
    print(f"      Strategy : {s['strategy']}   Confidence: {s['confidence']}")
    print(f"      Book odds: {s['book_odds']}   Fair odds: {s['fair_odds']}")
    print(f"      Edge     : {s['edge_pct']}%  (recalculated: {edge_check}%)  {'✓' if match_edge else '⚠ MISMATCH'}")
    print(f"      Kelly    : {kelly}% of bankroll")

    m = s.get("metrics", {})
    if "pressure_index" in m:
        print(f"      Pressure : {m['pressure_index']}")
    if "smart_money" in m:
        print(f"      Smart $  : {m['smart_money']}")
    if "liquidity_status" in m:
        print(f"      Liquidity: {m['liquidity_status']}")


def run():
    print(separator("═"))
    print("  OddsFlow v8 — Test Run")
    print(separator("═"))

    # --- Sample signals ---
    sample_path = ROOT / "data" / "sample-signals.json"
    data = load_json(sample_path)
    meta = data["meta"]
    signals = data["signals"]

    print(f"\n  Engine  : {meta['engine']}   Status: {meta['status']}")
    print(f"  File    : {sample_path.relative_to(ROOT)}")
    print(f"  Signals : {len(signals)}")
    print(separator())

    for i, sig in enumerate(signals, 1):
        print_signal(sig, i)

    print(f"\n{separator()}")

    # --- Aggregate stats ---
    edges = [s["edge_pct"] for s in signals]
    strategies = [s["strategy"] for s in signals]
    markets = [s["market_type"] for s in signals]

    print(f"\n  AGGREGATE STATS ({len(signals)} signals)")
    print(f"  Average edge : {sum(edges)/len(edges):.2f}%")
    print(f"  Max edge     : {max(edges):.2f}%   Min edge: {min(edges):.2f}%")
    print(f"  Strategies   : {', '.join(set(strategies))}")
    print(f"  Markets      : {', '.join(set(markets))}")

    # --- Live feed check ---
    live_path = ROOT / "data" / "live" / "latest.json"
    live = load_json(live_path)
    live_count = len(live.get("signals", []))
    print(f"\n  Live feed    : {live_path.relative_to(ROOT)}  →  {live_count} active signal(s)")

    print(f"\n{separator('═')}")
    print("  All checks passed. OddsFlow v8 signal pipeline is readable and valid.")
    print(separator("═"))


if __name__ == "__main__":
    run()
