import streamlit as st
from PIL import Image
import base64
import os

# 1. Configuration de la page
st.set_page_config(
    page_title="The Floral Corner | Boutique Premium",
    page_icon="🌸",
    layout="wide"
)

# 2. Fonction de conversion d'image sécurisée
def get_base64_image(image_path):
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except Exception:
            return None
    return None

img_base64 = get_base64_image("logo.jpg")

# 3. CSS forcé pour la lisibilité (Contraste maximal)
st.markdown(f"""
    <style>
    /* Arrière-plan animé (effet léger pour ne pas gêner la lecture) */
    .stApp {{
        background: linear-gradient(135deg, #fff5f7 0%, #f0fdf4 100%);
    }}

    /* Forcer la couleur du texte partout pour la lisibilité */
    html, body, [class*="st-"] {{
        color: #1a1a1a !important; /* Gris très foncé presque noir */
    }}

    /* Bande haute style Apple (Fixe et opaque pour lire le menu) */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 2px solid #d14d5d;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    /* Logo circulaire avec bordure pour le voir sur fond blanc */
    .logo-circle {{
        width: 65px;
        height: 65px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #d14d5d;
        background-color: white;
    }}

    /* Cartes produits : Fond blanc pur pour détacher le texte */
    .product-card {{
        background: white !important;
        border-radius: 20px;
        padding: 25px;
        border: 1px solid #eee;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        margin-bottom: 20px;
    }}
    
    .product-card h3, .product-card h4 {{
        color: #8e2d3a !important;
    }}

    .content-spacer {{ padding-top: 100px; }}
    
    /* Forcer les labels des champs de texte en noir */
    label p {{
        color: #000000 !important;
        font-weight: bold !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. Affichage de la Navigation
if img_base64:
    logo_html = f'<img src="data:image/jpeg;base64,{img_base64}" class="logo-circle">'
else:
    # Fallback si logo.jpg n'est pas trouvé
    logo_html = '<div class="logo-circle" style="display:flex;align-items:center;justify-content:center;font-weight:bold;color:#d14d5d;">TFC</div>'

st.markdown(f'<div class="nav-bar">{logo_html}</div><div class="content-spacer"></div>', unsafe_allow_html=True)

# 5. Titres principaux
st.markdown("<h1 style='text-align: center; color: #8e2d3a;'>The Floral Corner</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>🌸 1er Bar à Fleurs Mobile au Sénégal</p>", unsafe_allow_html=True)

# 6. Catalogue
st.markdown("---")
st.markdown("<h2 style='color: #8e2d3a;'>🎁 Nos Valentine Packages</h2>", unsafe_allow_html=True)

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
            <div style="font-size: 50px;">{p['icon']}</div>
            <h3 style="margin: 10px 0;">{p['nom']}</h3>
            <h4 style="color: #d14d5d !important; font-size: 1.4em;">{p['prix']}</h4>
            <p style="color: #555 !important;">{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Choisir {p['nom']}", key=f"btn_{i}"):
            st.session_state['selected_pack'] = p['nom']

# 7. Personnalisation
st.markdown("---")
st.markdown("<h2 style='color: #8e2d3a;'>✍️ Personnalisation</h2>", unsafe_allow_html=True)
message = st.text_area("Votre mot doux pour accompagner les fleurs :")
nom_client = st.text_input("Nom pour votre carte de fidélité VIP :")

# 8. Paiement
st.markdown("---")
st.markdown("<h2 style='color: #8e2d3a;'>💳 Paiement</h2>", unsafe_allow_html=True)
mode = st.radio("Moyen de paiement (Dakar) :", ["Orange Money / Wave", "Carte Bancaire", "Acompte 50%"])

if st.button("🚀 CONFIRMER MA COMMANDE"):
    if 'selected_pack' in st.session_state:
        st.balloons()
        st.success(f"Merci ! Commande pour le {st.session_state['selected_pack']} bien reçue.")
        whatsapp_msg = f"Bonjour Kalina, je souhaite commander le {st.session_state['selected_pack']}. Message : {message}"
        st.markdown(f"[👉 Cliquez ici pour finaliser sur WhatsApp](https://wa.me/221774474769?text={whatsapp_msg})")
    else:
        st.error("Veuillez sélectionner un pack ci-dessus avant de valider.")
