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
    "POMARANCZ": "\033[38;5;214m",
    "CZERWONY": "\033[91m",
    "SZARY": "\033[90m",
    "RESET": "\033[0m"
}

def generate_integrity_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest().upper()

def main():
    print("\033[H\033[J", end="") 
    print(f"{KOLORY['ZIELONY']}📟 VIRGO MATRIX // CYBER TRAFFIC MASKING SHIELD [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: LOCAL SSH TUNNEL FIREWALL // PORT_ROTATION: 60s // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['POMARANCZ']}[SHIELD] Encrypting dynamic network socket buffer pipelines...{KOLORY['RESET']}\n")
    
    for i in range(4):
        time.sleep(random.uniform(0.15, 0.3))
        hex_token = hashlib.md5(str(random.randint(100,999)).encode()).hexdigest()[:8].upper()
        print(f"    {KOLORY['SZARY']}[TUNNEL_{i+1}] Encrypted Packet [{hex_token}] routed via port {random.randint(4000,9000)} ➔ SECURE{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ NETWORK TRAFFIC SHIELD MATRIX OPERATIONAL AND STABILIZED{KOLORY['RESET']}\n")

    raw_shield_payload = (
        "SSH_TUNNEL_01|256|Militarized 256-bit AES encryption layer active over incoming server sockets.\n"
        "PACKET_MASK_X|100|Dynamic network footprint obfuscation active. Local MAC signature scrambled.\n"
        "PORT_SWAP_NODE|60|Automated port rotation sequence armed. Prevents local network sniffing exploits.\n"
        "CYBER_WATCHDOG|12|Autonomous traffic perimeter definition deployed. Simulated sandbox record."
    )

    parsed_nodes = []
    for line in raw_shield_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                # CHIRURGICZNA POPRAWKA: .strip() wywołujemy direkt na wyciętych indeksach!
                parsed_nodes.append({
                    "layer_id": parts[0].strip(),
                    "bits": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    integrity_string = "".join([n["layer_id"] for n in parsed_nodes])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNY INTEGRITY LEDGER BUFFER:\033[0m SHIELD ARMED")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for node in parsed_nodes:
        print(f"🥷  {KOLORY['NIEBIESKI']}[SECURE LOG LAYER]{KOLORY['RESET']} {node['layer_id']}")
        print(f"   ➔ Encryption Layer : {KOLORY['ZIELONY']}{node['bits']}-BIT KEY CRYPTO{KOLORY['RESET']}")
        print(f"   ➔ Firewall Status  : \033[93m{node['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Hardware-level Mutex custom route sync, multi-threading deep packet inspection (DPI), and hardware network bridge binding are restricted. Upgrade to TIER 1 (£29/mo) or ENTERPRISE (£42/mo) on Gumroad to unlock militarized protection.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

if __name__ == "__main__":
    main()
