import random

from .order import Order
from .order_element import OrderElement
from .product import Product

MAX_UNIT_PRICE = 30
MIN_UNIT_PRICE = 1
MAX_QUANTITY = 10
MIN_QUANTITY = 1


def generate_order_elements(number_of_products=None):
    order_elements = []
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ELEMENTS)
    for product_number in range(number_of_products):
        identifier = random.randint(1, 100)
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        product = Product(product_name, category_name, unit_price, identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
