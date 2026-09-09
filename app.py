import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CLASE POO - DataAnalyzer
# ============================================================

class DataAnalyzer:
    """
    Clase encargada de realizar operaciones de análisis
    exploratorio sobre un DataFrame.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    def clasificar_variables(self):
        """
        Clasifica las variables en numéricas y categóricas.
        """

        variables_numericas = self.df.select_dtypes(
            include=["number"]
        ).columns.tolist()

        variables_categoricas = self.df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        return variables_numericas, variables_categoricas

    def estadisticas_descriptivas(self):
        """
        Devuelve las estadísticas descriptivas de las
        variables numéricas.
        """

        variables_numericas, _ = self.clasificar_variables()

        return self.df[variables_numericas].describe()

    def resumen_variable(self, variable):
        """
        Calcula estadísticas básicas para una variable numérica.
        """

        serie = self.df[variable].dropna()

        moda = serie.mode()

        if not moda.empty:
            moda_valor = moda.iloc[0]
        else:
            moda_valor = "Sin moda"

        return {
            "media": serie.mean(),
            "mediana": serie.median(),
            "moda": moda_valor,
            "minimo": serie.min(),
            "maximo": serie.max(),
            "desviacion": serie.std()
        }

    def conteos_categoricos(self, variable):
        """
        Devuelve los conteos de una variable categórica.
        """

        return self.df[variable].value_counts()

    def proporciones_categoricas(self, variable):
        """
        Devuelve las proporciones porcentuales de una variable
        categórica.
        """

        return (
            self.df[variable]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )

    def valores_faltantes(self):
        """
        Calcula los valores faltantes por variable.
        """

        return self.df.isnull().sum()

    def comparacion_grupos(self, variable_numerica, variable_grupo):
        """
        Compara una variable numérica entre grupos.
        """

        return self.df.groupby(variable_grupo)[
            variable_numerica
        ].agg(
            ["mean", "median", "min", "max"]
        )

    def tabla_cruzada(self, variable_1, variable_2):
        """
        Genera una tabla de contingencia entre dos variables
        categóricas.
        """

        return pd.crosstab(
            self.df[variable_1],
            self.df[variable_2]
        )

    def tabla_proporciones(self, variable_1, variable_2):
        """
        Genera una tabla de proporciones por fila.
        """

        return (
            pd.crosstab(
                self.df[variable_1],
                self.df[variable_2],
                normalize="index"
            )
            .mul(100)
            .round(2)
        )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Módulos")

# Mostrar imagen solo si existe en el repositorio
if os.path.exists("IMAGEN DMC.png"):
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
    # OBJETIVO
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
    # DATOS DEL AUTOR
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
    # DATASET
    # --------------------------------------------------------

    st.subheader("📊 Breve explicación del dataset")

    st.write(
        """
        El dataset Bank Marketing contiene información relacionada con
        campañas de marketing telefónico de una institución bancaria.

        Los datos incluyen características de los clientes, información
        relacionada con las campañas de contacto y el resultado final
        de la campaña.
        """
    )

    # --------------------------------------------------------
    # TECNOLOGÍAS
    # --------------------------------------------------------

    st.subheader("🛠️ Tecnologías utilizadas")

    st.markdown(
        """
        - **Python:** lenguaje de programación utilizado para desarrollar
          el proyecto.

        - **Pandas:** biblioteca utilizada para la manipulación y análisis
          de los datos.

        - **Matplotlib:** biblioteca utilizada para la construcción de
          visualizaciones.

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
        En este módulo se realiza la carga, validación y exploración
        del dataset Bank Marketing. Se presentan los principales
        elementos del análisis exploratorio de datos (EDA).
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
    # VALIDACIÓN DE COLUMNAS
    # ========================================================

    columnas_esperadas = [
        "age",
        "job",
        "marital",
        "education",
        "default",
        "housing",
        "loan",
        "contact",
        "month",
        "day_of_week",
        "duration",
        "campaign",
        "pdays",
        "previous",
        "poutcome",
        "emp.var.rate",
        "cons.price.idx",
        "cons.conf.idx",
        "euribor3m",
        "nr.employed",
        "y"
    ]

    columnas_faltantes = [
        columna
        for columna in columnas_esperadas
        if columna not in df.columns
    ]

    if columnas_faltantes:

        st.warning(
            "⚠️ El archivo no contiene todas las columnas "
            "esperadas del dataset Bank Marketing."
        )

        st.write(
            "Columnas faltantes:"
        )

        st.write(columnas_faltantes)

    else:

        st.success(
            "✅ La estructura del dataset corresponde al conjunto "
            "de datos Bank Marketing."
        )

    # ========================================================
    # INFORMACIÓN GENERAL
    # ========================================================

    st.header("📋 Información del dataset")

    st.write(
        f"""
        El dataset contiene **{df.shape[0]:,} filas** y
        **{df.shape[1]} columnas**.
        """
    )

    # ========================================================
    # VISTA PREVIA - HEAD
    # ========================================================

    st.subheader("👀 Vista previa del dataset")

    st.write(
        """
        A continuación se muestran las primeras filas del dataset
        utilizando el método `head()`.
        """
    )

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # ========================================================
    # VISTA COMPLETA
    # ========================================================

    st.subheader("👀 Vista completa del dataset")

    st.write(
        """
        La siguiente tabla permite visualizar todas las filas y
        columnas del dataset.
        """
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=600
    )

    # ========================================================
    # DIMENSIONES
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
    # CREACIÓN DEL OBJETO POO
    # ========================================================

    analyzer = DataAnalyzer(df)

    variables_numericas, variables_categoricas = (
        analyzer.clasificar_variables()
    )

    # ========================================================
    # EDA
    # ========================================================

    st.divider()

    st.title("🔎 Análisis Exploratorio de Datos (EDA)")

    st.write(
        """
        En esta sección se realiza el análisis exploratorio del
        dataset Bank Marketing. Se estudian la estructura de los
        datos, los tipos de variables, las estadísticas descriptivas,
        los valores faltantes, las distribuciones y las relaciones
        entre variables.
        """
    )

    # ========================================================
    # TABS 1 - 10
    # ========================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
        [
            "📋 1. Información",
            "🔢 2. Clasificación",
            "📊 3. Estadísticas",
            "⚠️ 4. Faltantes",
            "📈 5. Numéricas",
            "📊 6. Categóricas",
            "🔗 7. Num vs Cat",
            "🔗 8. Cat vs Cat",
            "🎛️ 9. Parámetros",
            "💡 10. Hallazgos"
        ]
    )

    # ========================================================
    # ÍTEM 1
    # ========================================================

    with tab1:

        st.header(
            "📋 Ítem 1: Información general del dataset"
        )

        st.write(
            """
            En este apartado se presenta información general sobre
            la estructura del dataset, incluyendo los tipos de datos,
            la cantidad de registros y los valores faltantes.
            """
        )

        # ----------------------------------------------------
        # INFO
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
        # TIPOS
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
        # NULOS
        # ----------------------------------------------------

        st.subheader("⚠️ Conteo de valores nulos")

        valores_nulos = analyzer.valores_faltantes()

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
        # MÉTRICAS
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

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

        with col3:

            st.metric(
                "Memoria aproximada",
                f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
            )


    # ========================================================
    # ÍTEM 2
    # ========================================================

    with tab2:

        st.header(
            "🔢 Ítem 2: Clasificación de variables"
        )

        st.write(
            """
            Las variables del dataset se clasifican automáticamente
            en variables numéricas y categóricas mediante un método
            de la clase `DataAnalyzer`.
            """
        )

        col1, col2 = st.columns(2)

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

        fig, ax = plt.subplots(
            figsize=(7, 4)
        )

        ax.bar(
            resumen_variables["Tipo de variable"],
            resumen_variables["Cantidad"]
        )

        ax.set_title(
            "Cantidad de variables por tipo"
        )

        ax.set_xlabel(
            "Tipo de variable"
        )

        ax.set_ylabel(
            "Cantidad"
        )

        st.pyplot(fig)

        plt.close(fig)


    # ========================================================
    # ÍTEM 3
    # ========================================================

    with tab3:

        st.header(
            "📊 Ítem 3: Estadísticas descriptivas"
        )

        st.write(
            """
            Las estadísticas descriptivas permiten resumir el
            comportamiento de las variables numéricas mediante
            medidas de tendencia central y dispersión.
            """
        )

        st.subheader(
            "📈 Estadísticas mediante .describe()"
        )

        estadisticas = analyzer.estadisticas_descriptivas()

        st.dataframe(
            estadisticas,
            use_container_width=True
        )

        st.subheader(
            "🔍 Análisis de una variable"
        )

        variable = st.selectbox(
            "Seleccione una variable numérica:",
            variables_numericas,
            key="variable_item3"
        )

        resumen = analyzer.resumen_variable(
            variable
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Media",
                f"{resumen['media']:,.2f}"
            )

        with col2:

            st.metric(
                "Mediana",
                f"{resumen['mediana']:,.2f}"
            )

        with col3:

            if isinstance(
                resumen["moda"],
                (int, float)
            ):

                st.metric(
                    "Moda",
                    f"{resumen['moda']:,.2f}"
                )

            else:

                st.metric(
                    "Moda",
                    str(resumen["moda"])
                )

        st.subheader(
            "📐 Medidas de dispersión"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Mínimo",
                f"{resumen['minimo']:,.2f}"
            )

        with col2:

            st.metric(
                "Máximo",
                f"{resumen['maximo']:,.2f}"
            )

        with col3:

            st.metric(
                "Desviación estándar",
                f"{resumen['desviacion']:,.2f}"
            )

        st.subheader(
            "📝 Interpretación"
        )

        if resumen["media"] > resumen["mediana"]:

            interpretacion = (
                "La media es superior a la mediana, lo que puede "
                "sugerir cierta asimetría hacia valores altos."
            )

        elif resumen["media"] < resumen["mediana"]:

            interpretacion = (
                "La media es inferior a la mediana, lo que puede "
                "sugerir cierta asimetría hacia valores bajos."
            )

        else:

            interpretacion = (
                "La media y la mediana son similares, indicando "
                "una distribución relativamente equilibrada."
            )

        st.info(
            f"""
            Para **{variable}**, la media es **{resumen['media']:,.2f}**
            y la mediana es **{resumen['mediana']:,.2f}**.

            La desviación estándar es **{resumen['desviacion']:,.2f}**,
            lo que permite evaluar la dispersión de los datos.

            {interpretacion}
            """
        )


    # ========================================================
    # ÍTEM 4
    # ========================================================

    with tab4:

        st.header(
            "⚠️ Ítem 4: Análisis de valores faltantes"
        )

        st.write(
            """
            En este apartado se analiza la cantidad de valores
            faltantes presentes en cada variable.
            """
        )

        valores_nulos = analyzer.valores_faltantes()

        total_nulos = valores_nulos.sum()

        variables_con_nulos = (
            valores_nulos > 0
        ).sum()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total de valores faltantes",
                f"{total_nulos:,}"
            )

        with col2:

            st.metric(
                "Variables con faltantes",
                int(variables_con_nulos)
            )

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

        faltantes_grafico = valores_nulos[
            valores_nulos > 0
        ]

        st.subheader(
            "📊 Visualización"
        )

        if len(faltantes_grafico) > 0:

            fig, ax = plt.subplots(
                figsize=(10, 4)
            )

            ax.bar(
                faltantes_grafico.index,
                faltantes_grafico.values
            )

            ax.set_title(
                "Valores faltantes por variable"
            )

            ax.set_xlabel(
                "Variable"
            )

            ax.set_ylabel(
                "Cantidad de faltantes"
            )

            plt.xticks(
                rotation=45,
                ha="right"
            )

            st.pyplot(fig)

            plt.close(fig)

        else:

            st.success(
                "✅ El dataset no contiene valores faltantes."
            )

        st.subheader(
            "📝 Discusión"
        )

        if total_nulos == 0:

            st.write(
                """
                El dataset no presenta valores faltantes. Por lo tanto,
                no es necesario aplicar técnicas de imputación o
                eliminación de registros debido a datos ausentes.
                """
            )

        else:

            st.write(
                f"""
                Se identificaron **{total_nulos:,} valores faltantes**
                distribuidos en **{int(variables_con_nulos)} variables**.

                Antes de realizar análisis posteriores sería conveniente
                evaluar la causa de estos valores y determinar el
                tratamiento más adecuado.
                """
            )


    # ========================================================
    # ÍTEM 5
    # ========================================================

    with tab5:

        st.header(
            "📈 Ítem 5: Distribución de variables numéricas"
        )

        st.write(
            """
            Los histogramas permiten analizar la distribución de
            las variables numéricas, observando concentración,
            dispersión, asimetría y posibles valores extremos.
            """
        )

        variables_seleccionadas = st.multiselect(
            "Seleccione una o más variables numéricas:",
            variables_numericas,
            default=variables_numericas[:3],
            key="multiselect_item5"
        )

        if not variables_seleccionadas:

            st.warning(
                "⚠️ Seleccione al menos una variable."
            )

        else:

            numero_bins = st.slider(
                "Número de intervalos del histograma:",
                min_value=5,
                max_value=50,
                value=20,
                step=5,
                key="slider_item5"
            )

            for variable in variables_seleccionadas:

                st.subheader(
                    f"📊 Distribución de {variable}"
                )

                fig, ax = plt.subplots(
                    figsize=(9, 4)
                )

                ax.hist(
                    df[variable].dropna(),
                    bins=numero_bins,
                    edgecolor="black"
                )

                ax.set_title(
                    f"Histograma de {variable}"
                )

                ax.set_xlabel(
                    variable
                )

                ax.set_ylabel(
                    "Frecuencia"
                )

                st.pyplot(fig)

                plt.close(fig)

                media = df[variable].mean()
                mediana = df[variable].median()

                if media > mediana:

                    interpretacion = (
                        "La media es mayor que la mediana, lo que "
                        "puede indicar una distribución con asimetría "
                        "hacia valores altos."
                    )

                elif media < mediana:

                    interpretacion = (
                        "La media es menor que la mediana, lo que "
                        "puede indicar una distribución con asimetría "
                        "hacia valores bajos."
                    )

                else:

                    interpretacion = (
                        "La media y la mediana son similares, por lo "
                        "que la distribución presenta un centro "
                        "relativamente equilibrado."
                    )

                st.info(
                    f"""
                    **Interpretación visual**

                    La variable **{variable}** presenta una distribución
                    cuyo comportamiento puede observarse mediante el
                    histograma.

                    Media: **{media:,.2f}**

                    Mediana: **{mediana:,.2f}**

                    {interpretacion}
                    """
                )


    # ========================================================
    # ÍTEM 6
    # ========================================================

    with tab6:

        st.header(
            "📊 Ítem 6: Análisis de variables categóricas"
        )

        st.write(
            """
            Las variables categóricas se analizan mediante conteos,
            proporciones y gráficos de barras para identificar las
            categorías más frecuentes.
            """
        )

        variable_categorica = st.selectbox(
            "Seleccione una variable categórica:",
            variables_categoricas,
            key="selectbox_item6"
        )

        conteos = analyzer.conteos_categoricos(
            variable_categorica
        )

        proporciones = analyzer.proporciones_categoricas(
            variable_categorica
        )

        tabla_categorias = pd.DataFrame(
            {
                "Categoría": conteos.index,
                "Conteo": conteos.values,
                "Proporción (%)": proporciones.values
            }
        )

        st.subheader(
            "📋 Conteos y proporciones"
        )

        st.dataframe(
            tabla_categorias,
            use_container_width=True
        )

        st.subheader(
            "📊 Gráfico de barras"
        )

        fig, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.bar(
            conteos.index.astype(str),
            conteos.values
        )

        ax.set_title(
            f"Frecuencia de {variable_categorica}"
        )

        ax.set_xlabel(
            variable_categorica
        )

        ax.set_ylabel(
            "Cantidad"
        )

        plt.xticks(
            rotation=45,
            ha="right"
        )

        st.pyplot(fig)

        plt.close(fig)

        categoria_mayor = conteos.idxmax()
        cantidad_mayor = conteos.max()
        porcentaje_mayor = proporciones.loc[
            categoria_mayor
        ]

        st.info(
            f"""
            **Interpretación**

            La categoría más frecuente de **{variable_categorica}**
            es **{categoria_mayor}**, con **{cantidad_mayor:,}**
            registros.

            Esta categoría representa aproximadamente el
            **{porcentaje_mayor:.2f}%** del total.
            """
        )


    # ========================================================
    # ÍTEM 7
    # ========================================================

    with tab7:

        st.header(
            "🔗 Ítem 7: Análisis bivariado "
            "(numérico vs categórico)"
        )

        st.write(
            """
            Se analiza cómo se comporta una variable numérica según
            una variable categórica. En este proyecto se utiliza
            la variable objetivo **y**, que contiene los resultados
            de la campaña.
            """
        )

        if "y" in df.columns:

            variables_bivariadas = [
                variable
                for variable in variables_numericas
                if variable != "y"
            ]

            variable_numerica = st.selectbox(
                "Seleccione una variable numérica:",
                variables_bivariadas,
                key="selectbox_item7"
            )

            st.subheader(
                f"📊 {variable_numerica} vs y"
            )

            comparacion = analyzer.comparacion_grupos(
                variable_numerica,
                "y"
            )

            comparacion.columns = [
                "Media",
                "Mediana",
                "Mínimo",
                "Máximo"
            ]

            st.dataframe(
                comparacion,
                use_container_width=True
            )

            fig, ax = plt.subplots(
                figsize=(8, 5)
            )

            df.boxplot(
                column=variable_numerica,
                by="y",
                ax=ax
            )

            ax.set_title(
                f"{variable_numerica} según resultado de la campaña"
            )

            ax.set_xlabel(
                "Resultado y"
            )

            ax.set_ylabel(
                variable_numerica
            )

            plt.suptitle("")

            st.pyplot(fig)

            plt.close(fig)

            if "no" in df["y"].values and "yes" in df["y"].values:

                media_no = df.loc[
                    df["y"] == "no",
                    variable_numerica
                ].mean()

                media_yes = df.loc[
                    df["y"] == "yes",
                    variable_numerica
                ].mean()

                diferencia = media_yes - media_no

                st.info(
                    f"""
                    **Interpretación**

                    La media de **{variable_numerica}** para el grupo
                    **no** es **{media_no:,.2f}**.

                    La media para el grupo **yes** es
                    **{media_yes:,.2f}**.

                    La diferencia entre ambos grupos es de
                    **{diferencia:,.2f}**.

                    Esta comparación permite identificar diferencias
                    en el comportamiento de la variable numérica
                    según el resultado de la campaña.
                    """
                )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y'."
            )


    # ========================================================
    # ÍTEM 8
    # ========================================================

    with tab8:

        st.header(
            "🔗 Ítem 8: Análisis bivariado "
            "(categórico vs categórico)"
        )

        st.write(
            """
            Se estudia la relación entre dos variables categóricas.
            Se utiliza la variable objetivo **y** para observar cómo
            cambia el resultado de la campaña según diferentes
            categorías.
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
                key="selectbox_item8"
            )

            tabla_cruzada = analyzer.tabla_cruzada(
                variable_categorica_2,
                "y"
            )

            st.subheader(
                f"📋 Conteos: {variable_categorica_2} vs y"
            )

            st.dataframe(
                tabla_cruzada,
                use_container_width=True
            )

            st.subheader(
                "📊 Gráfico de barras"
            )

            fig, ax = plt.subplots(
                figsize=(10, 5)
            )

            tabla_cruzada.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                f"{variable_categorica_2} vs y"
            )

            ax.set_xlabel(
                variable_categorica_2
            )

            ax.set_ylabel(
                "Cantidad"
            )

            plt.xticks(
                rotation=45,
                ha="right"
            )

            st.pyplot(fig)

            plt.close(fig)

            st.subheader(
                "📈 Proporciones por categoría"
            )

            tabla_proporciones = analyzer.tabla_proporciones(
                variable_categorica_2,
                "y"
            )

            st.dataframe(
                tabla_proporciones,
                use_container_width=True
            )

            st.info(
                f"""
                **Interpretación**

                El análisis permite comparar los resultados **yes**
                y **no** dentro de cada categoría de
                **{variable_categorica_2}**.

                Las proporciones permiten realizar una comparación
                más justa entre categorías de diferentes tamaños.
                """
            )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y'."
            )


    # ========================================================
    # ÍTEM 9
    # ========================================================

    with tab9:

        st.header(
            "🎛️ Ítem 9: Análisis basado en parámetros seleccionados"
        )

        st.write(
            """
            Este apartado permite al usuario seleccionar variables
            y realizar un análisis dinámico del dataset.
            """
        )

        # ----------------------------------------------------
        # SELECTBOX
        # ----------------------------------------------------

        st.subheader(
            "🎯 Selección principal"
        )

        variable_principal = st.selectbox(
            "Seleccione una variable numérica principal:",
            variables_numericas,
            key="selectbox_item9"
        )

        # ----------------------------------------------------
        # MULTISELECT NUMÉRICAS
        # ----------------------------------------------------

        variables_num_seleccionadas = st.multiselect(
            "Seleccione variables numéricas:",
            variables_numericas,
            default=variables_numericas[:2],
            key="multiselect_num_item9"
        )

        # ----------------------------------------------------
        # MULTISELECT CATEGÓRICAS
        # ----------------------------------------------------

        variables_cat_seleccionadas = st.multiselect(
            "Seleccione variables categóricas:",
            variables_categoricas,
            default=variables_categoricas[:2],
            key="multiselect_cat_item9"
        )

        # ----------------------------------------------------
        # CHECKBOX
        # ----------------------------------------------------

        mostrar_estadisticas = st.checkbox(
            "Mostrar estadísticas descriptivas",
            value=True,
            key="checkbox_item9"
        )

        # ----------------------------------------------------
        # SLIDER
        # ----------------------------------------------------

        limite_categorias = st.slider(
            "Número máximo de categorías a visualizar:",
            min_value=2,
            max_value=15,
            value=8,
            step=1,
            key="slider_item9"
        )

        # ----------------------------------------------------
        # VARIABLE PRINCIPAL
        # ----------------------------------------------------

        st.subheader(
            f"📊 Análisis de {variable_principal}"
        )

        resumen_principal = analyzer.resumen_variable(
            variable_principal
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Media",
                f"{resumen_principal['media']:,.2f}"
            )

        with col2:

            st.metric(
                "Mediana",
                f"{resumen_principal['mediana']:,.2f}"
            )

        with col3:

            st.metric(
                "Desviación",
                f"{resumen_principal['desviacion']:,.2f}"
            )

        # ----------------------------------------------------
        # ESTADÍSTICAS
        # ----------------------------------------------------

        if mostrar_estadisticas:

            if variables_num_seleccionadas:

                st.subheader(
                    "📈 Estadísticas de variables seleccionadas"
                )

                estadisticas_parametros = df[
                    variables_num_seleccionadas
                ].describe()

                st.dataframe(
                    estadisticas_parametros,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Seleccione al menos una variable numérica."
                )

        # ----------------------------------------------------
        # CATEGÓRICAS
        # ----------------------------------------------------

        if variables_cat_seleccionadas:

            st.subheader(
                "📊 Variables categóricas seleccionadas"
            )

            for variable in variables_cat_seleccionadas:

                st.write(
                    f"**{variable}**"
                )

                conteos = (
                    df[variable]
                    .value_counts()
                    .head(limite_categorias)
                )

                fig, ax = plt.subplots(
                    figsize=(9, 4)
                )

                ax.bar(
                    conteos.index.astype(str),
                    conteos.values
                )

                ax.set_title(
                    f"Frecuencia de {variable}"
                )

                ax.set_xlabel(
                    variable
                )

                ax.set_ylabel(
                    "Cantidad"
                )

                plt.xticks(
                    rotation=45,
                    ha="right"
                )

                st.pyplot(fig)

                plt.close(fig)

        else:

            st.warning(
                "Seleccione al menos una variable categórica."
            )

        st.success(
            """
            ✅ El análisis se actualiza automáticamente según
            las variables y parámetros seleccionados por el usuario.
            """
        )


    # ========================================================
    # ÍTEM 10
    # ========================================================

    with tab10:

        st.header(
            "💡 Ítem 10: Hallazgos clave"
        )

        st.write(
            """
            En este apartado se presentan los principales hallazgos
            derivados del análisis exploratorio de datos.
            """
        )

        # ----------------------------------------------------
        # RESUMEN GENERAL
        # ----------------------------------------------------

        st.subheader(
            "📊 Resumen general del dataset"
        )

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
                "Numéricas",
                len(variables_numericas)
            )

        with col4:

            st.metric(
                "Categóricas",
                len(variables_categoricas)
            )

        # ----------------------------------------------------
        # VALORES FALTANTES
        # ----------------------------------------------------

        total_nulos = analyzer.valores_faltantes().sum()

        st.subheader(
            "⚠️ Calidad de los datos"
        )

        if total_nulos == 0:

            st.success(
                "✅ No se identificaron valores faltantes."
            )

        else:

            st.warning(
                f"Se identificaron {total_nulos:,} valores faltantes."
            )

        # ----------------------------------------------------
        # VARIABLE OBJETIVO
        # ----------------------------------------------------

        if "y" in df.columns:

            st.subheader(
                "🎯 Resultado de la campaña"
            )

            resultados = df["y"].value_counts()

            proporciones = (
                df["y"]
                .value_counts(normalize=True)
                .mul(100)
                .round(2)
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    "**Conteo de resultados**"
                )

                tabla_resultados = pd.DataFrame(
                    {
                        "Resultado": resultados.index,
                        "Cantidad": resultados.values
                    }
                )

                st.dataframe(
                    tabla_resultados,
                    use_container_width=True
                )

            with col2:

                st.write(
                    "**Proporción de resultados**"
                )

                tabla_proporciones_y = pd.DataFrame(
                    {
                        "Resultado": proporciones.index,
                        "Proporción (%)": proporciones.values
                    }
                )

                st.dataframe(
                    tabla_proporciones_y,
                    use_container_width=True
                )

            # ------------------------------------------------
            # GRÁFICO RESUMEN
            # ------------------------------------------------

            st.subheader(
                "📈 Visualización resumen"
            )

            fig, ax = plt.subplots(
                figsize=(8, 5)
            )

            ax.bar(
                resultados.index.astype(str),
                resultados.values
            )

            ax.set_title(
                "Distribución del resultado de la campaña"
            )

            ax.set_xlabel(
                "Resultado"
            )

            ax.set_ylabel(
                "Cantidad"
            )

            st.pyplot(fig)

            plt.close(fig)

            # ------------------------------------------------
            # HALLAZGOS
            # ------------------------------------------------

            resultado_mayoritario = resultados.idxmax()

            cantidad_mayoritaria = resultados.max()

            porcentaje_mayoritario = proporciones.loc[
                resultado_mayoritario
            ]

            st.subheader(
                "🔎 Principales insights"
            )

            st.markdown(
                f"""
                ### 1. Estructura del dataset

                El dataset contiene **{df.shape[0]:,} registros**
                y **{df.shape[1]} variables**, permitiendo realizar
                un análisis exploratorio amplio.

                ### 2. Tipos de variables

                Se identificaron **{len(variables_numericas)} variables
                numéricas** y **{len(variables_categoricas)} variables
                categóricas**.

                ### 3. Valores faltantes

                El análisis de calidad de datos identificó un total
                de **{total_nulos:,} valores faltantes**.

                ### 4. Resultado predominante

                La categoría más frecuente de la variable objetivo
                **y** es **{resultado_mayoritario}**, con
                **{cantidad_mayoritaria:,} registros**, equivalentes
                aproximadamente al **{porcentaje_mayoritario:.2f}%**
                del dataset.

                ### 5. Análisis de variables numéricas

                Los histogramas permiten observar la distribución,
                concentración y dispersión de las variables numéricas.

                ### 6. Análisis de variables categóricas

                Los conteos y proporciones permiten identificar las
                categorías predominantes dentro del dataset.

                ### 7. Análisis bivariado

                La comparación entre variables numéricas y categóricas
                permite identificar diferencias entre los grupos
                definidos por el resultado de la campaña.

                ### 8. Análisis dinámico

                Los controles interactivos permiten seleccionar
                variables y modificar el análisis de acuerdo con
                las preferencias del usuario.
                """
            )

        else:

            st.warning(
                "⚠️ No se encontró la variable objetivo 'y'."
            )

        # ----------------------------------------------------
        # CONCLUSIÓN
        # ----------------------------------------------------

        st.subheader(
            "🎓 Conclusión del EDA"
        )

        st.write(
            """
            El análisis exploratorio permite comprender la estructura
            del dataset Bank Marketing, identificar los tipos de
            variables, estudiar sus distribuciones, analizar
            relaciones entre grupos y obtener hallazgos relevantes.

            La aplicación permite realizar este proceso de manera
            interactiva, facilitando la exploración de los datos
            mediante diferentes parámetros seleccionados por el usuario.
            """
        )
