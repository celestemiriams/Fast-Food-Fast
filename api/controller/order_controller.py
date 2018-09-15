"""
This module contains the end point for orders
"""

from flask import request, jsonify, Response, json
from flask.views import MethodView
from api.app.models import OrderData
#from .orders import Orders

class OrdersController(MethodView):
    """A class-based view that dispatches request methods to the corresponding
    end points
    """
    orders = OrderData.order_data

    def get(self, order_id=None):
        """
        This function retrieves all orders made by users
        or retrieves a specific order if order id is given
        """

        #return a single order
        if order_id:
            single_order = {}
            for order in self.orders:
                if order['order_id'] == order_id:
                    single_order = {
                        'order_id':order['order_id'],
                        'item_category':order['item_category'],
                        'item_name':order['item_name'],
                        'quantity':order['quantity'],
                        'order_status':order['order_status']
                    }
            return jsonify(single_order)

        else:
            #return all orders if no id is specified
            return jsonify({'orders':self.orders})

    def post(self):
        """
        responds to post requests
        :param order_id:
        :return:
        """
        if str(request.url_rule) == "/api/v1/orders/":
            return OrdersController.post_an_order(self)

        return 'Errors'  # ReturnHandlers.could_not_process_request()


    #Make an order
    def post_an_order(self):
        """
        This function enables a user to make an order
        """
        request_data = request.get_json()
        if valid_order(request_data):
            make_order = {
                'order_id':len(self.orders) + 1, 'item_category':request_data['item_category'],
                'item_name':request_data['item_name'], 'quantity':request_data['quantity']
                }
            self.orders.append(make_order)
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "orders/" + str(len(self.orders) + 1)
            return response

        else:
            bad_object = {
                "error": "Please fill in all the fields",
                "help format": "Request format should be {'item_category': 'snacks',"
                               "'item_name': 'chips','quantity': '2' }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response

    #update order status
    def put(self, order_id):
        """
        Function to update order status by marking it complete,
        declining or accepting it
        """

        if isinstance(order_id, int):
            if not order_id < 0:
                if not isinstance(order_id, bool):
                    for order in self.orders:
                        if order['order_id'] == order_id:
                            order_json = request.get_json()
                            order['order_status'] == order_json['order_status']
                    return jsonify({"orders": [order for order in self.orders]})

                else:
                    raise TypeError("order status cannot be a boolean")

            else:
                raise ValueError("order id cannot be a int less than 0")

        else:
            raise TypeError("order id cannot be a string")


# Validating an order
def valid_order(order_object):
    """
    Check if user enters valid order details
    """
    if 'item_category' in order_object and 'item_name' in order_object and 'quantity' in order_object:
        return True
