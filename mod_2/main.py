from shop import data_generator
from shop.apple import Apple
from shop.order import Order
from shop.potato import Potato


def run():
    green_apple = Apple(species_name="Green", size="M", price=3.5)
    red_apple = Apple(species_name="Red", size="S", price=2.8)
    print(green_apple.species_name, green_apple)
    print(red_apple.species_name, red_apple)

    old_potato = Potato(species_name="Potato Old", size="S", price=1.55)
    print(old_potato.species_name, old_potato)
    some_order_elements = data_generator.generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_element=some_order_elements)
    print(my_order)


if __name__ == "__main__":
    run()
