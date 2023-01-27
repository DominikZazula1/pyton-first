
from shop.data_generator import generate_order_elements
from shop.order import Order


def run():
    order_elements = generate_order_elements()
    order = Order("Dominik", "ZZIZ", order_elements)
    print("imeie : ", order.name)
    print("nazwiska : ", order.surname)
    print("cena : ", order.total_price, "zl")
    print("Lista: \n")
    for element in order.order_elements:
        print(element)
    order1 = Order("Maria", "Bem")
    order_elements1 = generate_order_elements(number_of_products=20)
    order1.order_elements = order_elements1
    print("imeie : ", order1.name)
    print("nazwiska : ", order1.surname)
    print("cena : ", order1.total_price, "zl")
    print("Lista: \n")
    for element in order1.order_elements:
        print(element)


if __name__ == "__main__":
    run()
