"""This is orders class defining the class constructor """

class Orders:
    """This is orders class"""

    def __init__(self, order_id, item_category, item_name, order_status):
        """This is orders class constructor"""
        self.order_id = order_id
        self.item_category = item_category
        self.item_name = item_name
        self.order_status = order_status
        #self.user_id = user_id

    class OrderStatus:
        """Class contains status variables"""
        pending = "pending"
        accepted = "accepted"
        declined = "declined"
        completed = "completed"
