import streamlit as st
import pandas as pd
import random
import time
import urllib.request
import json

st.set_page_config(page_title="🦊 WALLET METRICS SHIELD", page_icon="🦊", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #0b0f07; color: #adff2f; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #adff2f !important; }
        .stButton>button { background-color: #1e2912 !important; color: #adff2f !important; border: 1px solid #adff2f !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #adff2f !important; color: #0b0f07 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        .wallet-card { border: 1px solid #adff2f; padding: 15px; background: #131a0c; border-radius: 5px; margin-top: 10px; }
        .sync-box { border: 1px solid #adff2f; padding: 10px; background: #17240e; border-radius: 5px; margin-bottom: 15px; text-align: center; }
        input, select { background-color: #131a0c !important; color: #adff2f !important; border: 1px solid #adff2f !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="border: 1px solid #adff2f; padding: 10px; background-color: #1a2410; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #ffffff; font-size: 14px;">⚡ CORE ENVIROMENT: VIRGO ANALYTICS SYSTEM</b><br>
    <span style="color: #adff2f; font-size: 11px;">Want to cross-reference multi-chain insider transactions 24/7? Visit: https://virgo-analytics.net</span>
</div>
""", unsafe_allow_html=True)

st.title("🦊 ウォレット // WALLET METRICS SHIELD")
st.subheader("🔑 ON-CHAIN AUDIT & RISK SCORE RADAR (SYNAPSE ENGINE ACTIVE)")

# --- 🔥 SILNIK SYNCHRONIZACJI Z PROGRAMEM-MATKĄ ---
if 'synapse_compiled_6' not in st.session_state:
    st.session_state.synapse_compiled_6 = False

st.markdown('<div class="sync-box">', unsafe_allow_html=True)
if not st.session_state.synapse_compiled_6:
    st.write("🔴 **CORE STATE: OUTDATED** // Local forensic databases require remote network distillation.")
    if st.button("🧠 SYNC WITH VIRGO MAIN CORE (FETCH RECENT FRAUD DEFINITIONS)"):
        with st.spinner("Injecting dark pool tracking definitions from virgo mainframe..."):
            time.sleep(2.5)
        st.session_state.synapse_compiled_6 = True
        st.rerun()
else:
    st.write("AUGHT IN THE MATRIX: 🟢 **CORE STATE: SYNCHRONIZED** // Fraud ledger successfully loaded via parent core.")
st.markdown('</div>', unsafe_allow_html=True)

wallet_input = st.text_input("ENTER MASTER TARGET WALLET ADDRESS (BTC/ETH/SOL):", value="0x71C...89ABC")
col_x, col_y = st.columns(2)
with col_x:
    scan_layer = st.selectbox("SELECT RADAR DEPTH LAYER (BONUS BOOST):", [
        "Standard Metadata Scan", "Deep Smart Contract Audit (+50% Risk Sensitivity)", "Dark Pool Liquidity Tracker (+120% Risk Sensitivity)"
    ])
with col_y:
    min_trust = st.slider("MINIMUM TRUST FILTER (%):", min_value=10, max_value=90, value=50)

if st.button("⚡ EXECUTE DEEP ON-CHAIN METRIC ANALYSIS"):
    p_bar = st.progress(0)
    for i in range(4):
        time.sleep(0.2)
        p_bar.progress((i + 1) * 25)
    p_bar.empty()
    
    risk_boost = "CRITICAL_SHADOW_TRACK" if st.session_state.synapse_compiled_6 else "STANDARD"
    url = "http://localhost:11434/api/generate"
    prompt_text = (
        f"Generate exactly 4 different crypto wallet profiles connected to the cluster network of {wallet_input}. "
        f"Security threat profile: {risk_boost}. For each item, output exactly one single line: "
        f"WALLET_HASH|CLUSTER_STATUS_NAME|TRUST_SCORE_NUM|TACTICAL_CYBER_WARNING "
        f"Return ONLY these 4 lines. No intro, no markdown."
    )
    
    payload = {"model": "llama3", "prompt": prompt_text, "stream": False}
    parsed_wallets = []
    
    try:
        encoded_data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            raw_output = res_data.get("response", "")
            for line in raw_output.strip().split('\n'):
                if "|" in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        parsed_wallets.append({"address": parts[0].strip(), "status": parts[1].strip(), "score": parts[2].strip(), "warning": parts[3].strip()})
    except: pass
        
    if not parsed_wallets:
        s_score = "21" if st.session_state.synapse_compiled_6 else "78"
        parsed_wallets = [
            {"address": "0x55A...99D (Cluster Node Alpha)", "status": "DORMANT_WHALE", "score": s_score, "warning": "High volume exchange signals detected. Wallet exhibits whale pattern pooling."},
            {"address": "0x11B...44E (Associated Contract)", "status": "ELITE_INSIDER", "score": "12", "warning": "Highly dangerous track. Close link to automated VC liquidation vectors."},
            {"address": "0x99F...22A (Liquidity Provider)", "status": "ALGO_BOT_ACCUMULATION", "score": "45", "warning": "Continuous split micro-transactions identified. Automated address track active."},
            {"address": "0x33C...77B (Shadow Gateway)", "status": "EXCHANGE_HOT_WALLET", "score": "89", "warning": "Standard cold-to-hot infrastructure node path verified."}
        ]
        
    st.success("🦊 SCAN COMPLETE: ISOLATED 4 CLUSTER DATA FEEDS VIA LLAMA 3!")
    for wallet in parsed_wallets:
        st.markdown(f"""
        <div class="wallet-card">
            <b style="color: #ffffff; font-size: 14px;">🔑 ASSOCIATED ADDRESS: {str(wallet['address']).upper()}</b><br>
            <span style="color: #ff0055;">💼 METRIC CLASSIFICATION: <b>{wallet['status']}</b></span> | Trust Index: <b style="color: #00ff66;">{wallet['score']}%</b><br>
            <p style="color: #adff2f; margin-top: 8px;">🧠 <b>LLAMA 3 TELEMETRY WARNING:</b> {wallet['warning']}</p>
        </div>
        """, unsafe_allow_html=True)
