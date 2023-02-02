from dataclasses import dataclass


@dataclass
class Potato:
    species_name: str
    size: str
    price: float

    def total_price(self, weight: float):
        return self.price * weight
