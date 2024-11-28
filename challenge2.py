# Importation des bibliothèques nécessaires

import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Création du titre

st.title("Manipulation de données et création de graphiques trop sylés")

# Sélection d'un dataset

data_choisi = st.selectbox("Quel dataset veux-tu utiliser ?", ['diamonds', 'flights', 'geyser', 'penguins', 'planets'])

if data_choisi == 'diamonds' :

    diamonds = sns.load_dataset("diamonds")
    df_diam = st.dataframe(diamonds)

    colonne_x = list(diamonds.columns)
    x = st.selectbox("Choisissez une colonne pour l'axe x de votre graphique :", colonne_x)

    colonne_y = list(diamonds.columns)
    y = st.selectbox("Choisissez une colonne pour l'axe y de votre graphique :", colonne_y)

    graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

    if graphique == 'scatter_chart':
        st.scatter_chart(diamonds, x = x, y = y)

    elif graphique == 'line_chart' :
        st.line_chart(diamonds, x = x, y = y)

    elif graphique == 'bar_chart' :
        st.bar_chart(diamonds, x = x, y = y)

    else :
        st.write("Pensez à choisir l'un des types de graphique !")


elif data_choisi == 'flights' :

    flights = sns.load_dataset("flights")
    df_fli = st.dataframe(flights)

    colonne_x = list(flights.columns)
    x = st.selectbox("Choisissez une colonne pour l'axe x de votre graphique :", colonne_x)

    colonne_y = list(flights.columns)
    y = st.selectbox("Choisissez une colonne pour l'axe y de votre graphique :", colonne_y)

    graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

    if graphique == 'scatter_chart':
        st.scatter_chart(flights, x = x, y = y)

    elif graphique == 'line_chart' :
        st.line_chart(flights, x = x, y = y)

    elif graphique == 'bar_chart' :
        st.bar_chart(flights, x = x, y = y)

    else :
        st.write("Pensez à choisir l'un des types de graphique !")

elif data_choisi == 'geyser' :

    geyser = sns.load_dataset("geyser")
    df_gey = st.dataframe(geyser)

    colonne_x = list(geyser.columns)
    x = st.selectbox("Choisissez une colonne pour l'axe x de votre graphique :", colonne_x)

    colonne_y = list(geyser.columns)
    y = st.selectbox("Choisissez une colonne pour l'axe y de votre graphique :", colonne_y)

    graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

    if graphique == 'scatter_chart':
        st.scatter_chart(geyser, x = x, y = y)

    elif graphique == 'line_chart' :
        st.line_chart(geyser, x = x, y = y)

    elif graphique == 'bar_chart' :
        st.bar_chart(geyser, x = x, y = y)

    else :
        st.write("Pensez à choisir l'un des types de graphique !")

elif data_choisi == 'penguins' :

    penguins = sns.load_dataset("penguins")
    df_peng = st.dataframe(penguins)

    colonne_x = list(penguins.columns)
    x = st.selectbox("Choisissez une colonne pour l'axe x de votre graphique :", colonne_x)

    colonne_y = list(penguins.columns)
    y = st.selectbox("Choisissez une colonne pour l'axe y de votre graphique :", colonne_y)

    graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

    if graphique == 'scatter_chart':
        st.scatter_chart(penguins, x = x, y = y)

    elif graphique == 'line_chart' :
        st.line_chart(penguins, x = x, y = y)

    elif graphique == 'bar_chart' :
        st.bar_chart(penguins, x = x, y = y)

    else :
        st.write("Pensez à choisir l'un des types de graphique !")

elif data_choisi == 'planets' :

    planets = sns.load_dataset("planets")
    df_pla = st.dataframe(planets)

    colonne_x = list(planets.columns)
    x = st.selectbox("Choisissez une colonne pour l'axe x de votre graphique :", colonne_x)

    colonne_y = list(planets.columns)
    y = st.selectbox("Choisissez une colonne pour l'axe y de votre graphique :", colonne_y)

    graphique = st.selectbox("Quel graphique veux-tu utiliser ?", ['scatter_chart', 'line_chart', 'bar_chart'])

    if graphique == 'scatter_chart':
        st.scatter_chart(planets, x = x, y = y)

    elif graphique == 'line_chart' :
        st.line_chart(planets, x = x, y = y)

    elif graphique == 'bar_chart' :
        st.bar_chart(planets, x = x, y = y)

    else :
        st.write("Pensez à choisir l'un des types de graphique !")

else:

    st.write("Pensez à choisir l'un des datasets proposé!")

# Ajout d'un bouton pour choisir d'afficher ou non une matrice de corrélation

if st.checkbox("Afficher la matrice de corrélation") :
        diam = st.checkbox("Diamonds")
        fli = st.checkbox("Flights")
        gey = st.checkbox("Geyser")
        peng = st.checkbox("Penguins")
        pla = st.checkbox("Planets")
        st.header("Voici une superbe matrice de corrélation :")
        if diam :
            diamonds = sns.load_dataset("diamonds")
            df_diam = diamonds.select_dtypes(include=['number'])
            if not df_diam.empty :
                corr_matrix = df_diam.corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr_matrix, annot=True)
                st.pyplot(fig)
        elif fli :
            flights = sns.load_dataset("flights")
            df_fli = flights.select_dtypes(include=['number'])
            if not df_fli.empty :
                corr_matrix = df_fli.corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr_matrix, annot=True)
                st.pyplot(fig)
        elif gey :
            geyser = sns.load_dataset("geyser")
            df_gey = geyser.select_dtypes(include=['number'])
            if not df_gey.empty :
                corr_matrix = df_gey.corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr_matrix, annot=True)
                st.pyplot(fig)
        elif peng :
            penguins = sns.load_dataset("penguins")
            df_pen = penguins.select_dtypes(include=['number'])
            if not df_pen.empty :
                corr_matrix = df_pen.corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr_matrix, annot=True)
                st.pyplot(fig)
        elif pla :
            planets = sns.load_dataset("planets")
            df_pla = planets.select_dtypes(include=['number'])
            if not df_pla.empty :
                corr_matrix = df_pla.corr()
                fig, ax = plt.subplots()
                sns.heatmap(corr_matrix, annot=True)
                st.pyplot(fig)
        else :
            st.write("Pensez à choisir l'un des datasets proposés!")


# Ajout d'une photographie jolie

st.image("CadreNoir.jpg")