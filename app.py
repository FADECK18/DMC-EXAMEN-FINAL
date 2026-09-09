import streamlit as st
import pandas as pd


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Módulos")

st.sidebar.image(
    "IMAGEN DMC.png",
    width=100
)

modulos = st.sidebar.selectbox(
    "Seleccione un módulo:",
    [
        "Modulo 1: Home",
        "Modulo 2: Carga del dataset"
    ]
)


# ============================================================
# MÓDULO 1: HOME
# ============================================================

if modulos == "Modulo 1: Home":

    st.markdown(
        """
        <h1 style="text-align: center;">
        APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON
        UTILIZANDO STREAMLIT
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------------------------------------
    # OBJETIVO DEL PROYECTO
    # --------------------------------------------------------

    st.subheader("🎯 Objetivo del proyecto")

    st.write(
        """
        El objetivo del proyecto es aplicar los conocimientos adquiridos
        durante el curso de Python Fundamentals para explorar, organizar
        y analizar un conjunto de datos mediante herramientas de Python.
        """
    )

    # --------------------------------------------------------
    # INFORMACIÓN DEL AUTOR
    # --------------------------------------------------------

    st.subheader("👤 Datos del autor")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Nombre completo**")
        st.write("Farid Estefano Garibay Fabian")

    with col2:
        st.write("**Curso / Especialización**")
        st.write("Python Fundamentals")

    with col3:
        st.write("**Año**")
        st.write("2026")

    # --------------------------------------------------------
    # EXPLICACIÓN DEL DATASET
    # --------------------------------------------------------

    st.subheader("📊 Breve explicación del dataset")

    st.write(
        """
        El análisis del dataset permitirá organizar la información,
        identificar características relevantes de los datos y obtener
        resultados que serán presentados de manera clara e interactiva
        mediante Streamlit.
        """
    )

    # --------------------------------------------------------
    # TECNOLOGÍAS UTILIZADAS
    # --------------------------------------------------------

    st.subheader("🛠️ Tecnologías utilizadas")

    st.markdown(
        """
        - **Python:** lenguaje de programación utilizado para desarrollar
          el proyecto.
          
        - **Pandas:** biblioteca utilizada para la manipulación y análisis
          de los datos.
          
        - **Streamlit:** herramienta utilizada para crear la aplicación
          web interactiva.
          
        - **GitHub:** plataforma utilizada para almacenar y gestionar
          el código del proyecto.
        """
    )


# ============================================================
# MÓDULO 2: CARGA DEL DATASET
# ============================================================

elif modulos == "Modulo 2: Carga del dataset":

    st.title(
        "📊 Módulo 2: Carga del Dataset"
    )

    st.write(
        """
        En este módulo se realiza la carga del dataset BankMarketing.csv,
        la validación del archivo, una vista previa de los datos y la
        identificación de sus dimensiones.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # CARGA DEL DATASET
    # --------------------------------------------------------

    st.header("📂 Carga del dataset")

    archivo = st.file_uploader(
        "Seleccione el archivo BankMarketing.csv",
        type=["csv"]
    )

    # --------------------------------------------------------
    # VALIDACIÓN DEL ARCHIVO
    # --------------------------------------------------------

    if archivo is None:

        st.warning(
            "⚠️ Debe cargar un archivo CSV para comenzar."
        )

        st.info(
            """
            Ningún análisis será ejecutado hasta que el archivo
            haya sido cargado correctamente.
            """
        )

        st.stop()

    # --------------------------------------------------------
    # LECTURA DEL DATASET
    # --------------------------------------------------------

    try:

        df = pd.read_csv(
            archivo,
            sep=";"
        )

        st.success(
            "✅ El archivo fue cargado correctamente."
        )

    except Exception as e:

        st.error(
            f"❌ Ocurrió un error al cargar el archivo: {e}"
        )

        st.stop()

    # --------------------------------------------------------
    # VALIDACIÓN DEL DATASET
    # --------------------------------------------------------

    if df.empty:

        st.error(
            "❌ El archivo fue cargado, pero no contiene datos."
        )

        st.stop()

    # --------------------------------------------------------
    # VISTA PREVIA DEL DATASET
    # --------------------------------------------------------

    st.header("👀 Vista previa del dataset")

    st.write(
        "A continuación se muestran las primeras 5 filas del dataset:"
    )

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # --------------------------------------------------------
    # DIMENSIONES DEL DATASET
    # --------------------------------------------------------

    st.header("📏 Dimensiones del dataset")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Número de filas",
            df.shape[0]
        )

    with col2:

        st.metric(
            "Número de columnas",
            df.shape[1]
        )

    # --------------------------------------------------------
    # INFORMACIÓN ADICIONAL
    # --------------------------------------------------------

    st.header("ℹ️ Información del archivo")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Nombre del archivo:**")
        st.write(archivo.name)

    with col2:

        st.write("**Tamaño del archivo:**")
        st.write(f"{archivo.size / 1024:.2f} KB")



