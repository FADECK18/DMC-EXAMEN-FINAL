import streamlit as st
import pandas as pd
import io


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
        El dataset Bank Marketing contiene información relacionada con
        campañas de marketing telefónico de una institución bancaria.
        Los datos permiten analizar características de los clientes,
        información relacionada con las campañas y el resultado final
        de la campaña.
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

    st.title("📊 Módulo 2: Carga del Dataset")

    st.write(
        """
        En este módulo se realiza la carga del dataset BankMarketing.csv,
        la validación del archivo, la visualización de los datos y la
        identificación de sus dimensiones.
        """
    )

    st.divider()

    # ========================================================
    # CARGA DEL DATASET
    # ========================================================

    st.header("📂 Carga del dataset")

    archivo = st.file_uploader(
        "Seleccione el archivo BankMarketing.csv",
        type=["csv"]
    )


    # ========================================================
    # VALIDACIÓN DEL ARCHIVO
    # ========================================================

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

        # IMPORTANTE:
        # Detiene la ejecución del módulo.
        # Por lo tanto, el EDA NO se ejecutará.
        st.stop()


    # ========================================================
    # LECTURA DEL DATASET
    # ========================================================

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


    # ========================================================
    # VALIDACIÓN DEL DATASET
    # ========================================================

    if df.empty:

        st.error(
            "❌ El archivo fue cargado, pero no contiene datos."
        )

        st.stop()


    # ========================================================
    # INFORMACIÓN DEL DATASET
    # ========================================================

    st.header("📋 Información del dataset")

    st.write(
        f"""
        El dataset contiene **{df.shape[0]:,} filas** y
        **{df.shape[1]} columnas**.
        """
    )


    # ========================================================
    # VISTA COMPLETA DEL DATASET
    # ========================================================

    st.header("👀 Vista completa del dataset")

    st.write(
        """
        La siguiente tabla permite visualizar todas las filas y
        todas las columnas del dataset. Utilice las barras de
        desplazamiento para recorrer la información.
        """
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=600
    )


    # ========================================================
    # DIMENSIONES DEL DATASET
    # ========================================================

    st.header("📏 Dimensiones del dataset")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Número de filas",
            f"{df.shape[0]:,}"
        )

    with col2:

        st.metric(
            "Número de columnas",
            df.shape[1]
        )


    # ========================================================
    # INFORMACIÓN DEL ARCHIVO
    # ========================================================

    st.header("ℹ️ Información del archivo")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Nombre del archivo:**")
        st.write(archivo.name)

    with col2:

        st.write("**Tamaño del archivo:**")
        st.write(
            f"{archivo.size / 1024:.2f} KB"
        )


    # ========================================================
    # ANÁLISIS EXPLORATORIO DE DATOS (EDA)
    # ========================================================

    st.divider()

    st.title("🔎 Análisis Exploratorio de Datos (EDA)")

    st.write(
        """
        En esta sección se realiza un análisis exploratorio del dataset
        Bank Marketing. El objetivo es conocer la estructura, los tipos
        de variables, las estadísticas descriptivas y la presencia de
        valores faltantes.
        """
    )


    # ========================================================
    # FUNCIÓN PERSONALIZADA PARA CLASIFICAR VARIABLES
    # ========================================================

    def clasificar_variables(dataframe):
        """
        Clasifica las variables del DataFrame en numéricas
        y categóricas.
        """

        variables_numericas = dataframe.select_dtypes(
            include=["number"]
        ).columns.tolist()

        variables_categoricas = dataframe.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        return variables_numericas, variables_categoricas


    # ========================================================
    # CLASIFICACIÓN DE VARIABLES
    # ========================================================

    variables_numericas, variables_categoricas = (
        clasificar_variables(df)
    )


    # ========================================================
    # TABS DEL EDA
    # ========================================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Ítem 1: Información general",
            "🔢 Ítem 2: Clasificación de variables",
            "📊 Ítem 3: Estadísticas descriptivas",
            "⚠️ Ítem 4: Valores faltantes"
        ]
    )


    # ========================================================
    # ÍTEM 1: INFORMACIÓN GENERAL DEL DATASET
    # ========================================================

    with tab1:

        st.header(
            "📋 Ítem 1: Información general del dataset"
        )

        st.write(
            """
            En este apartado se presenta información general sobre
            la estructura del dataset, incluyendo los tipos de datos
            y la cantidad de valores nulos.
            """
        )


        # ----------------------------------------------------
        # .info()
        # ----------------------------------------------------

        st.subheader("ℹ️ Información mediante .info()")

        buffer = io.StringIO()

        df.info(
            buf=buffer
        )

        st.text(
            buffer.getvalue()
        )


        # ----------------------------------------------------
        # TIPOS DE DATOS
        # ----------------------------------------------------

        st.subheader("🔤 Tipos de datos")

        tipos_datos = pd.DataFrame(
            {
                "Variable": df.columns,
                "Tipo de dato": df.dtypes.astype(str).values
            }
        )

        st.dataframe(
            tipos_datos,
            use_container_width=True
        )


        # ----------------------------------------------------
        # VALORES NULOS
        # ----------------------------------------------------

        st.subheader("⚠️ Conteo de valores nulos")

        valores_nulos = df.isnull().sum()

        tabla_nulos = pd.DataFrame(
            {
                "Variable": valores_nulos.index,
                "Valores nulos": valores_nulos.values
            }
        )

        st.dataframe(
            tabla_nulos,
            use_container_width=True
        )


        # ----------------------------------------------------
        # RESUMEN
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Filas",
                f"{df.shape[0]:,}"
            )

        with col2:

            st.metric(
                "Columnas",
                df.shape[1]
            )


    # ========================================================
    # ÍTEM 2: CLASIFICACIÓN DE VARIABLES
    # ========================================================

    with tab2:

        st.header(
            "🔢 Ítem 2: Clasificación de variables"
        )

        st.write(
            """
            Las variables del dataset se clasifican automáticamente
            en variables numéricas y categóricas mediante una función
            personalizada desarrollada en Python.
            """
        )


        # ----------------------------------------------------
        # COLUMNAS
        # ----------------------------------------------------

        col1, col2 = st.columns(2)


        # ----------------------------------------------------
        # VARIABLES NUMÉRICAS
        # ----------------------------------------------------

        with col1:

            st.subheader(
                "🔢 Variables numéricas"
            )

            st.metric(
                "Cantidad",
                len(variables_numericas)
            )

            for variable in variables_numericas:

                st.write(
                    f"• {variable}"
                )


        # ----------------------------------------------------
        # VARIABLES CATEGÓRICAS
        # ----------------------------------------------------

        with col2:

            st.subheader(
                "🔤 Variables categóricas"
            )

            st.metric(
                "Cantidad",
                len(variables_categoricas)
            )

            for variable in variables_categoricas:

                st.write(
                    f"• {variable}"
                )


        # ----------------------------------------------------
        # RESUMEN DE CLASIFICACIÓN
        # ----------------------------------------------------

        st.subheader(
            "📊 Resumen de clasificación"
        )

        resumen_variables = pd.DataFrame(
            {
                "Tipo de variable": [
                    "Numéricas",
                    "Categóricas"
                ],
                "Cantidad": [
                    len(variables_numericas),
                    len(variables_categoricas)
                ]
            }
        )

        st.dataframe(
            resumen_variables,
            use_container_width=True
        )

        st.bar_chart(
            resumen_variables.set_index(
                "Tipo de variable"
            )
        )


    # ========================================================
    # ÍTEM 3: ESTADÍSTICAS DESCRIPTIVAS
    # ========================================================

    with tab3:

        st.header(
            "📊 Ítem 3: Estadísticas descriptivas"
        )

        st.write(
            """
            Las estadísticas descriptivas permiten resumir el
            comportamiento de las variables numéricas. Se consideran
            medidas como la media, mediana, mínimo, máximo y dispersión.
            """
        )


        # ----------------------------------------------------
        # .describe()
        # ----------------------------------------------------

        st.subheader(
            "📈 Estadísticas mediante .describe()"
        )

        estadisticas = df[
            variables_numericas
        ].describe()

        st.dataframe(
            estadisticas,
            use_container_width=True
        )


        # ----------------------------------------------------
        # SELECCIÓN DE VARIABLE
        # ----------------------------------------------------

        st.subheader(
            "🔍 Análisis de una variable"
        )

        variable = st.selectbox(
            "Seleccione una variable numérica:",
            variables_numericas
        )


        # ----------------------------------------------------
        # CÁLCULOS
        # ----------------------------------------------------

        media = df[variable].mean()

        mediana = df[variable].median()

        minimo = df[variable].min()

        maximo = df[variable].max()

        desviacion = df[variable].std()


        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Media",
                f"{media:,.2f}"
            )

        with col2:

            st.metric(
                "Mediana",
                f"{mediana:,.2f}"
            )

        with col3:

            st.metric(
                "Desviación estándar",
                f"{desviacion:,.2f}"
            )


        # ----------------------------------------------------
        # INTERPRETACIÓN
        # ----------------------------------------------------

        st.subheader(
            "📝 Interpretación básica"
        )

        st.write(
            f"""
            Para la variable **{variable}**, la media es de
            **{media:,.2f}**, mientras que la mediana es de
            **{mediana:,.2f}**.

            La desviación estándar es de **{desviacion:,.2f}**,
            lo que permite evaluar el nivel de dispersión de los datos.

            El valor mínimo observado es **{minimo:,.2f}** y el
            valor máximo es **{maximo:,.2f}**.
            """
        )


    # ========================================================
    # ÍTEM 4: ANÁLISIS DE VALORES FALTANTES
    # ========================================================

    with tab4:

        st.header(
            "⚠️ Ítem 4: Análisis de valores faltantes"
        )

        st.write(
            """
            En este apartado se analiza la cantidad de valores
            faltantes existentes en cada variable del dataset.
            """
        )


        # ----------------------------------------------------
        # CONTEO
        # ----------------------------------------------------

        valores_nulos = df.isnull().sum()

        total_nulos = valores_nulos.sum()


        # ----------------------------------------------------
        # MÉTRICAS
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total de valores faltantes",
                f"{total_nulos:,}"
            )

        with col2:

            st.metric(
                "Variables con valores faltantes",
                int(
                    (valores_nulos > 0).sum()
                )
            )


        # ----------------------------------------------------
        # TABLA
        # ----------------------------------------------------

        tabla_faltantes = pd.DataFrame(
            {
                "Variable": valores_nulos.index,
                "Valores faltantes": valores_nulos.values
            }
        )

        st.dataframe(
            tabla_faltantes,
            use_container_width=True
        )


        # ----------------------------------------------------
        # VISUALIZACIÓN
        # ----------------------------------------------------

        st.subheader(
            "📊 Visualización de valores faltantes"
        )

        faltantes_grafico = valores_nulos[
            valores_nulos > 0
        ]


        if len(faltantes_grafico) > 0:

            st.bar_chart(
                faltantes_grafico
            )

        else:

            st.success(
                "✅ El dataset no contiene valores faltantes."
            )


        # ----------------------------------------------------
        # DISCUSIÓN
        # ----------------------------------------------------

        st.subheader(
            "📝 Discusión"
        )


        if total_nulos == 0:

            st.write(
                """
                El dataset no presenta valores faltantes. Esto significa
                que no es necesario aplicar técnicas de imputación o
                eliminación de registros debido a datos ausentes.
                """
            )

        else:

            st.write(
                f"""
                Se identificaron **{total_nulos:,} valores faltantes**
                distribuidos en **{int((valores_nulos > 0).sum())} variables**.

                Antes de realizar análisis posteriores, sería conveniente
                evaluar la causa de estos valores faltantes y determinar
                si corresponde imputarlos, eliminarlos o mantenerlos.
                """
            )
