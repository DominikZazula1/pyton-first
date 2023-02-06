import os


def save_to_file(order):
    file_path = os.path.join("data", "orders.txt")
    try:
        with open(file_path, mode="a") as order_file:
            order_file.write(str(order))
    except IOError:
        print("Nie mozna odczytac pliku!!")
    else:
        print("plik zapisany pomyslnie")


def load_file():
    file_path = os.path.join("data", "orders.txt")
    try:
        with open(file_path, mode="r") as order_file:
            return order_file.read()
    except IOError:
        print("Nie mozna odczytac pliku!!")

