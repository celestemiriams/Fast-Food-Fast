""" Tests Module"""

from unittest import TestCase
from flask import json
from run import App

class Tests(TestCase):

    """Tests run for the api"""
    def setUp(self):
        self.app = App
        self.client = self.app.test_client

    def Test_get_orders(self):
        """
        Test case for get orders endpoint, it gets all orders
        """
        result = self.client().get('/api/v1/orders/')
        self.assertEqual(result.status_code, 200)

    def test_get_an_order(self):
        """
        Test case for get an order endpoint, it gets a single order
        """
        result = self.client().get('/api/v1/orders/1/')
        self.assertEqual(result.status_code, 200)

        result1 = self.client().get('/api/v1/orders/jon/')
        self.assertEqual(result1.status_code, 404)

        result2 = self.client().get('/api/v1/orders/@')
        self.assertEqual(result2.status_code, 404)

        result3 = self.client().get('/api/v1/orders/10/')
        self.assertEqual(result3.status_code, 200)

    def test_post_an_order(self):
        """
        Test case for post an order endpoint, it makes a new order
        """
        result = self.client().post('/api/v1/orders/', data=json.dumps(
            dict(order_id=1, item_category="snacks", item_name="chips",
                 quantity=2)), content_type='application/json')
        self.assertEqual(result.status_code, 400)


