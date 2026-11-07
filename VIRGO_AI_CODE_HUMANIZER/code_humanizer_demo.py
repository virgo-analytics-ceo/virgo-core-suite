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
    print(f"{KOLORY['CYAN']}📟 VIRGO MATRIX // AI ACADEMIC CODE SYNTHESIZER [DEMO SANDBOX]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: LINGUISTIC SYNTAX OBFUSCATOR // MAX_LINES: 10_LIMIT // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['POMARANCZ']}[TUNING] Analyzing input bytecode microstructure patterns...{KOLORY['RESET']}\n")
    
    # Hakerski bonus: Animowany licznik optymalizacji współczynnika Human Score
    for i in range(4):
        time.sleep(random.uniform(0.2, 0.35))
        current_score = 65 + (i * 11) + random.randint(1, 3)
        if current_score > 100: current_score = 100
        print(f"    {KOLORY['SZARY']}[PASS_{i+1}] Applying punctuation shifts... Current Human Score: {KOLORY['ZIELONY']}{current_score}%{KOLORY['RESET']}")

    print(f"\n{KOLORY['ZIELONY']}✔ SYNTAX OBFUSCATION MATRIX COMPILED SUCCESSFULLY{KOLORY['RESET']}\n")

    raw_humanizer_payload = (
        "SOLIDITY_REFACTOR|100|Bypassed Turnitin/GPTZero code detectors. Safe math logic humanized via syntax offsets.\n"
        "PYTHON_MUTATION|98|Variable token arrays randomized. Core structure logic obfuscated from AI footprint leaks.\n"
        "JS_COMPILER_SHIFT|94|Asynchronous loop structures optimized with micro-punctuation padding variables.\n"
        "GO_SHARD_TUNING|91|Linguistic humanizer pattern verification locked. Simulated sandbox record."
    )

    parsed_shards = []
    for line in raw_humanizer_payload.strip().split('\n'):
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                parsed_shards.append({
                    "layer": parts[0].strip(),
                    "score": parts[1].strip(),
                    "msg": parts[2].strip()
                })

    integrity_string = "".join([s["layer"] for s in parsed_shards])
    package_hash = generate_integrity_sha256(integrity_string)

    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}")
    print(f"  🔐 \033[35mKRYPTOGRAFICZNA WERYFIKACJA SYGNATURY:\033[0m HUMANIZER CORE")
    print(f"  🔑 \033[90mANTI-ALTERATION DATA STAMP       ➔ HASH:[{package_hash}]{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    for shard in parsed_shards:
        print(f"📡 {KOLORY['NIEBIESKI']}[HUMANIZED MODULE LAYER]{KOLORY['RESET']} {shard['layer']}")
        print(f"   ➔ AI Bypassed Score : {KOLORY['ZIELONY']}{shard['score']}% HUMAN RATIO{KOLORY['RESET']}")
        print(f"   ➔ Optimization Log  : \033[93m{shard['msg']}\033[0m")
        print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")

    print(f"\n{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Whole repositories automated mapping, local neural humanization weights, and direct GitHub action pipelines bypass are restricted. Upgrade to TIER 1 (£29/mo) or ENTERPRISE (£42/mo) on Gumroad to unlock full system capabilities.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
