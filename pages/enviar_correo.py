import streamlit as st
import pandas as pd

from utils.excel import obtener_alumnos, obtener_idiomas, lista_niveles
from utils.correo import enviar_varios_email

st.title('Enviar correo')

tab1, tab2 = st.tabs(['Por alumnos', 'Por grupos'])

datos = obtener_alumnos()

# ENVIO DE CORREOS A UN ALUMNO
with tab1:
    st.header('Enviar correo a alumnos')

    # Formulario de envío
    with st.form('Enviar correo', clear_on_submit=True):
        # Relacionamos cada alumno con su correo
        nombre_alumnos = datos['Nombre'] + ' ' + datos['Apellidos']
        correos_alumnos = datos['Email']
        alumno_correo = pd.Series(data=correos_alumnos.to_list(), index=nombre_alumnos.to_list())

        # Seleccionamos los alumnos que queremos
        seleccion_alumnos = st.multiselect('Selecciona alumnos', nombre_alumnos)
        correos_a_enviar = alumno_correo[seleccion_alumnos]

        # Asunto y contenido
        asunto = st.text_input('Asunto del mensaje')
        contenido = st.text_area('Contenido del mensaje')

        # Enviar mensaje
        if st.form_submit_button('Enviar mensaje'):
            enviar_varios_email(correos_a_enviar, asunto, contenido, '{{nombre}}', seleccion_alumnos)
            st.success('Correos enviados correctamente')



# ENVÍO DE CORREOS A VARIOS ALUMNOS
with tab2:
    st.header('Enviar correo a grupos de clase')

    # Enviar correos por grupos
    with st.form('Enviar correos por grupos', clear_on_submit=True):
        st.write('Si alguno de los filtros se queda vacío, no se aplicará dicho filtro')
        # Filtros
        idiomas = obtener_idiomas(datos).index
        idiomas_seleccionados = st.multiselect('Idioma', idiomas)
        if idiomas_seleccionados == []:
            idiomas_seleccionados = idiomas

        niveles = lista_niveles(datos)
        niveles_seleccionados = st.multiselect('Nivel', niveles)
        if niveles_seleccionados == []:
            niveles_seleccionados = niveles

        opciones_pagado = ['Pagado', 'Pendiente']
        pagado = st.multiselect('Estado de Pago', opciones_pagado)
        if pagado == []:
            pagado = opciones_pagado

        opciones_activo = ['Sí', 'No']
        activo = st.multiselect('Activo', opciones_activo)
        if activo == []:
            activo = opciones_activo

        # Asunto y contenido del mensaje
        asunto = st.text_input('Asunto del mensaje')
        contenido = st.text_area('Contenido del mensaje')


        # Filtrar datos
        condicion = (datos['Idioma'].isin(idiomas_seleccionados) 
                     & datos['Nivel'].isin(niveles_seleccionados) 
                     & datos['Estado_Pago'].isin(pagado) 
                     & datos['Activo'].isin(activo))
        datos_filtrados = datos[condicion]


        # Enviar mensaje
        if st.form_submit_button('Enviar'):
            enviar_varios_email(datos_filtrados['Email'].to_list(), asunto, contenido, '{{nombre}}', datos_filtrados['Nombre'].to_list())
            st.success('Correos enviados correctamente')