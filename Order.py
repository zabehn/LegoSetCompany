class Order(object):
    """description of class"""

    def __init__(self):
        self.product_ids = []
        self.product_quantities = []
        self.price = 0

    def add_to_order(self, product_id, quantity, price):
        self.product_ids.append(product_id)
        self.product_quantities.append(quantity)
        self.price = self.price + price

    def _str_(self):
        for x,y in zip(self.product_ids,self.product_quantities):
            print(x+"|"+y)


