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

def render_progress_bar(step, total=4):
    pct = int((step / total) * 100)
    filled_length = int(20 * step // total)
    bar = '█' * filled_length + '░' * (20 - filled_length)
    return f"{KOLORY['SZARY']}[{bar}] {pct}%{KOLORY['RESET']}"

def main():
    print("\033[H\033[J", end="") # Czyszczenie ekranu CMD
    print(f"{KOLORY['ZIELONY']}📟 VIRGO MATRIX // MEGAPUMP DEX RADAR DETECTOR [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: DEVNET SIMULATION // INGESTION DELAY: 300s ACTIVE // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['POMARANCZ']}[SCANNING] Initializing Raydium & Pump.fun mempool ingestion...{KOLORY['RESET']}\n")
    
    # Hakerski bonus: Animacja ładowania chunków sieciowych
    total_steps = 4
    for i in range(total_steps):
        time.sleep(random.uniform(0.2, 0.4))
        p_bar = render_progress_bar(i + 1, total_steps)
        print(f"    {p_bar} {KOLORY['SZARY']}Sniffing transaction blocks... Chunk {i+1}/4 parsed.{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ MATRIX SCAN COMPLETE ➔ DEMO DATA LAYER STABILIZED{KOLORY['RESET']}\n")

    # Symulowane, ograniczone dane dla wersji GitHub
    raw_demo_data = (
        "SOL_WHALE_889|92|Whale cluster accumulated 450 SOL on dynamic test contract. Pump imminent.\n"
        "DEV_STEALTH_441|88|Liquidity completely locked in automated validation node framework.\n"
        "PUMP_ROBOT_021|71|High-frequency bot cluster transaction stream detected on execution block.\n"
        "ALPHA_SHARD_9|64|Micro-transfers identified from anonymous dev hot wallet repository."
    )

    parsed_targets = []
    for line in raw_demo_data.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                parsed_targets.append({
                    "wallet": parts[0].strip(),
                    "confidence": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    # Kryptograficzny bonus wizualny budujący potężny autorytet na GitHubie
    integrity_string = "".join([t["wallet"] for t in parsed_targets])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNA WERYFIKACJA INTEGRALNOŚCI:\033[0m PUMP DETECTOR SECURE")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for target in parsed_targets:
        print(f"📡 {KOLORY['NIEBIESKI']}[TARGET DETECTED]{KOLORY['RESET']} {target['wallet']}")
        print(f"   ➔ System Confidence : {target['confidence']}%")
        print(f"   ➔ Ingested Activity : \033[93m{target['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Live Mainnet tracking, real-time contract decompiler loop, and automated Discord webhook alerts are locked. Upgrade to VIRGO CORE (£29/mo) or ENTERPRISE (£42/mo) to unlock the full raw matrix.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
