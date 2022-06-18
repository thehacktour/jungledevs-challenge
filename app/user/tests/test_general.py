from django.test import TestCase
from rest_framework import status

def test_inicial(self):
    response = self.client.get('http://localhost:8000/api/oficial/user/')
    self.assertEqual(response.status_code, 200)
