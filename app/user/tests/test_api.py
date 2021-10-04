from django.test import TestCase

class ApiTestCase(TestCase):
    def test_inicial(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
