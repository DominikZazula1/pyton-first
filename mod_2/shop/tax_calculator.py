from .order_element import OrderElement


class TaxRate:
    FRUITS_AND_VEGETABLES = 0.05
    FOOD = 0.08
    OTHERS = 0.2


class TaxCalculator:
    @staticmethod
    def calculate_taxes(element: OrderElement):
        if element.product.category == "Owoce i warzywa":
            tax_rate = TaxRate.FRUITS_AND_VEGETABLES
        elif element.product.category == "Jedzenie":
            tax_rate = TaxRate.FOOD
        else:
            tax_rate = TaxRate.OTHERS
        return tax_rate * element.product.unit_price
