# database.py

import sqlite3
from config import ConfigDataBase

def create_tables():
    """
        Crea las tablas necesarias en la base de datos si no existen.

        La función crea las siguientes tablas:
        - Tabla 'personas': Almacena información sobre las personas.
            - id (int): Identificador único (clave primaria).
            - nombre (str): Nombre de la persona (único y no nulo).

        - Tabla 'bitacora': Registra las búsquedas realizadas.
            - id (int): Identificador único (clave primaria).
            - busqueda_nombre (str): Nombre buscado en la bitácora (no nulo).
            - fecha_busqueda (str): Fecha y hora de la búsqueda en la bitácora (no nulo).
            - resultado (bool): Resultado de la búsqueda (no nulo).
            - persona_id (int): Clave foránea que hace referencia al id en la tabla personas (puede ser nulo).

        Ejemplo de uso:
        ```python
            create_tables()
        ```

        Nota: Esta función debe ejecutarse al inicio de la aplicación para asegurar que las tablas estén disponibles.
    """
    with sqlite3.connect(ConfigDataBase.DATABASE_URI) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_nombre ON personas (LOWER(TRIM(nombre)));
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bitacora (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                busqueda_nombre TEXT NOT NULL,
                fecha_busqueda TEXT NOT NULL,
                resultado BOOLEAN NOT NULL,
                persona_id INTEGER, -- Nueva columna para la clave foránea
                FOREIGN KEY (persona_id) REFERENCES personas(id) ON DELETE SET NULL
            )
        ''')
        conn.commit()
