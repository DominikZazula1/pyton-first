# Zabezpiecz listę pozycji w zamówieniu i łączną wartość zamówienia przed utratą spójności.
#
# W tym celu:
#
# Zamień listę pozycji w zamówieniu na zmienną prywatną. Zamień również metodę obliczającą łączny koszt zamówienia na
# prywatną. Dodaj metodę publiczną umożliwiającą dodanie nowego produktu do zamówienia (potrzebne będą informacje o
# produkcie i ilości). Pamiętaj wywołać ponownie przeliczenie łącznej wartości zamówienia.

from shop.product import Product
from shop.order import generate_order


def run():
    order = generate_order()
    print(order)
    print(len(order))
    order.add_order_element(Product("allla", "ddddddad", 12.13), 32)
    print(order)
    print(len(order))


if __name__ == "__main__":
    run()
