from .discount_policy import default_policy
from .order_element import OrderElement
from .product import Product


class Order:
    MAX_ELEMENTS = 5

    def __init__(self, name: str, surname: str, order_element=None, discount_policy=None):
        self._name = name
        self._surname = surname
        if order_element is None:
            order_element = []
        if len(order_element) > self.MAX_ELEMENTS:
            order_element = order_element[:self.MAX_ELEMENTS]
        self._order_elements = order_element
        if discount_policy is None:
            self._discount_policy = default_policy
        else:
            self._discount_policy = discount_policy
        self._total_price = self._calculate_total_price()

    @property
    def order_elements(self):
        return self._order_elements

    @property
    def total_price(self):
        return self._calculate_total_price()

    @order_elements.setter
    def order_elements(self, elements):
        elements_count = len(self._order_elements) + len(elements)
        if self._order_elements.__class__ != elements.__class__:
            print(NotImplemented)
        elif elements_count <= self.MAX_ELEMENTS:
            self._order_elements.extend(elements)
        else:
            self._order_elements.extend(elements[:self.MAX_ELEMENTS - elements_count])
        self._total_price = self._calculate_total_price()

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self._name} {self._surname}"
        for product in self._order_elements:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self._total_price} \n  "
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
        return round(self._discount_policy(total_price), 2)

    def add_order_element(self, product: Product, quantity: int):
        if len(self._order_elements) < self.MAX_ELEMENTS:
            self._order_elements.append(OrderElement(product, quantity))
        else:
            print("nie ma wiecej miejsca!!")


class ExpressOrder(Order):
    def __init__(self, name: str, surname: str, delivery_date: str, order_element=None, discount_policy=None):
        super().__init__(name, surname, order_element, discount_policy)
        self.delivery_date = delivery_date
        self._total_price += 20

    def __str__(self):
        return_valiu = "=" * 20
        return_valiu += f"\nZamawia pan/pania  {self._name} {self._surname}"
        for product in self._order_elements:
            return_valiu += f"\n  {str(product)}"
        return_valiu += f"\ncena calego zamowienia wynosi: {self._total_price} \n  "
        return_valiu += f"\data dostawy: {self.delivery_date} \n  "
        return_valiu += "=" * 20
        return return_valiu
