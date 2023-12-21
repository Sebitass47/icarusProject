
Breve descripción de tu aplicación.

## Requisitos

- Python 3.x
- pip (instalado con Python)

## Configuración del Entorno

1. **Crea un entorno virtual (opcional pero recomendado):**

```bash
   python -m venv venv
```

2. **Activa el entorno virtual**

En Windows:

```bash
    .\venv\Scripts\activate
```
En Linux/Mac:

```bash
    source venv/bin/activate
```

3. **Instala las dependencias**


```bash
    pip install -r requirements.txt
```

## Ejecutar la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
    flask --app run run
```

La aplicación estará disponible en http://127.0.0.1:5000/.

## Base de Datos

### Tabla: personas
- id: Identificador único de la persona (clave primaria).
- nombre: Nombre de la persona (único y no nulo).

### Tabla: bitacora
- id: Identificador único de la entrada en la bitácora (clave primaria).
- busqueda_nombre: Nombre buscado en la bitácora (no nulo).
- fecha_busqueda: Fecha y hora de la búsqueda en la bitácora (no nulo).
- resultado: Resultado de la búsqueda (booleano, no nulo).
- persona_id: Clave foránea que hace referencia al id en la tabla personas (puede ser nulo).

## API

### Ruta: /buscar (Método POST)
Esta ruta permite buscar un nombre en la base de datos.

#### Parámetros de Entrada:
nombre (obligatorio): Nombre que se desea buscar.

#### Respuesta JSON:
```json
    {
    "encontrado": true
    }
```

encontrado: Valor booleano que indica si se encontró el nombre en la base de datos.

## Ejecutar Pruebas
Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
python tests.py
```