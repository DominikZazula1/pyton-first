class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price


class PercentageDiscount(DiscountPolicy):
    def __init__(self, percentage_rabat):
        self.percentage_rabat = (100 - percentage_rabat) / 100

    def apply_discount(self, total_price):
        return total_price * self.percentage_rabat


class AbsoluteDiscount(DiscountPolicy):
    def __init__(self, rabat):
        self.rabat = rabat

    def apply_discount(self, total_price):
        if total_price < self.rabat:
            print("nie mozna udzielic rabatu")
            return 0
        return total_price - self.rabat


