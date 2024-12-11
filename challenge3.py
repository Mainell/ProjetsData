import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


# Données utilisateurs permettant d'accéder à la partie réservée


lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',

   'password': 'utilisateurMDP',

   'email': 'utilisateur@gmail.com',

   'failed_login_attemps': 0, # Sera géré automatiquement

   'logged_in': False, # Sera géré automatiquement

   'role': 'utilisateur'},

  'root': {'name': 'root',

   'password': 'rootMDP',

   'email': 'admin@gmail.com',

   'failed_login_attemps': 0, # Sera géré automatiquement

   'logged_in': False, # Sera géré automatiquement

   'role': 'administrateur'}}}


# Données utilisateurs collectées 

authenticator = Authenticate(

    lesDonneesDesComptes, # Les données des comptes

    "cookie name", # Le nom du cookie, un str quelconque

    "cookie key", # La clé du cookie, un str quelconque

    30, # Le nombre de jours avant que le cookie expire 

)

# Préparation de définitions

def accueil():

    st.title("Les fêtes de fin d'année approchent !")


# Fonction d'authentification
authenticator.login()

st.image("poleexpress.jpg")

if st.session_state["authentication_status"]:


    with st.sidebar:
        st.write("Bienvenue petit lutin !!")
        authenticator.logout("Déconnexion")

    option = st.sidebar.selectbox("Dans quel univers souhaitez-vous aller pour les fêtes de fin d'année ?", ["Accueil", "Univers classique", "Envie de plus de magie ?"])

    if option == "Accueil":
        st.write("Te voilà arrivé sur la page d'accueil, bravo !")
        st.write("Envie d'écouter une petite musique de saison ?")

        # Ajout d'un fond sonore
        st.audio("vent.mp3", format="audio/mpeg")

    elif option == "Univers classique":
        st.write("Voici ce qu'il te reste à préparer...")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.header("Une cheminée")

            st.image("https://fitrahma.com/wp-content/uploads/2024/10/28-idees-de-decoration-de-cheminee-de-Noel-ravissantes-pour-une-maison-festive-800x530.jpg")


        with col2:

            st.header("Un sapin")

            st.image("https://disneylandparis-news.com//app/uploads/2024/09/Christmas_Decorations-scaled.jpg")


        with col3:

            st.header("De la tisane, bien sûr !")

            st.image("https://cache.natureetdecouvertes.com/Medias/Images/Articles/92391890/92391890-tisane-de-no-l-bio_1.jpg")

    else:
        st.write("J'étais sûre que tu voudrais aller dans un monde extraordinaire !")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.header("Une surprise ?")

            st.image("https://admin.esports.gg/wp-content/uploads/2024/11/Ekko-and-Powder-Arcane-Season-2-968x544.jpg")


        with col2:

            st.header("Ceci est ton nouvel animal de compagnie!")

            st.image("https://i.pinimg.com/236x/cb/01/f1/cb01f1892cb75693e8afed5b9fb0719d.jpg")


        with col3:

            st.header("Prends-en bien soin <3")

            st.image("https://carolinefaget.fr/wp-content/uploads/2015/12/lumière-noël.jpg")




# Si les champs username et password ne sont pas correctement remplis

elif st.session_state["authentication_status"] is False:

    st.error("Oups ! L'username et/ou le password ne correspondent pas à ce qui est attendu...")


# Si les champs username et password sont restés vides

elif st.session_state["authentication_status"] is None:

    st.warning('Les champs username et mot de passe doivent être remplis pour pouvoir vous emmener dans un voyage inespéré !')