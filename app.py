import streamlit as st
import pandas as pd

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Aplicación Python Fundamentals",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# CARGAR DATASET
# -----------------------------
URL_DATASET = "https://raw.githubusercontent.com/FADECK18/DMC-EXAMEN-FINAL/refs/heads/main/BankMarketing.csv"

try:
    df = pd.read_csv(URL_DATASET)
except Exception as e:
    st.error(f"No se pudo cargar el dataset: {e}")
    st.stop()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Módulo")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Modulo 1", "Modulo 2", "Modulo 3"]
)

# -----------------------------
# HOME
# -----------------------------
if modulos == "Home":

    st.markdown(
        "<h1 align='center'>APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON UTILIZANDO STREAMLIT</h1>",
        unsafe_allow_html=True
    )

    st.subheader("Breve descripción del objetivo del análisis")

    st.markdown("""
    El objetivo del proyecto es aplicar los conocimientos adquiridos
    durante el curso de Python Fundamentals para explorar, organizar
    y analizar un conjunto de datos mediante herramientas de Python.
    """)

    st.subheader("DATOS DEL AUTOR")

    st.markdown("**Nombre completo:**")
    st.markdown("Farid Estefano Garibay Fabian")

    st.markdown("**Curso / Especialización:**")
    st.markdown("Python Fundamentals")

    st.markdown("**Año:**")
    st.markdown("2026")

    st.subheader("Breve explicación del dataset")

    st.markdown("""
    El análisis del dataset permitirá organizar la información, identificar
    características relevantes de los datos y obtener resultados que serán
    presentados de manera clara e interactiva mediante Streamlit.
    """)

    st.subheader("Tecnologías utilizadas")

    st.markdown("""
    - **Python:** lenguaje de programación utilizado para desarrollar el proyecto.
    - **Pandas:** biblioteca utilizada para la manipulación y análisis de los datos.
    - **Streamlit:** herramienta utilizada para crear la aplicación web interactiva.
    - **GitHub:** plataforma utilizada para almacenar y gestionar el código del proyecto.
    """)

# -----------------------------
# MÓDULO 1
# -----------------------------
elif modulos == "Modulo 1":

    st.title("Módulo 1")

    st.subheader("Vista general del dataset")

    st.write("Número de filas:", df.shape[0])
    st.write("Número de columnas:", df.shape[1])

    st.dataframe(df.head())

# -----------------------------
# MÓDULO 2
# -----------------------------
elif modulos == "Modulo 2":

    st.title("Módulo 2")

    st.subheader("Información del dataset")

    st.dataframe(df.describe(include="all"))

# -----------------------------
# MÓDULO 3
# -----------------------------
elif modulos == "Modulo 3":

    st.title("Módulo 3")

    st.subheader("Datos completos")

    st.dataframe(df)
