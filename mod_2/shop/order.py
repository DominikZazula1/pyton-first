import random

from .order_element import OrderElement
from .product import Product


class Order:
    def __init__(self, name: str, surname: str, order_element=None):
        self.name = name
        self.surname = surname
        if order_element is None:
            order_element = []
        self._order_element = order_element

        self.total_price = self._calculate_total_price()

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self.name} {self.surname}"
        for product in self._order_element:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self.total_price} \n  "
        return_valiu += "=" * 20
        return return_valiu

    def __len__(self):
        return len(self._order_element)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_element) != len(other.order_element):
            return False

        if self.name != other.name or self.surname != other.surname:
            return False

        for order_element in self._order_element:
            if order_element not in other.order_element:
                return False
        return True

    def _calculate_total_price(self):
        total_price = 0
        for product in self._order_element:
            total_price += product.total_price()
        return round(total_price, 2)

    def add_order_element(self, product: Product, quantity: int):
        self._order_element.append(OrderElement(product, quantity))


def generate_order():
    number_of_order_element = random.randint(1, 10)
    order_element = []
    for product_number in range(number_of_order_element):
        name = f"Product-{product_number}"
        category = f"Categoria-{product_number}"
        order_element.append(
            OrderElement(Product(name, category, round(random.uniform(1, 200), 2)), random.randint(1, 20)))
    order = Order("arek", "kowalski", order_element)
    return order
