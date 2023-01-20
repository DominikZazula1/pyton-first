from shop.apple import Apple
from shop.potato import Potato


def run():
    green_apple = Apple("apple", "M", 3.99)
    old_apple = Apple("old apple", "S", 1.99)
    red_apple = Apple("red apple", "M", 4.99)

    green_potato = Potato("bad potato", "S", 3.99)
    old_potato = Potato("old potato", "S", 1.99)
    sweat_potato = Apple("sweat potato", "S", 4.99)

    print(green_apple.total_price(12))
    print(green_potato.total_price(21))


if __name__ == "__main__":
    run()
