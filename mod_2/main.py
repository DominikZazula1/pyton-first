from mod_2.shop.order import ExpressOrder
from shop import data_generator


def run():
    order_elements = data_generator.generate_order_elements()
    express_order = ExpressOrder(
        delivery_date="10-05-2020",
        name="M",
        surname="L",
        order_element=order_elements
    )
    print(express_order)


if __name__ == "__main__":
    run()
