import streamlit as st
import base64
import os
import urllib.parse

# 1. CONFIGURATION
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except Exception:
        pass
    return ""

# Récupération des images locales (Assurez-vous que les fichiers existent)
img_logo = get_base64_image("logo.jpg")
img_sweet = get_base64_image("bouquet.jpeg")
img_love = get_base64_image("fleur.jpeg")
img_wave_local = get_base64_image("wavelogo.png")
img_cash_local = get_base64_image("cash.png")

# Initialisation du panier
if 'panier' not in st.session_state:
    st.session_state['panier'] = []

# --- CSS & HEADER ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    [data-testid="stHeader"] {{ visibility: hidden; }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 2rem; max-width: 100%; }}

    .stApp {{
        background: linear-gradient(-45deg, #7d0a0a, #d14d5d, #2d5a27, #fce4ec);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 75px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 55px; height: 55px;
        border-radius: 50%; border: 2px solid white;
        background: white; object-fit: cover;
    }}

    .content-spacer {{ padding-top: 100px; }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div style="color: white; font-weight: bold; font-size: 1.1rem;">
            🛒 <span style="background: #ff69b4; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem;">{len(st.session_state['panier'])}</span>
        </div>
    </div>
    
    <div class="content-spacer"></div>

    <div style="text-align: center; color: white; margin-bottom: 30px;">
        <h1 style="font-size: 2.2rem; margin:0; color: #ffffff; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="letter-spacing: 5px; opacity: 0.9; font-size: 0.7rem; color: white;">
            Digitalisation des Menus & Services
        </p>
    </div>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### 🌸 Nos Valentine Packages")
col1, col2 = st.columns(2)

packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "val": 20000, "img": f"data:image/jpeg;base64,{img_sweet}"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "val": 30000, "img": f"data:image/jpeg;base64,{img_love}"}
]

for i, p in enumerate(packs):
    with (col1 if i == 0 else col2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.85); padding:10px; border-radius:18px; margin-bottom:10px; text-align:center;">
                <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; border-radius: 12px; background: white; display: flex; align-items: center; justify-content: center;">
                    <img src="{p['img']}" style="width:100%; height:100%; object-fit: cover;">
                </div>
                <h5 style="color: #111; margin:10px 0 2px 0; font-size:0.85rem; font-weight: bold;">{p['nom']}</h5>
                <p style="color: #d14d5d; font-weight: bold; font-size:0.8rem;">{p['prix']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter au panier", key=f"add_{i}", use_container_width=True):
            st.session_state['panier'].append(p)
            st.rerun()

# --- PANIER ---
if len(st.session_state['panier']) > 0:
    with st.expander("🧐 Détails de votre panier"):
        total = 0
        for idx, item in enumerate(st.session_state['panier']):
            st.write(f"• {item['nom']} - {item['prix']}")
            total += item['val']
        st.write(f"**TOTAL : {total:,} F CFA**")
        if st.button("Vider mon panier", use_container_width=True):
            st.session_state['panier'] = []
            st.rerun()

# --- CARTE VIP ---
st.divider()
col_n, col_p = st.columns(2)
with col_n:
    nom = st.text_input("Nom de famille").strip()
with col_p:
    prenom = st.text_input("Prénom").strip()

user_name = f"{prenom} {nom}".strip().upper()

st.markdown(f"""
    <div style="background: linear-gradient(135deg, #111, #333); border: 1px solid #d4af37; border-radius: 15px; padding: 20px; color: #d4af37; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
        <div style="font-size: 0.6rem; letter-spacing: 2px;">THE FLORAL CORNER VIP</div>
        <div style="font-size: 1.1rem; margin: 15px 0; font-weight: bold; min-height: 1.5rem;">{user_name if user_name else "VOTRE NOM"}</div>
    </div>
""", unsafe_allow_html=True)

# --- PAIEMENT ---
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("💳 Mode de paiement")

option_paiement = st.radio(
    "Sélectionnez votre option de règlement :",
    ("Wave - Mobile Money", "Orange Money", "MasterCard", "Espèces"),
    horizontal=True
)

# Logos mapping
logos = {
    "Wave - Mobile Money": f"data:image/png;base64,{img_wave_local}",
    "Orange Money": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Orange_logo.svg",
    "MasterCard": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg",
    "Espèces": f"data:image/png;base64,{img_cash_local}"
}

st.markdown(f"""
    <div style="text-align: center; margin: 15px 0;">
        <div style="display: inline-block; background: white; padding: 12px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <img src="{logos.get(option_paiement, '')}" height="45" style="object-fit: contain;">
        </div>
    </div>
""", unsafe_allow_html=True)

# --- VALIDATION ---
if st.button("🚀 CONFIRMER MA COMMANDE", type="primary", use_container_width=True):
    if not nom or not prenom:
        st.error("⚠️ Veuillez entrer votre nom et prénom.")
    elif not st.session_state['panier']:
        st.error("⚠️ Votre panier est vide.")
    else:
        articles = ", ".join([x['nom'] for x in st.session_state['panier']])
        # Encodage du message pour URL
        wa_msg = urllib.parse.quote(f"Bonjour Kalina ! Je commande : {articles}. Paiement via {option_paiement}. Client : {prenom} {nom}.")
        
        st.success("Commande prête ! Cliquez sur le bouton ci-dessous pour finaliser sur WhatsApp.")
        st.markdown(f"""
            <a href="https://wa.me/221774474769?text={wa_msg}" target="_blank" style="text-decoration:none;">
                <div style="background:#25d366; color:white; padding:18px; border-radius:12px; text-align:center; font-weight:bold; font-size:1.2rem; cursor:pointer;">
                    PAYER AVEC {option_paiement.upper()} SUR WHATSAPP 📲
                </div>
            </a>
        """, unsafe_allow_html=True)
