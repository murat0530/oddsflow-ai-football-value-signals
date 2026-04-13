#!/usr/bin/env python3
"""
OddsFlow v8 — Telegram Signal Bot

Commands:
  /start   — Welcome message
  /signals — Active live signals
  /sample  — Sample signals (demo)
  /help    — Command list

Auto-notify: checks live signals every POLL_INTERVAL seconds,
sends a message to CHAT_ID when new signals appear.

Setup:
  cp .env.example .env       # fill in BOT_TOKEN and CHAT_ID
  python3 telegram_bot.py
"""

import json
import os
import threading
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Config — read from environment (or .env loaded externally)
# ---------------------------------------------------------------------------
BOT_TOKEN     = os.getenv("BOT_TOKEN", "")
CHAT_ID       = os.getenv("CHAT_ID", "")           # auto-notify target chat
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "300"))  # seconds

ROOT        = Path(__file__).parent
LIVE_PATH   = ROOT / "data" / "live" / "latest.json"
SAMPLE_PATH = ROOT / "data" / "sample-signals.json"

API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def tg_post(method: str, payload: dict) -> dict:
    resp = requests.post(f"{API}/{method}", json=payload, timeout=10)
    return resp.json()


def send_message(chat_id, text: str, parse_mode: str = "HTML") -> None:
    tg_post("sendMessage", {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    })


# ---------------------------------------------------------------------------
# Signal formatting
# ---------------------------------------------------------------------------

MARKET_EMOJI = {
    "ASIAN_HANDICAP": "⚽",
    "OVER_UNDER":     "🎯",
    "1X2":            "🏆",
}

CONFIDENCE_EMOJI = {
    "HIGH":   "🔴",
    "MEDIUM": "🟡",
    "LOW":    "🟢",
}

SMART_MONEY_LABELS = {
    "STEAM_MOVE_DETECTED": "🔥 Steam Move",
    "RLM_DETECTED":        "↩️ Reverse Line Move",
    "CLV_DETECTED":        "📈 CLV",
    "NONE":                None,
}


def format_signal(s: dict, idx: int) -> str:
    emoji  = MARKET_EMOJI.get(s["market_type"], "📊")
    conf   = CONFIDENCE_EMOJI.get(s["confidence"], "")
    edge   = s["edge_pct"]
    strat  = s["strategy"].replace("_", " ")
    m      = s.get("metrics", {})

    lines = [
        f"{emoji} <b>{s['match']}</b>",
        f"🏅 {s['league']}",
        f"📌 <b>{s['selection']}</b>   {conf} {s['confidence']}",
        f"📐 Strategy: <code>{strat}</code>",
        f"💰 Book: <b>{s['book_odds']}</b>  |  Fair: {s['fair_odds']}  |  Edge: <b>+{edge}%</b>",
    ]

    if "pressure_index" in m:
        lines.append(f"📊 Pressure: {m['pressure_index']}")

    sm = m.get("smart_money", "NONE")
    sm_label = SMART_MONEY_LABELS.get(sm)
    if sm_label:
        lines.append(f"🏦 Smart Money: {sm_label}")

    if "liquidity_status" in m:
        lines.append(f"💧 Liquidity: {m['liquidity_status']}")

    return "\n".join(lines)


