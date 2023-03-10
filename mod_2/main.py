from mod_2.shop.errors import OrderLimitError
from shop import data_generator
from shop.order import Order


def run():
    # order_elements_on_limit = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    # order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limit)
    # print(order_on_limit)

    # product = data_generator.generate_product()
    # quantity = data_generator.generate_quantity()
    # order_on_limit.add_product_to_order(product, quantity)
    try:
        order_elements_over_limit = data_generator.generate_order_elements(Order.MAX_ELEMENTS + 1)
        order_over_limit = Order("Bob", "Kowalski", order_elements=order_elements_over_limit)
    except Exception as error:
        print("przekroczono limit miejsc w zamowieniu, ktory wynosi: ", error.allowed_limit)


if __name__ == "__main__":
    run()
