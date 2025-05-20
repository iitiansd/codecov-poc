from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class TestCalculatorAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/calculate/'

    def test_addition(self):
        response = self.client.post(self.url, {'a': 5, 'b': 3, 'operation': 'add'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 8)

    def test_subtraction(self):
        response = self.client.post(self.url, {'a': 10, 'b': 4, 'operation': 'subtract'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 6)

    def test_multiplication(self):
        response = self.client.post(self.url, {'a': 7, 'b': 6, 'operation': 'multiply'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 42)

    def test_division(self):
        response = self.client.post(self.url, {'a': 20, 'b': 4, 'operation': 'divide'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 5)

    def test_division_by_zero(self):
        response = self.client.post(self.url, {'a': 10, 'b': 0, 'operation': 'divide'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_invalid_operation(self):
        response = self.client.post(self.url, {'a': 10, 'b': 5, 'operation': 'modulo'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_missing_parameters(self):
        response = self.client.post(self.url, {'a': 10}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_invalid_input_types(self):
        response = self.client.post(
            self.url,
            {'a': 'five', 'b': 'three', 'operation': 'add'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
