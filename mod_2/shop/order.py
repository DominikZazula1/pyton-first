import random

from .product import Product


class Order:
    def __init__(self, name: str, surname: str, products=None):
        self.name = name
        self.surname = surname
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = round(total_price, 2)

    def print_order(self):
        print("=" * 20)
        print("Zamawia pan/pani ", self.name, " ", self.surname)
        for product in self.products:
            product.print_product()
        print("cena calego zamowienia wynosi: ", self.total_price)
        print("=" * 20)


def generate_order():
    number_of_products = random.randint(1, 10)
    products = []
    for product_number in range(number_of_products):
        name = f"Product-{product_number}"
        category = f"Categoria-{product_number}"
        products.append(Product(name, category, round(random.uniform(1, 200), 2)))
    order = Order("arek", "kowalski", products)
    return order
