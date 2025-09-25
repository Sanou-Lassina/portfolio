import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import base64

# Configuration de la page
st.set_page_config(
    page_title="Portfolio | Lassina Sanou",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Si vous avez un fichier CSS séparé, décommentez la ligne suivante
# local_css("style.css")

# CSS inline pour la mise en forme
st.markdown("""
<style>
    .main-header {
        font-size: 50px;
        color: #1E88E5;
        text-align: center;
        padding: 20px;
    }
    .section-header {
        font-size: 30px;
        color: #1E88E5;
        border-bottom: 2px solid #1E88E5;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    .project-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        margin-bottom: 20px;
        background-color: white;
    }
    .stProgress > div > div > div > div {
        background-color: #1E88E5;
    }
    .profile-img {
        border-radius: 10%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        margin: 0 auto;
        display: block;
        border: 5px solid #1E88E5;
    }
    .social-icon {
        font-size: 30px;
        margin-right: 15px;
        color: #1E88E5;
    }
    .skill-bar {
        height: 20px;
        background-color: #e0e0e0;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .skill-fill {
        height: 100%;
        border-radius: 10px;
        background-color: #1E88E5;
        text-align: center;
        color: white;
        line-height: 20px;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour charger les images en base64 (pour les projets)
def img_to_bytes(img_path):
    img = Image.open(img_path)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    data_uri = base64.b64encode(buffer.read()).decode()
    return data_uri

# Header principal
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('<h2 class="main-header">👋 BIENVENUE SUR MON PORTFOLIO</h2>', unsafe_allow_html=True)
    st.markdown("### Statisticien, Data Analyst & Data Scientist")
    st.markdown("---")


# Barre latérale pour les informations personnelles
with st.sidebar:
    # Image de profil - utilisation d'une image locale
    try:
        # Remplacez "profile.jpg" par le chemin de votre image
        img = Image.open("profile.jpg")
        
        # Création d'un conteneur centré pour l'image
        with st.container():
            st.image(img, use_container_width=True, caption=" ")
            
    except FileNotFoundError:
        with st.container():
            st.error("Image de profil non trouvée. Veuillez ajouter un fichier 'profile.jpg' dans le répertoire de l'application.")
            st.image("https://via.placeholder.com/200", use_container_width=True, caption="Image manquante")


    st.markdown("# SANOU Lassina")
    st.markdown("*Statisticien, Data Analyst & Data Scientist*")
    st.markdown("---")
    
    st.markdown("## 📞 Contact")
    st.markdown("- 📧 slassina92@gmail.com")
    st.markdown("- 📱 (+226) 74544113 / 62972111")
    
    st.markdown("## 🔗 Social")
    st.markdown('<div class="social-icon">', unsafe_allow_html=True)
    st.markdown('[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](www.linkedin.com/in/slassina)')
    st.markdown('[![GitHub](https://img.icons8.com/ios-glyphs/48/000000/github.png)](https://github.com/Sanou-Lassina/)')
    st.markdown('[![Facebook](https://img.icons8.com/color/48/000000/facebook.png)](https://www.facebook.com/lassina.sanou.56)')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("## 📊 Compétences")
    skills = {
        "Python": 90,
        "R": 90,
        "SQL": 75,
        "STATA": 80,
        "SPSS": 80,
        "Power Bi": 95,
        "TABLEAU": 75,
        "Excel Avancé": 95,
        "Vusialisation": 90,
        "Machine Learning": 80,
        "Streamlit": 70,
    }
    
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level)

# Section À propos
st.markdown('<h2 class="section-header">À propos de moi</h2>', unsafe_allow_html=True)
about_me = """
Je suis un **Statisticien, Data Analyst et Data Scientist** passionné avec 
2 ans d'expérience dans le traitement, analysse et visualisation des 
données. Ma mission principale en tant que data analyse et data scientist 
est d’exploiter les données massives (big data) afin d’en extraire des 
informations pertinentes pour aider à la prise de décision stratégique. 
J’analyse, modélise et interprète des données complexes à l’aide de 
techniques statistiques avancées, d’apprentissage automatique 
(machine learning) et de visualisation par tableaux de bord.

Mes compétences techniques incluent **Python, R, Stata, SQL** pour la Data 
Science et aussin en **Excel Avancé, Power Bi, Tableau, SPSS, Sphinx, 
EpiInfo** pour la Data Analyst par visualisation à travers les tableaux de 
bords dynamiques et interactives.

J’ai également une solide expérience dans l’utilisation des outils modernes 
de suivi et évaluation tels que **KoboToolbox, ODK, DHIS2 et Google Forms**. 
A ces compétences s'ajoute l'administration et la gestion de Bases de 
données avec **MS Access, MySQL, BigQuery et Oracle Database**

Je suis également un debutant dans le déploiement de modèles et la création 
d'applications interactives en **API, Docker, le Clound** ainsi que **Streamlit**.
"""
st.markdown(about_me)



# Section Projets
st.markdown('<h2 class="section-header">Mes trois derniers projets</h2>', unsafe_allow_html=True)

# Projet 1
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        # Utilisation d'une image locale si disponible, sinon placeholder
        try:
            project_img = Image.open("project11.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+11", use_container_width=True)
        
        try:
            project_img = Image.open("project12.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+12", use_container_width=True)
        
        try:
            project_img = Image.open("project13.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+13", use_container_width=True)
        
        try:
            project_img = Image.open("project14.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+14", use_container_width=True)
        

    with col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### Analyse exploratoire et développement d'une plateforme de prévision de la production de céréales au Burkina Faso.")
        st.markdown("L’analyse exploratoire constitue une première étape essentielle, permettant de :\n- Mesurer la corrélation entre les variables climatiques (température, précipitations, humidité, vent, ensoleillement) et les rendements des cultures, afin d’identifier les facteurs les plus déterminants.\n- Détecter les régions à forte variabilité interannuelle, en mettant en évidence les fluctuations de production et les anomalies climatiques au fil des années.\n- Offrir une interface simple, interactive et intuitive, accessible via le web grâce à Streamlit, permettant aux utilisateurs de consulter à la fois les données historiques et les prévisions à venir.")
       
        about_me = """
        **Rrésultats :**
        - **1. Importance de la validation croisée spatiale** : Grâce au GroupKFold, le modèle est évalué en laissant une région entière en dehors à chaque itération. Cela teste vraiment la capacité du modèle à généraliser sur une région jamais vue, ce qui est plus réaliste que la CV classique.
        - **2. Performance globale** : le best_score_ correspond au R² moyen sur les folds. Plus ce score est proche de 1, mieux le modèle explique la variance du rendement. Si le score est négatif, cela signifie que le modèle prédit moins bien qu’une simple moyenne 
        - **3. Interprétation métier** : le modèle apprend à prédire le rendement céréalier (tonne/ha) à partir : du climat (précipitations, température, humidité, vent, ensoleillement), de la superficie cultivée, de l’année (tendance temporelle), et des caractéristiques régionales et types de céréales.
        - **4. Les variables les plus importantes (via feature_importances_ du RandomForest)** vont indiquer quels facteurs influencent le plus la production.
        """
        st.markdown(about_me)

        st.markdown("**Technologies :** \n - Python (Pandas, Scipy, Matplotlib/Seaborn \n - Streamlit")
        st.markdown("[Voir le projet sur Google Colab](https://colab.research.google.com/drive/14Paui8Yf24fTbSfTMSULxlqx-Mem5N74?usp=sharing)")

        if st.button("Lien de la Visualisation" , key="vis1"):
            st.info("⚠️ Cette partie est en cours d'établissement")

        
        st.markdown('</div>', unsafe_allow_html=True)

# Projet 2
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### Modélisation de Préduction pour augmenter le profit d'une campagne marketing.")
        
        about_me = """
        Ce projet s’appuie sur une base de données riche en informations 
        sur le comportement d’achat, les caractéristiques socio-démographiques 
        et l’historique d’interaction des clients avec les campagnes marketing 
        de l’entreprise.
        
        **L’objectif est de construire un modèle prédictif capable d’identifier 
        les clients les plus susceptibles de répondre positivement à une 
        nouvelle offre.**
        
        Une telle approche permet de passer d’un marketing de masse, 
        coûteux et peu efficace, à un marketing ciblé et personnalisé, 
        maximisant ainsi le retour sur investissement (ROI).
        
        En intégrant des variables comme le revenu, la composition 
        familiale, les habitudes de consommation (par produit), les 
        canaux d’achat privilégiés (web, magasin, catalogue), ou encore 
        l’historique de réponse aux campagnes, le modèle permettra de 
        comprendre qui achète, quoi, comment et quand
        """
        st.markdown(about_me)


        st.markdown("**Technologies:** Python, Scikit-learn, Pandas, NumPy, Seaborn, Matplotlib")
        st.markdown("[Voir le projet sur Google Colab](https://colab.research.google.com/drive/1YOmx4uDFggizyO-Y0MvkcuWWYZCEXuZx?usp=sharing)")
        
        if st.button("Lien de la Visualisation" , key="vis2"):
            st.info("⚠️ Cette partie est en cours d'établissement")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        try:
            project_img = Image.open("project21.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+21", use_container_width=True)

        try:
            project_img = Image.open("project22.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+22", use_container_width=True)


# Projet 3
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            project_img = Image.open("projet31.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+31", use_container_width=True)
        
        try:
            project_img = Image.open("projet32.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+32", use_container_width=True)
        
        try:
            project_img = Image.open("projet34.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+34", use_container_width=True)
        
        try:
            project_img = Image.open("projet35.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+35", use_container_width=True)
        
        try:
            project_img = Image.open("projet36.png")
            st.image(project_img, use_container_width=True)
        except FileNotFoundError:
            st.image("https://via.placeholder.com/400x250?text=Projet+36", use_container_width=True)
  
  
    with col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### Clustering et Réduction de Dimensions.")
        about_me = """
        **Contexte**: Une entreprise automobile envisage de pénétrer de nouveaux marchés 
        avec ses produits existants (P1, P2, P3, P4 et P5). Après une étude 
        de marché approfondie, elle a déduit que le comportement du nouveau 
        marché est similaire à celui du marché existant.
        
        Sur leur marché actuel, l'équipe commerciale a classé tous les 
        clients en 4 segments (A, B, C, D). Ensuite, ils ont effectué une 
        approche et une communication segmentées pour un segment différent 
        de clients. Cette stratégie a fonctionné exceptionnellement bien 
        pour eux. Ils prévoient d'utiliser la même stratégie pour les 
        nouveaux marchés et ont identifié plus de 10000 nouveaux clients 
        potentiels.
        
        **Concretement mon projet doit aider le responsable à prédire le 
        bon groupe de nouveaux clients.**
        
        **L'Objectifs** est d'appliquer des techniques de clustering et 
        d'utiliser des techniques de réduction de dimension pour 
        visualiser les clusters en fin d'indentifier les groupes de clients
        par rapport à leur comportement d'achat.
        
        """
        st.markdown(about_me)

        about_me = """
        *RESUME DES RESULTATS* : Trois grands profils de clients ont été 
        identifiés :
        Un groupe dominant (Cluster 0), assez homogène.
        Un groupe différencié (Cluster 1) qui se distingue nettement sur PCA1.
        Un groupe intermédiaire (Cluster 2) qui partage des caractéristiques avec les deux premiers.
        
        **Intérêt business :**
        Cette segmentation permet de mieux cibler les stratégies marketing, 
        les offres commerciales ou encore les actions de fidélisation.
        
        **Par exemple :**
        Cluster 0 : clients “premium” à forte valeur → programmes VIP, 
        fidélisation.
        Cluster 1 : clients “économes” → offres promotionnelles pour les 
        inciter à consommer plus.
        Cluster 2 : clients “intermédiaires” → stratégie hybride pour les 
        faire basculer vers plus de valeur.

        **👉 En résumé**, ce clustering révèle des segments distincts de 
        clientèle, utiles pour adapter les actions commerciales et 
        améliorer la personnalisation des services
        """
        st.markdown(about_me)


        st.markdown("**Technologies:** Python : Scikit-learn (KMeans, PCA), t-SN")
        st.markdown("[Voir le projet sur Google Colab](https://colab.research.google.com/drive/1LcAZeiXJBcQm1tWK3KeBk36PznmCnol1?usp=sharing)")

        if st.button("Lien pour la Visualisation" , key="vis3"):
            st.info("⚠️ Cette partie est en cours d'établissement")

        st.markdown('</div>', unsafe_allow_html=True)


# Section Expérience professionnelle
st.markdown('<h2 class="section-header">Expérience Professionnelle</h2>', unsafe_allow_html=True)

exp_data = {
    "Poste": ["Stagiaire en Data Analyst", "Stagiaire Statisticien Data Analyst", "Stagiaire Gestion de base de données", "Étudiant stagiaire"],
    "Entreprise": ["Africa Data Entry", "Direction des Statistiques Sectorielles et de l'Evaluation", "Centre Médicale de DO", "INERA DRREA"],
    "Période": ["Depuis Avril 2025", "Aout 2024 à Fevrier 2025", "Aout à Septembre 2022", "2017 à 2018"],
    "Description": [
        "Dans le cadre de ce stage au sein de l’entreprise Africa Data Entry, je suis chargé d’exploiter et d’analyser des bases de données issues de divers projets de collecte d’informations socio-économiques et sur les données agricoles d’assurer le nettoyage, le traitement et la structuration des données à l’aide, en vue de produire des analyses statistiques descriptives et inférentielles pertinentes pour l’aide à la décision et développer des modèles prédictifs pour visualiser les indicateurs clés de performance (KPI).",
        "Dans le cadre de ce stage de Master 2 en Statistique Appliquée à la Direction des Statistiques Sectorielles et de l'Évaluation du Ministère de la Santé, j’ai contribué à l’exploitation, à l’analyse et à la valorisation des données sanitaires nationales. Mes missions ont porté sur le nettoyage, la structuration et l’analyse de données issues des systèmes d’information sanitaire en vue de produire des indicateurs statistiques fiables pour le suivi-évaluation des politiques de santé publique.",
        "En tant que stagiaire en gestion de base de données au Centre Médical de DO, j’ai été chargé de la mise à jour, de la structuration et de la sécurisation et la saisie des données médicales à l’aide du logiciel Microsoft Access. Concevoir et optimiser des bases de données pour la gestion des dossiers patients, des consultations et des traitements.",
        "L’analyse de l’impact des mauvaises herbes sur les rendements des cultures agricoles. Participer à la collecte de données sur le terrain, à leur saisie, puis à leur traitement statistique à l’aide des logiciels Excel, SPSS et R. Contribué au nettoyage et à l’organisation des bases de données expérimentales, réalisé des analyses descriptives et comparatives pour évaluer l’effet de différents types de mauvaises herbes sur la croissance des cultures."
    ]
}


# Vérification que tous les tableaux ont la même longueur
lengths = [len(v) for v in exp_data.values()]
if len(set(lengths)) != 1:
    st.error("Erreur: Les tableaux de données d'expérience professionnelle n'ont pas la même longueur!")
else:
    df_exp = pd.DataFrame(exp_data)
    st.table(df_exp)


# Section Formation
st.markdown('<h2 class="section-header">Formation</h2>', unsafe_allow_html=True)

education_data = {
    "Diplôme": ["Master en Statistique Appliquée et Aide à la Décision", "Licence en Statistique Informatique", "Baccalauréat série D", "Certificat d'expertise en gestion des projets", "Certificat d'expertise en suivi et évaluation"],
    "Établissement": ["Université NAZI BONI de Bobo Dioulasso", "Université NAZI BONI de Bobo Dioulasso", "Collège Evangélique", "CESAR EXPERTISE à Ouagadougou", "CESAR EXPERTISE à Ouagadougou"],
    "Année": ["2020 - 2023", "2015 - 2019", "2013 - 2014", "Avril - Juin 2023", "Février - Avril 2023"]
}


# Vérification que tous les tableaux ont la même longueur
lengths = [len(v) for v in education_data.values()]
if len(set(lengths)) != 1:
    st.error("Erreur: Les tableaux de données de formation n'ont pas la même longueur!")
else:
    df_edu = pd.DataFrame(education_data)
    st.table(df_edu)


# Section Contact
st.markdown('<h2 class="section-header">Me laisser un message</h2>', unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/slassina92@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Votre nom" required>
     <input type="email" name="email" placeholder="Votre email" required>
     <textarea name="message" placeholder="Votre message" required></textarea>
     <button type="submit">Envoyer</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# CSS pour le formulaire de contact
st.markdown("""
<style>
input[type=text], input[type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
}

button[type=submit] {
    background-color: #1E88E5;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button[type=submit]:hover {
    background-color: #0D47A1;
}
</style>
""", unsafe_allow_html=True)

# Pied de page
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>© 2025 SANOU Lassina - Tous droits réservés</div>", unsafe_allow_html=True)