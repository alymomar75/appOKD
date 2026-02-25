import streamlit as st
from PIL import Image
import base64
import os

# Configuration de la page
st.set_page_config(
    page_title="The Floral Corner | Boutique Premium",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FONCTION POUR L'IMAGE EN BASE64 (SÉCURISÉE) ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

img_base64 = get_base64_image("logo.jpg")

# --- INJECTION DU STYLE CSS ---
st.markdown(f"""
    <style>
    /* Effet Liquide Glacé iOS 26 */
    .stApp {{
        background: linear-gradient(135deg, #fce4ec 0%, #e8f5e9 50%, #fce4ec 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }}
    
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Barre de navigation Apple Style */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        z-index: 999;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .logo-circle {{
        width: 65px;
        height: 65px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.4s ease;
    }}
    
    .logo-circle:hover {{
        transform: scale(1.1) rotate(5deg);
    }}

    .product-card {{
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        transition: 0.3s all ease-in-out;
        text-align: center;
        margin-bottom: 15px;
    }}

    .product-card:hover {{
        transform: translateY(-8px);
        background: rgba(255, 255, 255, 0.7);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }}

    .content-spacer {{ padding-top: 100px; }}
    </style>
    """, unsafe_allow_html=True)

# --- BARRE DE NAVIGATION ---
logo_tag = f'<img src="data:image/jpeg;base64,{img_base64}" class="logo-circle">' if img_base64 else '<div class="logo-circle" style="background:#d14d5d; color:white; display:flex; align-items:center; justify-content:center;">TFC</div>'

st.markdown(f'<div class="nav-bar">{logo_tag}</div><div class="content-spacer"></div>', unsafe_allow_html=True)

# --- CORPS DU SITE ---
st.markdown("<h1 style='text-align: center; color: #4a148c;'>The Floral Corner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>✨ 1er Bar à Fleurs Mobile au Sénégal 🇸🇳</p>", unsafe_allow_html=True)

# Catalogue
st.write("### 🎁 Valentine Packages 2026")
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
            <h3>{p['nom']}</h3>
            <h4 style="color: #d14d5d;">{p['prix']}</h4>
            <p style="font-size: 0.8em; color: #555;">{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Choisir {p['nom']}", key=f"btn_{i}"):
            st.session_state['selected'] = p['nom']

# Personnalisation
st.divider()
st.subheader("✍️ Votre touche personnelle")
msg = st.text_area("Mot doux pour le bouquet")
nom_client = st.text_input("Nom pour la carte VIP", "Prénom Nom")

# Paiement
st.divider()
st.subheader("💳 Paiement (Dakar)")
mode = st.radio("Moyen de paiement", ["Orange Money / Wave", "Carte Bancaire", "Acompte 50%"])

if st.button("🚀 VALIDER LA COMMANDE"):
    if 'selected' in st.session_state:
        st.balloons()
        st.success(f"Commande pour {st.session_state['selected']} enregistrée !")
        # Optionnel: Lien WhatsApp
        whatsapp_url = f"https://wa.me/221774474769?text=Commande%20{st.session_state['selected']}%20par%20{nom_client}"
        st.markdown(f"[Cliquer ici pour confirmer sur WhatsApp]({whatsapp_url})")
    else:
        st.error("Veuillez choisir un pack.")
