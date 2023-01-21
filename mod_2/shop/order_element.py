from .product import Product


class OrderElement:

    def __init__(self, name: str, category: str, unit_price: float, quantity=1):
        self.order_element = Product(name, category, unit_price)
        self.quantity = quantity

    def print_order_element(self):
        print("nazwa produktu: ", self.order_element.name,
              " | kategoria: ", self.order_element.category,
              " | cena: ", self.order_element.unit_price,
              " | ilosc: ", self.quantity)

    def total_price(self):
        return self.order_element.unit_price * self.quantity
