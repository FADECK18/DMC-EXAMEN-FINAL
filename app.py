import streamlit as st
import pandas as pd

st.sidebar.title("Módulo")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Modulo 1", "Modulo 2", "Modulo 3"])

if modulos == "Home":

    st.markdown(
        "<h1 align='center'>APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON UTILIZANDO STREAMLIT</h1>",
        unsafe_allow_html=True)

    st.subheader("Breve descripción del objetivo del análisis")

    st.markdown("""El objetivo del proyecto es aplicar los conocimientos adquiridos
        durante el curso de Python Fundamentals para explorar, organizar
        y analizar un conjunto de datos mediante herramientas de Python.""")

    st.subheader("DATOS DEL AUTOR")

    st.markdown("**Nombre completo:**")
    st.markdown("Farid Estefano Garibay Fabian")

    st.markdown("**Curso / Especialización:**")
    st.markdown("Python Fundamentals")

    st.markdown("**Año:**")
    st.markdown("2026")

    st.subheader("Breve explicación del dataset")

    st.markdown("""El análisis del dataset permitirá organizar la información, identificar
        características relevantes de los datos y obtener resultados que serán
        presentados de manera clara e interactiva mediante Streamlit.""")

    st.subheader("Tecnologías utilizadas")

    st.markdown(
        """
        - **Python:** lenguaje de programación utilizado para desarrollar el proyecto.
        - **Pandas:** biblioteca utilizada para la manipulación y análisis de los datos.


elif modulos == "Modulo 2":

    st.title(
        "📊 Módulo 2: Carga del Dataset y Análisis Exploratorio de Datos"
    )

    st.markdown("""
    En este módulo se realiza la carga del dataset y un Análisis
    Exploratorio de Datos (EDA), utilizando herramientas de Python,
    Pandas, Matplotlib y Streamlit.
    """)

    # ========================================================
    # CARGA DEL DATASET
    # ========================================================

    st.header("📂 Carga del dataset")

    archivo = st.file_uploader(
        "Seleccione el archivo BankMarketing.csv",
        type=["csv"]
    )

    # ========================================================
    # VALIDACIÓN
    # ========================================================

    if archivo is None:

        st.warning(
            "⚠️ Debe cargar un archivo CSV para comenzar el análisis."
        )

        st.info("""
        Ningún análisis será ejecutado hasta que el archivo
        haya sido cargado correctamente.
        """)

        st.stop()


        - **Streamlit:** herramienta utilizada para crear la aplicación web interactiva.
        - **GitHub:** plataforma utilizada para almacenar y gestionar el código del proyecto.
        """
    )
