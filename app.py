com/photo-1550989460-0adf9ea622e2?q=80&w=500"},
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
