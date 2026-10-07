import streamlit as st  

# NAVEGACIÓN
pagina_inicio = st.Page('pages/inicio.py', title='Inicio', icon='🏠')
pagina_alumnos = st.Page('pages/alumnos.py', title='Alumnos', icon='🧑🏻‍🎓')
pagina_enviar_correo = st.Page('pages/enviar_correo.py', title='Enviar correo', icon='📨')
navegacion = st.navigation([pagina_inicio, pagina_alumnos, pagina_enviar_correo])
navegacion.run()