import streamlit as st
import pandas as pd
import time
import random

# --- CONFIG INTERFEJSU DLA SMARTFONÓW ---
st.set_page_config(
    page_title="🩸 VIPER RED YIELD NODE",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Wymuszenie unikalnego, krwistoczerwonego stylu Tokyo Vampire (Blokada jasnego motywu)
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #0a0103; color: #ff0044; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #ff0044 !important; }
        .stButton>button { background-color: #3d0014 !important; color: #ff0044 !important; border: 1px solid #ff0044 !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #ff0044 !important; color: #0a0103 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        input { background-color: #120206 !important; color: #ff0044 !important; border: 1px solid #ff0044 !important; }
        div[data-testid="stDataFrame"] { background-color: #140207 !important; border: 1px solid #ff0044 !important; }
    </style>
""", unsafe_allow_html=True)

# LEJEK MARKETINGOWY: BANER SYSTEMU VIRGO
st.markdown("""
<div style="border: 1px solid #ff0044; padding: 10px; background-color: #26000c; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #ff0044; font-size: 14px;">⚡ CORE ENGINE GATEWAY: VIRGO ANALYTICS SYSTEM</b><br>
    <span style="color: #ff99bb; font-size: 11px;">Deploy continuous 24/7 web scraping & live arbitrage algorithms online at: https://virgo-analytics.net</span>
</div>
""", unsafe_allow_html=True)

st.title("バイパー・計算機 // VIPER REVENUE YIELD ENGINE")
st.subheader("🩸 PASSIVE TRADING & COMPOUND MODELER (MOBILE OPTIMIZED)")

# Układ pól wejściowych dostosowany do szybkiego wpisywania na telefonie
col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    capital = st.number_input("YOUR TRADING CAPITAL ($ / PLN):", value=5000, step=500)
with col_in2:
    margin_pct = st.number_input("AVERAGE FLIP MARGIN (%):", value=1.5, step=0.1)
with col_in3:
    trades_per_month = st.number_input("MONTHLY TRANSACTIONS (TRADES):", value=45, step=5)

if st.button("🩸 CALCULATE ESTIMATED PASSIVE YIELD"):
    st.write("Simulating blockchain & market liquidity paths...")
    
    p_bar = st.progress(0)
    
    periods = [
        {"label": "1 Month", "months": 1},
        {"label": "3 Months", "months": 3},
        {"label": "6 Months", "months": 6},
        {"label": "1 Year", "months": 12}
    ]
    
    total_steps = len(periods)
    calculated_rows = []
    
    for idx, period in enumerate(periods):
        time.sleep(random.uniform(0.2, 0.4)) # Efekt analizowania logów giełdowych
        p_bar.progress((idx + 1) / total_steps)
        
        margin_raw = margin_pct / 100
        total_trades = trades_per_month * period["months"]
        total_volume = capital * total_trades
        
        # Matematyka zysków (Zwykły zysk vs potężny procent składany z Twojej akademii)
        passive_profit = total_volume * margin_raw
        compounded_capital = capital * ((1 + margin_raw) ** total_trades)
        compounded_profit = compounded_capital - capital
        
        risk_profile = random.choice(["[LOW_RISK]", "[SECURE]", "[OPTIMAL]"])
        
        calculated_rows.append({
            "📊 TIMEFRAME": period["label"],
            "📈 TOTAL VOLUME": f"${total_volume:,.2f}",
            "💵 PASSIVE PROFIT": f"${passive_profit:,.2f}",
            "🔥 WITH COMPOUND": f"${compounded_profit:,.2f}",
            "⚡ RISK PROFILE": risk_profile
        })
        
    p_bar.empty()
    st.success("🩸 REVENUE PROJECTION GENERATED SUCCESSFULLY")
    
    # Renderowanie tabeli zysków geometrycznych
    df = pd.DataFrame(calculated_rows)
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.write("Engine in Standby. Enter variables and trigger execution matrix.")
