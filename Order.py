class Order(object):
    """description of class"""

    def __init__(self):
        self.product_ids = []
        self.product_quantities = []

    def add_to_order(self, product_id, quantity):
        self.product_ids.append(product_id)
        self.product_quantities.append(quantity)

