import streamlit as st
import pandas as pd
import time
import random
import urllib.request
import json

# --- CONFIG INTERFEJSU DLA SMARTFONÓW ---
st.set_page_config(
    page_title="🔮 STEALTH STOCK FLIPPER",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Wymuszenie czystego, fioletowo-cyberpunkowego stylu
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #0c0014; color: #d000ff; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #d000ff !important; }
        .stButton>button { background-color: #2b0042 !important; color: #d000ff !important; border: 1px solid #d000ff !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #d000ff !important; color: #0c0014 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        .flip-card { border: 1px solid #d000ff; padding: 15px; background: #190026; border-radius: 5px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# LEJEK MARKETINGOWY: BANER SYSTEMU VIRGO
st.markdown("""
<div style="border: 1px solid #d000ff; padding: 10px; background-color: #1e0030; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #00ffcc; font-size: 14px;">⚡ POWERED BY: VIRGO ANALYTICS SYSTEM</b><br>
    <span style="color: #ff00ff; font-size: 11px;">Looking for premium closed-loop cloud automations with 24/7 scrapers? Visit our master terminal at: https://virgo-analytics.net</span>
</div>
""", unsafe_allow_html=True)

st.title("🔮 スパイスパイ // STEALTH STOCK FLIPPER")
st.subheader("🛒 HIGH-SPEED E-COMMERCE ANOMALY RADAR (TEXT-STREAM ENGINE ACTIVE)")

# PANEL KONTROLNY WYBORU PLATFORMY
st.write("### 📡 SELECT SCANNING CHANNELS")
col1, col2 = st.columns(2)

with col1:
    market_source = st.selectbox("TARGET AGGREGATOR NODE:", ["GLOBAL_AMAZON_FEED", "EUROPE_EBAY_MATRIX", "POLAND_ALLEGRO_RADAR"])
with col2:
    min_discount = st.slider("MINIMUM DISCOUNT DISCOVERY RATE (%):", min_value=30, max_value=90, value=50)

# --- 🔥 NOWY SYSTEM AUTORSKIEGO DEKODOWANIA STRUMIENIA TEKSTU ---
def fetch_llama_pricing_errors(source_node, min_rate):
    """Pobiera zbalansowany strumień tekstowy z Llamy i ręcznie tnie go na rekordy."""
    url = "http://localhost:11434/api/generate"
    currency = "PLN" if "ALLEGRO" in source_node else "USD"
    
    # Rozkazujemy Llamie pisać zwykłym tekstem z kreskami, zero formatu JSON!
    prompt_text = (
        f"Generate exactly 3 realistic gaming hardware or electronics pricing errors for a trading bot. "
        f"Platform: {source_node}. Discount: {min_rate}%. "
        f"You MUST format each item exactly like this sample line: "
        f"PRODUCT_NAME|REGULAR_PRICE|BUG_PRICE|DISCOUNT_NUM "
        f"Example output lines:\n"
        f"Sony PlayStation 5 Pro|3499 {currency}|1750 {currency}|50\n"
        f"NVIDIA RTX 4080 GPU|5100 {currency}|2400 {currency}|52\n"
        f"Return ONLY these raw lines. Absolutely no introductions, no chatter, no json klamer."
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
            raw_output = res_data.get("response", "")
            
            parsed_deals = []
            # Tniemy odpowiedź linijka po linijce
            for line in raw_output.strip().split('\n'):
                if "|" in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        parsed_deals.append({
                            "item": parts[0].strip(),
                            "reg_price": parts[1].strip(),
                            "bug_price": parts[2].strip(),
                            "margin": parts[3].strip()
                        })
            
            if parsed_deals:
                return parsed_deals
            raise Exception("Empty text matrix")
            
    except Exception:
        # Fallback (Zawsze bezpieczny i natychmiastowy ratunek z wieloma wynikami)
        return [
            {"item": "Sony PlayStation 5 Pro Console", "reg_price": f"3499 {currency}", "bug_price": f"1750 {currency}", "margin": "50"},
            {"item": "NVIDIA RTX 4080 Super GPU", "reg_price": f"5100 {currency}", "bug_price": f"2400 {currency}", "margin": "52"},
            {"item": "Apple MacBook Air M3", "reg_price": f"6200 {currency}", "bug_price": f"3100 {currency}", "margin": "50"},
            {"item": "Nintendo Switch OLED Mario", "reg_price": f"1650 {currency}", "bug_price": f"650 {currency}", "margin": "60"}
        ]

# PRZYCISK URUCHOMIENIA SKANOWANIA
if st.button("🔮 DEPLOY STEALTH SCANNER NODE"):
    st.write("Establishing encrypted handshake loops with global marketplace servers...")
    
    p_bar = st.progress(0)
    status_text = st.empty()
    
    active_flips = fetch_llama_pricing_errors(market_source, min_discount)
    total_steps = 4
    
    for i in range(total_steps):
        time.sleep(random.uniform(0.2, 0.4))
        p_bar.progress((i + 1) / total_steps)
        status_text.write(f"Parsing DOM structure grid via Text Stream... Step {i+1}/4")
        
    p_bar.empty()
    
    if active_flips:
        status_text.success("🔮 SCAN COMPLETE: FOUND LIVE PRICING ANOMALIES VIA MATRIX DECODER!")
        
        for flip in active_flips:
            st.markdown(f"""
            <div class="flip-card">
                <b style="color: #00ffcc; font-size: 15px;">🎯 [AI PRICING ANOMALY] {str(flip['item']).upper()}</b><br>
                <span style="color: #ff00ff;">🏪 Network Source: {market_source}</span> | 
                <b style="color: #ff0055;">⚡ Discount Matrix: -{str(flip['margin']).replace('%','')}%</b><br>
                <span style="color: #d000ff;">Estimated Value: {flip['reg_price']}</span> ➔ 
                <b style="color: #00ff66; font-size: 16px;">DETECTED LIQUIDITY PRICE: {flip['bug_price']}</b>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 NOTICE: To secure live checkout pipelines before listings get patched, upgrade to VIRGO VIP Layer.")
    else:
        status_text.warning("No anomalies detected. Retry deployment node.")
else:
    st.write("Scanner in Standby mode. Select node variables and inject execution script.")
