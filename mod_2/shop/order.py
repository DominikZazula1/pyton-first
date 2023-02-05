from .discount_policy import DiscountPolicy
from .errors import OrderLimitError
from .order_element import OrderElement
from .product import Product


class Order:
    MAX_ELEMENTS = 5

    def __init__(self, name: str, surname: str, order_elements=None, discount_policy=None):
        self._name = name
        self._surname = surname

        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

        if discount_policy is None:
            self._discount_policy = DiscountPolicy()
        else:
            self._discount_policy = discount_policy

    @property
    def order_elements(self):
        return self._order_elements

    @property
    def total_price(self):
        total_price = 0
        for product in self._order_elements:
            total_price += product.total_price()
        return round(self._discount_policy.apply_discount(total_price), 2)

    @order_elements.setter
    def order_elements(self, value):
        if len(value) > Order.MAX_ELEMENTS:
            raise OrderLimitError(Order.MAX_ELEMENTS)
        self._order_elements = value

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self._name} {self._surname}"
        for product in self._order_elements:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self.total_price} \n  "
        return_valiu += "=" * 20
        return return_valiu

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        if len(self._order_elements) != len(other.order_element):
            return False

        if self._name != other.name or self._surname != other.surname:
            return False

        for order_element in self._order_elements:
            if order_element not in other.order_element:
                return False
        return True

    def _calculate_total_price(self):
        total_price = 0
        for product in self._order_elements:
            total_price += product.total_price()
        return round(self._discount_policy.apply_discount(total_price), 2)

    def add_order_element(self, product: Product, quantity: int):
        if len(self._order_elements) < self.MAX_ELEMENTS:
            self._order_elements.append(OrderElement(product, quantity))
        else:
            raise OrderLimitError(Order.MAX_ELEMENTS)


class ExpressOrder(Order):
    EXPRESS_DELIVERY_FEE = 20

    def __init__(self, delivery_date: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        return super().total_price - ExpressOrder.EXPRESS_DELIVERY_FEE

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self._name} {self._surname}"
        for product in self._order_elements:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self.total_price} \n  "
        return_valiu += f"data dostawy: {self.delivery_date} \n  "
        return_valiu += "=" * 20
        return return_valiu
