from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.order_element import OrderElement
from shop.order import Order
from shop.product import Product


def total_cost(order: Order):
    return order.total_price


def run():
    orders = [Order.generate_order(5), Order.generate_order(5), Order.generate_order(5), Order.generate_order(5),
              Order.generate_order(5)]
    for order in orders:
        print(order.total_price)
    print("-" * 10)
    orders.sort(key=total_cost)
    for order in orders:
        print(order.total_price)
    orders_element = [OrderElement(Product("a", "Owoce i warzywa", 10), 10),
                      OrderElement(Product("b", "Owoce i warzywa", 20), 5),
                      OrderElement(Product("c", "Owoce i warzywa", 100), 1)]
    order1 = Order("Dominik", "Zazula", orders_element)
    order2 = Order("Dominik", "Zazula", orders_element, loyal_customer_policy)
    order3 = Order("Dominik", "Zazula", orders_element, christmas_policy)
    print("=" * 10, "\n")
    print(order1.total_price)
    print(order2.total_price)
    print(order3.total_price)


if __name__ == "__main__":
    run()
