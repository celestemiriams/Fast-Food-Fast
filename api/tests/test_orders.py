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
            dict(item_category=False, item_name="chips", quantity=3)),
                                 content_type='application/json')
        resp = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 400)
        self.assertIn("data", resp)
        self.assertIn("error_message", resp)
        self.assertIsInstance(resp['data'], list)
        self.assertEqual(resp['error_message'], "some of these fields are missing")

        result = self.client().post('/api/v1/orders/', data=json.dumps(
            dict(item_category="snacks", item_name="", quantity="")),
                                 content_type='application/json')
        resp = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 400)
        self.assertIn("data", resp)
        self.assertIn("error_message", resp)
        self.assertIsInstance(resp['data'], dict)
        self.assertEqual(resp['error_message'], "some of these fields have empty/no values")

        result = self.client().post('/api/v1/orders/', data=json.dumps(
            dict(item_category="snacks", item_name="chips", quantity="2")),
                                 content_type='application/json')
        resp = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 201)
        self.assertIn("data", resp)
        self.assertNotIn("error_message", resp)
        self.assertIn("success_message", resp)
        self.assertTrue(resp['data'])
        self.assertEqual(resp['success_message'], "successfully placed an order.")

    
    def test_update_order_status(self):
        """
        Test case for order endpoint, it tests updates made to an order
        """
        result = self.client().put('/api/v1/orders/20/')
        self.assertEqual(result.status_code, 200)

        result = self.client().put('/api/v1/orders/@/')
        self.assertEqual(result.status_code, 404)

        result = self.client().put('/api/v1/orders/1/', data=json.dumps(
            dict(item_category="snacks", item_name="chips", quantity=2)),
                                content_type='application/json')
        resp = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 201)
        self.assertIn("success_message", resp)




