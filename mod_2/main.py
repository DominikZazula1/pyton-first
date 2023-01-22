from shop.tax_calculator import TaxCalculator
from shop.order_element import OrderElement
from shop.order import Order
from shop.product import Product


def run():
    order = Order.generate_order(40)
    print(order)
    print(len(order))
    order.add_order_element(Product("allla", "ddddddad", 12.13), 32)

    cookie = Product("Ciastko", "Jedzenie", 4)
    tomato = Product("Pomidor", "Owoce i warzywa", 3)
    something = Product("Coś", "Nieznana kategoria", 50)
    ten_cookies = OrderElement(cookie, 10)
    five_tomatoes = OrderElement(tomato, 5)
    single_something = OrderElement(something, 1)

    cookies_tax = TaxCalculator.calculate_taxes(ten_cookies)
    tomatoes_tax = TaxCalculator.calculate_taxes(five_tomatoes)
    something_tax = TaxCalculator.calculate_taxes(single_something)

    print(f"Cena ciastek: {ten_cookies.total_price()} + {cookies_tax:.2f}")
    print(f"Cena pomidorów: {five_tomatoes.total_price()} + {tomatoes_tax:.2f}")
    print(f"Cena czegoś: {single_something.total_price()} + {something_tax:.2f}")


if __name__ == "__main__":
    run()
