import unittest
import requests

class TestBuscarAPI(unittest.TestCase):
    """
        ### Clase de pruebas unitarias para el endpoint de búsqueda en la API.

        #### Métodos de prueba:
            - test_buscar_persona_existente: Prueba el caso en que se busca una persona existente.
            - test_buscar_persona_inexistente: Prueba el caso en que se busca una persona inexistente.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_buscar_persona_existente(self):
        """
            ### Prueba la búsqueda de una persona existente en la base de datos.

            #### Se espera que el servidor responda con un código de estado 200 y un JSON con la clave 'encontrado' en True.
        """
        payload = {"nombre": "sebastian martinez"}
        response = requests.post("http://localhost:5000/buscar", json=payload)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue("encontrado" in data)
        self.assertTrue(data["encontrado"])

    def test_buscar_persona_inexistente(self):
        """
            ### Prueba la búsqueda de una persona inexistente en la base de datos.

            #### Se espera que el servidor responda con un código de estado 200 y un JSON con la clave 'encontrado' en False.
        """
        payload = {"nombre": "juan carlos villegas"}
        response = requests.post("http://localhost:5000/buscar", json=payload)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertTrue("encontrado" in data)
        self.assertFalse(data["encontrado"])

if __name__ == '__main__':
    unittest.main()
