import csv
import os

from .product import ProductCategory
from .store import AvailableProduct, Store


def load_store(file_name="store.csv"):
    with open(file_name, newline="") as store_file:
        csv_reader = csv.DictReader(store_file)
        return [
            AvailableProduct(
                name=row["name"],
                category=ProductCategory[row["category"]],
                unit_price=float(row["unit_price"]),
                identifier=int(row["identifier"]),
                quantity=int(row["quantity"])
            )
            for row in csv_reader
        ]


def save_store(file_name="store.csv"):
    with open(file_name, mode="w", newline="") as store_file:
        headers = ["name", "category", "unit_price", "identifier", "quantity"]
        writer = csv.DictWriter(store_file, fieldnames=headers)
        writer.writeheader()
        for available_product in Store.AVAILABLE_PRODUCTS:
            writer.writerow({
                "name": available_product.product.name,
                "category": available_product.product.category.name,
                "unit_price": available_product.product.unit_price,
                "identifier": available_product.product.identifier,
                "quantity": available_product.quantity
            })


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

