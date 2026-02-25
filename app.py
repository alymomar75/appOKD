import streamlit as st
import base64
import os
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="The Floral Corner | Boutique",
    page_icon="🌸",
    layout="wide"
)

# --- FONCTION POUR CONVERTIR LES IMAGES EN BASE64 ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# On récupère le logo et on prépare des placeholders pour tes photos de fleurs
# Remplace 'pack1.jpg', etc., par les noms de tes fichiers sur GitHub
img_logo = get_base64_image("logo.jpg")

# --- CSS : FOND LIQUIDE ROUGE & NAVBAR APPLE ---
st.markdown(f"""
    <style>
    /* Fond Liquide Glacé Rougeâtre */
    .stApp {{
        background: linear-gradient(135deg, #7d0a0a 0%, #d14d5d 50%, #fce4ec 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }}
    
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Navbar Apple-Style avec Logo Circulaire */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 90px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 75px;
        height: 75px;
        border-radius: 50%;
        border: 2px solid white;
        background: white;
        object-fit: cover;
    }}

    .content-spacer {{ padding-top: 120px; }}

    /* Titres avec couleurs spécifiques */
    .title-container {{ text-align: center; margin-bottom: 20px; }}
    .t-the {{ color: #2d5a27; font-size: 45px; font-weight: bold; }}
    .t-floral {{ color: #ff69b4; font-size: 50px; font-family: 'serif'; italic; }}
    .t-corner {{ color: #2d5a27; font-size: 45px; font-weight: bold; }}
    .t-by {{ color: #2d5a27; font-size: 20px; font-weight: bold; display: block; }}

    /* Cartes Produits */
    .product-card {{
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        color: #1a1a1a;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }}
    .product-img {{
        width: 100%;
        height: 200px;
        border-radius: 15px;
        object-fit: cover;
        margin-bottom: 10px;
    }}

    /* Carte de Fidélité VIP Temp Réel */
    .vip-card {{
        background: linear-gradient(135deg, #d4af37 0%, #aa891a 100%);
        border-radius: 20px;
        padding: 30px;
        color: white;
        text-align: center;
        border: 2px solid #f1d38e;
        box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        margin-top: 20px;
    }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
    </div>
    <div class="content-spacer"></div>

    <div class="title-container">
        <span class="t-the">THE</span> <span class="t-floral">Floral</span> <span class="t-corner">CORNER</span>
        <span class="t-by">BY KALINA</span>
        <p style="color: white; font-style: italic;">1er Bar à Fleurs Mobile au Sénégal 🇸🇳</p>
    </div>
    """, unsafe_allow_html=True)

# --- CATALOGUE AVEC PHOTOS ---
st.write("## 🎁 Nos Valentine Packages 2026")

# Liste des packs. Remplace les 'url_ou_chemin' par tes vraies photos.
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166?q=80&w=500"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F", "img": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?q=80&w=500"},
    {"nom": "PACK PASSION", "prix": "40.000 F", "img": "https://images.unsplash.com/photo-1550989460-0adf9ea622e2?q=80&w=500"},
    {"nom": "PACK MBEUGUEL SIGNATURE", "prix": "60.000 F", "img": "https://images.unsplash.com/photo-1533616688419-b7a585564566?q=80&w=500"}
]

col1, col2 = st.columns(2)
for i, p in enumerate(packs):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}" class="product-img">
                <h3 style="margin:0;">{p['nom']}</h3>
                <h4 style="color: #d14d5d;">{p['prix']}</h4>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Choisir {p['nom']}", key=f"p_{i}")

# --- FORMULAIRE & CARTE VIP ---
st.divider()
st.subheader("💳 Personnalisation & Fidélité")

col_form, col_card = st.columns([1, 1])

with col_form:
    nom = st.text_input("Nom", placeholder="Ex: Diop")
    prenom = st.text_input("Prénom", placeholder="Ex: Mariama")
    message = st.text_area("Mot doux pour le bouquet")

with col_card:
    # Rendu de la carte en temps réel
    nom_complet = f"{prenom} {nom}".strip()
    st.markdown(f"""
        <div class="vip-card">
            <h3 style="margin:0; letter-spacing: 2px;">THE FLORAL CORNER VIP</h3>
            <hr style="border: 0.5px solid rgba(255,255,255,0.3);">
            <p style="font-size: 24px; font-weight: bold; text-transform: uppercase;">
                {nom_complet if nom_complet else "VOTRE NOM ICI"}
            </p>
            <p style="font-size: 12px; opacity: 0.8;">MEMBRE PRIVILÉGIÉ • DAKAR</p>
            <div style="text-align: right; font-size: 20px;">💎</div>
        </div>
    """, unsafe_allow_html=True)

# --- PAIEMENT & VALIDATION ---
st.divider()
mode = st.radio("Moyen de paiement", ["Orange Money / Wave", "Carte Bancaire", "Espèces (Livraison)"])

if st.button("🚀 VALIDER LA COMMANDE"):
    if nom_complet:
        st.balloons()
        st.success(f"Merci {prenom} ! Kalina prépare votre pack.")
        wa_link = f"https://wa.me/221774474769?text=Commande%20de%20{nom_complet}%20:%20{message}"
        st.markdown(f"[📲 Cliquer ici pour confirmer sur WhatsApp]({wa_link})")
    else:
        st.error("Veuillez entrer votre nom pour la carte VIP.")
