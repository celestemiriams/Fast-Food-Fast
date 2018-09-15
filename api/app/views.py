"""
Urls class, to handle request urls
"""

from ..controller.order_controller import OrdersController


class Urls(object):
    """
    Class to generate urls via static method generate
    """

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        It takes no arguments
        :param app: takes in the app variable
        :return: urls
        """

        app.add_url_rule('/api/v1/',
                         view_func=OrdersController.as_view('welcome'), strict_slashes=False)
        app.add_url_rule('/api/v1/orders/',
                         view_func=OrdersController.as_view('get_all_orders'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/<int:orders_id>/',
                         view_func=OrdersController.as_view('get_an_order'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/',
                         view_func=OrdersController.as_view('post_an_order'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/<int:order_id>/',
                         view_func=OrdersController.as_view('update_order_status'), methods=['PUT'],
                         strict_slashes=False)