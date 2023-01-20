import random

from shop.apple import Apple
from shop.order import Order, generate_order
from shop.potato import Potato
from shop.product import Product


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
