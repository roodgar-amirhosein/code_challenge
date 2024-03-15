from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import datetime
from main.models import Orders


class BuyStockViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test data
        user1 = 'user1'
        stock1 = 'stock1'
        Orders.objects.create(user=user1, stock=stock1, status='accepted', creation_date=datetime.now(), price=100,
                              quantity=10)

    def test_valid_request(self):
        client = APIClient()
        data = {
            'user': 'user1',
            'stockname': 'stock1',
            'quantity': 5
        }
        response = client.post('/BuyStock/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Accept')

    def test_invalid_request_missing_user(self):
        client = APIClient()
        data = {
            'stockname': 'stock1',
            'quantity': 5
        }
        response = client.post('/BuyStock/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_request_invalid_stock(self):
        client = APIClient()
        data = {
            'user': 'user1',
            'stockname': 'invalid_stock',
            'quantity': 5
        }
        response = client.post('/BuyStock/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_request_insufficient_quantity(self):
        client = APIClient()
        data = {
            'user': 'user1',
            'stockname': 'stock1',
            'quantity': 100000000
        }
        response = client.post('/BuyStock/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 'Deny')


###################################################################################################
class FetchOrdersAPITests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Orders.objects.create(user='user1', stock='stock1', status='Accepted', creation_date=datetime.now(),
                              price=100, quantity=10)

        Orders.objects.create(user='user2', stock='stock2', status='Accepted', creation_date=datetime.now(),
                              price=200, quantity=15)

        Orders.objects.create(user='user2', stock='stock3', status='Denied',
                              creation_date=datetime(2022, 2, 10, 8, 0, 0),
                              price=150, quantity=1000000000)

        Orders.objects.create(user='user1', stock='stock3', status='Accepted',
                              creation_date=datetime(2022, 2, 10, 8, 0, 0),
                              price=120, quantity=5)

    def test_fetch_orders(self):
        client = APIClient()
        response = client.get('/fetch_orders')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

