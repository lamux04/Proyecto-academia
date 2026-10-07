import streamlit as st
import smtplib
from email.message import EmailMessage

HOST_SMTP = 'smtp.gmail.com'
PUERTO_SMTP = 587

def procesar_contenido(contenido: str, clave: str, valor: str):
    """
    Dado un string, cambia las apariciones de clave por valor

    Args:
        contenido: String original
        clave: String a buscar
        valor: String por el cual se modificará clave

    Returns:
        Devuelve el nuevo string modificado
    """
    return contenido.replace(clave, valor)

def enviar_varios_email(destinos: list, asunto: str, contenido: str, clave = '', lista_valores = []):
    """
    Envia un email a varios destinos permitiendo personalizar el email mediante una clave

    Args:
        destinos: Lista con los correos de los destinatarios
        asunto: Asunto del mensaje
        contenido: Contenido del mensaje
        clave: Clave utilizada para identificar los valores que queremos reemplazar
        lista_valores: Lista de valores del mismo tamaño que destinos que reemplazara clave por estos valores por cada destino
    """
    # Abrimos la conexión SMPT
    servidor = smtplib.SMTP(HOST_SMTP, PUERTO_SMTP)
    servidor.starttls()
    servidor.login(st.secrets['EMAIL'], st.secrets['EMAIL_PASSWORD'])


    # Mandar mensaje a cada destino
    for i, destino in enumerate(destinos):
        # Creo el objeto con el mensaje
        mensaje = EmailMessage()
        mensaje['From'] = st.secrets['EMAIL']
        mensaje['To'] = destino
        mensaje['Subject'] = asunto
        contenido_procesado = procesar_contenido(contenido, clave, lista_valores[i]) if clave != '' else contenido
        mensaje.set_content(contenido_procesado)

        # Enviamos el mensaje personalizado
        servidor.send_message(mensaje)
        print(f'Correo enviado a {destino}')

    # Cerrar sesión del servidor
    servidor.quit()