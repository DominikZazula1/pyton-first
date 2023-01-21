from .product import Product


class OrderElement:

    def __init__(self, product: Product, quantity=1):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return str(self.product) + f"| ilosc:  {self.quantity}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        elif self.product != other.product:
            return False
        elif self.quantity == other.quantity:
            return True
        else:
            return False

    def total_price(self):
        return self.product.unit_price * self.quantity
