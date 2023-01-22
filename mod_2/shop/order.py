import random

from .discount_policy import default_policy
from .order_element import OrderElement
from .product import Product


class Order:
    MAX_ELEMENTS = 5

    def __init__(self, name: str, surname: str, order_element=None, discount_policy=None):
        self.name = name
        self.surname = surname
        if order_element is None:
            order_element = []
        if len(order_element) > self.MAX_ELEMENTS:
            order_element = order_element[:self.MAX_ELEMENTS]
        self._order_elements = order_element
        if discount_policy is None:
            discount_policy = default_policy
        self.total_price = self._calculate_total_price(discount_policy)

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self.name} {self.surname}"
        for product in self._order_elements:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self.total_price} \n  "
        return_valiu += "=" * 20
        return return_valiu

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other.order_element):
            return False

        if self.name != other.name or self.surname != other.surname:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_element:
                return False
        return True

    def _calculate_total_price(self, discount_policy):
        total_price = 0
        for product in self._order_elements:
            total_price += product.total_price()
        return round(discount_policy(total_price), 2)

    def add_order_element(self, product: Product, quantity: int):
        if len(self._order_elements) < self.MAX_ELEMENTS:
            self._order_elements.append(OrderElement(product, quantity))
        else:
            print("nie ma wiecej miejsca!!")

    @classmethod
    def generate_order(cls, quantity,):

        order_element = []
        for product_number in range(quantity):
            name = f"Product-{product_number}"
            category = f"Categoria-{product_number}"
            order_element.append(
                OrderElement(Product(name, category, round(random.uniform(1, 200), 2)), random.randint(1, 20)))
        order = Order("arek", "kowalski", order_element, )
        return order
