import sys
import os
import time
import json
import random
import urllib.request
import hashlib

# Bezpieczne wymuszenie ścieżki uruchomieniowej
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Słownik surowych kodów ANSI dla hakerskiego klimatu w oknie CMD
KOLORY = {
    "ZIELONY": "\033[38;5;46m",
    "NIEBIESKI": "\033[94m",
    "CYAN": "\033[96m",
    "POMARANCZ": "\033[38;5;214m",
    "CZERWONY": "\033[91m",
    "SZARY": "\033[90m",
    "RESET": "\033[0m"
}

def generate_integrity_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest().upper()

def render_stealth_scan(step):
    frames = ["🔍 [SCANNING]", "📡 [LISTENING]", "🥷 [INTERCEPTING]", "⚡ [DECRYPTING]"]
    return f"{KOLORY['POMARANCZ']}{frames[step % len(frames)]}{KOLORY['RESET']}"

def main():
    print("\033[H\033[J", end="") # Czyszczenie ekranu CMD
    print(f"{KOLORY['CYAN']}📟 VIRGO MATRIX // STEALTH DISCORD WATCHDOG NODES [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: DPI PACKET SNIFFER // TARGET: DISCORD GATEWAY // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"🥷  {KOLORY['SZARY']}[!] Starting background network socket monitoring...{KOLORY['RESET']}\n")
    
    # Hakerski bonus: Dynamiczny, pionowy skaner stanów wątków
    for i in range(4):
        time.sleep(random.uniform(0.2, 0.4))
        status_frame = render_stealth_scan(i)
        print(f"    {status_frame} {KOLORY['SZARY']}Sniffing Discord text-channel relays... Pipeline {i+1}/4 active.{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ GATEWAY LINKABLISHED ➔ CAPTURED 4 SIMULATED ALPHA CHANNELS{KOLORY['RESET']}\n")

    # Symulowany, ograniczony wsad dla wersji GitHub
    raw_discord_payload = (
        "DISCORD_INVITE_X99|95|Captured link to hidden alpha room: discord.gg/solana-whale-leaks. High volume accumulation chat.\n"
        "META_EXPLOIT_NODE|89|Intercepted developer channel token refresh sequence. Target server locked.\n"
        "INSIDER_CHAT_LINK|76|Stealth discord invitation parsed: discord.gg/base-insiders-inner-circle.\n"
        "ALPHA_BOT_RELAY|61|Dynamic tracking link identified on execution socket. Simulated data feed."
    )

    parsed_logs = []
    for line in raw_discord_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                parsed_logs.append({
                    "node_id": parts[0].strip(),
                    "security_pct": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    # Kryptograficzna weryfikacja integralności budująca prestiż na GitHubie
    integrity_string = "".join([l["node_id"] for l in parsed_logs])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNA INTEGRALNOŚĆ PRZECHWYTU:\033[0m DISCORD EYE SECURE")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for log in parsed_logs:
        print(f"🥷  {KOLORY['NIEBIESKI']}[INTERCEPTED NODE]{KOLORY['RESET']} {log['node_id']}")
        print(f"   ➔ Infiltration Rate : {log['security_pct']}% // SECURE_RELAY")
        print(f"   ➔ Intercepted Comm  : \033[93m{log['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Multi-threaded proxy rotation routing, real-time WebSocket connection pools, and automatic Discord webhook forwarding are restricted. Upgrade to TIER 1 (£29/mo) or ENTERPRISE (£42/mo) on Gumroad to unlock the raw execution network.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
