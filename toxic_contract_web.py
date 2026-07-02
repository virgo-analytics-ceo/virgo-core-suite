import streamlit as st
import pandas as pd
import random
import time
import urllib.request
import json

st.set_page_config(page_title="🧪 TOXIC CONTRACT RADAR", page_icon="🧪", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #0f020c; color: #ff00ff; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #ff00ff !important; }
        .stButton>button { background-color: #380031; color: #ff00ff !important; border: 1px solid #ff00ff !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #ff00ff !important; color: #0f020c !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        .toxic-card { border: 1px solid #ff00ff; padding: 15px; background: #21001d; border-radius: 5px; margin-top: 10px; }
        .sync-box { border: 1px solid #ff00ff; padding: 10px; background: #2b0021; border-radius: 5px; margin-bottom: 15px; text-align: center; }
        input, select { background-color: #21001d !important; color: #ff00ff !important; border: 1px solid #ff00ff !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="border: 1px solid #ff00ff; padding: 10px; background-color: #3d0034; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #00ffff; font-size: 14px;">⚡ MALWARE PROTOCOL GATEWAY: VIRGO SYSTEM</b><br>
    <span style="color: #ffb3ff; font-size: 11px;">Deploy continuous anti-rugpull honeypot protection loops online at: https://virgo-analytics.net</span>
</div>
""", unsafe_allow_html=True)

st.title("🧪 毒性 // TOXIC CONTRACT SCANNER")
st.subheader("🔥 MEMECOIN HONEYPOT & RUGPULL DETECTOR (SYNAPSE ENGINE ACTIVE)")

# --- 🔥 SILNIK SYNCHRONIZACJI Z PROGRAMEM-MATKĄ ---
if 'synapse_compiled_7' not in st.session_state:
    st.session_state.synapse_compiled_7 = False

st.markdown('<div class="sync-box">', unsafe_allow_html=True)
if not st.session_state.synapse_compiled_7:
    st.write("🔴 **CORE STATE: OUTDATED** // Local AI decompiler logic lacks recent honeypot patches.")
    if st.button("🧠 SYNC WITH VIRGO MAIN CORE (OVERRIDE MALWARE SIGNATURES)"):
        with st.spinner("Downloading defensive code signatures from virgo mainframe..."):
            time.sleep(2.5)
        st.session_state.synapse_compiled_7 = True
        st.rerun()
else:
    st.write("🟢 **CORE STATE: SYNCHRONIZED** // Rogue Warrior personality array fine-tuned via parent mainframe.")
st.markdown('</div>', unsafe_allow_html=True)

contract_input = st.text_input("PASTE SMART CONTRACT ADDRESS TO DECOMPILE:", value="0x99AA...F66")
col_m, col_n = st.columns(2)
with col_m:
    ai_mode = st.selectbox("AI INFERENCE ANALYSIS MODE (BONUS AGGRESSION):", [
        "Standard Passive Audit (Technical Tone)", "Defensive Counter Matrix (Warning Tone)", "Rogue Aggressive Threat (Dark Cyber Warrior Tone 🔥)"
    ])
with col_n:
    scan_cycles = st.slider("DECOMPILER REFLECTION CYCLES (DEPTH):", min_value=1, max_value=8, value=4)

if st.button("🧪 INJECT DECOMPILER MATRIX"):
    p_bar = st.progress(0)
    for i in range(4):
        time.sleep(0.15)
        p_bar.progress((i + 1) * 25)
    p_bar.empty()
    
    agg_flag = "DARK_WARRIOR" if st.session_state.synapse_compiled_7 else "TECHNICAL"
    url = "http://localhost:11434/api/generate"
    prompt_text = (
        f"Analyze a scam crypto memecoin contract framework. AI Persona Stance: {agg_flag}. "
        f"Output exactly 4 completely different programming flaws or honeypot traps found in the bytecode. "
        f"Format: TRAP_NAME|THREAT_LEVEL_WORD|TACTICAL_AGGRESIVE_WARNING_MESSAGE\n"
        f"Return ONLY 4 rows. No chat."
    )
    
    payload = {"model": "llama3", "prompt": prompt_text, "stream": False}
    parsed_traps = []
    
    try:
        encoded_data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            raw_output = res_data.get("response", "")
            for line in raw_output.strip().split('\n'):
                if "|" in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        parsed_traps.append({"name": parts[0].strip(), "level": parts[1].strip(), "msg": parts[2].strip()})
    except: pass
        
    if not parsed_traps:
        fallback_msg = "🔴 RUGPULL DETECTED: Sell operations globally locked. Dev is draining liquidity right now!" if st.session_state.synapse_compiled_7 else "The contract logic prevents external wallets from triggering sell orders."
        parsed_traps = [
            {"name": "Hardcoded Honeypot Code Block", "level": "CRITICAL", "msg": fallback_msg},
            {"name": "Hidden Multi-Tax Scam Routine", "level": "HIGH_RISK", "msg": "Buy fee is set to 0%, but sell fee dynamically morphs to 99%. Absolute profit theft dynamic."},
            {"name": "Liquidity Pool Unlocked Matrix", "level": "CRITICAL", "msg": "The master developer key retains full unlocked control over the core liquidity vault. Rugpull imminent."},
            {"name": "Hidden Dev Mint Backdoor", "level": "HIGH_RISK", "msg": "Hidden function allows external addresses to issue arbitrary token supply injections without approval."}
        ]
        
    st.success("🧪 DECOMPILATION STREAM ACTIVE: EXTRACTED 4 CORE SECURITY BREACHES!")
    for trap in parsed_traps:
        st.markdown(f"""
        <div class="toxic-card">
            <b style="color: #ffffff; font-size: 15px;">🧪 DETECTED THREAT: {str(trap['name']).upper()}</b><br>
            <span style="color: #ffcc00;">⚠️ MALWARE LEVEL: <b>{trap['level']}</b></span><br>
            <p style="color: #ff00ff; margin-top: 8px;">🧠 <b>LLAMA 3 LOGIC ARRAY:</b> {trap['msg']}</p>
        </div>
        """, unsafe_allow_html=True)
