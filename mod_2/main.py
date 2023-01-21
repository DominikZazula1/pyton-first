from shop.order import generate_order


def run():
    order = generate_order()
    print(order)
    print(len(order))
    order1 = order
    print(order == order1)
    order2 = generate_order()
    print(order == order2)


if __name__ == "__main__":
    run()
