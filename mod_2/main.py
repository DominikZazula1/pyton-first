class Product:
    def __int__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Order:
    def __int__(self, name, surname, products=None):
        self.name = name
        self.surname = surname
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price


class Apple:
    def __int__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


class Potato:
    def __int__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = price


if __name__ == "__main__":
    kosiarka = Product("kosiarka", "maszyna", 1299.99)
    telefon = Product("samsung", "telefon", 699.99)
    washing_machine = Product("pralka", "rtv", 3999.99)
    produkty = [kosiarka, telefon, washing_machine]

    order = Order("Dominik", "Zazula", produkty)
    order1 = Order("jan", "Kowalski")

    green_apple = Apple("apple", 34, 3.99)
    old_apple = Apple("old apple", 32, 1.99)
    red_apple = Apple("red apple", 31, 4.99)

    green_potato = Potato("bad potato", 24, 3.99)
    old_potato = Potato("old potato", 32, 1.99)
    sweat_potato = Apple("sweat potato", 31, 4.99)
