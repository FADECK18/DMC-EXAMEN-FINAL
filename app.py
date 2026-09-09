import io
import os

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Bank Marketing - Python Fundamentals",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CLASE DE ANÁLISIS
# ============================================================

class DataAnalyzer:
    """
    Clase encargada de encapsular las principales operaciones
    de análisis exploratorio del dataset.
    """

    def __init__(self, dataframe):
        self.df = dataframe

    # --------------------------------------------------------
    # CLASIFICACIÓN DE VARIABLES
    # --------------------------------------------------------

    def clasificar_variables(self):
        numericas = self.df.select_dtypes(
            include=["number"]
        ).columns.tolist()

        categoricas = self.df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        return numericas, categoricas

    # --------------------------------------------------------
    # ESTADÍSTICAS DESCRIPTIVAS
    # --------------------------------------------------------

    def estadisticas_descriptivas(self):
        return self.df.describe(include="all").T

    # --------------------------------------------------------
    # RESUMEN DE UNA VARIABLE
    # --------------------------------------------------------

    def resumen_variable(self, variable):
        serie = self.df[variable]

        resumen = {
            "Variable": variable,
            "Tipo de dato": str(serie.dtype),
            "Valores únicos": serie.nunique(),
            "Valores faltantes": serie.isna().sum()
        }

        if pd.api.types.is_numeric_dtype(serie):
            resumen["Media"] = serie.mean()
            resumen["Mediana"] = serie.median()
            resumen["Moda"] = serie.mode().iloc[0] if not serie.mode().empty else None
            resumen["Mínimo"] = serie.min()
            resumen["Máximo"] = serie.max()
            resumen["Desviación estándar"] = serie.std()

        return resumen

    # --------------------------------------------------------
    # CONTEOS CATEGÓRICOS
    # --------------------------------------------------------

    def conteos_categoricos(self, variable):
        return self.df[variable].value_counts(dropna=False)

    # --------------------------------------------------------
    # PROPORCIONES CATEGÓRICAS
    # --------------------------------------------------------

    def proporciones_categoricas(self, variable):
        return (
            self.df[variable]
            .value_counts(normalize=True, dropna=False)
            .mul(100)
            .round(2)
        )

    # --------------------------------------------------------
    # VALORES FALTANTES
    # --------------------------------------------------------

    def valores_faltantes(self):
        faltantes = self.df.isna().sum()

        porcentaje = (
            self.df.isna().mean() * 100
        ).round(2)

        resultado = pd.DataFrame({
            "Valores faltantes": faltantes,
            "Porcentaje (%)": porcentaje
        })

        return resultado.sort_values(
            by="Valores faltantes",
            ascending=False
        )

    # --------------------------------------------------------
    # COMPARACIÓN DE GRUPOS
    # --------------------------------------------------------

    def comparacion_grupos(self, variable_numerica, variable_grupo):
        return (
            self.df
            .groupby(variable_grupo)[variable_numerica]
            .agg(
                Media="mean",
                Mediana="median",
                Mínimo="min",
                Máximo="max",
                Desviación="std",
                Cantidad="count"
            )
            .round(2)
        )

    # --------------------------------------------------------
    # TABLA CRUZADA
    # --------------------------------------------------------

    def tabla_cruzada(self, variable_1, variable_2):
        return pd.crosstab(
            self.df[variable_1],
            self.df[variable_2]
        )

    # --------------------------------------------------------
    # TABLA DE PROPORCIONES
    # --------------------------------------------------------

    def tabla_proporciones(self, variable_1, variable_2):
        return pd.crosstab(
            self.df[variable_1],
            self.df[variable_2],
            normalize="index"
        ).mul(100).round(2)

    # --------------------------------------------------------
    # HISTOGRAMA
    # --------------------------------------------------------

    def histograma(self, variable, bins=20):
        fig, ax = plt.subplots()

        ax.hist(
            self.df[variable].dropna(),
            bins=bins
        )

        ax.set_title(
            f"Distribución de {variable}"
        )
        ax.set_xlabel(variable)
        ax.set_ylabel("Frecuencia")

        return fig

    # --------------------------------------------------------
    # GRÁFICO DE BARRAS
    # --------------------------------------------------------

    def grafico_barras(self, variable):
        conteos = self.df[variable].value_counts()

        fig, ax = plt.subplots()

        conteos.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            f"Frecuencia de {variable}"
        )
        ax.set_xlabel(variable)
        ax.set_ylabel("Cantidad")

        plt.xticks(rotation=45)

        return fig

    # --------------------------------------------------------
    # BOXPLOT
    # --------------------------------------------------------

    def boxplot_por_grupo(
        self,
        variable_numerica,
        variable_grupo
    ):
        fig, ax = plt.subplots()

        grupos = []

        nombres = self.df[variable_grupo].dropna().unique()

        for grupo in nombres:
            datos = self.df[
                self.df[variable_grupo] == grupo
            ][variable_numerica].dropna()

            grupos.append(datos)

        ax.boxplot(
            grupos,
            labels=nombres
        )

        ax.set_title(
            f"{variable_numerica} según {variable_grupo}"
        )
        ax.set_xlabel(variable_grupo)
        ax.set_ylabel(variable_numerica)

        return fig


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Navegación")

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

    st.title(
        "APLICACIÓN INTERACTIVA CONSTRUIDA EN PYTHON UTILIZANDO STREAMLIT"
    )

    st.header("🎯 Objetivo del proyecto")

    st.write(
        """
        El objetivo de este proyecto es aplicar los conocimientos
        adquiridos en el curso **Python Fundamentals** mediante el
        desarrollo de una aplicación interactiva utilizando Python,
        Pandas y Streamlit.

        La aplicación permite cargar, organizar, explorar y analizar
        un conjunto de datos relacionado con campañas de marketing
        de una institución financiera.
        """
    )

    st.divider()

    st.header("👨‍💻 Información del proyecto")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Autor:** Farid Estefano Garibay Fabian")
        st.write("**Curso:** Python Fundamentals")

    with col2:
        st.write("**Año:** 2026")
        st.write("**Dataset:** BankMarketing.csv")

    st.divider()

    st.header("📊 Sobre el dataset")

    st.write(
        """
        El dataset **BankMarketing.csv** contiene información
        relacionada con clientes y campañas de marketing realizadas
        por una institución financiera.

        Las variables permiten analizar características de los clientes,
        información de contacto, resultados de campañas anteriores,
        duración de llamadas y la aceptación final de la campaña.
        """
    )

    st.divider()

    st.header("🛠️ Tecnologías utilizadas")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("🐍 Python")

    with col2:
        st.info("🐼 Pandas")

    with col3:
        st.info("📊 Streamlit")

    with col4:
        st.info("🐙 GitHub")

    st.success(
        "Seleccione el Módulo 2 desde el menú lateral para comenzar "
        "con la carga y exploración del dataset."
    )


