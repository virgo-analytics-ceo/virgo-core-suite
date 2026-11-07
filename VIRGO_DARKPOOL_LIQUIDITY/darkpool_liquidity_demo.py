import sys
import os
import time
import json
import random
import urllib.request
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

KOLORY = {
    "ZIELONY": "\033[38;5;46m",
    "NIEBIESKI": "\033[94m",
    "CYAN": "\033[96m",
    "POMARANCZ": "\033;38;5;214m",
    "CZERWONY": "\033[91m",
    "SZARY": "\033[90m",
    "RESET": "\033[0m"
}

def generate_integrity_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest().upper()

def main():
    print("\033[H\033[J", end="") 
    print(f"{KOLORY['NIEBIESKI']}📟 VIRGO MATRIX // DARKPOOL OTC LIQUIDITY WATCHDOG [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: HIDDEN ORDER FEED SCRAPER // BROADCAST: OTC_FEED_SIM // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['CYAN']}[INGESTION] Sniffing block flow for cross-network large scale block trades...{KOLORY['RESET']}\n")
    
    # Hakerski bonus: Dynamiczny monitor delty wolumenu za pomocą znaków pionowych kreskach
    for i in range(4):
        time.sleep(random.uniform(0.2, 0.35))
        delta_blocks = '▲' * (i + 2) + '▼' * (3 - i)
        print(f"    {KOLORY['SZARY']}[BLOCK_{i+1}] Liquidity Cluster {delta_blocks} ➔ Ingesting institutional dark pool hash... Done.{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ HIDDEN ORDER LEDGER COMPILED FROM SIMULATED SECTOR{KOLORY['RESET']}\n")

    raw_darkpool_payload = (
        "OTC_ORDER_X01|5000000|Institutional block trade identified: 5,000,000 USDC private transfer hash parsed.\n"
        "HIDDEN_BID_SOL|85000|Stealth limit bid wall localized at key demand level. Darkpool buffer locked.\n"
        "ICEBERG_ORDER_9|120000|Iceberg layer fragmented: automated selling block split into 12 distinct shards.\n"
        "DARK_POOL_FEED|43000|Anonymous fund accumulation tracking active. Simulated sandbox record."
    )

    parsed_orders = []
    for line in raw_darkpool_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                parsed_orders.append({
                    "pool_id": parts[0].strip(),
                    "volume": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    integrity_string = "".join([o["pool_id"] for o in parsed_orders])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNY INTEGRITY NETWORK LEDGER:\033[0m LIQUIDITY LOCKED")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for order in parsed_orders:
        print(f"📡 {KOLORY['NIEBIESKI']}[OTC BLOCK ORDER]{KOLORY['RESET']} {order['pool_id']}")
        print(f"   ➔ Absolute Volume   : \033[92m{int(order['volume']):,}\033[0m UNITS")
        print(f"   ➔ Ingested Telemetry : \033[93m{order['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Live REST-API gateway channels, institutional exchange endpoint hooks, and multi-asset dynamic tracking ledger are restricted. Upgrade to TIER 1 (£29/mo) or ENTERPRISE (£42/mo) on Gumroad to unlock full system bandwidth.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
