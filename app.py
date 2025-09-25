import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Portfolio | Lassina Sanou", page_icon="🌍", layout="wide")

# --- En-tête ---
st.title("👋 Bienvenue sur mon Portfolio")
st.subheader("Je suis Lassina Sanou, passionné de Data Science et Développement")

# --- Image de profil ---
image = Image.open("profil.jpg")  # Mets une photo de toi dans ton dossier
st.image(image, width=200)

st.markdown("---")

# --- À propos ---
st.header("À propos de moi")
st.write("""
Je suis un jeune professionnel passionné par :
- 📊 Data Science & Machine Learning  
- 🌍 Analyse économique et développement  
- 💻 Développement d’applications web et prédictives  

Ma mission principale en tant que Data Scientist est d’exploiter les
données massives (big data) afin d’en extraire des informations
pertinentes pour aider à la prise de décision stratégique. J’analyse,
modélise et interprète des données complexes à l’aide de techniques
statistiques, d’apprentissage automatique (machine learning) et de
visualisation.
""")

# --- Compétences ---
st.header("Compétences")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Data Science")
    st.write("- Python, Pandas, Scikit-learn")
    st.write("- XGBoost, Machine Learning")
    st.write("- Power BI, DataViz")

with col2:
    st.subheader("💻 Développement")
    st.write("- Streamlit, FastAPI")
    st.write("- HTML, CSS, JavaScript")
    st.write("- Git, GitHub")

with col3:
    st.subheader("🌍 Économie & Dév.")
    st.write("- Analyse économique")
    st.write("- Politiques publiques")
    st.write("- Développement local")

# --- Projets ---
st.header("Mes Projets")
st.write("Voici quelques projets récents :")

st.markdown("✅ [Application de prédiction de la production céréalière au Burkina Faso](https://github.com/tonprofil/projet-cereales)")
st.markdown("✅ [Tableau de bord Power BI pour l'analyse socio-économique](https://github.com/tonprofil/projet-dashboard)")
st.markdown("✅ [API de Machine Learning avec FastAPI](https://github.com/tonprofil/api-ml)")

# --- Contact ---
st.header("📬 Contact")
st.write("N’hésitez pas à me contacter :")
st.write("Numéros : (+226) 74544113 / 62972111")
st.write("📧 Email : slassina92@gmail.com")
st.write("🔗 LinkedIn : [Mon LinkedIn](www.linkedin.com/in/slassina)")
st.write("💻 GitHub : [Mon GitHub](https://github.com/Sanou-Lassina)")
