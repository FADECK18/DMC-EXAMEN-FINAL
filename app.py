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

    # ============================================================
    # ÍTEMS 5 AL 10 DEL ANÁLISIS EXPLORATORIO DE DATOS
    # ============================================================

    st.divider()

    tab5, tab6, tab7 = st.tabs(
        [
            "📈 Ítem 5: Variables numéricas",
            "📊 Ítem 6: Variables categóricas",
            "🔗 Ítem 7: Numérico vs categórico"
        ]
    )

    tab8, tab9, tab10 = st.tabs(
        [
            "🔗 Ítem 8: Categórico vs categórico",
            "🎛️ Ítem 9: Análisis por parámetros",
            "💡 Ítem 10: Hallazgos clave"
        ]
    )


    # ============================================================
    # ÍTEM 5
    # ============================================================

    with tab5:

        st.header("📈 Ítem 5: Distribución de variables numéricas")

        st.write(
            """
            En este apartado se analiza la distribución de las variables
            numéricas mediante histogramas. Los histogramas permiten
            observar la concentración de los datos, su dispersión y la
            posible presencia de valores extremos o distribuciones
            asimétricas.
            """
        )

        st.subheader("📊 Selección de variables")

        variables_numericas_seleccionadas = st.multiselect(
            "Seleccione una o más variables numéricas:",
            variables_numericas,
            default=variables_numericas[:3]
        )

        if len(variables_numericas_seleccionadas) == 0:

            st.warning(
                "⚠️ Seleccione al menos una variable numérica "
                "para visualizar su distribución."
            )

        else:

            numero_bins = st.slider(
                "Seleccione el número de intervalos del histograma:",
                min_value=5,
                max_value=50,
                value=20,
                step=5
            )

            for variable in variables_numericas_seleccionadas:

                st.subheader(f"📊 Distribución de {variable}")

                fig, ax = plt.subplots(figsize=(9, 4))

                ax.hist(
                    df[variable].dropna(),
                    bins=numero_bins,
                    edgecolor="black"
                )

                ax.set_title(
                    f"Distribución de la variable {variable}"
                )
                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                st.pyplot(fig)

                media = df[variable].mean()
                mediana = df[variable].median()

                if media > mediana:
                    interpretacion = (
                        "La media es mayor que la mediana, lo que puede "
                        "indicar una distribución con cierta asimetría "
                        "hacia valores altos."
                    )

                elif media < mediana:
                    interpretacion = (
                        "La media es menor que la mediana, lo que puede "
                        "indicar una distribución con cierta asimetría "
                        "hacia valores bajos."
                    )

                else:
                    interpretacion = (
                        "La media y la mediana son similares, por lo que "
                        "la distribución presenta una tendencia más "
                        "equilibrada respecto a su centro."
                    )

                st.info(
                    f"""
                    **Interpretación visual:**

                    La variable **{variable}** presenta una distribución
                    que permite observar cómo se concentran sus valores.

                    La media es **{media:,.2f}** y la mediana es
                    **{mediana:,.2f}**.

                    {interpretacion}
                    """
                )


    # ============================================================
    # ÍTEM 6
    # ============================================================

    with tab6:

        st.header("📊 Ítem 6: Análisis de variables categóricas")

        st.write(
            """
            En este apartado se analizan las variables categóricas
            mediante conteos y proporciones. Los gráficos de barras
            permiten identificar las categorías más frecuentes y
            comparar su participación dentro del dataset.
            """
        )

        variable_categorica = st.selectbox(
            "Seleccione una variable categórica:",
            variables_categoricas,
            key="variable_categorica_item6"
        )

        conteos = df[variable_categorica].value_counts()

        proporciones = (
            df[variable_categorica]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )

        tabla_categorias = pd.DataFrame({
            "Categoría": conteos.index,
            "Conteo": conteos.values,
            "Proporción (%)": proporciones.values
        })

        st.subheader("📋 Conteos y proporciones")

        st.dataframe(
            tabla_categorias,
            use_container_width=True
        )

        st.subheader("📊 Gráfico de barras")

        fig, ax = plt.subplots(figsize=(10, 5))

        conteos.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            f"Frecuencia de {variable_categorica}"
        )
        ax.set_xlabel(variable_categorica)
        ax.set_ylabel("Cantidad")

        plt.xticks(rotation=45, ha="right")

        st.pyplot(fig)

        categoria_mas_frecuente = conteos.idxmax()
        cantidad_mayor = conteos.max()
        proporcion_mayor = proporciones.max()

        st.info(
            f"""
            **Interpretación:**

            La categoría más frecuente de **{variable_categorica}**
            es **{categoria_mas_frecuente}**, con **{cantidad_mayor:,}**
            registros, lo que representa aproximadamente un
            **{proporcion_mayor:.2f}%** del total de observaciones.
            """
        )


    # ============================================================
    # ÍTEM 7
    # ============================================================

    with tab7:

        st.header(
            "🔗 Ítem 7: Análisis bivariado "
            "(numérico vs categórico)"
        )

        st.write(
            """
            En este apartado se analiza la relación entre variables
            numéricas y una variable categórica. Se utiliza la variable
            objetivo **y**, que indica si el cliente aceptó o no la
            propuesta de depósito a plazo.
            """
        )

        if "y" in df.columns:

            variable_numerica_bivariada = st.selectbox(
                "Seleccione una variable numérica:",
                [
                    variable
                    for variable in variables_numericas
                    if variable not in ["y"]
                ],
                key="variable_numerica_item7"
            )

            st.subheader(
                f"📊 {variable_numerica_bivariada} vs y"
            )

            grupos = df.groupby("y")[
                variable_numerica_bivariada
            ].agg(
                ["mean", "median", "min", "max"]
            )

            grupos.columns = [
                "Media",
                "Mediana",
                "Mínimo",
                "Máximo"
            ]

            st.dataframe(
                grupos,
                use_container_width=True
            )

            fig, ax = plt.subplots(figsize=(8, 5))

            df.boxplot(
                column=variable_numerica_bivariada,
                by="y",
                ax=ax
            )

            ax.set_title(
                f"{variable_numerica_bivariada} según resultado y"
            )
            ax.set_xlabel("Resultado de la campaña")
            ax.set_ylabel(variable_numerica_bivariada)

            plt.suptitle("")

            st.pyplot(fig)

            media_no = df[
                df["y"] == "no"
            ][variable_numerica_bivariada].mean()

            media_si = df[
                df["y"] == "yes"
            ][variable_numerica_bivariada].mean()

            st.info(
                f"""
                **Interpretación:**

                La media de **{variable_numerica_bivariada}** para los
                clientes con resultado **no** es de **{media_no:,.2f}**,
                mientras que para los clientes con resultado **yes**
                es de **{media_si:,.2f}**.

                La comparación permite identificar diferencias en el
                comportamiento de esta variable numérica según el
                resultado de la campaña.
                """
            )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y'."
            )


    # ============================================================
    # ÍTEM 8
    # ============================================================

    with tab8:

        st.header(
            "🔗 Ítem 8: Análisis bivariado "
            "(categórico vs categórico)"
        )

        st.write(
            """
            En este apartado se estudia la relación entre dos variables
            categóricas. Se utiliza la variable objetivo **y** para
            comparar cómo cambia el resultado de la campaña según
            diferentes categorías.
            """
        )

        if "y" in df.columns:

            categoricas_sin_y = [
                variable
                for variable in variables_categoricas
                if variable != "y"
            ]

            variable_categorica_2 = st.selectbox(
                "Seleccione una variable categórica:",
                categoricas_sin_y,
                key="variable_categorica_item8"
            )

            tabla_cruzada = pd.crosstab(
                df[variable_categorica_2],
                df["y"]
            )

            st.subheader(
                f"📋 Conteo: {variable_categorica_2} vs y"
            )

            st.dataframe(
                tabla_cruzada,
                use_container_width=True
            )

            st.subheader("📊 Gráfico de barras")

            fig, ax = plt.subplots(figsize=(10, 5))

            tabla_cruzada.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                f"{variable_categorica_2} según resultado y"
            )
            ax.set_xlabel(variable_categorica_2)
            ax.set_ylabel("Cantidad")

            plt.xticks(rotation=45, ha="right")

            st.pyplot(fig)

            st.subheader("📈 Proporciones")

            tabla_proporciones = pd.crosstab(
                df[variable_categorica_2],
                df["y"],
                normalize="index"
            ).mul(100).round(2)

            st.dataframe(
                tabla_proporciones,
                use_container_width=True
            )

            st.info(
                f"""
                **Interpretación:**

                La tabla y el gráfico permiten comparar la cantidad
                de clientes que obtuvieron resultados **yes** y **no**
                dentro de cada categoría de **{variable_categorica_2}**.

                Las proporciones permiten realizar una comparación
                más adecuada entre categorías con diferentes tamaños
                de muestra.
                """
            )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y'."
            )


    # ============================================================
    # ÍTEM 9
    # ============================================================

    with tab9:

        st.header(
            "🎛️ Ítem 9: Análisis basado en parámetros seleccionados"
        )

        st.write(
            """
            Este apartado permite realizar un análisis dinámico del
            dataset. El usuario puede seleccionar variables numéricas
            y categóricas mediante controles interactivos.
            """
        )

        st.subheader("🎯 Selección de variables numéricas")

        variables_numericas_parametros = st.multiselect(
            "Seleccione las variables numéricas que desea analizar:",
            variables_numericas,
            default=variables_numericas[:2],
            key="multiselect_numericas_item9"
        )

        st.subheader("🏷️ Selección de variables categóricas")

        variables_categoricas_parametros = st.multiselect(
            "Seleccione las variables categóricas:",
            variables_categoricas,
            default=variables_categoricas[:2],
            key="multiselect_categoricas_item9"
        )

        mostrar_estadisticas = st.checkbox(
            "Mostrar estadísticas descriptivas",
            value=True
        )

        if mostrar_estadisticas:

            if len(variables_numericas_parametros) > 0:

                st.subheader("📊 Estadísticas de las variables seleccionadas")

                estadisticas_parametros = df[
                    variables_numericas_parametros
                ].describe()

                st.dataframe(
                    estadisticas_parametros,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Seleccione al menos una variable numérica."
                )

        if len(variables_categoricas_parametros) > 0:

            st.subheader("📋 Análisis de variables categóricas")

            for variable in variables_categoricas_parametros:

                st.write(f"**Variable: {variable}**")

                conteos_parametros = (
                    df[variable]
                    .value_counts()
                    .head(10)
                )

                st.bar_chart(
                    conteos_parametros
                )

        else:

            st.warning(
                "Seleccione al menos una variable categórica."
            )

        st.success(
            """
            ✅ El análisis se actualiza automáticamente según las
            variables seleccionadas por el usuario.
            """
        )


    # ============================================================
    # ÍTEM 10
    # ============================================================

    with tab10:

        st.header("💡 Ítem 10: Hallazgos clave")

        st.write(
            """
            En este apartado se resumen algunos de los principales
            hallazgos obtenidos durante el análisis exploratorio
            de datos.
            """
        )

        st.subheader("📊 Resumen general")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Registros",
                f"{df.shape[0]:,}"
            )

        with col2:
            st.metric(
                "Variables",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Variables numéricas",
                len(variables_numericas)
            )

        with col4:
            st.metric(
                "Variables categóricas",
                len(variables_categoricas)
            )

        st.subheader("📈 Resultado de la variable objetivo")

        if "y" in df.columns:

            resultados_y = df["y"].value_counts()

            proporciones_y = (
                df["y"]
                .value_counts(normalize=True)
                .mul(100)
                .round(2)
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Conteo de resultados**")

                st.dataframe(
                    pd.DataFrame({
                        "Resultado": resultados_y.index,
                        "Cantidad": resultados_y.values
                    }),
                    use_container_width=True
                )

            with col2:

                st.write("**Proporción de resultados**")

                st.dataframe(
                    pd.DataFrame({
                        "Resultado": proporciones_y.index,
                        "Proporción (%)": proporciones_y.values
                    }),
                    use_container_width=True
                )

            fig, ax = plt.subplots(figsize=(7, 4))

            resultados_y.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                "Distribución del resultado de la campaña"
            )
            ax.set_xlabel("Resultado")
            ax.set_ylabel("Cantidad")

            plt.xticks(rotation=0)

            st.pyplot(fig)

            resultado_mayoritario = resultados_y.idxmax()
            cantidad_mayoritaria = resultados_y.max()
            porcentaje_mayoritario = proporciones_y[
                resultado_mayoritario
            ]

            st.subheader("🔎 Principales insights")

            st.markdown(
                f"""
                **1. Estructura del dataset:**  
                El dataset contiene **{df.shape[0]:,} registros**
                y **{df.shape[1]} variables**, lo que proporciona
                una base amplia para realizar análisis exploratorios.

                **2. Variables:**  
                Se identificaron **{len(variables_numericas)} variables
                numéricas** y **{len(variables_categoricas)} variables
                categóricas**.

                **3. Valores faltantes:**  
                El análisis de valores faltantes permite determinar
                si existen datos ausentes que puedan afectar los
                análisis posteriores.

                **4. Variable objetivo:**  
                El resultado más frecuente de la campaña es
                **{resultado_mayoritario}**, con **{cantidad_mayoritaria:,}**
                registros, equivalente aproximadamente al
                **{porcentaje_mayoritario:.2f}%**.

                **5. Análisis bivariado:**  
                Las comparaciones entre variables numéricas y
                categóricas permiten identificar diferencias entre
                los clientes según el resultado de la campaña.

                **6. Análisis categórico:**  
                Las variables categóricas permiten identificar
                patrones de frecuencia y diferencias entre grupos.
                """
            )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y', "
                "por lo que no es posible generar todos los hallazgos."
            )


