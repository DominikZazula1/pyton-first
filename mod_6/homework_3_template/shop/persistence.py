import csv
import dataclasses
import json
import os

from mod_2.shop.product import Product
from .order import Order
from .order_element import OrderElement
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


def save_order(order, file_name="orders.json"):
    new_order_data = {
        "client_first_name": order.client_first_name,
        "client_last_name": order.client_last_name,
        "order_elements": [
            {
                "product": {
                    "name": order_element.product.name,
                    "category": order_element.product.category.name,
                    "unit_price": order_element.product.unit_price,
                    "identifier": order_element.product.identifier,
                },
                "quantity": order_element.quantity
            } for order_element in order.order_elements
        ]
    }
    try:
        with open(file_name, "r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{order.client_first_name}-{order.client_last_name}"
    if client_id not in orders_by_clients_data:
        orders_by_clients_data[client_id] = []
    orders_by_clients_data[client_id].append(new_order_data)

    with open(file_name, "w") as orders_file:
        json.dump({"orders": orders_by_clients_data}, orders_file, indent=4)


def load_orders(client_first_name, client_last_name, file_name="orders.json"):
    try:
        with open(file_name, "r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders", {})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{client_first_name}-{client_last_name}"
    if client_id not in orders_by_clients_data:
        return []
    orders = orders_by_clients_data[client_id]
    return [
        Order(
            client_first_name=order["client_first_name"],
            client_last_name=order["client_last_name"],
            order_elements=[OrderElement(
                quantity=order_element["quantity"],
                product=Product(
                    name=order_element["product"]["name"],
                    category=ProductCategory[order_element["product"]["category"]],
                    unit_price=order_element["product"]["unit_price"],
                    identifier=order_element["product"]["identifier"],
                )
            ) for order_element in order["order_elements"]],
        ) for order in orders
    ]
