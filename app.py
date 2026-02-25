import streamlit as st
import base64
import os

# 1. CONFIGURATION
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

img_logo = get_base64_image("logo.jpg")

if 'panier' not in st.session_state:
    st.session_state['panier'] = []

# --- CSS RÉPARÉ POUR MOBILE & DESIGN PRO ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    [data-testid="stHeader"] {{ visibility: hidden; }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 2rem; max-width: 100%; }}

    /* FOND LIQUIDE */
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

    /* NAVBAR FIXÉE (LOGO GAUCHE / PANIER DROITE) */
    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 75px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
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

    /* DESIGN DU PIED DE PAGE INSTAGRAM (PRO) */
    .insta-footer {{
        margin: 50px auto;
        padding: 20px;
        max-width: 300px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        backdrop-filter: blur(10px);
    }}

    .insta-badge {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        text-decoration: none;
        color: white !important;
        font-weight: 600;
        font-size: 14px;
        letter-spacing: 0.5px;
    }}

    /* BOUTONS STREAMLIT HARMONISÉS */
    div.stButton > button {{
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div style="color: white; font-weight: bold; font-size: 1.2rem;">
            🛒 <span style="background: #ff69b4; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem;">{len(st.session_state['panier'])}</span>
        </div>
    </div>
    
    <div class="content-spacer"></div>

    <div style="text-align: center; color: white;">
        <h1 style="font-size: 2.2rem; margin:0; color: #2d5a27;">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="letter-spacing: 5px; opacity: 0.8; font-size: 0.7rem;">BY KALINA</p>
    </div>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### 🌸 Nos Valentine Packages")
col1, col2 = st.columns(2)
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "img": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9"}
]

for i, p in enumerate(packs):
    with (col1 if i == 0 else col2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.85); padding:12px; border-radius:18px; margin-bottom:10px; text-align:center;">
                <img src="{p['img']}" style="width:100%; border-radius:12px; height:180px; object-fit:cover;">
                <h5 style="color: #111; margin:10px 0 2px 0; font-size:0.9rem;">{p['nom']}</h5>
                <p style="color: #d14d5d; font-weight: bold; font-size:0.8rem;">{p['prix']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter au panier", key=f"add_{i}", use_container_width=True):
            st.session_state['panier'].append(p)
            st.rerun()

# --- RÉCAPITULATIF PANIER ---
if len(st.session_state['panier']) > 0:
    with st.expander("🧐 Voir le détail de mon panier"):
        for item in st.session_state['panier']:
            st.write(f"• {item['nom']} ({item['prix']})")
        if st.button("Vider mon panier", type="secondary"):
            st.session_state['panier'] = []
            st.rerun()

# --- CARTE VIP ---
st.divider()
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
user_name = f"{prenom} {nom}".strip().upper()
st.markdown(f"""
    <div style="background: linear-gradient(135deg, #111, #333); border: 1px solid #d4af37; border-radius: 15px; padding: 20px; color: #d4af37; box-shadow: 0 10px 20px rgba(0,0,0,0.3);">
        <div style="font-size: 0.6rem; letter-spacing: 2px;">THE FLORAL CORNER VIP</div>
        <div style="font-size: 1.1rem; margin: 15px 0; font-weight: bold;">{user_name if user_name else "VOTRE NOM"}</div>
        <div style="text-align: right; font-size: 0.5rem; opacity: 0.6;">SÉNÉGAL 2026</div>
    </div>
""", unsafe_allow_html=True)

# --- BOUTON DE VALIDATION ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("☑ CONFIRMER MA COMMANDE", type="primary", use_container_width=True):
    if nom and prenom and st.session_state['panier']:
        items_list = ", ".join([x['nom'] for x in st.session_state['panier']])
        wa_msg = f"Bonjour Kalina ! Je souhaite valider ma commande pour : {items_list}. Je suis {prenom} {nom}."
        st.markdown(f'''<a href="https://wa.me/221774474769?text={wa_msg}" target="_blank" style="text-decoration:none;">
            <div style="background:#25d366; color:white; padding:18px; border-radius:12px; text-align:center; font-weight:bold; box-shadow: 0 4px 15px rgba(37,211,102,0.4);">
                ENVOYER SUR WHATSAPP 📲
            </div></a>''', unsafe_allow_html=True)
    else:
        st.warning("Vérifiez votre nom et votre panier.")

# --- FOOTER INSTAGRAM PROFESSIONNEL ---
st.markdown(f"""
    <div class="insta-footer">
        <a href="https://www.instagram.com/the_floral_corner/" class="insta-badge" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" width="28">
            <span>the_floral_corner</span>
        </a>
    </div>
    <div style="text-align: center; opacity: 0.5; font-size: 0.6rem; color: white; padding-bottom: 20px;">
        © 2026 THE FLORAL CORNER • DAKAR, SÉNÉGAL
    </div>
""", unsafe_allow_html=True)
