from dataclasses import dataclass
from .product import Product


@dataclass
class OrderElement:
    product: Product
    quantity: int = 1

    def __str__(self):
        return str(self.product) + f"| ilosc:  {self.quantity}"

    def total_price(self):
        return self.product.unit_price * self.quantity
