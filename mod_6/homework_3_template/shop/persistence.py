import csv
import os

from .product import ProductCategory
from .store import AvailableProduct, Store


def load_store(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.reader(store_file)
        next(csv_reader)
        return [
            AvailableProduct(
                name=row[0],
                category=ProductCategory[row[1]],
                unit_price=float(row[2]),
                identifier=int(row[3]),
                quantity=int(row[4])
            )
            for row in csv_reader
        ]


def save_store(file_name="store.csv"):
    with open(file_name, mode="w", newline="") as store_file:
        csv_writer = csv.writer(store_file)
        # csv_writer = csv.writer(store_file, delimiter=";", quotechar="|", quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["name", "category", "unit_price", "identifier", "quantity"])
        for available_product in Store.AVAILABLE_PRODUCTS:
            csv_writer.writerow([
                available_product.product.name,
                available_product.product.category,
                available_product.product.unit_price,
                available_product.product.identifier,
                available_product.quantity
            ])


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

