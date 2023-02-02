from dataclasses import dataclass
from enum import Enum


class ProductCategory(Enum):
    FOOD = "Jedzonko"
    OTHER = "Inne"
    TOOLS = "Narzędzia"


@dataclass
class Product:
    name: str
    category: ProductCategory
    unit_price: float
    identifier: int

    def __str__(self):
        return f"nazwa produktu: {self.name} " \
               f"| kategoria:  {self.category.value} " \
               f"| cena:  {self.unit_price} "


@dataclass
class ExpiringProduct(Product):
    year_of_production: int
    years_of_validity: int

    def dose_expire(self, year):
        return year > self.year_of_production + self.years_of_validity
