import streamlit as st
import base64
import os

# 1. CONFIGURATION (BARRE LATÉRALE CACHÉE)
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Récupération du logo
img_logo = get_base64_image("logo.jpg")

# --- CSS RÉPARÉ : NAVBAR TRANSPARENTE & STYLE PRO ---
st.markdown(f"""
    <style>
    /* Masquer les éléments Streamlit inutiles */
    [data-testid="stSidebar"] {{ display: none; }}
    [data-testid="stHeader"] {{ visibility: hidden; }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 5rem; max-width: 100%; }}

    /* FOND LIQUIDE ROUGE GLACÉ (CONSERVÉ) */
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

    /* NAVBAR RÉTABLIE (Translucide) */
    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 90px;
        background: rgba(255, 255, 255, 0.1); /* Effet translucide */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 40px;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }}

    .logo-circle {{
        width: 70px; height: 70px;
        border-radius: 50%; border: 2px solid white;
        background: white; object-fit: cover;
    }}

    .cart-icon {{ font-size: 24px; color: white; cursor: pointer; }}

    .content-spacer {{ padding-top: 130px; }}

    /* TYPOGRAPHIE ET TITRES */
    .brand-title {{
        text-align: center; color: #2d5a27; font-weight: 900; line-height: 1;
    }}
    .floral-text {{ color: #ff69b4; font-family: 'serif'; font-style: italic; }}

    /* BOUTONS PRODUITS PRO */
    .stButton>button {{
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    
    /* BOUTON DE VALIDATION FLASHY MAIS PRO (Sans fusée) */
    div.stButton > button:first-child[kind="primary"] {{
        background: linear-gradient(90deg, #d14d5d, #7d0a0a);
        color: white;
        border: none;
        padding: 1.5rem;
        font-size: 1.2rem;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    /* BOUTON WHATSAPP ÉPURÉ */
    .wa-link {{
        position: fixed;
        bottom: 25px; right: 25px;
        background: #25d366; color: white !important;
        padding: 12px 20px; border-radius: 30px;
        text-decoration: none; font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        z-index: 1000;
        display: flex; align-items: center; gap: 8px;
    }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div class="cart-icon">🛒</div>
    </div>
    
    <div class="content-spacer"></div>

    <div class="brand-title">
        <h1 style="font-size: 3rem; margin:0;">THE <span class="floral-text">Floral</span> CORNER</h1>
        <p style="letter-spacing: 4px; color: white; font-size: 0.9rem;">BY KALINA</p>
    </div>
    """, unsafe_allow_html=True)

# --- BOUTON WHATSAPP DISCRET ---
st.markdown(f"""
    <a href="https://wa.me/221774474769?text=Bonjour Kalina, je suis sur votre site et j'aimerais avoir des informations sur vos bouquets." class="wa-link" target="_blank">
        Envoyer un message 📩
    </a>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### Nos Collections de Saison")

col1, col2 = st.columns(2)
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "img": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9"}
]

for i, p in enumerate(packs):
    with (col1 if i == 0 else col2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.85); padding:12px; border-radius:18px; margin-bottom:10px;">
                <img src="{p['img']}" style="width:100%; border-radius:15px; height:220px; object-fit:cover;">
                <h4 style="color: #1a1a1a; margin-top:10px; margin-bottom:0;">{p['nom']}</h4>
                <p style="color: #d14d5d; font-weight: bold;">{p['prix']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter au panier", key=f"btn_{i}"):
            st.session_state['cart'] = p['nom']
            st.toast(f"{p['nom']} sélectionné")

# --- CARTE DE FIDÉLITÉ ---
st.write("---")
st.subheader("Votre Carte Membre")
c_user, c_card = st.columns([1, 1])

with c_user:
    u_nom = st.text_input("Nom de famille")
    u_prenom = st.text_input("Prénom")

with c_card:
    full_name = f"{u_prenom} {u_nom}".strip().upper()
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #222, #444); border: 1px solid #d4af37; border-radius: 15px; padding: 25px; color: #d4af37; font-family: monospace; box-shadow: 0 10px 20px rgba(0,0,0,0.4);">
            <div style="font-size: 0.7rem; opacity: 0.8;">MEMBRE VIP</div>
            <div style="font-size: 1.4rem; margin: 15px 0; letter-spacing: 2px;">{full_name if full_name else "VOTRE NOM"}</div>
            <div style="text-align: right; font-size: 0.6rem;">THE FLORAL CORNER 🌸</div>
        </div>
    """, unsafe_allow_html=True)

# --- BOUTON DE VALIDATION FINAL ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("CONFIRMER MA COMMANDE", type="primary"):
    if u_nom and u_prenom:
        pack_final = st.session_state.get('cart', 'Bouquet Signature')
        msg = f"Bonjour Kalina ! Je souhaite commander le {pack_final}. Je m'appelle {u_prenom} {u_nom}."
        st.success("Commande enregistrée !")
        st.markdown(f"""<a href="https://wa.me/221774474769?text={msg}" target="_blank">
            <button style="width:100%; padding:15px; background:#25d366; color:white; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">
            FINALISER SUR WHATSAPP
            </button></a>""", unsafe_allow_html=True)
    else:
        st.warning("Veuillez renseigner votre nom pour la carte VIP.")
