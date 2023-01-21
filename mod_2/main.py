from shop.potato import Potato
from shop.apple import Apple
from shop.order import generate_order


def run():
    order = generate_order()
    print(order)

    print(Apple("green", "M", 12.31))
    print(Potato("green", "M", 2.31))


if __name__ == "__main__":
    run()
