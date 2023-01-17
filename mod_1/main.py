from mod_1.shopping_list import shopping_list_maker


def run_shop():
    x = True
    while x:
        shopping_list_maker.add_to_list(input("podaj nazwe produktu: "), int(input("podaj ilosc: ")))
        if 1 == int(input("jesli chcesz zakonczyc wcisnij 1. ")):
            x = False
    for a in shopping_list_maker.basket:
        print(a[1])
        print(a[2])
        print(a[3])

if __name__ == "__main__":
    run_shop()