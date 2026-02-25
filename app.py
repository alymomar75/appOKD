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

# Initialisation du panier dans la session
if 'panier' not in st.session_state:
    st.session_state['panier'] = []

# --- CSS AVANCÉ ---
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

    /* NAVBAR AVEC PANIER CLIQUABLE */
    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 80px;
        background: rgba(255, 255, 255, 0.1);
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
        width: 60px; height: 60px;
        border-radius: 50%; border: 2px solid white;
        background: white; object-fit: cover;
    }}

    .content-spacer {{ padding-top: 110px; }}

    /* BOUTON PANIER DANS LA NAV */
    .cart-btn {{
        background: none;
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    /* PRODUITS */
    .product-box {{
        background: rgba(255, 255, 255, 0.85); 
        padding: 15px; border-radius: 18px; text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# --- BARRE DE NAVIGATION ---
# Note: On utilise des colonnes Streamlit pour simuler la navbar car les boutons HTML bruts ne peuvent pas déclencher de fonctions Python facilement
with st.container():
    cols_nav = st.columns([1, 10, 2])
    with cols_nav[0]:
        st.markdown(f'<img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">', unsafe_allow_html=True)
    with cols_nav[2]:
        if st.button(f"🛒 ({len(st.session_state['panier'])})"):
            st.session_state['voir_panier'] = True
            st.toast("Direction votre panier...")

st.markdown('<div class="content-spacer"></div>', unsafe_allow_html=True)

# --- TITRE ---
st.markdown("""
    <div style="text-align: center; color: white;">
        <h1 style="font-size: 2.8rem; margin:0; color: #2d5a27;">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="letter-spacing: 5px; opacity: 0.9;">BY KALINA</p>
    </div>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### Nos Valentine Packages")
col1, col2 = st.columns(2)
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "img": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9"}
]

for i, p in enumerate(packs):
    with (col1 if i == 0 else col2):
        st.markdown(f"""
            <div class="product-box">
                <img src="{p['img']}" style="width:100%; border-radius:12px; height:200px; object-fit:cover;">
                <h4 style="color: #111; margin:10px 0 5px 0;">{p['nom']}</h4>
                <p style="color: #d14d5d; font-weight: bold;">{p['prix']}</p>
            </div>
        """, unsafe_allow_html=True)
        # Bouton Ajouter au panier
        if st.button(f"Ajouter au panier", key=f"add_{i}"):
            st.session_state['panier'].append(p)
            st.toast(f"{p['nom']} ajouté !")
            st.rerun()

# --- SECTION PANIER (S'affiche si on clique sur l'icône) ---
if st.session_state.get('voir_panier', False):
    st.markdown("---")
    st.subheader("🛒 Votre Panier")
    if len(st.session_state['panier']) > 0:
        for item in st.session_state['panier']:
            st.write(f"✅ {item['nom']} - {item['prix']}")
        if st.button("Vider le panier"):
            st.session_state['panier'] = []
            st.rerun()
    else:
        st.info("Votre panier est vide pour le moment.")

# --- FIDÉLITÉ ---
st.divider()
st.subheader("Carte VIP")
c_in, c_vis = st.columns(2)
with c_in:
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
with c_vis:
    user_name = f"{prenom} {nom}".strip().upper()
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #111, #333); border: 1px solid #d4af37; border-radius: 12px; padding: 20px; color: #d4af37;">
            <div style="font-size: 0.6rem;">VIP MEMBER</div>
            <div style="font-size: 1.2rem; margin: 10px 0;">{user_name if user_name else "CLIENT"}</div>
        </div>
    """, unsafe_allow_html=True)

# --- VALIDATION ---
if st.button("🚀 CONFIRMER MA COMMANDE", type="primary"):
    if nom and prenom and st.session_state['panier']:
        articles = ", ".join([x['nom'] for x in st.session_state['panier']])
        wa_msg = f"Bonjour Kalina ! Je commande : {articles}. Je suis {prenom} {nom}."
        st.success("Prêt pour l'envoi !")
        st.markdown(f'<a href="https://wa.me/221774474769?text={wa_msg}" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">FINALISER SUR WHATSAPP 📲</div></a>', unsafe_allow_html=True)
    elif not st.session_state['panier']:
        st.error("Votre panier est vide !")
    else:
        st.warning("Complétez votre nom pour la carte VIP.")

# --- FOOTER INSTAGRAM ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; padding: 30px; background: rgba(0,0,0,0.1);">
        <a href="https://www.instagram.com/the_floral_corner/" target="_blank" style="text-decoration:none; color:white;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" width="30" style="margin-bottom:10px;"><br>
            @the_floral_corner
        </a>
    </div>
""", unsafe_allow_html=True)
