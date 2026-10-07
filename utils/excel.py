import pandas as pd

RUTA_EXCEL = 'data/academia_alumnos_demo.xlsx'

def obtener_alumnos():
    """
    Lee el excel de los datos de los alumnos
    
    Returns:
        Dataframe con los datos de los alumnos
    """
    return pd.read_excel(RUTA_EXCEL)

def guardar_alumnos(datos : pd.DataFrame):
    """
    Guarda los alumnos en el excel

    Args:
        datos: Dataframe con los datos de los alumnos
    """
    datos.to_excel(RUTA_EXCEL, index=False)

def alumnos_activos(datos: pd.DataFrame):
    """
    Devuelve el número de alumnos que están marcados como activos

    Args:
        datos: Dataframe con los datos de los alumnos

    Returns:
        Número de alumnos activos
    """

    return (datos['Activo'] == 'Sí').sum()

def porcentaje_impagos(datos: pd.DataFrame):
    """
    Devuelve el porcentaje de alumnos activos que no han pagado

    Args:
        datos: Dataframe con los datos de los alumnos

    Returns:
        Porcentaje de impagos
    """
    df_activos = datos[datos['Activo'] == 'Sí']
    numero_alumnos_activos = df_activos.shape[0]

    if numero_alumnos_activos > 0:
        numero_impagos = (df_activos['Estado_Pago'] == 'Pendiente').sum()
        return numero_impagos / numero_alumnos_activos
    else:
        return None

def obtener_idiomas(datos: pd.DataFrame):
    """
    Dado un dataframe devuelve una lista con los idiomas

    Args:
        datos: Dataframe con los datos de los alumnos

    Returns:
        Series el número de alumnos cursando cada idioma
    """
    return datos['Idioma'].value_counts()

def obtener_nivel(datos: pd.DataFrame, idioma):
    """
    Dado un DataFrame y un idioma devuelve una lista con los alumnos que hay en cada nivel de dicho idioma

    Args:
        datos: DataFrame con los alumnos
        idioma: Idioma del cual queremos ver el número de alumnos por nivel

    Returns:
        Serie con el número de alumnos por nivel en el idioma seleccionado
    """

    return datos[datos['Idioma'] == idioma]['Nivel'].value_counts()

def lista_niveles(datos: pd.DataFrame):
    """
    Dado un DataFrame devuelve la lista de los diferentes niveles que hay en el dataset.

    Args:
        datos: DataFrame con los alumnos
    
    Returns:
        Array de los diferentes niveles en datos
    """
    return datos['Nivel'].unique()

def nuevo_alumno(datos: pd.DataFrame, nombre, apellidos, email, idioma, nivel, pagado, activo):
    """
    Introduce un nuevo alumno en el dataframe

    Args:
        datos: DataFrame con los alumnos
        nombre: Nombre del nuevo alumno
        apellidos: Apellidos del nuevo alumno
        email: email del nuevo alumno
        idioma: idioma en el que se matricula el nuevo alumno
        nivel: nivel en el que se matricula el nuevo alumno
        pagado: True si esta pagado y False si no esta pagado
        activo: True si esta activo y False si no esta activo

    Returns:
        Devuelve el dataset con el nuevo alumno introducido
    """

    alumno = {
        'Nombre': nombre,
        'Apellidos': apellidos,
        'Email': email,
        'Idioma': idioma,
        'Nivel': nivel,
        'Estado_Pago': 'Pagado' if idioma else 'Pendiente',
        'Activo': 'Si' if activo else 'No'
    }

    datos.loc[len(datos)] = alumno
    return datos