import streamlit as st

st.sidebar.title("Módulo")

st.sidebar.image("IMAGEN DMC.png", width=100)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    ["Home", "Modulo 1", "Modulo 2", "Modulo 3"])

if modulos == "Home":

    st.markdown("<h1 align='center'>APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON UTILIZANDO STREAMLIT</h1>", unsafe_allow_html=True)

    st.subheader("Nombre completo del estudiante")
    st.markdown("Farid Estefano Garibay Fabian")

    st.subheader("Nombre del módulo")
    st.markdown("Python Fundamentals")

    st.subheader("Información general del estudiante")
    st.markdown("Soy contador y busco especializarme en análisis de datos para combinar mi experiencia financiera con nuevas herramientas tecnológicas y así potenciar mi perfil profesional.")

    st.subheader("Año")
    st.markdown("2026")

    st.subheader("Breve descripción del proyecto")
    st.markdown("El proyecto facilita la aplicación práctica de lo aprendido en clase, consolidando los contenidos del primer módulo de Python Fundamentals.")

    st.subheader("Tecnologías utilizadas")
    st.markdown("Python, Streamlit y GitHub.")
