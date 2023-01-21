class Product:

    def __init__(self, name: str, category: str, unit_price: float):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def __str__(self):
        return f"nazwa produktu: {self.name} " \
               f"| kategoria:  {self.category} " \
               f"| cena:  {self.unit_price} "

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
            return (self.name == other.name and
                    self.category_name == other.category_name and
                    self.unit_price == other.unit_price)

