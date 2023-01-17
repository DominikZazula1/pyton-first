
class Product:
    pass
class Orders:
    pass
class Apple:
    pass
class Potato:
    pass
kartofel = Potato()
kartofel1 = Potato()
zamowienie = Orders()
zamowienie1 = Orders()
zamowienie2 = Orders()
zamowienie3 = Orders()
zamowienie4 = Orders()
jabko = Apple()
jabko1 = Apple()
produkt = Product()
auto = Product()
kawa = Product()
woda = Product()
print(kartofel)
print(zamowienie)
print(jabko)
print(produkt)
print(type(kartofel), type(kartofel1))
print(type(jabko), type(jabko1))
orders_list = [zamowienie, zamowienie1, zamowienie2, zamowienie3, zamowienie4]
products_dic = {
    "produkt": produkt,
    "auto": auto,
    "kawa": kawa,
    "woda": woda
}