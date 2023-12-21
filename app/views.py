from flask import jsonify, request, abort
from run import app
from app.managers import *
# from app.models import buscar_en_bd

# En views.py
@app.route('/buscar', methods=['POST'])
def buscar():
    """
    Endpoint para buscar un nombre en la base de datos.

    Método HTTP: POST

    Parámetros de entrada (JSON):
    - nombre (str, obligatorio): Nombre que se desea buscar en la base de datos.

    Respuesta (JSON):
    - encontrado (bool): Indica si se encontró el nombre en la base de datos.

    Códigos de estado HTTP:
    - 200 OK: La solicitud fue exitosa.
    - 400 Bad Request: El parámetro 'nombre' es requerido o está malformado.
    - 500 Internal Server Error: Error interno del servidor.

    Ejemplo de solicitud:
    ```
    curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Ejemplo"}' http://localhost:5000/buscar
    ```

    Ejemplo de respuesta exitosa:
    ```
    {"encontrado": true}
    ```

    Ejemplo de respuesta cuando el nombre no se encuentra:
    ```
    {"encontrado": false}
    """
    try:
        data = request.get_json()
        name = data.get('nombre')

        if not name:
            abort(400, description="El parámetro 'nombre' es requerido.")

        result = search_person(name)
        return jsonify({"encontrado": result})

    except Exception as e:
        abort(500, description="Error interno del servidor.")