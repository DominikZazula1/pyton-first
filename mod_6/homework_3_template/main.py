#
# Uzupełnij szablon kodu o odpowiednie implementacje (oznaczenia )
#  - Funkcje z user_interface po uruchomieniu programu zapytają użytkownika o dane (imię i nazwisko)
#  a następnie zaproponują dodanie kolejnych towarów do zamówienia.
#  - W celu kontroli dostępności towarów klasa Store, posiada zdefiniowaną listę dostępnych produktów i ich liczbę.
#  Podczas dodawania kolejnych produktów do zamówienia aktualizuj ich stan w Store i gdyby okazało się,
#  że nie można zrealizować oczekiwań klienta wyrzuć odpowiedni wyjątek i obsłuż go komunikatem dla użytkownika.
from shop.errors import NotValidInput


def three_letters_of_name(string):
    if len(string) != 3:
        raise NotValidInput("litery maja byc 3")


def run_homework():
    try:
        three_letters_of_name(input("jak sie zaczyna twoje imie? podaj 3 litery: "))
    except NotValidInput as error:
        print(error.args)
    else:
        print("podane dane sa prawidlowe")
    finally:
        print("koniec programu")


if __name__ == '__main__':
    run_homework()
