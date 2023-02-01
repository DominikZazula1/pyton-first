# Napisz test sprawdzający poprawność wykonanej w poprzednim module metody magicznej __eq__ w klasie Product - czyli 
# porównywania produktów.
#
# Dla przypomnienia, dwa produkty są sobie równe, gdy mają taką samą nazwę, taką samą kategorię i taką samą cenę 
# jednostkową.
#
# Wykorzystaj tuple do przygotowania różnych zestawów parametrów danych do algorytmu testującego.
from mod_2.shop.product import Product


def run_test_eq():
    parameters = [
        ("A", "B", 10, "A", "B", 10, True),
        ("A", "B", 10, "C", "B", 10, False),
        ("A", "B", 10, "A", "C", 10, False),
        ("A", "B", 10, "A", "B", 11, False),
        ("A", "B", 10, "C", "D", 10, False),
        ("A", "B", 10, "C", "B", 11, False),
        ("A", "B", 10, "A", "C", 11, False),
        ("A", "B", 10, "D", "C", 11, False),

    ]

    for params in parameters:
        name, category, price, other_name, other_category, other_price, equality = params
        result = Product(name, category, price) == Product(other_name, other_category, other_price)

        if result == equality:
            print("OK")
        else:
            print(
                f"Błąd! Dla parametrów: {params} wynik promocji to {result} zamiast {equality}")


if __name__ == "__main__":
    run_test_eq()
