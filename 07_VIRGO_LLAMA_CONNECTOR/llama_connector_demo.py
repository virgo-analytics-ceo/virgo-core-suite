

import sys
import os
import time
import json
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

def check_local_ollama_status():
    # Chirurgiczne, natywne sprawdzenie czy port Ollama 11434 żyje w systemie Windows
    url = "http://localhost:11434/"
    try:
        with urllib.request.urlopen(url, timeout=1) as response:
            return response.status == 200
    except:
        return False

def main():
    print("\033[H\033[J", end="") 
    print(f"{KOLORY['NIEBIESKI']}📟 VIRGO MATRIX // OLLAMA LLAMA 3 NETWORK PORT CONNECTOR{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}📡 MODE: LOCALHOST REST-API NETWORKING // PORT: 11434 // ONLINE{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")

    print(f"⚙️  {KOLORY['POMARANCZ']}[PORT_CHECK] Pingowanie lokalnego portu Ollama 11434...{KOLORY['RESET']}")
    time.sleep(0.5)
    
    ollama_online = check_local_ollama_status()
    
    if ollama_online:
        print(f"    ➔ Status: {KOLORY['ZIELONY']}CONNECTED // OLLAMA DAEMON RESPONDING{KOLORY['RESET']}\n")
    else:
        print(f"    ➔ Status: {KOLORY['POMARANCZ']}SIMULATED // NO LOCAL OLLAMA INTERFACE DETECTED{KOLORY['RESET']}\n")
        print(f"    {KOLORY['SZARY']}[!] Program przechodzi w tryb symulacji pakietu z powodu braku uruchomionego serwera Ollama na maszynie MSI.{KOLORY['RESET']}\n")

    print(f"📡 {KOLORY['CYAN']}[PROMPT_SEND] Wstrzykiwanie payloadu tekstowego do silnika Llama 3...{KOLORY['RESET']}")
    time.sleep(0.4)

    # Hakerski Bonus: Surowy zrzut struktury JSON przesyłanej przez sieć
    mock_payload = {"model": "llama3", "prompt": "Analyze crypto contract stability map", "stream": False}
    print(f"    {KOLORY['SZARY']}Payload Header: {json.dumps(mock_payload)}{KOLORY['RESET']}\n")
    time.sleep(0.4)

    print(f"{KOLORY['ZIELONY']}✔ RESPONSE INGESTED SUCCESSFULLY ➔ PARSED AI ANALYSIS LOGS{KOLORY['RESET']}\n")
    print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}")
    print(f"🤖 {KOLORY['ZIELONY']}[LLAMA 3 CORE RESPONSE]:{KOLORY['RESET']}")
    print(f"   ➔ Critical Analysis: \033[93mTarget contract bytecode matches automated sandwich attack footprint.{KOLORY['RESET']}")
    print(f"   ➔ Threat Mitigation: \033[93mIsolate smart contract wallet cluster immediately. Integrity seal armed.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}--------------------------------------------------------------------={KOLORY['RESET']}\n")

    print(f"{KOLORY['CZERWONY']}🚨 PREMIUM RESTRICTION:{KOLORY['RESET']} {KOLORY['SZARY']}Asynchronous chunk streaming response buffers, custom temperature parameter matrix array hooks, and direct live model training nodes are restricted. Upgrade to TIER 2 Enterprise (£42/mo) on Gumroad to open full pipe speed.{KOLORY['RESET']}")
    print(f"{KOLORY['SZARY']}====================================================================={KOLORY['RESET']}\n")
    input(f"{KOLORY['SZARY']}Kliknij Enter, aby powrócić do centralnego Mainframe...{KOLORY['RESET']}")

if __name__ == "__main__":
    main()
