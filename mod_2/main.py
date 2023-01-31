

from shop.delivery import products_delivery


def run():
    # Rozbuduj rozwiązanie zadania drugiego z poprzedniej lekcji dodając funkcję, która będzie sprawdzać,
    # których z zamówionych produktów jeszcze brakuje, po otrzymaniu kolejnej dostawy.
    # W tym celu najpierw zaimplementuj funkcję, products_delivery, która reprezentuje otrzymanie dostawy produktów.
    # Funkcja ta powinna zwracać listę produktów przywiezionych w ramach dostawy - w ramach symulacji niech wylosuje z
    # powtórzeniami pięć nazw produktów (z listy dziesięciu dostępnych nazw produktów wylosuj pięć elementów ale tak,
    # żeby mogły się one powtórzyć na liście wynikowej).
    # W skrypcie main najpierw “zamów dostawę”, a potem sprawdź, które produkty są jeszcze potrzebne.
    # Aby porównać otrzymane produkty z listą jeszcze potrzebnych wykorzystaj set. Następnie, tak długo realizuj
    # kolejne zamówienia aż ostatecznie wszystkie z potrzebnych produktów zostaną dostarczone.

    needed_products = [
        "chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]
    delivery =[]
    while not set(needed_products) == set(delivery):
        delivery += products_delivery()
        missing_product = set(needed_products).difference(set(delivery))
        print("brakujace produkty: \n", missing_product)
        print("deliwery: \n", set(delivery), "\n")


if __name__ == "__main__":
    run()
