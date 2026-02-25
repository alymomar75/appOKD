import streamlit as st
from PIL import Image
import base64
import os

# Configuration de la page
st.set_page_config(
    page_title="The Floral Corner | Premium",
    page_icon="🌸",
    layout="wide"
)

# --- FONCTION IMAGE BASE64 POUR LE LOGO ---
st.image("logo.jpg")
def get_base64_image(image_path):
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except: return None
    return None

img_base64 = get_base64_image("logo.jpg")

# --- CSS : EFFET LIQUIDE ROUGE & TEXTE COLORÉ ---
st.markdown(f"""
    <style>
    /* Fond Rouge Floral avec effet liquide glacé */
    .stApp {{
        background: linear-gradient(135deg, #7d0a0a 0%, #d14d5d 50%, #fce4ec 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }}
    
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Barre de navigation Apple Glass plus large */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 120px;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.3);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .logo-circle {{
        width: 90px;
        height: 90px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid white;
        background: white;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    .logo-circle:hover {{ transform: scale(1.15); }}

    .content-spacer {{ padding-top: 150px; }}

    /* Titre Spécifique : THE (vert), Floral (rose), CORNER (vert) */
    .brand-title {{
        text-align: center;
        font-family: 'serif';
        font-weight: bold;
        font-size: 3.5em;
        margin-bottom: 0;
    }}
    .text-green {{ color: #2d5a27; }}
    .text-pink {{ color: #ff69b4; font-style: italic; }}
    .sub-brand {{
        text-align: center;
        color: #2d5a27;
        font-size: 1.2em;
        margin-top: -10px;
        font-weight: bold;
    }}

    /* Cases de saisie claires/blanches pour lisibilité */
    input, textarea {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #1a1a1a !important;
        border-radius: 12px !important;
    }}

    /* Carte de Fidélité VIP Premium */
    .fidelity-card {{
        background: linear-gradient(135deg, #d4af37 0%, #f1d38e 100%);
        padding: 40px;
        border-radius: 25px;
        color: #1a1a1a;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.5);
    }}

    /* Cartes Produits Effet Glace */
    .product-card {{
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        color: #1a1a1a;
        border: 1px solid white;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
logo_html = f'<img src="data:image/jpeg;base64,{img_base64}" class="logo-circle">' if img_base64 else '<div class="logo-circle" style="background:white;"></div>'
st.markdown(f'<div class="nav-bar">{logo_html}</div><div class="content-spacer"></div>', unsafe_allow_html=True)

# --- TITRE PERSONNALISÉ ---
st.markdown("""
    <div class="brand-title">
        <span class="text-green">THE</span> 
        <span class="text-pink">Floral</span> 
        <span class="text-green">CORNER</span>
    </div>
    <div class="sub-brand">BY KALINA</div>
    """, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>🌸 Atelier Floral Mobile • Dakar, Sénégal</p>", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("## 🎁 Valentine Packages 2026")
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F CFA", "desc": "Bento + Rose", "icon": "❤️"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F CFA", "desc": "Bento + Bouquet", "icon": "🌹"},
    {"nom": "PACK PASSION", "prix": "40.000 F CFA", "desc": "Bento + Cupcakes + Bouquet", "icon": "🧁"},
    {"nom": "PACK MBEUGUEL SIGNATURE", "prix": "60.000 F CFA", "desc": "Bento Cake + Cupcakes + Biscuits + Bouquet", "icon": "👑"},
]

col1, col2 = st.columns(2)
for i, p in enumerate(packs):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="product-card">
            <div style="font-size: 40px;">{p['icon']}</div>
            <h3 style="color: #d14d5d;">{p['nom']}</h3>
            <h4 style="color: #1a1a1a;">{p['prix']}</h4>
            <p style="font-size: 0.9em; color: #444;">{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter {p['nom']}", key=i):
            st.session_state['selected'] = p['nom']

# --- FORMULAIRE ---
st.divider()
msg = st.text_area("✍️Votre touche personnelle:")
nom_vip = st.text_input("Votre nom pour la carte de fidélité :")

# --- CARTE DE FIDÉLITÉ ---
if nom_vip:
    st.markdown(f"""
    <div class="fidelity-card">
        <h2 style="margin:0;">THE FLORAL CORNER VIP</h2>
        <p style="letter-spacing: 5px; font-size: 1.5em; font-weight: bold;">{nom_vip.upper()}</p>
        <p>Membre Privilégié - Dakar</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAIEMENT ---
st.divider()
mode = st.radio("Moyen de paiement", ["Orange Money / Wave", "Carte Bancaire", "Acompte 50%"])

if st.button("🚀 VALIDER LA COMMANDE"):
    if 'selected' in st.session_state:
        st.balloons()
        wa_url = f"https://wa.me/221774474769?text=Commande%20{st.session_state['selected']}%20par%20{nom_vip}"
        st.success(f"Commande de {st.session_state['selected']} initiée !")
        st.markdown(f"[📲 Cliquez ici pour finaliser sur WhatsApp]({wa_url})")
