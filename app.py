import streamlit as st
from PIL import Image

# Configuration de la page pour un affichage optimal sur Mobile et PC
st.set_page_config(
    page_title="The Floral Corner by Kalina",
    page_icon="🌸",
    layout="wide"
)

# --- STYLE CSS (Adapté pour le look floral) ---
st.markdown("""
    <style>
    .main { background-color: #fffafb; }
    .stButton>button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #d14d5d; 
        color: white; 
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    .product-card { 
        border: 1px solid #f9e1e4; 
        padding: 20px; 
        border-radius: 15px; 
        background: white; 
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2, h3 { color: #8e2d3a; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER / LOGO ---
col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 2, 1])
with col_logo_2:
    try:
        logo = Image.open("logo.jpg")
        st.image(logo, use_container_width=True)
    except:
        st.title("🌸 THE FLORAL CORNER")
        st.markdown("<h4 style='text-align: center;'>BY KALINA</h4>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-style: italic;'>1er Bar à Fleurs Mobile au Sénégal 🇸🇳<br>Atelier floral unique & personnalisé pour vos événements.</p>", unsafe_allow_html=True)

# --- SECTION CATALOGUE ---
st.divider()
st.header("🎁 Valentine Packages 2026")

# Liste des produits basée sur tes images
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F CFA", "desc": "Bento + Rose", "emoji": "❤️"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F CFA", "desc": "Bento + Bouquet", "emoji": "🌹"},
    {"nom": "PACK PASSION", "prix": "40.000 F CFA", "desc": "Bento + Cupcakes + Bouquet", "emoji": "🧁"},
    {"nom": "PACK MBEUGUEL SIGNATURE", "prix": "60.000 F CFA", "desc": "Bento Cake + Cupcakes + Biscuits + Bouquet", "emoji": "👑"},
]

# Affichage en colonnes (se superposent sur mobile)
col1, col2 = st.columns(2)

selected_package = None

for i, p in enumerate(packs):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="product-card">
            <h2 style='font-size: 1.2em;'>{p['emoji']} {p['nom']}</h2>
            <p style='color: #d14d5d; font-size: 1.3em; font-weight: bold;'>{p['prix']}</p>
            <p style='font-size: 0.9em; color: #666;'>{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Choisir {p['nom']}", key=f"btn_{i}"):
            st.session_state['selected_pack'] = p['nom']
            st.toast(f"{p['nom']} sélectionné !")

# --- SECTION PERSONNALISATION (Nouveauté) ---
st.divider()
st.header("✨ Personnalisez votre attention")

col_perso_1, col_perso_2 = st.columns(2)

with col_perso_1:
    st.subheader("📝 Mot doux")
    note = st.text_area("Écrivez le message à joindre au bouquet :", 
                         placeholder="Ex: Joyeuse Saint-Valentin mon amour...", 
                         max_chars=200)
    
with col_perso_2:
    st.subheader("🎀 Détails de l'Atelier")
    couleur_ruban = st.selectbox("Couleur du ruban :", ["Rouge Passion", "Rose Poudré", "Blanc Pur", "Doré"])
    date_livraison = st.date_input("Date de livraison souhaitée (Dakar) :")

# --- CARTE DE FIDÉLITÉ ---
st.divider()
st.header("💳 Votre Carte de Fidélité")
with st.expander("Générer ma carte personnalisée"):
    nom_client = st.text_input("Nom sur la carte", "Votre Nom")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #2d5a27, #1e3a1a); color: white; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #c5a059;">
        <h3 style='color: white; margin:0;'>THE FLORAL CORNER VIP</h3>
        <p style='font-size: 1.1em; letter-spacing: 2px;'>{nom_client.upper()}</p>
        <hr style='border: 0.5px solid #c5a059;'>
        <p style='font-size: 0.8em;'>Membre de l'Atelier Floral - Sénégal</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAIEMENT ---
st.divider()
st.header("🛍️ Validation & Paiement")
mode_paiement = st.radio("Moyen de paiement :", ["Orange Money / Wave", "Carte Bancaire", "Acompte 50%"])

if mode_paiement == "Orange Money / Wave":
    st.warning("⚠️ Pour valider, envoyez l'acompte aux numéros : +221 77 447 47 69 / +221 77 669 85 90")

if st.button("🚀 ENVOYER MA COMMANDE"):
    if 'selected_pack' not in st.session_state:
        st.error("Veuillez choisir un Pack (bouton 'Choisir') en haut de la page.")
    else:
        st.balloons()
        st.success(f"Merci ! Votre commande pour le '{st.session_state['selected_pack']}' avec le ruban {couleur_ruban} a été reçue.")
        st.info(f"Note transmise : « {note} »")

st.markdown("<p style='text-align: center; color: gray; font-size: 0.8em;'><br>© 2026 The Floral Corner by Kalina - Dakar, Sénégal</p>", unsafe_allow_html=True)
