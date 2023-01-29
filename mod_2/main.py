from mod_2.shop.order import Order
from shop.discount_policy import PercentageDiscount, AbsoluteDiscount
from shop import data_generator


def run():
    order_elements = data_generator.generate_order_elements()
    ten_percent_discount = PercentageDiscount(10)
    hundred_pln_discount = AbsoluteDiscount(100)

    no_discount_order = Order(
        name="M",
        surname="L",
        order_element=order_elements,
    )
    order_with_percentage_discount = Order(
        name="M",
        surname="L",
        order_element=order_elements,
        discount_policy=ten_percent_discount,
    )
    order_with_absolute_value_discount = Order(
        name="M",
        surname="L",
        order_element=order_elements,
        discount_policy=hundred_pln_discount,
    )

    print(no_discount_order)
    print(order_with_percentage_discount)
    print(order_with_absolute_value_discount)


if __name__ == "__main__":
    run()
