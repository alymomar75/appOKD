000 F CFA", "desc": "Bento Cake + Cupcakes + Biscuits + Bouquet", "icon": "👑"},
]

col1, col2 = st.columns(2)

for i, p in enumerate(packs):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="product-card">
            <span style="font-size: 40px;">{p['icon']}</span>
            <h3>{p['nom']}</h3>
            <h4 style="color: #d14d5d;">{p['prix']}</h4>
            <p style="font-size: 0.9em;">{p['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Sélectionner {p['nom']}", key=i):
            st.session_state['choice'] = p['nom']

# --- FORMULAIRE DE PERSONNALISATION ---
st.divider()
st.subheader("✍️ Personnalisation & Message")
col_a, col_b = st.columns(2)

with col_a:
    message = st.text_area("Mot doux à joindre au bouquet", placeholder="Écrivez ici...")
    couleur = st.select_slider("Couleur dominante souhaitée", options=["Rouge", "Rose", "Blanc", "Mixte"])

with col_b:
    st.info("💡 Statut : Atelier ouvert • Précommandes jusqu'au 10 Fév.")
    nom_carte = st.text_input("Nom pour la carte de fidélité VIP", "Prénom Nom")

# --- PAIEMENT ---
st.divider()
st.subheader("💳 Finalisation")
option = st.radio("Mode de règlement", ["Orange Money / Wave", "Carte Bancaire", "Acompte 50%"])

if st.button("CONFIRMER LA COMMANDE"):
    if 'choice' in st.session_state:
        st.balloons()
        st.success(f"Commande validée : {st.session_state['choice']}")
        st.write(f"Destinataire : {nom_carte}")
        if option == "Orange Money / Wave":
            st.warning("Envoyez votre paiement au +221 77 447 47 69 pour confirmer.")
    else:
        st.error("Veuillez d'abord choisir un pack ci-dessus.")

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; color: #888;">
        The Floral Corner by Kalina | Dakar, Sénégal <br>
        <i>Atelier floral unique & personnalisé</i>
    </div>
    """, unsafe_allow_html=True)
