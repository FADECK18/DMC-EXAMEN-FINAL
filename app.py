import streamlit as st

# Menú lateral
st.sidebar.title("Módulo")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Modulo 1", "Modulo 2", "Modulo 3"]
)

# Módulo Home
if modulos == "Home":

    # Título del proyecto
    st.markdown(
        "<h1 align='center'>APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON UTILIZANDO STREAMLIT</h1>",
        unsafe_allow_html=True
    )

    # Imagen principal
    st.image("IMAGEN PYTHON_N.png")

    # Breve descripción del objetivo del análisis
    st.subheader("Breve descripción del objetivo del análisis")

    st.markdown(
        """
        El objetivo del proyecto es aplicar los conocimientos adquiridos
        durante el curso de Python Fundamentals para explorar, organizar
        y analizar un conjunto de datos mediante herramientas de Python.

        A través del análisis se busca obtener información relevante de los
        datos, identificar patrones y facilitar la interpretación de los
        resultados mediante una aplicación interactiva desarrollada con
        Streamlit.
        """
    )

    # Datos del autor
    st.subheader("DATOS DEL AUTOR")

    st.markdown("**Nombre completo:**")
    st.markdown("Farid Estefano Garibay Fabian")

    st.markdown("**Curso / Especialización:**")
    st.markdown("Python Fundamentals")

    st.markdown("**Año:**")
    st.markdown("2026")

    # Breve explicación del dataset
    st.subheader("Breve explicación del dataset")

    st.markdown(
        """
        El dataset constituye la fuente principal de información utilizada
        para desarrollar el análisis del proyecto. Está compuesto por un
        conjunto de registros y variables que serán explorados y procesados
        utilizando herramientas de Python y Pandas.

        El análisis del dataset permitirá organizar la información, identificar
        características relevantes de los datos y obtener resultados que serán
        presentados de manera clara e interactiva mediante Streamlit.
        """
    )

    # Tecnologías utilizadas
    st.subheader("Tecnologías utilizadas")

    st.markdown(
        """
        - **Python:** lenguaje de programación utilizado para desarrollar el proyecto.
        - **Pandas:** biblioteca utilizada para la manipulación y análisis de los datos.
        - **Streamlit:** herramienta utilizada para crear la aplicación web interactiva.
        - **GitHub:** plataforma utilizada para almacenar y gestionar el código del proyecto.
        """
    )
