import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 

    def setUp(self): 
        self.client = app.test_client()
    
    def test_home_endpoint_returns_ok_and_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json.get("message"), "API is running")

    def test_login_endpoint_provides_token(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200) 
        self.assertTrue('access_token' in response.json)

    def test_protected_endpoint_is_unauthorized_without_token(self):
        """ Testa se a rota protegida (/protected) barra o acesso sem token. """
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401) 

if __name__ == '__main__':
    unittest.main()