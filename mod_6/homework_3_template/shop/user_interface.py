
from enum import Enum

from .errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from .order import Order
from .persistence import save_to_file, load_file, save_order, load_orders
from .store import Store


class Action(Enum):
    NEW_ORDER = "1"
    HISTORY = "2"


def handle_customer():
    say_hello()
    selected_action = select_action()
    if selected_action is Action.NEW_ORDER:
        order = init_order()
        while want_more_products():
            add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
        # save_to_file(order)
        save_order(order)
        print_order_summary(order)
    else:
        show_history()


def select_action():
    selected_action = input("Chcesz złożyć nowe zamówienie (1) czy zobaczyć historię swoich zamówień (2)? ")
    try:
        return Action(selected_action)
    except ValueError:
        print("Możliwe są tylko dwie opcje - domyślnie wybieramy nowe zamówienie ;)")
        return Action.NEW_ORDER


def show_history():
    name = input("Jak masz na imie? ")
    surname = input("Jak masz na nazwisko? ")
    orders = load_orders(name, surname)
    print("Lista zamówień:")
    for order in orders:
        print(order)


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    name = input("Podaj imie: ")
    surname = input("Podaj nazwisko: ")
    return Order(name, surname)


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(input_error)
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput(f"Numer produktu musi być liczbą")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"Numer produktu musi mieścić się w przedziale 0 - {max_index}")

    return product_index


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput(f"Liczba sztuk musi być liczbą")

    if quantity < 1:
        raise NotValidInput(f"Liczba sztuk to co najmniej 1")

    return quantity


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")





