class Potato:
    def __init__(self, species_name: str, size: str, price: float):
        self.species_name = species_name
        self.size = size
        self.price = price

    def total_price(self, weight: float):
        return self.price * weight