def format_signals_message(signals: list, title: str) -> str:
    if not signals:
        return f"<b>{title}</b>\n\nŞu an aktif sinyal yok. 🔇"

    parts = [f"<b>{title}</b>  ({len(signals)} sinyal)\n"]
    for i, sig in enumerate(signals, 1):
        parts.append(f"─── Sinyal {i} ───")
        parts.append(format_signal(sig, i))

    edges = [s["edge_pct"] for s in signals]
    parts.append(f"\n📈 Ort. Edge: <b>{sum(edges)/len(edges):.1f}%</b>")
    parts.append("\n⚠️ <i>Bu veriler yalnızca bilgilendirme amaçlıdır.</i>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------

def cmd_start(chat_id) -> None:
    text = (
        "👋 <b>OddsFlow v8 Sinyal Botu</b>\n\n"
        "AI destekli futbol değer sinyalleri.\n\n"
        "<b>Komutlar:</b>\n"
        "/signals — Aktif canlı sinyaller\n"
        "/sample  — Demo sinyaller\n"
        "/help    — Bu mesaj\n\n"
        f"⏱ Otomatik bildirim her <b>{POLL_INTERVAL}s</b>."
    )
    send_message(chat_id, text)


def cmd_signals(chat_id) -> None:
    data    = load_json(LIVE_PATH)
    signals = data.get("signals", [])
    text    = format_signals_message(signals, "📡 Canlı Sinyaller")
    send_message(chat_id, text)


def cmd_sample(chat_id) -> None:
    data    = load_json(SAMPLE_PATH)
    signals = data.get("signals", [])
    text    = format_signals_message(signals, "🧪 Örnek Sinyaller (Demo)")
    send_message(chat_id, text)


def cmd_help(chat_id) -> None:
    cmd_start(chat_id)


COMMANDS = {
    "/start":   cmd_start,
    "/signals": cmd_signals,
    "/sample":  cmd_sample,
    "/help":    cmd_help,
}


def handle_update(update: dict) -> None:
    msg = update.get("message") or update.get("edited_message")
    if not msg:
        return
    text    = msg.get("text", "").strip()
    chat_id = msg["chat"]["id"]

    # strip bot username suffix (e.g. /start@MyBot)
    command = text.split("@")[0].split()[0].lower() if text else ""

    handler = COMMANDS.get(command)
    if handler:
        try:
            handler(chat_id)
        except Exception as exc:
            send_message(chat_id, f"❌ Hata: {exc}")


# ---------------------------------------------------------------------------
# Long-polling loop (commands)
# ---------------------------------------------------------------------------

def polling_loop() -> None:
    offset = None
    print("[bot] Polling başladı...")
    while True:
        try:
            params = {"timeout": 30, "allowed_updates": ["message"]}
            if offset:
                params["offset"] = offset
            resp = requests.get(f"{API}/getUpdates", params=params, timeout=40)
            data = resp.json()
            if not data.get("ok"):
                time.sleep(5)
                continue
            for update in data.get("result", []):
                offset = update["update_id"] + 1
                handle_update(update)
        except Exception as exc:
            print(f"[polling] Hata: {exc}")
            time.sleep(5)


# ---------------------------------------------------------------------------
# Auto-notify: watch live signals
# ---------------------------------------------------------------------------

_last_signal_ids: set = set()


def auto_notify() -> None:
    global _last_signal_ids
    if not CHAT_ID:
        return
    try:
        data    = load_json(LIVE_PATH)
        signals = data.get("signals", [])
        current_ids = {s["id"] for s in signals}
        new_signals = [s for s in signals if s["id"] not in _last_signal_ids]

        if new_signals:
            text = format_signals_message(new_signals, "🚨 Yeni Sinyaller!")
            send_message(CHAT_ID, text)
            print(f"[notify] {len(new_signals)} yeni sinyal gönderildi.")

        _last_signal_ids = current_ids
    except Exception as exc:
        print(f"[notify] Hata: {exc}")


def notify_loop() -> None:
    print(f"[notify] Otomatik kontrol her {POLL_INTERVAL}s...")
    while True:
        time.sleep(POLL_INTERVAL)
        auto_notify()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if not BOT_TOKEN:
        print("HATA: BOT_TOKEN ayarlanmamış.")
        print("  export BOT_TOKEN=<token>  veya .env dosyasını düzenle.")
        return

    # verify token
    me = tg_post("getMe", {})
    if not me.get("ok"):
        print(f"HATA: Geçersiz token — {me}")
        return
    bot_name = me["result"]["username"]
    print(f"[bot] @{bot_name} olarak bağlandı.")

    if CHAT_ID:
        print(f"[bot] Otomatik bildirim → chat_id: {CHAT_ID}")
        t = threading.Thread(target=notify_loop, daemon=True)
        t.start()
    else:
        print("[bot] CHAT_ID yok — otomatik bildirim devre dışı.")

    polling_loop()


if __name__ == "__main__":
    main()
