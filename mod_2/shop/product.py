class Product:

    def __init__(self, name: str, category: str, unit_price: float):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def print_product(self):
        print("nazwa produktu: ", self.name, " kategoria: ", self.category, "cena: ", self.unit_price)
