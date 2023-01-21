from .product import Product


class OrderElement:

    def __init__(self, product: Product, quantity=1):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return str(self.product) + f"| ilosc:  {self.quantity}"

    def total_price(self):
        return self.product.unit_price * self.quantity
