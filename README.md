
# Language Academy Management Automation

Aplicación desarrollada para centralizar la gestión de alumnos de una academia de idiomas y automatizar tareas administrativas que habitualmente se realizan de forma manual mediante Excel y correo electrónico.

El proyecto nace como un ejemplo de cómo automatizar procesos internos de un negocio utilizando Python, transformando un flujo basado en hojas de cálculo en una aplicación sencilla y visual.

## Features

### Student management

- Visualización de alumnos desde una interfaz web.
- Edición directa de los datos.
- Alta de nuevos alumnos.
- Eliminación de alumnos.
- Gestión de información como:
  - Nombre y apellidos
  - Email
  - Idioma
  - Nivel
  - Estado de pago
  - Estado activo/inactivo

Los datos se almacenan actualmente en un archivo Excel, permitiendo integrar la aplicación con un flujo de trabajo existente basado en hojas de cálculo.

### Dashboard

Panel con información relevante sobre el estado de la academia:

- Número de alumnos activos.
- Porcentaje de pagos pendientes.
- Distribución de alumnos por idioma.
- Distribución de alumnos por nivel.
- Visualizaciones interactivas.

### Email automation

Sistema de envío de correos electrónicos mediante SMTP.

Permite:

- Filtrar destinatarios por diferentes características.
- Seleccionar múltiples idiomas o niveles.
- Filtrar por estado de pago o estado del alumno.
- Enviar mensajes a múltiples alumnos.
- Personalizar el contenido de los mensajes para cada destinatario.

## Tech Stack

- **Python**
- **Streamlit**
- **pandas**
- **Plotly**
- **SMTP**
- **openpyxl**

## Architecture

El proyecto mantiene separada la interfaz de usuario de la lógica relacionada con el acceso y modificación de los datos.

```text
project/
├── app.py
├── pages/
│   ├── alumnos.py
│   └── ...
├── utils/
│   ├── excel.py
│   └── ...
├── data/
│   └── alumnos.xlsx
├── .streamlit/
│   └── secrets.toml
├── requirements.txt
└── README.md
```

> `secrets.toml` contiene información sensible y no debe incluirse en el repositorio.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Para utilizar el sistema de envío de correos es necesario configurar las credenciales SMTP.

Crea:

```text
.streamlit/secrets.toml
```

y añade:

```toml
EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

Para Gmail se recomienda utilizar una **App Password** en lugar de la contraseña principal de la cuenta.

No subas este archivo al repositorio.

Añádelo al `.gitignore`:

```gitignore
.streamlit/secrets.toml
```

## Running the application

Ejecuta:

```bash
streamlit run app.py
```

Streamlit iniciará la aplicación y proporcionará una dirección local desde la que acceder a ella.

## Demo

A public demo will be available soon.

> La versión pública utilizará datos ficticios y limitará las funcionalidades sensibles, como el envío real de emails.

## Purpose

Aunque el caso de uso utilizado es una academia de idiomas, el objetivo del proyecto es demostrar cómo pueden automatizarse procesos administrativos comunes en diferentes tipos de negocios.

La misma arquitectura puede adaptarse a procesos como:

- Gestión de clientes.
- Seguimiento de pagos.
- Comunicación automatizada.
- Gestión de registros.
- Dashboards de negocio.
- Automatización de tareas basadas en Excel.

## Future improvements

- Migración de Excel a una base de datos.
- Sistema de autenticación.
- Roles y permisos.
- Gestión de grupos y profesores.
- Historial de pagos.
- Plantillas de correo reutilizables.
- Automatización de recordatorios.
- Mayor control de validación de datos.

## Status

🚧 **Work in progress**

El proyecto se encuentra en desarrollo activo como parte de un portfolio de soluciones de automatización para negocios.
