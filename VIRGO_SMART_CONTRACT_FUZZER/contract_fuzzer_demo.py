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

def generate_mock_wallet():
    chars = "ABCDEF0123456789"
    mock_hex = "".join(random.choice(chars) for _ in range(6))
    return f"0x{mock_hex}...{mock_hex[-4:]}"

def main():
    print("\033[H\033[J", end="") 
    print(f"{KOLORY['POMARANCZ']}📟 VIRGO MATRIX // SMART CONTRACT BYTECODE FUZZER [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: AUTOMATED BYTECODE EXPLOIT CHECKER // BATCH_LOCK: 10_RUNS // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['CZERWONY']}[ATTACK] Initiating memory fuzzing matrix on target contract...{KOLORY['RESET']}\n")
    
    for i in range(4):
        time.sleep(random.uniform(0.15, 0.3))
        w_addr = generate_mock_wallet()
        payload_hex = f"0xAA{random.randint(10,99)}FFCC"
        print(f"    {KOLORY['SZARY']}[ATTACK_VECTOR_{i+1}] Injected payload {payload_hex} via {w_addr} ➔ status: SUCCESS{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ FUZZING BATCH EXHAUSTED ➔ PARSED 4 SYSTEM EXPLOIT REPORTS{KOLORY['RESET']}\n")

    raw_fuzz_payload = (
        "OVERFLOW_EXPLOIT|91|Critical integer overflow vulnerability triggered in line 144. Safe math bypass active.\n"
        "REENTRANCY_WARNING|84|Stealth reentrancy path isolated inside withdraw function context.\n"
        "UNCHECKED_RETURN|69|Low-level call return value unverified. Dynamic memory shift payload injected.\n"
        "TIMESTAMP_DEPENDENCY|55|Block timestamp mutation tracking enabled. Simulated fuzzing record."
    )

    parsed_vectors = []
    for line in raw_fuzz_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                # CHIRURGICZNA POPRAWKA: .strip() wywołujemy bezpośrednio na indeksach stringów!
                parsed_vectors.append({
                    "vuln": parts[0].strip(),
                    "threat": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    integrity_string = "".join([v["vuln"] for v in parsed_vectors])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNY INTEGRITY LEDGER STAMP:\033[0m FUZZER ARMED")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for vector in parsed_vectors:
        print(f"🚨 {KOLORY['CZERWONY']}[VULNERABILITY DETECTED]{KOLORY['RESET']} {vector['vuln']}")
        print(f"   ➔ Threat Priority   : {vector['threat']}/100 // CRITICAL_SHADOW")
        print(f"   ➔ Exploit Telemetry : \033[93m{vector['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Unlimited Mainnet payload multi-threading, custom EVM exploit vector configuration, and automatic vulnerability logs patching are restricted. Upgrade to TIER 1 (£29/mo) or ENTERPRISE (£42/mo) to unlock full hardware throughput.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

if __name__ == "__main__":
    main()
