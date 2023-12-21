import sqlite3
from datetime import datetime
from config import ConfigDataBase

def search_person(name):
    """
        ### Busca una persona en la base de datos por nombre.

        #### Parámetros:
        - name (str): Nombre de la persona a buscar.

        #### Retorna:
        - bool: True si se encontró la persona, False si no se encontró.

        #### Ejemplo de uso:
        ```python
            result = search_person("Ejemplo")
        ```

        La función también registra la búsqueda en la bitácora utilizando la función log_search.
    """
    cleaned_name = name.strip().lower()
    with sqlite3.connect(ConfigDataBase.DATABASE_URI) as conn:
        cursor = conn.cursor()
        person = cursor.execute('SELECT id FROM personas WHERE lower(trim(nombre)) = ?', (cleaned_name,)).fetchone()
        if person:
            log_search(True, cleaned_name, person[0])
            return True
        else:
            log_search(False, cleaned_name, None)
            return False

def log_search(result, search_name, person_id):
    """
        ### Registra una búsqueda en la bitácora.

        #### Parámetros:
        - result (bool): Resultado de la búsqueda.
        - search_name (str): Nombre buscado.
        - person_id (int or None): ID de la persona encontrada o None si no se encontró ninguna.

        #### Ejemplo de uso:
        ```python
            log_search(True, "Ejemplo", 1)
        ```

        Esta función inserta un registro en la tabla 'bitacora' con la información de la búsqueda.
    """
    with sqlite3.connect(ConfigDataBase.DATABASE_URI) as conn:
        cursor = conn.cursor()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO bitacora (busqueda_nombre, fecha_busqueda, resultado, persona_id) VALUES (?, ?, ?, ?)',
                       (search_name, now, result, person_id))
        conn.commit()