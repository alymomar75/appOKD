import streamlit as st
import base64
import os

# 1. CONFIGURATION DE LA PAGE (DOIT ÊTRE EN PREMIER)
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed" # Cache la barre latérale par défaut
)

# --- FONCTIONS UTILES ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_logo = get_base64_image("logo.jpg")

# --- CSS AVANCÉ (MODE SOMBRE/CLAIR & FULL WIDTH) ---
st.markdown(f"""
    <style>
    /* Supprimer les marges par défaut de Streamlit et la barre latérale */
    [data-testid="stSidebar"] {{ display: none; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 0rem; max-width: 100%; }}

    /* Fond Adaptatif (Dégradé liquide rouge glacé) */
    .stApp {{
        background: linear-gradient(135deg, #7d0a0a 0%, #d14d5d 50%, #fce4ec 100%);
        background-attachment: fixed;
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }}
    
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Barre de Navigation plein écran style iOS 26 */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 85px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 65px;
        height: 65px;
        border-radius: 50%;
        border: 2px solid white;
        background: white;
        object-fit: cover;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}

    .content-spacer {{ padding-top: 110px; }}

    /* Adaptabilité Texte (Sombre/Clair) */
    @media (prefers-color-scheme: dark) {{
        .product-card {{ background: rgba(30, 30, 30, 0.8) !important; color: white !important; }}
        .stMarkdown p, .stMarkdown h2 {{ color: white !important; }}
    }}
    @media (prefers-color-scheme: light) {{
        .product-card {{ background: rgba(255, 255, 255, 0.85) !important; color: #1a1a1a !important; }}
        .stMarkdown p, .stMarkdown h2 {{ color: #1a1a1a !important; }}
    }}

    /* Titres Logo Textuel */
    .title-container {{ text-align: center; line-height: 1.1; }}
    .t-the {{ color: #2d5a27; font-size: clamp(30px, 8vw, 50px); font-weight: 900; }}
    .t-floral {{ color: #ff69b4; font-size: clamp(35px, 9vw, 55px); font-family: 'serif'; font-style: italic; }}
    .t-corner {{ color: #2d5a27; font-size: clamp(30px, 8vw, 50px); font-weight: 900; }}

    /* Cartes Produits Interactives */
    .product-card {{
        border-radius: 25px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease;
        border: 1px solid rgba(255,255,255,0.3);
        margin-bottom: 20px;
    }}
    .product-card:hover {{ transform: translateY(-10px); }}
    
    .product-img {{
        width: 100%;
        height: 220px;
        border-radius: 20px;
        object-fit: cover;
    }}

    /* Carte VIP Luxueuse */
    .vip-card {{
        background: linear-gradient(145deg, #222, #444);
        border: 1px solid #d4af37;
        border-radius: 18px;
        padding: 25px;
        color: #d4af37;
        text-align: left;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        font-family: 'Courier New', Courier, monospace;
    }}
    .vip-chip {{
        width: 40px;
        height: 30px;
        background: linear-gradient(90deg, #d4af37, #f1d38e);
        border-radius: 5px;
        margin-bottom: 20px;
    }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div style="color: white; font-weight: bold; font-size: 1.2em;">🌸 2026</div>
    </div>
    <div class="content-spacer"></div>

    <div class="title-container">
        <span class="t-the">THE</span> <span class="t-floral">Floral</span> <span class="t-corner">CORNER</span><br>
        <span style="color: #2d5a27; font-weight: bold; letter-spacing: 3px;">BY KALINA</span>
    </div>
    """, unsafe_allow_html=True)

# --- SECTION PRODUITS ---
st.markdown("<h2 style='text-align: center;'>Nos Valentine Packages</h2>", unsafe_allow_html=True)

# Ici, tu peux ajouter plusieurs images par pack dans une liste
packs = [
    {"id": "sweet", "nom": "PACK SWEET HEART", "prix": "20.000 F", "imgs": ["https://images.unsplash.com/photo-1591886960571-74d43a9d4166"]},
    {"id": "love", "nom": "PACK LOVE STORY", "prix": "30.000 F", "imgs": ["https://images.unsplash.com/photo-1526047932273-341f2a7631f9"]},
    {"id": "passion", "nom": "PACK PASSION", "prix": "40.000 F", "imgs": ["https://images.unsplash.com/photo-1550989460-0adf9ea622e2"]},
    {"id": "vip", "nom": "SIGNATURE VIP", "prix": "60.000 F", "imgs": ["https://images.unsplash.com/photo-1533616688419-b7a585564566"]}
]

cols = st.columns(2)
for i, p in enumerate(packs):
    with cols[i % 2]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{p['imgs'][0]}" class="product-img">
                <h3 style="margin-top:10px;">{p['nom']}</h3>
                <h4 style="color: #ff69b4;">{p['prix']}</h4>
            </div>
        """, unsafe_allow_html=True)
        # Expander pour voir plus de photos
        with st.expander(f"📷 Voir détails {p['nom']}"):
            st.write("Photos supplémentaires du pack :")
            st.image(p['imgs'][0], use_container_width=True)
        if st.button(f"Sélectionner {p['nom']}", key=p['id']):
            st.session_state['selected_pack'] = p['nom']

# --- FORMULAIRE & CARTE DYNAMIQUE ---
st.markdown("---")
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("carte de fidélité & message personnalisé")
    nom = st.text_input("Nom de famille")
    prenom = st.text_input("Prénom")
    message = st.text_area("Votre mot doux")

with c2:
    # Rendu dynamique de la carte VIP
    full_name = f"{prenom} {nom}".strip().upper()
    st.markdown(f"""
        <div class="vip-card">
            <div class="vip-chip"></div>
            <div style="font-size: 0.8em; opacity: 0.7;">MEMBRE PRIVILÉGIÉ</div>
            <div style="font-size: 1.5em; font-weight: bold; margin: 10px 0;">
                {full_name if full_name else "VOTRE NOM ICI"}
            </div>
            <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                <div style="font-size: 0.7em;">VALIDITÉ: 02/27</div>
                <div style="font-size: 1.2em;">THE FLORAL CORNER 🌸</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- BOUTON DE VALIDATION ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("✔ CONFIRMER MA COMMANDE", use_container_width=True):
    if nom and prenom:
        st.balloons()
        pack_nom = st.session_state.get('selected_pack', 'Non spécifié')
        wa_text = f"Bonjour Kalina ! Commande de {prenom} {nom}. Pack: {pack_nom}. Message: {message}"
        st.success("Commande prête ! Cliquez sur le lien pour envoyer sur WhatsApp.")
        st.markdown(f"""<a href="https://wa.me/+221774474769?text={wa_text}" target="_blank">
            <button style="width:100%; padding:15px; background-color:#25D366; color:white; border:none; border-radius:10px; font-weight:bold;">
            FINALISER SUR WHATSAPP 📲
            </button></a>""", unsafe_allow_html=True)
    else:
        st.warning("Veuillez remplir votre nom et prénom pour la carte VIP.")
