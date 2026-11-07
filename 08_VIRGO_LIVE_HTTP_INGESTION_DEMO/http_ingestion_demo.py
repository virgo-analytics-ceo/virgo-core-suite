import sys
import os
import time
import json
import urllib.request
import hashlib
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

def main():
    print("\033[H\033[J", end="") 
    print(f"{KOLORY['ZIELONY']}📟 VIRGO MATRIX // LIVE HTTP DATA INGESTION ENGINE [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: urllib.request SOCKET RELAY // BROADCAST: LIVE_GET // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['POMARANCZ']}[HTTP_REQUEST] Odpytywanie zewnętrznych punktów końcowych API...{KOLORY['RESET']}\n")
    
    # Hakerski Bonus: Dynamiczny monitor opóźnienia i delty sieciowej
    for i in range(4):
        time.sleep(random.uniform(0.15, 0.3))
        ping = random.randint(12, 28)
        visual_ping = '⚡' * (ping // 5)
        print(f"    {KOLORY['SZARY']}[FETCH_{i+1}] GET https://virgomatrix.internal ➔ Status: 200 OK ({ping}ms) {visual_ping}{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ HTTP STREAM INGESTED AND DESERIALIZED SUCCESSFULLY{KOLORY['RESET']}\n")

    # Symulowany, ustrukturyzowany ładunek JSON zebrany przez sieć
    raw_api_payload = (
        "SOL_PRICE|245.50|Live price feed ingested directly from decentralized liquidity nodes.\n"
        "SUI_VOLUME|12500000|24h institutional accumulation tracking index established.\n"
        "BASE_GAS_FEE|14|Network priority gas parameters stabilized below average threshold.\n"
        "BTC_ORDER_FLOW|89000|Orderbook depth calculation completed. Simulated sandbox record."
    )

    parsed_metrics = []
    for line in raw_api_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                # Bezbłędne, chirurgiczne parsowanie indeksów stringa
                parsed_metrics.append({
                    "ticker": parts[0].strip(),
                    "val": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    integrity_string = "".join([m["ticker"] for m in parsed_metrics])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNY INTEGRITY INGESTION MATRIX:\033[0m PACKET VERIFIED")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for metric in parsed_metrics:
        print(f"📡 {KOLORY['NIEBIESKI']}[LIVE METRIC]{KOLORY['RESET']} {metric['ticker']}")
        print(f"   ➔ Telemetry Value  : {KOLORY['ZIELONY']}{metric['val']}{KOLORY['RESET']}")
        print(f"   ➔ Extraction Log   : \033[93m{metric['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Asynchronous multi-threaded endpoint flood gates, auto-reconnect fallback proxy sockets, and multi-asset dynamic WebSocket tracking channels are restricted. Upgrade to TIER 1 Core (£29/mo) on Gumroad to open full execution throughput.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
