import streamlit as st
import plotly.express as px
import pandas as pd

from utils.excel import obtener_alumnos, alumnos_activos, porcentaje_impagos, obtener_idiomas, obtener_nivel

st.title('Dashboard de la Academia')

# KPIs PRINCIPALES
col1, col2 = st.columns(2)
datos = obtener_alumnos()

with col1:
    st.metric('Alumnos activos', alumnos_activos(datos))

with col2:
    st.metric('Impagos', porcentaje_impagos(datos), format='percent')

# GRÁFICO DE ALUMNOS POR IDIOMA
idiomas = obtener_idiomas(datos)
df_idiomas = pd.DataFrame({
    'Idiomas': idiomas.index,
    'Alumnos': idiomas.values
})


fig = px.pie(
    df_idiomas, 
    names='Idiomas', 
    values='Alumnos',
    title='Porcentaje de alumnos por idioma'
)
st.plotly_chart(fig)

# GRÁFICO DE BARRAS DE ALUMNOS POR NIVEL EN CADA IDIOMA
columnas = st.columns(idiomas.size)
for i, idioma in enumerate(idiomas.index):
    with columnas[i]:
        niveles = obtener_nivel(datos, idioma)
        df_niveles = pd.DataFrame({
            'Nivel': niveles.index,
            'Alumnos': niveles.values
        })

        fig = px.bar(
            df_niveles, 
            x='Alumnos', 
            y='Nivel',
            title=f'Alumnos por nivel ({idioma})',
            color='Nivel'
        )
        st.plotly_chart(fig)