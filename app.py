import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
# MÓDULO 2
# -----------------------------
# ============================================================
# MÓDULO 2
# ============================================================

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

    # ========================================================
    # LECTURA DEL DATASET
    # ========================================================

    try:

        df = pd.read_csv(
            archivo,
            sep=";"
        )

    except Exception as e:

        st.error(
            f"❌ Ocurrió un error al cargar el archivo: {e}"
        )

        st.stop()

    # ========================================================
    # VALIDACIÓN DEL DATASET
    # ========================================================

    if df.empty:

        st.error(
            "❌ El archivo fue cargado, pero no contiene datos."
        )

        st.stop()

    st.success(
        "✅ El archivo fue cargado correctamente."
    )

    # ========================================================
    # VISTA PREVIA
    # ========================================================

    st.subheader("Vista previa del dataset")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # ========================================================
    # DIMENSIONES
    # ========================================================

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

    # ========================================================
    # CREAR ANALIZADOR
    # ========================================================

    analyzer = DataAnalyzer(df)

    # ========================================================
    # CLASIFICACIÓN
    # ========================================================

    numericas, categoricas = analyzer.classify_variables()

    # ========================================================
    # TABS
    # ========================================================

    tabs = st.tabs([
        "1. Información general",
        "2. Clasificación",
        "3. Estadísticas",
        "4. Valores faltantes",
        "5. Variables numéricas",
        "6. Variables categóricas",
        "7. Numérica vs categórica",
        "8. Categórica vs categórica",
        "9. Análisis dinámico",
        "10. Hallazgos clave"
    ])

    # ========================================================
    # ÍTEM 1
    # ========================================================

    with tabs[0]:

        st.header(
            "Ítem 1: Información general del dataset"
        )

        st.markdown("""
        Este apartado permite conocer la estructura del dataset,
        los tipos de datos y la existencia de valores nulos.
        """)

        info_df = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de dato": df.dtypes.astype(str),
            "Valores no nulos": df.notnull().sum(),
            "Valores nulos": df.isnull().sum()
        })

        st.dataframe(
            info_df,
            use_container_width=True
        )

        st.subheader("Resumen del dataset")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Filas",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Columnas",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Valores nulos",
                int(df.isnull().sum().sum())
            )

    # ========================================================
    # ÍTEM 2
    # ========================================================

    with tabs[1]:

        st.header(
            "Ítem 2: Clasificación de variables"
        )

        st.markdown("""
        Las variables se clasifican automáticamente en numéricas
        y categóricas mediante una función personalizada.
        """)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Variables numéricas")

            st.metric(
                "Cantidad",
                len(numericas)
            )

            for variable in numericas:
                st.write("•", variable)

        with col2:

            st.subheader("Variables categóricas")

            st.metric(
                "Cantidad",
                len(categoricas)
            )

            for variable in categoricas:
                st.write("•", variable)

    # ========================================================
    # ÍTEM 3
    # ========================================================

    with tabs[2]:

        st.header(
            "Ítem 3: Estadísticas descriptivas"
        )

        st.dataframe(
            analyzer.descriptive_statistics(),
            use_container_width=True
        )

        st.subheader(
            "Media, mediana y moda"
        )

        variable = st.selectbox(
            "Seleccione una variable numérica:",
            numericas,
            key="estadistica"
        )

        media = df[variable].mean()
        mediana = df[variable].median()
        moda = analyzer.mode(variable)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Media",
                f"{media:.2f}"
            )

        with col2:
            st.metric(
                "Mediana",
                f"{mediana:.2f}"
            )

        with col3:
            st.metric(
                "Moda",
                f"{moda:.2f}"
            )

    # ========================================================
    # ÍTEM 4
    # ========================================================

    with tabs[3]:

        st.header(
            "Ítem 4: Análisis de valores faltantes"
        )

        faltantes = analyzer.missing_values()

        faltantes_df = pd.DataFrame({
            "Variable": faltantes.index,
            "Valores faltantes": faltantes.values
        })

        faltantes_df = faltantes_df[
            faltantes_df["Valores faltantes"] > 0
        ]

        if faltantes_df.empty:

            st.success(
                "✅ El dataset no presenta valores faltantes."
            )

        else:

            st.dataframe(
                faltantes_df,
                use_container_width=True
            )

            fig, ax = plt.subplots()

            ax.bar(
                faltantes_df["Variable"],
                faltantes_df["Valores faltantes"]
            )

            ax.set_title(
                "Valores faltantes por variable"
            )

            ax.set_xlabel("Variable")
            ax.set_ylabel("Cantidad")

            plt.xticks(rotation=45)

            st.pyplot(fig)

    # ========================================================
    # ÍTEM 5
    # ========================================================

    with tabs[4]:

        st.header(
            "Ítem 5: Distribución de variables numéricas"
        )

        variable_hist = st.selectbox(
            "Seleccione una variable:",
            numericas,
            key="histograma"
        )

        st.pyplot(
            analyzer.histogram(variable_hist)
        )

        st.markdown(f"""
        **Interpretación:** El histograma permite observar la
        distribución de **{variable_hist}**, identificando
        concentración, dispersión y posibles valores extremos.
        """)

    # ========================================================
    # ÍTEM 6
    # ========================================================

    with tabs[5]:

        st.header(
            "Ítem 6: Análisis de variables categóricas"
        )

        variable_cat = st.selectbox(
            "Seleccione una variable categórica:",
            categoricas,
            key="categorica"
        )

        conteos = df[variable_cat].value_counts()

        proporciones = (
            df[variable_cat]
            .value_counts(normalize=True) * 100
        )

        tabla_cat = pd.DataFrame({
            "Conteo": conteos,
            "Proporción (%)": proporciones.round(2)
        })

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Conteos")

            st.dataframe(
                tabla_cat,
                use_container_width=True
            )

        with col2:

            st.subheader("Gráfico")

            st.pyplot(
                analyzer.bar_chart(variable_cat)
            )

    # ========================================================
    # ÍTEM 7
    # ========================================================

    with tabs[6]:

        st.header(
            "Ítem 7: Análisis bivariado — numérica vs categórica"
        )

        variable_num = st.selectbox(
            "Seleccione una variable numérica:",
            numericas,
            key="bivariado_num"
        )

        grupo = df.groupby("y")[variable_num].agg(
            ["mean", "median"]
        )

        grupo.columns = [
            "Media",
            "Mediana"
        ]

        st.dataframe(
            grupo,
            use_container_width=True
        )

        fig, ax = plt.subplots()

        df.boxplot(
            column=variable_num,
            by="y",
            ax=ax
        )

        ax.set_title(
            f"{variable_num} vs y"
        )

        ax.set_xlabel(
            "Resultado de la campaña"
        )

        ax.set_ylabel(
            variable_num
        )

        plt.suptitle("")

        st.pyplot(fig)

    # ========================================================
    # ÍTEM 8
    # ========================================================

    with tabs[7]:

        st.header(
            "Ítem 8: Análisis bivariado — categórica vs categórica"
        )

        variable_cat_biv = st.selectbox(
            "Seleccione una variable categórica:",
            categoricas,
            key="bivariado_cat"
        )

        tabla_cruzada = pd.crosstab(
            df[variable_cat_biv],
            df["y"],
            normalize="index"
        ) * 100

        st.dataframe(
            tabla_cruzada.round(2),
            use_container_width=True
        )

        fig, ax = plt.subplots()

        tabla_cruzada.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            f"{variable_cat_biv} vs y"
        )

        ax.set_xlabel(
            variable_cat_biv
        )

        ax.set_ylabel(
            "Proporción (%)"
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    # ========================================================
    # ÍTEM 9
    # ========================================================

    with tabs[8]:

        st.header(
            "Ítem 9: Análisis basado en parámetros seleccionados"
        )

        col1, col2 = st.columns(2)

        with col1:

            variables_seleccionadas = st.multiselect(
                "Seleccione variables numéricas:",
                numericas,
                default=numericas[:3]
            )

        with col2:

            categoria_filtro = st.selectbox(
                "Seleccione una variable categórica:",
                categoricas,
                key="filtro_categoria"
            )

        max_categorias = min(
            10,
            df[categoria_filtro].nunique()
        )

        cantidad_categorias = st.slider(
            "Número de categorías a mostrar:",
            min_value=2,
            max_value=max_categorias,
            value=min(5, max_categorias)
        )

        mostrar_datos = st.checkbox(
            "Mostrar tabla de datos filtrados"
        )

        categorias_filtro = (
            df[categoria_filtro]
            .value_counts()
            .head(cantidad_categorias)
            .index
        )

        df_filtrado = df[
            df[categoria_filtro].isin(categorias_filtro)
        ]

        if variables_seleccionadas:

            st.subheader(
                "Estadísticas del análisis seleccionado"
            )

            st.dataframe(
                df_filtrado[
                    variables_seleccionadas
                ].describe(),
                use_container_width=True
            )

            st.subheader(
                "Promedios por categoría"
            )

            resumen = df_filtrado.groupby(
                categoria_filtro
            )[variables_seleccionadas].mean()

            st.dataframe(
                resumen.round(2),
                use_container_width=True
            )

        else:

            st.warning(
                "Seleccione al menos una variable numérica."
            )

        if mostrar_datos:

            st.subheader(
                "Datos filtrados"
            )

            st.dataframe(
                df_filtrado,
                use_container_width=True
            )

    # ========================================================
    # ÍTEM 10
    # ========================================================

    with tabs[9]:

        st.header(
            "Ítem 10: Hallazgos clave"
        )

        total_clientes = len(df)

        clientes_si = (
            df["y"]
            .value_counts()
            .get("yes", 0)
        )

        tasa_conversion = (
            clientes_si / total_clientes * 100
        )

        edad_promedio = df["age"].mean()

        duracion_promedio = df["duration"].mean()

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total de clientes",
                f"{total_clientes:,}"
            )

        with col2:

            st.metric(
                "Aceptaron",
                f"{clientes_si:,}"
            )

        with col3:

            st.metric(
                "Tasa de aceptación",
                f"{tasa_conversion:.2f}%"
            )

        with col4:

            st.metric(
                "Edad promedio",
                f"{edad_promedio:.1f}"
            )

        st.subheader(
            "Distribución del resultado"
        )

        resultado = df["y"].value_counts()

        fig, ax = plt.subplots()

        resultado.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Resultado de la campaña"
        )

        ax.set_xlabel("Resultado")
        ax.set_ylabel("Número de clientes")

        plt.xticks(rotation=0)

        st.pyplot(fig)

        st.subheader(
            "Insights principales"
        )

        st.markdown(f"""
        ### 🔎 Hallazgo 1

        El dataset contiene **{total_clientes:,} registros** y
        **{df.shape[1]} variables**.

        ### 🔎 Hallazgo 2

        La tasa general de aceptación de la campaña es de
        aproximadamente **{tasa_conversion:.2f}%**.

        ### 🔎 Hallazgo 3

        La edad promedio de los clientes es de aproximadamente
        **{edad_promedio:.1f} años**.

        ### 🔎 Hallazgo 4

        La duración promedio de las llamadas es de aproximadamente
        **{duracion_promedio:.1f} segundos**.

        ### 🔎 Hallazgo 5

        El análisis bivariado permite observar diferencias entre
        los clientes que aceptaron y los que no aceptaron la oferta.
        """)