# ============================================================
# MÓDULO 2: CARGA DEL DATASET
# ============================================================

elif modulos == "Modulo 2: Carga del dataset":

    st.title("📊 Módulo 2: Carga del Dataset")

    st.write(
        """
        En este módulo se realiza la carga, validación y exploración
        del dataset **Bank Marketing**. Se presentan diferentes
        elementos del análisis exploratorio de datos (EDA) para
        identificar relaciones y comportamientos relevantes.
        """
    )

    st.divider()

    # ========================================================
    # CONTEXTO DEL DATASET
    # ========================================================

    st.header("📌 Contexto del dataset")

    st.write(
        """
        Se entrega el archivo **BankMarketing.csv**, correspondiente
        a una institución financiera que busca entender los factores
        relacionados con la aceptación de sus campañas de marketing.

        Durante los últimos 6 meses, la efectividad de las campañas,
        medida como:

        **Efectividad = (Ventas / Base) × 100%**

        disminuyó de **12% a 8%**, situación que afectó los bonos de
        los ejecutivos comerciales.

        Por este motivo, el objetivo de este análisis es estudiar los
        datos de la última campaña para descubrir relaciones,
        comportamientos y características relevantes entre las
        diferentes variables.

        El análisis se desarrolla desde un enfoque exploratorio,
        buscando generar información útil para la **toma de decisiones**
        comerciales y para comprender mejor el comportamiento de los
        clientes.
        """
    )

    st.info(
        """
        🎯 **Objetivo del análisis**

        Identificar patrones y relaciones relevantes en los datos de
        la última campaña que puedan contribuir a comprender la caída
        de efectividad y apoyar futuras decisiones comerciales.
        """
    )

    st.warning(
        """
        ⚠️ El análisis es exploratorio. Las relaciones encontradas
        entre variables no deben interpretarse automáticamente como
        relaciones de causa y efecto.
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
    # LECTURA DEL ARCHIVO
    # ========================================================

    try:

        df = pd.read_csv(
            archivo,
            sep=";"
        )

    except Exception as e:

        st.error(
            f"❌ No fue posible leer el archivo: {e}"
        )

        st.stop()

    # ========================================================
    # VALIDACIÓN
    # ========================================================

    if df.empty:

        st.error(
            "❌ El archivo CSV está vacío."
        )

        st.stop()

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

        st.error(
            "❌ El archivo no contiene todas las columnas esperadas."
        )

        st.write(
            "Columnas faltantes:",
            columnas_faltantes
        )

        st.stop()

    st.success(
        "✅ El archivo fue cargado y validado correctamente."
    )

    # ========================================================
    # INFORMACIÓN DEL ARCHIVO
    # ========================================================

    st.header("📄 Información del archivo")

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
            "Tamaño",
            f"{archivo.size / 1024:.2f} KB"
        )

    # ========================================================
    # PREVISUALIZACIÓN
    # ========================================================

    st.subheader("👀 Vista previa del dataset")

    st.write(
        """
        A continuación se muestran las primeras filas del dataset
        para verificar visualmente que la información fue cargada
        correctamente.
        """
    )

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    # ========================================================
    # DATASET COMPLETO
    # ========================================================

    with st.expander("📋 Mostrar dataset completo"):

        st.dataframe(
            df,
            use_container_width=True
        )

    # ========================================================
    # OBJETO DE ANÁLISIS
    # ========================================================

    analyzer = DataAnalyzer(df)

    st.divider()

    st.header("🔎 Análisis Exploratorio de Datos (EDA)")

    st.write(
        """
        El siguiente análisis se encuentra organizado en diez
        secciones para estudiar las principales características,
        distribuciones y relaciones presentes en el dataset.
        """
    )

    # ========================================================
    # TABS DEL EDA
    # ========================================================

    tabs = st.tabs(
        [
            "1. Información general",
            "2. Clasificación",
            "3. Estadísticas",
            "4. Faltantes",
            "5. Distribuciones",
            "6. Categóricas",
            "7. Numérica vs objetivo",
            "8. Categórica vs objetivo",
            "9. Análisis dinámico",
            "10. Hallazgos"
        ]
    )

    # ========================================================
    # 1. INFORMACIÓN GENERAL
    # ========================================================

    with tabs[0]:

        st.subheader(
            "1. Información general del dataset"
        )

        st.write(
            """
            Esta sección permite conocer la estructura del dataset,
            sus tipos de datos y la cantidad de valores faltantes.
            """
        )

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
                "Valores totales",
                f"{df.size:,}"
            )

        st.subheader("Tipos de datos")

        tipos = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de dato": [
                str(tipo)
                for tipo in df.dtypes
            ],
            "Valores únicos": [
                df[columna].nunique()
                for columna in df.columns
            ],
            "Valores faltantes": [
                df[columna].isna().sum()
                for columna in df.columns
            ]
        })

        st.dataframe(
            tipos,
            use_container_width=True
        )

        st.subheader("Información técnica")

        buffer = io.StringIO()

        df.info(buf=buffer)

        st.text(
            buffer.getvalue()
        )

        st.write(
            """
            **Interpretación:** esta información permite verificar
            si las variables están correctamente almacenadas y conocer
            la estructura general antes de realizar análisis más
            específicos.
            """
        )

    # ========================================================
    # 2. CLASIFICACIÓN DE VARIABLES
    # ========================================================

    with tabs[1]:

        st.subheader(
            "2. Clasificación de variables"
        )

        st.write(
            """
            Las variables se clasifican en numéricas y categóricas.
            Esta clasificación permite seleccionar posteriormente
            las técnicas y gráficos apropiados para cada tipo de dato.
            """
        )

        numericas, categoricas = analyzer.clasificar_variables()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Variables numéricas",
                len(numericas)
            )

            st.write(numericas)

        with col2:

            st.metric(
                "Variables categóricas",
                len(categoricas)
            )

            st.write(categoricas)

        clasificacion = pd.DataFrame({
            "Variable": df.columns,
            "Tipo": [
                "Numérica"
                if columna in numericas
                else "Categórica"
                for columna in df.columns
            ]
        })

        st.dataframe(
            clasificacion,
            use_container_width=True
        )

        st.write(
            """
            **Interpretación:** las variables numéricas permiten
            estudiar medidas como media, mediana y dispersión,
            mientras que las variables categóricas permiten estudiar
            frecuencias, proporciones y diferencias entre grupos.
            """
        )

    # ========================================================
    # 3. ESTADÍSTICAS DESCRIPTIVAS
    # ========================================================

    with tabs[2]:

        st.subheader(
            "3. Estadísticas descriptivas"
        )

        st.write(
            """
            Se calculan estadísticas descriptivas para comprender
            la tendencia central y dispersión de las variables
            numéricas.
            """
        )

        numericas, _ = analyzer.clasificar_variables()

        st.dataframe(
            df[numericas].describe().T.round(2),
            use_container_width=True
        )

        st.subheader(
            "Media, mediana y moda"
        )

        variable_stats = st.selectbox(
            "Seleccione una variable numérica:",
            numericas
        )

        resumen = analyzer.resumen_variable(
            variable_stats
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Media",
                f"{resumen['Media']:.2f}"
            )

        with col2:
            st.metric(
                "Mediana",
                f"{resumen['Mediana']:.2f}"
            )

        with col3:
            st.metric(
                "Moda",
                f"{resumen['Moda']:.2f}"
            )

        st.write(
            f"""
            **Interpretación:** para la variable **{variable_stats}**,
            la media representa el promedio de los valores, la mediana
            representa el valor central y la moda corresponde al valor
            que aparece con mayor frecuencia.

            La comparación entre media y mediana permite observar si
            existe una posible asimetría en la distribución.
            """
        )

        st.write(
            f"""
            La desviación estándar de **{variable_stats}** es de
            **{resumen['Desviación estándar']:.2f}**, lo que permite
            evaluar la dispersión de los valores alrededor de su media.
            """
        )

    # ========================================================
    # 4. VALORES FALTANTES
    # ========================================================

    with tabs[3]:

        st.subheader(
            "4. Análisis de valores faltantes"
        )

        st.write(
            """
            Se revisa la existencia de datos faltantes para determinar
            si pueden afectar la interpretación de los resultados.
            """
        )

        faltantes = analyzer.valores_faltantes()

        st.dataframe(
            faltantes,
            use_container_width=True
        )

        total_faltantes = int(
            df.isna().sum().sum()
        )

        if total_faltantes == 0:

            st.success(
                "✅ No se encontraron valores faltantes en el dataset."
            )

        else:

            st.warning(
                f"⚠️ Se encontraron {total_faltantes:,} valores faltantes."
            )

            faltantes_grafico = (
                faltantes[
                    faltantes["Valores faltantes"] > 0
                ]
            )

            if not faltantes_grafico.empty:

                fig, ax = plt.subplots()

                faltantes_grafico[
                    "Valores faltantes"
                ].plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_title(
                    "Valores faltantes por variable"
                )

                ax.set_xlabel("Variable")
                ax.set_ylabel("Cantidad")

                plt.xticks(rotation=45)

                st.pyplot(fig)

                plt.close(fig)

        st.write(
            """
            **Interpretación:** cuando existen valores faltantes,
            es importante considerar su cantidad y distribución antes
            de realizar conclusiones. En caso contrario, los análisis
            pueden realizarse sobre la información disponible.
            """
        )

    # ========================================================
    # 5. DISTRIBUCIONES NUMÉRICAS
    # ========================================================

    with tabs[4]:

        st.subheader(
            "5. Distribuciones de variables numéricas"
        )

        st.write(
            """
            Los histogramas permiten visualizar cómo se distribuyen
            los valores de las principales variables numéricas.
            """
        )

        numericas, _ = analyzer.clasificar_variables()

        variables_hist = st.multiselect(
            "Seleccione las variables numéricas:",
            numericas,
            default=[
                variable
                for variable in [
                    "age",
                    "duration",
                    "campaign"
                ]
                if variable in numericas
            ]
        )

        bins = st.slider(
            "Número de intervalos del histograma:",
            min_value=5,
            max_value=50,
            value=20
        )

        if variables_hist:

            columnas = st.columns(
                min(2, len(variables_hist))
            )

            for i, variable in enumerate(variables_hist):

                with columnas[i % len(columnas)]:

                    fig = analyzer.histograma(
                        variable,
                        bins
                    )

                    st.pyplot(fig)

                    plt.close(fig)

                    resumen = analyzer.resumen_variable(
                        variable
                    )

                    st.write(
                        f"""
                        **{variable}:** media =
                        {resumen['Media']:.2f},
                        mediana =
                        {resumen['Mediana']:.2f}.
                        """
                    )

        else:

            st.info(
                "Seleccione al menos una variable."
            )

    # ========================================================
    # 6. VARIABLES CATEGÓRICAS
    # ========================================================

    with tabs[5]:

        st.subheader(
            "6. Análisis de variables categóricas"
        )

        st.write(
            """
            Se analizan las frecuencias y proporciones de las
            variables categóricas mediante tablas y gráficos
            de barras.
            """
        )

        _, categoricas = analyzer.clasificar_variables()

        variable_cat = st.selectbox(
            "Seleccione una variable categórica:",
            categoricas,
            index=(
                categoricas.index("job")
                if "job" in categoricas
                else 0
            )
        )

        conteos = analyzer.conteos_categoricos(
            variable_cat
        )

        proporciones = analyzer.proporciones_categoricas(
            variable_cat
        )

        tabla_cat = pd.DataFrame({
            "Cantidad": conteos,
            "Proporción (%)": proporciones
        })

        st.dataframe(
            tabla_cat,
            use_container_width=True
        )

        fig = analyzer.grafico_barras(
            variable_cat
        )

        st.pyplot(fig)

        plt.close(fig)

        st.write(
            f"""
            **Interpretación:** la tabla permite identificar qué
            categorías tienen mayor presencia en la variable
            **{variable_cat}** y qué porcentaje representan
            dentro del conjunto de datos.
            """
        )

    # ========================================================
    # 7. NUMÉRICA VS Y
    # ========================================================

    with tabs[6]:

        st.subheader(
            "7. Relación entre variable numérica y aceptación"
        )

        st.write(
            """
            Se comparan variables numéricas según el resultado de la
            campaña (`y`), donde `yes` representa aceptación y `no`
            representa no aceptación.
            """
        )

        numericas, _ = analyzer.clasificar_variables()

        variables_preferidas = [
            variable
            for variable in [
                "age",
                "duration",
                "campaign"
            ]
            if variable in numericas
        ]

        variable_num = st.selectbox(
            "Seleccione una variable numérica:",
            numericas,
            index=(
                numericas.index("duration")
                if "duration" in numericas
                else 0
            )
        )

        comparacion = analyzer.comparacion_grupos(
            variable_num,
            "y"
        )

        st.dataframe(
            comparacion,
            use_container_width=True
        )

        fig = analyzer.boxplot_por_grupo(
            variable_num,
            "y"
        )

        st.pyplot(fig)

        plt.close(fig)

        if "yes" in df["y"].unique() and "no" in df["y"].unique():

            media_yes = df.loc[
                df["y"] == "yes",
                variable_num
            ].mean()

            media_no = df.loc[
                df["y"] == "no",
                variable_num
            ].mean()

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Media cuando y = yes",
                    f"{media_yes:.2f}"
                )

            with col2:
                st.metric(
                    "Media cuando y = no",
                    f"{media_no:.2f}"
                )

            st.write(
                f"""
                **Interpretación:** la variable **{variable_num}**
                presenta diferencias entre los grupos `yes` y `no`.
                Esto permite identificar comportamientos asociados
                con distintos resultados de la campaña.

                Esta diferencia debe interpretarse como una relación
                observada en los datos y no necesariamente como una
                relación causal.
                """
            )

    # ========================================================
    # 8. CATEGÓRICA VS Y
    # ========================================================

    with tabs[7]:

        st.subheader(
            "8. Relación entre variable categórica y aceptación"
        )

        st.write(
            """
            Se estudia cómo cambia la aceptación de la campaña
            según diferentes categorías de clientes o características
            de contacto.
            """
        )

        _, categoricas = analyzer.clasificar_variables()

        categoricas_sin_y = [
            variable
            for variable in categoricas
            if variable != "y"
        ]

        variable_cat_y = st.selectbox(
            "Seleccione una variable categórica:",
            categoricas_sin_y,
            index=(
                categoricas_sin_y.index("education")
                if "education" in categoricas_sin_y
                else 0
            )
        )

        tabla = analyzer.tabla_cruzada(
            variable_cat_y,
            "y"
        )

        tabla_prop = analyzer.tabla_proporciones(
            variable_cat_y,
            "y"
        )

        st.subheader("Frecuencias")

        st.dataframe(
            tabla,
            use_container_width=True
        )

        st.subheader(
            "Proporciones de aceptación por categoría (%)"
        )

        st.dataframe(
            tabla_prop,
            use_container_width=True
        )

        if "yes" in tabla_prop.columns:

            fig, ax = plt.subplots()

            tabla_prop["yes"].plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                f"Aceptación según {variable_cat_y}"
            )

            ax.set_xlabel(
                variable_cat_y
            )

            ax.set_ylabel(
                "Aceptación (%)"
            )

            plt.xticks(rotation=45)

            st.pyplot(fig)

            plt.close(fig)

        st.write(
            f"""
            **Interpretación:** la proporción de aceptación puede
            variar entre las categorías de **{variable_cat_y}**.
            Esta información puede ayudar a identificar segmentos
            donde la campaña presenta comportamientos diferentes.
            """
        )

    # ========================================================
    # 9. ANÁLISIS DINÁMICO
    # ========================================================

    with tabs[8]:

        st.subheader(
            "9. Análisis basado en parámetros seleccionados"
        )

        st.write(
            """
            Esta sección permite realizar un análisis dinámico.
            El usuario puede seleccionar una variable, varias
            variables numéricas y categorías específicas para
            explorar diferentes segmentos del dataset.
            """
        )

        numericas, categoricas = analyzer.clasificar_variables()

        variable_principal = st.selectbox(
            "Variable principal:",
            df.columns.tolist()
        )

        variables_numericas = st.multiselect(
            "Variables numéricas para analizar:",
            numericas,
            default=[
                variable
                for variable in [
                    "age",
                    "duration"
                ]
                if variable in numericas
            ]
        )

        variable_filtro = st.selectbox(
            "Variable categórica para filtrar:",
            categoricas
        )

        categorias_disponibles = sorted(
            df[variable_filtro]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        categorias_seleccionadas = st.multiselect(
            "Seleccione categorías:",
            categorias_disponibles
        )

        aplicar_filtro = st.checkbox(
            "Aplicar filtro seleccionado"
        )

        limite = st.slider(
            "Cantidad máxima de filas a mostrar:",
            min_value=10,
            max_value=500,
            value=100,
            step=10
        )

        df_dinamico = df.copy()

        if aplicar_filtro and categorias_seleccionadas:

            df_dinamico = df_dinamico[
                df_dinamico[
                    variable_filtro
                ].astype(str).isin(
                    categorias_seleccionadas
                )
            ]

        st.metric(
            "Filas resultantes",
            f"{len(df_dinamico):,}"
        )

        st.subheader(
            "Resultado del análisis"
        )

        columnas_mostrar = [
            variable_principal
        ]

        for variable in variables_numericas:

            if variable not in columnas_mostrar:

                columnas_mostrar.append(
                    variable
                )

        st.dataframe(
            df_dinamico[
                columnas_mostrar
            ].head(limite),
            use_container_width=True
        )

        if variables_numericas and not df_dinamico.empty:

            st.subheader(
                "Estadísticas de las variables seleccionadas"
            )

            st.dataframe(
                df_dinamico[
                    variables_numericas
                ].describe().T.round(2),
                use_container_width=True
            )

        st.write(
            """
            **Interpretación:** el análisis dinámico permite explorar
            diferentes segmentos sin modificar el código. Esto facilita
            comparar comportamientos y obtener información específica
            para apoyar la toma de decisiones.
            """
        )

    # ========================================================
    # 10. HALLAZGOS CLAVE
    # ========================================================

    with tabs[9]:

        st.subheader(
            "10. Hallazgos clave y toma de decisiones"
        )

        st.write(
            """
            Esta sección resume algunos comportamientos relevantes
            identificados a partir del análisis exploratorio.
            """
        )

        # ----------------------------------------------------
        # DISTRIBUCIÓN DEL OBJETIVO
        # ----------------------------------------------------

        conteo_y = df["y"].value_counts()

        porcentaje_y = (
            df["y"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Resultado de la campaña"
            )

            st.dataframe(
                pd.DataFrame({
                    "Cantidad": conteo_y,
                    "Porcentaje (%)": porcentaje_y
                }),
                use_container_width=True
            )

        with col2:

            fig, ax = plt.subplots()

            conteo_y.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                "Distribución de aceptación"
            )

            ax.set_xlabel(
                "Resultado"
            )

            ax.set_ylabel(
                "Cantidad"
            )

            plt.xticks(rotation=0)

            st.pyplot(fig)

            plt.close(fig)

        # ----------------------------------------------------
        # DURACIÓN
        # ----------------------------------------------------

        if "duration" in df.columns:

            media_duration_yes = df.loc[
                df["y"] == "yes",
                "duration"
            ].mean()

            media_duration_no = df.loc[
                df["y"] == "no",
                "duration"
            ].mean()

            st.subheader(
                "Duración de las llamadas"
            )

            st.write(
                f"""
                La duración promedio de las llamadas que terminaron
                en aceptación (`yes`) fue de aproximadamente
                **{media_duration_yes:.0f} segundos**, mientras que
                en las que terminaron en no aceptación (`no`) fue de
                aproximadamente **{media_duration_no:.0f} segundos**.

                Esto muestra una diferencia importante en la duración
                de las interacciones entre ambos grupos.
                """
            )

        # ----------------------------------------------------
        # CONTACTO
        # ----------------------------------------------------

        if "contact" in df.columns:

            tabla_contacto = pd.crosstab(
                df["contact"],
                df["y"],
                normalize="index"
            ).mul(100).round(2)

            st.subheader(
                "Resultado según canal de contacto"
            )

            st.dataframe(
                tabla_contacto,
                use_container_width=True
            )

            if "yes" in tabla_contacto.columns:

                canal_mejor = (
                    tabla_contacto["yes"]
                    .idxmax()
                )

                porcentaje_mejor = (
                    tabla_contacto["yes"]
                    .max()
                )

                st.write(
                    f"""
                    En los datos analizados, el canal **{canal_mejor}**
                    presenta la mayor proporción observada de aceptación,
                    con aproximadamente **{porcentaje_mejor:.2f}%**.

                    Este resultado puede ser considerado como un elemento
                    para evaluar la estrategia de contacto de futuras
                    campañas.
                    """
                )

        # ----------------------------------------------------
        # POUTCOME
        # ----------------------------------------------------

        if "poutcome" in df.columns:

            tabla_poutcome = pd.crosstab(
                df["poutcome"],
                df["y"],
                normalize="index"
            ).mul(100).round(2)

            st.subheader(
                "Resultado según campañas anteriores"
            )

            st.dataframe(
                tabla_poutcome,
                use_container_width=True
            )

            if "yes" in tabla_poutcome.columns:

                categoria_mejor = (
                    tabla_poutcome["yes"]
                    .idxmax()
                )

                porcentaje_mejor = (
                    tabla_poutcome["yes"]
                    .max()
                )

                st.write(
                    f"""
                    La categoría **{categoria_mejor}** presenta la mayor
                    proporción observada de aceptación, aproximadamente
                    **{porcentaje_mejor:.2f}%**.

                    Esto sugiere que el historial de campañas anteriores
                    puede ser una variable relevante para segmentar y
                    priorizar esfuerzos comerciales.
                    """
                )

        # ----------------------------------------------------
        # CONCLUSIONES
        # ----------------------------------------------------

        st.subheader(
            "🎯 Conclusiones para la toma de decisiones"
        )

        st.markdown(
            """
            **1. La aceptación de la campaña es relativamente baja.**

            La distribución de la variable objetivo `y` muestra que
            la aceptación representa una proporción menor del total
            de contactos. Debido al contexto de reducción de efectividad
            de **12% a 8%**, resulta importante revisar cómo se asignan
            los esfuerzos comerciales.

            **2. La duración de las llamadas presenta diferencias
            entre los resultados.**

            Las llamadas que terminan en aceptación presentan una
            duración promedio diferente respecto a las llamadas que
            terminan en no aceptación. Este comportamiento puede servir
            para estudiar la calidad y características de las
            interacciones comerciales.

            **3. El canal de contacto presenta diferencias en la
            aceptación.**

            Los resultados muestran que la proporción de aceptación
            cambia según el medio utilizado para contactar al cliente.
            Esta información puede ser considerada al momento de revisar
            la estrategia de contacto.

            **4. El resultado de campañas anteriores es relevante
            para la segmentación.**

            Las categorías de `poutcome` presentan diferentes niveles
            de aceptación. Por ello, el historial disponible puede ser
            útil para priorizar determinados segmentos de clientes.

            **5. La segmentación permite orientar mejor los recursos
            comerciales.**

            Las diferencias observadas según características de los
            clientes, canales de contacto y antecedentes de campañas
            permiten plantear estrategias diferenciadas en lugar de
            utilizar un único enfoque para toda la base.

            En conjunto, estos hallazgos permiten comprender mejor el
            comportamiento de la última campaña y generan información
            útil para apoyar decisiones destinadas a mejorar la gestión
            comercial y evaluar posibles acciones frente a la caída de
            efectividad.
            """
        )

        st.success(
            """
            ✅ **Conclusión general:** el análisis exploratorio permite
            identificar diferencias importantes entre grupos de clientes
            y características de las interacciones. Estos resultados
            pueden utilizarse como base para revisar la segmentación,
            los canales de contacto y la asignación de recursos en
            futuras campañas.
            """
        )
