import streamlit as st
import base64
import os
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fonction pour encoder les images locales en Base64
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except Exception:
        pass
    return ""

# Récupération des images (Vérifiez que ces fichiers sont bien dans votre dossier sur GitHub)
img_logo = get_base64_image("logo.jpg")
img_sweet = get_base64_image("bouquet.jpeg")
img_love = get_base64_image("fleur.jpeg")
img_wave_local = get_base64_image("wavelogo.png")
img_cash_local = get_base64_image("cash.png")

# Initialisation de la session pour le panier
if 'panier' not in st.session_state:
    st.session_state['panier'] = []

# --- CSS PERSONNALISÉ & ANIMATIONS ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    [data-testid="stHeader"] {{ visibility: hidden; }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 2rem; max-width: 100%; }}

    /* Fond dégradé animé */
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

    /* Barre de navigation fixe */
    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 70px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 50px; height: 50px;
        border-radius: 50%; border: 2px solid white;
        background: white; object-fit: cover;
    }}

    .content-spacer {{ padding-top: 90px; }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div style="color: white; font-weight: bold;">
            🛒 <span style="background: #ff69b4; padding: 3px 10px; border-radius: 12px; font-size: 0.8rem;">{len(st.session_state['panier'])}</span>
        </div>
    </div>
    
    <div class="content-spacer"></div>

    <div style="text-align: center; color: white; margin-bottom: 25px;">
        <h1 style="font-size: 2rem; margin:0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="letter-spacing: 3px; opacity: 0.9; font-size: 0.7rem; text-transform: uppercase;">
            Digitalisation des Menus & Services
        </p>
    </div>
""", unsafe_allow_html=True)

# --- SECTION CATALOGUE ---
st.write("### 🌸 Nos Valentine Packages")
col1, col2 = st.columns(2)

# Liste des produits avec valeur numérique pour le calcul
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "val": 20000, "img": f"data:image/jpeg;base64,{img_sweet}"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "val": 30000, "img": f"data:image/jpeg;base64,{img_love}"}
]

for i, p in enumerate(packs):
    target_col = col1 if i == 0 else col2
    with target_col:
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding:10px; border-radius:15px; margin-bottom:10px; text-align:center; color: #333;">
                <div style="width: 100%; aspect-ratio: 1 / 1; overflow: hidden; border-radius: 10px; background: #eee;">
                    <img src="{p['img']}" style="width:100%; height:100%; object-fit: cover;">
                </div>
                <h4 style="margin:10px 0 5px 0; font-size:0.9rem;">{p['nom']}</h4>
                <p style="color: #d14d5d; font-weight: bold; font-size:1rem; margin-bottom:10px;">{p['prix']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter au panier", key=f"btn_{i}", use_container_width=True):
            st.session_state['panier'].append(p)
            st.rerun()

# --- GESTION DU PANIER ---
if len(st.session_state['panier']) > 0:
    with st.expander("🧐 Voir le détail de mon panier"):
        total_cmd = 0
        for idx, item in enumerate(st.session_state['panier']):
            st.write(f"✅ {item['nom']} — **{item['prix']}**")
            total_cmd += item['val']
        st.divider()
        st.write(f"### TOTAL : {total_cmd:,} F CFA")
        if st.button("🗑️ Vider le panier", use_container_width=True):
            st.session_state['panier'] = []
            st.rerun()

# --- FORMULAIRE CLIENT & CARTE VIP ---
st.divider()
st.subheader("👤 Informations Client")
c1, c2 = st.columns(2)
with c1:
    nom = st.text_input("Nom").strip()
with c2:
    prenom = st.text_input("Prénom").strip()

nom_complet = f"{prenom} {nom}".strip().upper()

st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1a1a1a, #444); border: 1.5px solid #d4af37; border-radius: 15px; padding: 20px; color: #d4af37; box-shadow: 0 8px 15px rgba(0,0,0,0.3); text-align: left;">
        <div style="font-size: 0.6rem; letter-spacing: 2px; opacity: 0.8;">THE FLORAL CORNER VIP MEMBER</div>
        <div style="font-size: 1.2rem; margin-top: 15px; font-weight: bold; letter-spacing: 1px;">{nom_complet if nom_complet else "VOTRE NOM ICI"}</div>
        <div style="text-align: right; font-size: 0.5rem; margin-top: 10px; opacity: 0.5;">PREMIUM ACCESS</div>
    </div>
""", unsafe_allow_html=True)

# --- PAIEMENT ---
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("💳 Mode de paiement")
option_paiement = st.radio(
    "Comment souhaitez-vous régler ?",
    ("Wave", "Orange Money", "MasterCard", "Espèces"),
    horizontal=True
)

# Gestion des logos de paiement
logos_dict = {
    "Wave": f"data:image/png;base64,{img_wave_local}",
    "Orange Money": "https://upload.wikimedia.org/wikipedia/commons/c/c8/Orange_logo.svg",
    "MasterCard": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg",
    "Espèces": f"data:image/png;base64,{img_cash_local}"
}

st.markdown(f"""
    <div style="text-align: center; margin: 10px 0;">
        <div style="display: inline-block; background: white; padding: 10px; border-radius: 10px;">
            <img src="{logos_dict.get(option_paiement)}" height="40" style="object-fit: contain;">
        </div>
    </div>
""", unsafe_allow_html=True)

# --- VALIDATION FINALE ---
if st.button("🚀 FINALISER MA COMMANDE", type="primary", use_container_width=True):
    if not nom or not prenom:
        st.error("⚠️ Merci de renseigner votre Nom et Prénom.")
    elif not st.session_state['panier']:
        st.warning("⚠️ Votre panier est vide. Ajoutez un pack pour continuer.")
    else:
        # Construction du message WhatsApp
        articles_liste = ", ".join([x['nom'] for x in st.session_state['panier']])
        message_wa = f"Bonjour The Floral Corner ! Je souhaite commander : {articles_liste}. Mode de paiement : {option_paiement}. Client : {prenom} {nom}."
        
        # Encodage pour URL
        encoded_msg = urllib.parse.quote(message_wa)
        whatsapp_url = f"https://wa.me/221774474769?text={encoded_msg}"
        
        st.success("Commande validée ! Cliquez sur le bouton WhatsApp ci-dessous.")
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="text-decoration:none;">
                <div style="background:#25d366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; font-size:1.1rem;">
                    Ouvrir WhatsApp pour payer 📲
                </div>
            </a>
        """, unsafe_allow_html=True)
