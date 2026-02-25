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

# --- CSS COMPLET ---
st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{ display: none; }}
    .main .block-container {{ padding-top: 0rem; padding-bottom: 5rem; max-width: 100%; }}

    /* Fond Liquide Dynamique */
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

    /* Barre de Nav Apple-Style Edge-to-Edge */
    .nav-bar {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 80px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 30px;
        z-index: 9999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 60px; height: 60px;
        border-radius: 50%; border: 2px solid white;
        background: white; object-fit: cover;
    }}

    /* Icône Panier avec infobulle */
    .cart-icon {{
        font-size: 28px; color: white; cursor: pointer; position: relative;
    }}
    .cart-icon:hover::after {{
        content: "Ajoutez un pack à votre panier en bas";
        position: absolute; top: 40px; right: 0;
        background: white; color: black; font-size: 12px;
        padding: 5px 10px; border-radius: 5px; width: 180px;
    }}

    .content-spacer {{ padding-top: 120px; }}

    /* Bouton Flashy Confirmer */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #ff0055, #ff69b4);
        color: white !important;
        border: none;
        border-radius: 50px;
        padding: 20px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.6);
        transition: 0.3s;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0% {{ transform: scale(1); box-shadow: 0 0 20px rgba(255, 0, 85, 0.6); }}
        50% {{ transform: scale(1.02); box-shadow: 0 0 40px rgba(255, 0, 85, 0.9); }}
        100% {{ transform: scale(1); box-shadow: 0 0 20px rgba(255, 0, 85, 0.6); }}
    }}

    /* Bouton WhatsApp Flottant */
    .wa-float {{
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white !important;
        border-radius: 50px;
        padding: 15px 25px;
        font-weight: bold;
        text-decoration: none;
        z-index: 100;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    /* Carte VIP Luxe */
    .vip-card {{
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%);
        border: 1px solid #d4af37;
        border-radius: 15px; padding: 20px; color: #d4af37;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    </style>

    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
        <div class="cart-icon">🛒</div>
    </div>
    
    <div class="content-spacer"></div>

    <div style="text-align: center;">
        <h1 style="color: #2d5a27; margin-bottom:0;">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="color: white; letter-spacing: 2px;">BY KALINA</p>
    </div>
    """, unsafe_allow_html=True)

# --- BOUTON WHATSAPP FLOTTANT ---
message_wa_direct = "Bonsoir Kalina ! J'ai parcouru votre magnifique site et je suis vraiment intéressé(e) par vos compositions florales. Pourriez-vous m'aider à choisir le cadeau parfait ?"
st.markdown(f"""
    <a href="https://wa.me/221774474769?text={message_wa_direct}" class="wa-float" target="_blank">
        <span>Besoin d'aide ? Contactez-nous</span> 📲
    </a>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### 🎁 Choisissez votre bonheur")
packs = [
    {"id": "p1", "nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166"},
    {"id": "p2", "nom": "PACK LOVE STORY", "prix": "30.000 F", "img": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9"}
]

c1, c2 = st.columns(2)
for i, p in enumerate(packs):
    with (c1 if i==0 else c2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding:15px; border-radius:20px; text-align:center;">
                <img src="{p['img']}" style="width:100%; border-radius:15px; height:200px; object-fit:cover;">
                <h3 style="color: black;">{p['nom']}</h3>
                <h4 style="color: #d14d5d;">{p['prix']}</h4>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Ajouter au panier : {p['nom']}", key=p['id']):
            st.session_state['selection'] = p['nom']
            st.toast(f"Ajouté : {p['nom']} 🛒")

# --- FIDÉLITÉ ---
st.divider()
col_f1, col_f2 = st.columns(2)
with col_f1:
    nom_u = st.text_input("Votre Nom")
    prenom_u = st.text_input("Votre Prénom")
with col_f2:
    full_name = f"{prenom_u} {nom_u}".strip().upper()
    st.markdown(f"""
        <div class="vip-card">
            <small>VIP MEMBER</small>
            <div style="font-size: 20px; font-weight: bold; margin: 10px 0;">{full_name if full_name else "NOM DU CLIENT"}</div>
            <div style="text-align: right; font-size: 10px;">THE FLORAL CORNER SENEGAL</div>
        </div>
    """, unsafe_allow_html=True)

# --- VALIDATION ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 CONFIRMER MA COMMANDE"):
    if nom_u and prenom_u:
        pack_choisi = st.session_state.get('selection', 'Pack non défini')
        msg_final = f"Bonsoir Kalina ! Je viens de commander via votre site. Je suis {prenom_u} {nom_u} et j'ai choisi le {pack_choisi}. J'ai vraiment hâte !"
        st.success("Génial ! Finalisons cela sur WhatsApp.")
        st.markdown(f"""<a href="https://wa.me/221774474769?text={msg_final}" target="_blank">
            <div style="background:#25d366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">
            CLIQUER ICI POUR ENVOYER LE RÉCAPITULATIF 📲
            </div></a>""", unsafe_allow_html=True)
    else:
        st.error("N'oubliez pas d'entrer votre nom pour votre carte VIP !")
