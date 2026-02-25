import streamlit as st
import base64
import os

# Configuration de la page
st.set_page_config(
    page_title="The Floral Corner",
    page_icon="🌸",
    layout="wide"
)

# --- FONCTION IMAGE BASE64 ---
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

img_logo = get_base64_image("logo.jpg")

# --- CSS & EFFET PARALLAX MOBILE ---
st.markdown(f"""
    <style>
    /* Fond principal avec dégradé liquide */
    #main_bg {{
        position: fixed;
        top: -10%;
        left: -10%;
        width: 120%;
        height: 120%;
        background: linear-gradient(135deg, #7d0a0a 0%, #d14d5d 50%, #fce4ec 100%);
        background-size: cover;
        z-index: -1;
        transition: transform 0.1s ease-out;
    }}

    /* Barre de navigation ultra-fine pour éviter les chevauchements */
    .nav-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 999;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .logo-circle {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        border: 2px solid white;
        background: white;
    }}

    /* Conteneur principal décalé pour ne pas être sous la barre */
    .main-content {{
        margin-top: 100px;
        padding: 20px;
        text-align: center;
    }}

    /* Style des titres selon tes instructions */
    .title-the {{ color: #2d5a27; font-size: 40px; font-weight: bold; }}
    .title-floral {{ color: #ff69b4; font-size: 45px; font-family: 'Brush Script MT', cursive; }}
    .title-corner {{ color: #2d5a27; font-size: 40px; font-weight: bold; }}
    .title-by {{ color: #2d5a27; font-size: 18px; display: block; margin-top: -10px; }}

    /* Amélioration de la lisibilité des cases */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border: 2px solid #2d5a27 !important;
    }}
    
    label p {{ color: white !important; font-weight: bold; text-shadow: 1px 1px 2px black; }}
    </style>

    <div id="main_bg"></div>
    
    <div class="nav-bar">
        <img src="data:image/jpeg;base64,{img_logo}" class="logo-circle">
    </div>

    <div class="main-content">
        <span class="title-the">THE</span>
        <span class="title-floral">Floral</span>
        <span class="title-corner">CORNER</span>
        <span class="title-by">BY KALINA</span>
        <p style="color: white; font-style: italic;">🌸 1er Bar à Fleurs Mobile au Sénégal</p>
    </div>

    <script>
    // Script pour l'effet de mouvement sur mobile (Gyroscope)
    const bg = document.getElementById('main_bg');
    window.addEventListener('deviceorientation', (event) => {{
        let x = event.beta;  // Inclinaison avant/arrière
        let y = event.gamma; // Inclinaison gauche/droite
        
        // Limiter le mouvement
        if (x > 45) x = 45; if (x < -45) x = -45;
        if (y > 45) y = 45; if (y < -45) y = -45;

        bg.style.transform = `translate(${{y/2}}px, ${{x/2}}px)`;
    }});
    </script>
    """, unsafe_allow_html=True)

# --- CONTENU STREAMLIT (LE RESTE DU CODE) ---
st.markdown("<br>", unsafe_allow_html=True)

# Packs de vente
col1, col2 = st.columns(2)
packs = [
    {"nom": "PACK SWEET HEART", "prix": "20.000 F CFA", "icon": "❤️"},
    {"nom": "PACK LOVE STORY", "prix": "30.000 F CFA", "icon": "🌹"},
    {"nom": "PACK PASSION", "prix": "40.000 F CFA", "icon": "🧁"},
    {"nom": "PACK MBEUGUEL SIGNATURE", "prix": "60.000 F CFA", "icon": "👑"}
]

for i, p in enumerate(packs):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.9); padding: 15px; border-radius: 15px; margin-bottom: 10px; text-align: center; color: black;">
                <h3 style="margin:0;">{p['icon']} {p['nom']}</h3>
                <h4 style="color: #d14d5d; margin:0;">{p['prix']}</h4>
            </div>
        """, unsafe_allow_html=True)
        st.button("Choisir ce pack", key=f"btn_{i}")

# Formulaire
st.divider()
note = st.text_area("✍️Votre touche personnelle pour accompagner les fleurs :")
nom_vip = st.text_input("Nom pour la carte de fidélité :")

if st.button("🚀 VALIDER LA COMMANDE"):
    st.balloons()
    st.success("Commande enregistrée ! Cliquez sur le lien WhatsApp pour finaliser.")
