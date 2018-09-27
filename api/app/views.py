"""
Urls class, to handle request urls
"""

from ..controller.order_controller import OrdersController


class Urls:
    """
    Class to generate urls via static method generate
    """

    @staticmethod
    def generate(app):
        """
        Generate urls on the app context
        :return: urls
        """

        app.add_url_rule('/api/v1/orders/',
                         view_func=OrdersController.as_view('get_all_orders'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/<int:order_id>/',
                         view_func=OrdersController.as_view('get_an_order'),
                         methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/',
                         view_func=OrdersController.as_view('post_an_order'),
                         methods=['POST'], strict_slashes=False)
        app.add_url_rule('/api/v1/orders/<int:order_id>/',
                         view_func=OrdersController.as_view('put'), methods=['PUT'],
                         strict_slashes=False)
