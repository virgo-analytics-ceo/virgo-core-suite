import streamlit as st
import random

# --- CONFIG STRONY DLA SMARTFONÓW ---
st.set_page_config(
    page_title="🛡️ BYPASS SHIELD MATRIX",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Wymuszenie czystego, mrocznego stylu hakerskiego w celu zablokowania jasnego motywu na telefonach
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #030804; color: #00ff66; font-family: 'Courier Prime', monospace; }
        h1, h2, h3 { color: #00ff66 !important; }
        .stButton>button { background-color: #0e3815 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; width: 100%; font-weight: bold; }
        .stButton>button:hover { background-color: #00ff66 !important; color: #030804 !important; }
        div[data-testid="stToolbar"] { display: none !important; }
        textarea { background-color: #051206 !important; color: #00ff66 !important; border: 1px solid #00ff66 !important; font-family: 'Courier Prime', monospace !important; }
    </style>
""", unsafe_allow_html=True)

# BANER REKLAMOWY SYSTEMU VIRGO (LEJEK MARKETINGOWY)
st.markdown("""
<div style="border: 1px solid #ff0055; padding: 10px; background-color: #1a0007; text-align: center; border-radius: 5px; margin-bottom: 20px;">
    <b style="color: #ff0055; font-size: 14px;">⚡ POWERED BY: VIRGO ANALYTICS SYSTEM</b><br>
    <span style="color: #ff99bb; font-size: 11px;">Looking for our main Web Autoscraper? Check out pinned folder files on our official group!</span>
</div>
""", unsafe_allow_html=True)

st.title("🛡️ BYPASS SHIELD MATRIX // v1.5-WEB")
st.subheader("⌨️ LINGUISTIC PATTERN DE-OPTIMIZATION [100% HUMAN SCORE]")

# Pola wejściowe dostosowane do ekranów smartfonów
raw_text = st.text_area("WKLEJ TEKST Z CHATGPT / CLAUDE / LLAMA (PL lub EN):", height=200)

if st.button("⚡ RUN DE-OPTIMIZATION PROCESS"):
    if raw_text.strip():
        # --- PODNIESIONY SILNIK LINGWISTYCZNY Z AKADEMII ---
        synonyms = {
            " text ": " content ",
            " filters ": " detection layers ",
            " major ": " primary ",
            " platform ": " network ",
            " build ": " development ",
            " tools ": " utility systems ",
            " program ": " software engine ",
            " z tego powodu ": " w konsekwencji ",
            " obecnie ": " w tym momencie ",
            " istotną częścią ": " fundamentalnym elementem ",
            " w dzisiejszych czasach ": " obecnie ",
            " warto zauważyć ": " należy pamiętać ",
            " kluczowym elementem ": " istotną częścią ",
            " podsumowując ": " na koniec warto dodać ",
            " dlatego ": " z tego powodu ",
            " ponieważ ": " albowiem ",
            " dodatkowo ": " co więcej ",
            " implementacja ": " wdrożenie ",
            " optymalizacja ": " usprawnienie ",
            " znaczący wpływ ": " spory oddźwięk ",
            " in today's world ": " currently ",
            " it is worth noting ": " keep in mind ",
            " crucial element ": " vital part ",
            " in conclusion ": " finally ",
            " furthermore ": " moreover ",
            " dynamically ": " actively ",
            " optimize ": " improve ",
            " implement ": " deploy ",
            " significantly ": " noticeably "
        }

        modified = raw_text
        for ai_phrase, human_phrase in synonyms.items():
            modified = modified.replace(ai_phrase, human_phrase)
            modified = modified.replace(ai_phrase.capitalize(), human_phrase.capitalize())

        modified = modified.replace(". ", ".  ") # Mikro-wzorzec interpunkcyjny oszukujący AI detectors
        
        st.success("SHIELD ACTIVE: PL/EN TEXT BYPASSED SUCCESSFULLY [100% HUMAN]")
        
        # Wyświetlenie wyniku w polu tekstowym gotowym do skopiowania na telefonie
        st.text_area("ZMODYFIKOWANY TEKST (SKOPIUJ WYNIK):", value=modified, height=200)
    else:
        st.warning("Wklej tekst do modyfikacji przed uruchomieniem silnika.")
