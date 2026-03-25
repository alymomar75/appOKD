import streamlit as st
import urllib.parse
import base64
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FONCTIONS UTILES ---
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
    except:
        pass
    return ""

# Initialisation des variables de session
if 'choix_pack' not in st.session_state:
    st.session_state.choix_pack = None
if 'prix_pack' not in st.session_state:
    st.session_state.prix_pack = ""

# --- CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    .stApp {
        background: linear-gradient(-45deg, #7d0a0a, #d14d5d, #2d5a27, #fce4ec);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .product-card {
        background: rgba(255,255,255,0.9);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 10px;
        color: #333;
    }
    .product-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
    }
    .vip-card {
        background: linear-gradient(135deg, #111, #333);
        color: #d4af37;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #d4af37;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; color: white; padding: 20px 0;">
        <h1 style="font-size: 2.2rem; margin:0;">THE <span style="color: #ff69b4; font-family: serif; font-style: italic;">Floral</span> CORNER</h1>
        <p style="letter-spacing: 3px; opacity: 0.8; font-size: 0.8rem; text-transform: uppercase;">Digitalisation des Menus & Services</p>
    </div>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
st.write("### 🌸 Nos Valentine Packages")
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F", "img": "https://images.unsplash.com/photo-1550989460-0adf9ea622e2?q=80&w=500"},
    {"nom": "PACK MBEUGUEL SIGNATURE", "prix": "60.000 F", "img": "https://images.unsplash.com/photo-1533616688419-b7a585564566?q=80&w=500"}
]

col1, col2 = st.columns(2)
for i, p in enumerate(packs):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}" class="product-img">
                <h4 style="margin:10px 0 5px 0;">{p['nom']}</h4>
                <h5 style="color: #d14d5d; font-weight: bold;">{p['prix']}</h5>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Choisir {p['nom']}", key=f"btn_{i}", use_container_width=True):
            st.session_state.choix_pack = p['nom']
            st.session_state.prix_pack = p['prix']
            st.toast(f"✅ {p['nom']} sélectionné !")

# Affichage du choix actuel
if st.session_state.choix_pack:
    st.info(f"📍 Sélection : **{st.session_state.choix_pack}** ({st.session_state.prix_pack})")

# --- FORMULAIRE & CARTE VIP ---
st.divider()
st.subheader("💳 Personnalisation & Fidélité")
col_form, col_card = st.columns([1, 1])

with col_form:
    nom = st.text_input("Nom", placeholder="Ex: Diop").strip()
    prenom = st.text_input("Prénom", placeholder="Ex: Mariama").strip()
    message_bouquet = st.text_area("Mot doux pour le bouquet")

with col_card:
    nom_affichage = f"{prenom} {nom}".strip().upper()
    st.markdown(f"""
        <div class="vip-card">
            <h3 style="margin:0; letter-spacing: 2px; font-size: 12px;">THE FLORAL CORNER VIP</h3>
            <hr style="border: 0.5px solid rgba(212,175,55,0.2); margin: 15px 0;">
            <p style="font-size: 20px; font-weight: bold; min-height: 25px;">
                {nom_affichage if nom_affichage else "VOTRE NOM ICI"}
            </p>
            <p style="font-size: 10px; opacity: 0.7;">MEMBRE PRIVILÉGIÉ • DAKAR</p>
            <div style="text-align: right; font-size: 20px;">💎</div>
        </div>
    """, unsafe_allow_html=True)

# --- PAIEMENT & VALIDATION ---
st.divider()
mode_paiement = st.radio("Moyen de paiement", ["Orange Money / Wave", "Carte Bancaire", "Espèces (Livraison)"], horizontal=True)

if st.button("🚀 VALIDER MA COMMANDE", type="primary", use_container_width=True):
    if not nom or not prenom:
        st.error("⚠️ Veuillez entrer votre nom et prénom pour la carte VIP.")
    elif not st.session_state.choix_pack:
        st.warning("⚠️ Veuillez sélectionner un pack floral ci-dessus.")
    else:
        st.balloons()
        texte_commande = (
            f"Bonjour Kalina ! Nouvelle commande :\n\n"
            f"👤 Client : {nom_affichage}\n"
            f"🌸 Pack : {st.session_state.choix_pack}\n"
            f"💰 Prix : {st.session_state.prix_pack}\n"
            f"💳 Paiement : {mode_paiement}\n"
            f"📝 Message : {message_bouquet}"
        )
        msg_encoded = urllib.parse.quote(texte_commande)
        wa_url = f"https://wa.me/221774474769?text={msg_encoded}"
        
        st.success(f"Merci {prenom} ! Votre commande est prête à être envoyée.")
        st.markdown(f"""
            <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                <div style="background-color: #25D366; color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 1.1rem;">
                    CONFIRMER SUR WHATSAPP 📲
                </div>
            </a>
        """, unsafe_allow_html=True)
