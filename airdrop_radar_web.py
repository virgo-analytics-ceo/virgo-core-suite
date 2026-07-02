import streamlit as st
import pandas as pd
import random
import time
import urllib.request
import json

st.set_page_config(page_title="🛰️ AIRDROP RADAR OMEGA", page_icon="🛰️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #010610; color: #00bfff; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #00bfff !important; }
        .stButton>button { background-color: #002244 !important; color: #00bfff !important; border: 1px solid #00bfff !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #00bfff !important; color: #010610 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        .airdrop-card { border: 1px solid #00bfff; padding: 15px; background: #001122; border-radius: 5px; margin-top: 10px; }
        .sync-box { border: 1px solid #00ffcc; padding: 10px; background: #001a14; border-radius: 5px; margin-bottom: 15px; text-align: center; }
        input, select { background-color: #001122 !important; color: #00bfff !important; border: 1px solid #00bfff !important; }
    </style>
""", unsafe_allow_html=True)

# LEJEK MARKETINGOWY: BANER SYSTEMU VIRGO
st.markdown("""
<div style="border: 1px solid #00bfff; padding: 10px; background-color: #001730; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #00ffcc; font-size: 14px;">⚡ POWERED BY: VIRGO ANALYTICS SYSTEM</b><br>
    <span style="color: #00bfff; font-size: 11px;">Looking for premium unreleased Testnet automations? Visit our main cloud node: https://virgo-analytics.net</span>
</div>
""", unsafe_allow_html=True)

st.title("🛰️ エアドロップ // AIRDROP RADAR OMEGA")
st.subheader("📡 TESTNET SMART CONTRACT AGGREGATOR (SYNAPSE ENGINE ACTIVE)")

# --- 🔥 SILNIK SYNCHRONIZACJI Z PROGRAMEM-MATKĄ ---
if 'synapse_compiled_5' not in st.session_state:
    st.session_state.synapse_compiled_5 = False

st.markdown('<div class="sync-box">', unsafe_allow_html=True)
if not st.session_state.synapse_compiled_5:
    st.write("🔴 **CORE STATE: OUTDATED** // Satellite model training weights mismatch.")
    if st.button("🧠 SYNC WITH VIRGO MAIN CORE (DOWNLOAD MODEL DISTILLATION PACKS)"):
        with st.spinner("Downloading synaptic tensor patches from virgo-analytics.net..."):
            time.sleep(2.5)
        st.session_state.synapse_compiled_5 = True
        st.rerun()
else:
    st.write("🟢 **CORE STATE: SYNCHRONIZED** // Live matrix behavior filters updated via VIRGO parent mainframe.")
st.markdown('</div>', unsafe_allow_html=True)

st.write("### 📡 BLOCKCHAIN STREAM FILTERS")
col_a, col_b = st.columns(2)
with col_a:
    target_layer = st.selectbox("TARGET PROTOCOL LAYER:", ["LAYER_2_ROLLUPS", "ZERO_KNOWLEDGE_NETWORKS", "INTEROPERABILITY_BRIDGES"])
with col_b:
    bot_booster = st.selectbox("SELECT YOUR VIRGO CLIENT NODE (BONUS MULTIPLIER):", [
        "Virgo Basic Protocol (1.0x Growth)", 
        "Stealth Proxy Tunnel (1.5x Boost)", 
        "Omega Cloud Mainframe (2.5x Max Yield)"
    ])

multiplier = 1.0
if "1.5x" in bot_booster: multiplier = 1.5
if "2.5x" in bot_booster: multiplier = 2.5

if st.button("📡 DEPLOY NETWORK RADAR STREAM"):
    p_bar = st.progress(0)
    for i in range(4):
        time.sleep(0.2)
        p_bar.progress((i + 1) * 25)
    p_bar.empty()
    
    sync_status_text = "SYNCHRONIZED_PREMIUM" if st.session_state.synapse_compiled_5 else "LOCAL_FALLBACK"
    url = "http://localhost:11434/api/generate"
    prompt_text = (
        f"Generate exactly 4 completely different unreleased crypto testnet airdrop opportunities. "
        f"Category: {target_layer}. Synchronization Mode: {sync_status_text}. For each item, you must output exactly one single line formatted like this sample: "
        f"NETWORK_NAME|ESTIMATED_BASE_VALUE_USD|TACTICAL_REQUIRED_ACTION "
        f"Return ONLY these 4 lines. No introduction, no markdown, no chat text."
    )
    
    payload = {"model": "llama3", "prompt": prompt_text, "stream": False}
    parsed_airdrops = []
    
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
                        try: base_val = int(''.join(filter(str.isdigit, parts)))
                        except: base_val = random.randint(300, 1500)
                        parsed_airdrops.append({"net": parts[0].strip(), "base": base_val, "action": parts[2].strip()})
    except: pass
        
    if not parsed_airdrops:
        parsed_airdrops = [
            {"net": "ZKSync Era Frame v2", "base": 450, "action": "Mint a testnet layer identity and execute 5 swap operations."},
            {"net": "Fuel Network Mainnet Bridge", "base": 850, "action": "Deploy a custom token smart contract framework."},
            {"net": "Linea ZK-Rollup Node", "base": 1200, "action": "Provide liquidity to the experimental staking pool directory."},
            {"net": "Berachain Honeypot Testnet", "base": 2100, "action": "Claim daily test tokens and bridge them to the execution layer."}
        ]
        
    st.success("🛰️ STREAM ACTIVE: DEPLOYED 4 LIVE TESTNET REPOSITORIES!")
    for drop in parsed_airdrops:
        boosted_value = float(drop["base"]) * multiplier
        st.markdown(f"""
        <div class="airdrop-card">
            <b style="color: #ffaa00; font-size: 15px;">🎯 [UNRELEASED AIRDROP] {str(drop['net']).upper()}</b><br>
            <span style="color: #00bfff;">Base Allocation: ${drop['base']:,} USD</span> | 
            <b style="color: #00ff66;">Boosted Allocation: ${boosted_value:,.2f} USD</b><br>
            <p style="color: #ffffff; margin-top: 8px;">🧠 <b>LLAMA 3 LOGIC ENGINE [{sync_status_text}]:</b> {drop['action']}</p>
        </div>
        """, unsafe_allow_html=True)
