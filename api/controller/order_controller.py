"""
This module contains the orders controller
"""

from flask import request, jsonify, Response, json
from flask.views import MethodView
from api.app.models import OrderData

class OrdersController(MethodView):
    """A class-based view that dispatches request methods to the corresponding
        class methods. For example, if you implement a ``get`` method, it will be
        used to handle ``GET`` requests. :
    """

    def welcome(self):
        return 'Welcome to Fast_Food_Fast website for your food delivery services!'

    #Get all Orders
    def get_all_orders(self):
        """
        This function retrieves all orders made by users
        """
        orders = OrderData.order_data
        return jsonify({'orders':orders})

    #Get a specific order
    def get_an_order(self, order_id):
        """This function returns a specific order given the order id"""
        orders = OrderData.order_data

        if order_id:
            order_ = {}
            for order in orders:
                if order['order_id'] == order_id:
                    order_ = {
                        'order_id':order['order_id'],
                        'item_category':order['item_category'],
                        'item_name':order['item_name'],
                        'quantity':order['quantity']
                    }
            return jsonify(order_)

    #Make an order
    def post_an_order(self):
        """
        This function enables a user to make an order
        """
        orders = OrderData.order_data
        request_data = request.get_json()
        if valid_order(request_data):
            make_order = {
                'order_id':request_data['order_id'],
                'item_category':request_data['item_category'],
                'item_name':request_data['item_name'],
                'quantity':request_data['quantity']
            }
            orders.append(make_order)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "orders/" + str(request_data['question_id'])
            return response
        else:
            bad_object = {
                "error": "Invalid Order Format",
                "help format": "Request format should be {'order_id': '5','item_category': 'snacks',"
                               "'item_name': 'chips','quantity': '2' }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response

    #update order status


# Validating an order
def valid_order(order_object):
    """
    Check if user enters valid order details 
    """
    if 'order_id' in order_object and 'item_category' in order_object and 'item_name' in order_object and 'quantity' in order_object:
        return True
    else:
        return False