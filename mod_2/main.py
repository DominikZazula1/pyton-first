import random


class Product:

    def __init__(self, name: str, category: str, unit_price: float):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def print_product(self):
        print("nazwa produktu: ", self.name, " kategoria: ", self.category, "cena: ", self.unit_price)


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


class Apple:
    def __init__(self, species_name: str, size: str, price: float):
        self.species_name = species_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, species_name: str, size: str, price: float):
        self.species_name = species_name
        self.size = size
        self.price = price


def generate_order():
    number_of_products = random.randint(1, 10)
    products = []
    for product_number in range(number_of_products):
        name = f"Product-{product_number}"
        category = f"Categoria-{product_number}"
        products.append(Product(name, category, round(random.uniform(1, 200), 2)))
    order = Order("arek", "kowalski", products)
    return order


def run():
    order = generate_order()
    order.print_order()
    kosiarka = Product(name="kosiarka", category="maszyna", unit_price=1299.99)
    telefon = Product("samsung", "telefon", 699.99)
    washing_machine = Product("pralka", "rtv", 3999.99)
    produkty = [kosiarka, telefon, washing_machine]
    kosiarka.print_product()
    telefon.print_product()
    washing_machine.print_product()

    order = Order("Dominik", "Zazula", produkty)
    order1 = Order("jan", "Kowalski")
    order.print_order()
    order1.print_order()

    green_apple = Apple("apple", "M", 3.99)
    old_apple = Apple("old apple", "S", 1.99)
    red_apple = Apple("red apple", "M", 4.99)

    green_potato = Potato("bad potato", "S", 3.99)
    old_potato = Potato("old potato", "S", 1.99)
    sweat_potato = Apple("sweat potato", "S", 4.99)


if __name__ == "__main__":
    run()
