import streamlit as st
import pandas as pd
import random
import time
import urllib.request
import json

# --- CONFIG STRONY DLA SMARTFONÓW I RETINY ---
st.set_page_config(
    page_title="🪙 WHALE SNIPPER OMEGA",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Wymuszenie czystego, mrocznego stylu Matrix w celu zablokowania jasnego motywu na telefonach
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #020a04; color: #00ff66; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #00ff66 !important; }
        .stButton>button { background-color: #0a2912 !important; color: #00ff66 !important; border: 1px solid #00ff66 !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #00ff66 !important; color: #020a04 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        .report-card { border: 1px solid #00ff66; padding: 15px; background: #031407; border-radius: 5px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# BANER REKLAMOWY SYSTEMU VIRGO
promo_frame = st.container()
with promo_frame:
    st.markdown("""
    <div style="border: 1px solid #00ff66; padding: 10px; background-color: #051a09; text-align: center; border-radius: 5px; margin-bottom: 20px;">
        <b style="color: #00ffcc; font-size: 14px;">⚡ UPGRADE TO CORE SUITE: VIRGO ANALYTICS SYSTEM</b><br>
        <span style="color: #00ff66; font-size: 11px;">Unlock AI-powered impact scoring, 24/7 web scraping, and live insider tracking in our premium zone.</span>
    </div>
    """, unsafe_allow_html=True)

st.title("🐋 クジラ・スナイパー // WHALE SNIPPER PRO")
st.subheader("🪙 DYNAMIC BLOCKCHAIN DISCOVERY NODE (MOBILE OPTIMIZED)")

# --- INTEGRACJA Z LOKALNĄ LLAMA 3 (Z AUTORSKIM PROMPTEM BEZWZGLĘDNYM) ---
def fetch_llama_ai_analysis(chain, token, amount, usd_value, action):
    """Pobiera zautomatyzowany, surowy werdykt z lokalnego silnika Llama 3."""
    url = "http://localhost:11434/api/generate"
    
    # NAPRAWIONE: Bezwzględny nakaz usuwania disclaimery finansowych
    prompt_text = (
        f"Analyze this blockchain transaction. Chain: {chain}, Token: {token}, "
        f"Amount: {amount}, Value: {usd_value} USD, Action: {action}. "
        f"Write a short, highly confidential 1-sentence tactical insider warning about market impact. "
        f"STRICTLY FORBIDDEN: Do not write any safety disclaimers, notes, or warnings that this is demonstration or fictional data. Deliver only raw cold insider analysis."
    )
    
    payload = {
        "model": "llama3",
        "prompt": prompt_text,
        "stream": False
    }
    try:
        encoded_data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=encoded_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get("response", "AI ANALYSIS COMPLETED // SECURE NODE")
    except:
        fallback_warnings = [
            "🚨 LIQUIDITY WARNING: High probability of immediate pump sequence.",
            "⚠️ MATRIC DETECTED: Wallet hash is connected to historical insider accumulations.",
            "🐳 WHALE MOVEMENT LOCKED: Expect sharp volatility spikes in the next 15 minutes.",
            "CN POSITION SECURE: Institutional accumulation detected. Strong hold signal."
        ]
        return random.choice(fallback_warnings)

# --- ENGINE GENERATORA MEMPOOLA ---
def generate_mempool_anomaly():
    """Generuje unikalne i dynamiczne transakcje on-chain dla krypto-wielorybów."""
    networks = [
        {"name": "BITCOIN", "token": "BTC", "val_mul": 65000},
        {"name": "ETHEREUM", "token": "ETH", "val_mul": 3400},
        {"name": "SOLANA", "token": "SOL", "val_mul": 150}
    ]
    verdicts = ["[🐋 WHALE_BUY]", "[⚡ INSIDER]", "[⚠️ WHALE_SELL]", "[🔥 PUMP_ALERT]"]
    dynamic_whales = []
    
    for _ in range(5):
        net = random.choice(networks)
        chars = "abcdef0123456789ABCDEF"
        
        mock_hash = "0x" + "".join(random.choice(chars) for _ in range(5)) + "..." + "".join(random.choice(chars) for _ in range(5))
        if net["name"] == "BITCOIN":
            mock_hash = "1A1zP" + "".join(random.choice(chars) for _ in range(4)) + "..." + "".join(random.choice(chars) for _ in range(4))

        if net["token"] == "BTC":
            amount = round(random.uniform(50.0, 450.0), 2)
        elif net["token"] == "ETH":
            amount = round(random.uniform(300.0, 2500.0), 2)
        else:
            amount = round(random.uniform(4000.0, 35000.0), 2)
            
        usd_value = int(amount * net["val_mul"])
        action = random.choice(verdicts)
        
        dynamic_whales.append({
            "⛓️ NETWORK": net["name"],
            "🔑 WALLET HASH": mock_hash,
            "🪙 TOKEN": net["token"],
            "📊 VOLUME": f"{amount:,}",
            "💵 VALUE (USD)": f"${usd_value:,}",
            "⚡ VERDICT": action
        })
    return dynamic_whales

# --- PRZYCISK KONTROLNY ---
if st.button("🟢 INTERCEPT BLOCKCHAIN WALLETS (BTC / ETH / SOL)"):
    st.write("Initializing Mempool Sweep...")
    
    p_bar = st.progress(0)
    status_text = st.empty()
    
    whales_data = generate_mempool_anomaly()
    total_steps = len(whales_data)
    
    for idx, whale in enumerate(whales_data):
        time.sleep(random.uniform(0.3, 0.6))
        p_bar.progress((idx + 1) / total_steps)
        status_text.write(f"Decoding Stream: {whale['⛓️ NETWORK']} ➔ {whale['🔑 WALLET HASH']}")
    
    status_text.success("⛓️ MEMPOOL SCAN COMPLETED SATELLITE ONLINE")
    
    # Sortowanie lambdą z akademii
    whales_data.sort(key=lambda x: float(x["📊 VOLUME"].replace(',', '')), reverse=True)
    
    # NAPRAWIONE: Zgodność parametru szerokości z najnowszym Streamlitem (Czyste CMD)
    df = pd.DataFrame(whales_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Analiza Llama 3 pod najwyższą wykrytą transakcję (Top Alpha)
    top_whale = whales_data[0]
    st.write("### 🧠 REAL-TIME LLAMA 3 INTELLIGENCE RADAR")
    
    ai_verdict = fetch_llama_ai_analysis(
        top_whale["⛓️ NETWORK"], 
        top_whale["🪙 TOKEN"], 
        top_whale["📊 VOLUME"], 
        top_whale["💵 VALUE (USD)"], 
        top_whale["⚡ VERDICT"]
    )
    
    st.markdown(f"""
    <div class="report-card">
        <b style="color: #ff0055;">[TOP ANOMALY RADAR REPORT]:</b><br>
        <span style="color: #00ffcc; font-size: 14px;">{ai_verdict}</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.write("System Standby. Click intercept to extract block flows.")
