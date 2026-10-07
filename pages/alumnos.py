import streamlit as st

from utils.excel import obtener_alumnos, guardar_alumnos, obtener_idiomas, lista_niveles, nuevo_alumno

def on_click_enviar():
    datos = obtener_alumnos()
    try:
        # Obtenemos variables del formulario
        nombre = st.session_state['nombre']
        apellidos = st.session_state['apellidos']
        email = st.session_state['email']
        idioma = st.session_state['idioma']
        if idioma == 'Otro':
            idioma = st.session_state['nuevo_idioma']
        nivel = st.session_state['nivel']
        if nivel == 'Otro':
            nivel = st.session_state['nuevo_nivel']
        pagado = st.session_state['pagado']
        activo = st.session_state['activo']

        # Guardamos el nuevo alumno
        datos = nuevo_alumno(datos, nombre, apellidos, email, idioma, nivel, pagado, activo)
        guardar_alumnos(datos)
        st.session_state['exito_añadir'] = True

        # Reiniciar el formulario
        st.session_state['nombre'] = ''
        st.session_state['apellidos'] = ''
        st.session_state['email'] = ''
        st.session_state['idioma'] = 'Inglés'
        st.session_state['nivel'] = 'A1'
        st.session_state['pagado'] = False
        st.session_state['activo'] = False
    except Exception as e:
        print(e)
        st.session_state['exito_añadir'] = False

def on_click_eliminar():
    datos = obtener_alumnos()
    indice = st.session_state['id_alumno']
    if 0 <= indice and indice < len(datos):
        datos = datos.drop(indice)
        guardar_alumnos(datos)
        st.session_state['exito_eliminar'] = True
    else:
        st.session_state['exito_eliminar'] = False

st.title('Alumnos')

# EDICIÓN DEL DATAFRAME
datos = obtener_alumnos()
df_actualizado = st.data_editor(datos, key='editor_alumnos')

if st.button('Guardar cambios'):
    guardar_alumnos(df_actualizado)
    st.success('Cambios guardados correctamente')


# FORMULARIO PARA LA INSERCIÓN DE UN NUEVO ALUMNO
with st.container(border=True):
    st.subheader('Inserción de alumno   ')
    col1, col2  = st.columns(2)
    with col1:
        nombre = st.text_input('Nombre', key='nombre')

    with col2:
        apellidos = st.text_input('Apellidos', key='apellidos')

    email = st.text_input('Email', key='email')

    col1, col2 = st.columns(2)

    with col1:
        lista_idiomas = obtener_idiomas(datos).index.to_list() + ['Otro']
        idioma = st.selectbox('Idioma', lista_idiomas, key='idioma')
        if idioma == 'Otro':
            idioma = st.text_input('Nuevo idioma', key='nuevo_idioma')

    with col2:
        listado_niveles = lista_niveles(datos).tolist() + ['Otro']
        nivel = st.selectbox('Nivel', listado_niveles, key='nivel')
        if nivel == 'Otro':
            nivel = st.text_input('Nuevo nivel', key='nuevo_nivel')

    col1, col2 = st.columns(2)

    with col1:
        pagado = st.toggle('Pagado', key='pagado')

    with col2:
        activo = st.toggle('Activo', key='activo')

    if st.button('Añadir alumno', on_click=on_click_enviar):
        if st.session_state['exito_añadir']:
            st.success('Alumno añadido correctamente')
        else:
            st.error('El alumno no se pudo añadir correctamente')

# ELIMINACIÓN DE ALUMNOS
with st.form('eliminacion_alumnos', clear_on_submit=True):
    st.subheader('Eliminación de alumno')

    indice = st.number_input('Id del alumno', step=1, key='id_alumno')
    if st.form_submit_button('Eliminar', on_click=on_click_eliminar):
        if st.session_state['exito_eliminar']:
            st.success('Alumno eliminado correctamente')
        else:
            st.error('Id incorrecto')