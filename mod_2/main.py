from shop.apple import Apple
from shop.order import generate_order


def run():
    order = generate_order()
    order.print_order()


if __name__ == "__main__":
    run()
