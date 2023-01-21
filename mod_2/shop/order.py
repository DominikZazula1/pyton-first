import random

from .order_element import OrderElement



class Order:
    def __init__(self, name: str, surname: str, order_element=None):
        self.name = name
        self.surname = surname
        if order_element is None:
            order_element = []
        self.order_element = order_element

        total_price = 0
        for product in order_element:
            total_price += product.total_price()
        self.total_price = round(total_price, 2)

    def print_order(self):
        print("=" * 20)
        print("Zamawia pan/pani ", self.name, " ", self.surname)
        for product in self.order_element:
            product.print_order_element()
        print("cena calego zamowienia wynosi: ", self.total_price)
        print("=" * 20)


def generate_order():
    number_of_order_element = random.randint(1, 10)
    order_element = []
    for product_number in range(number_of_order_element):
        name = f"Product-{product_number}"
        category = f"Categoria-{product_number}"
        order_element.append(OrderElement(name, category, round(random.uniform(1, 200), 2), random.randint(1, 20)))
    order = Order("arek", "kowalski", order_element)
    return order
