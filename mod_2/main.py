import random


def run():
    # Zadanie nr 1 Używając list comprehensions wygeneruj listy zawierające liczby od 1 do 30 podzielne kolejno przez
    # 3 oraz przez 5. To znaczy, że na pierwszej liście powinny znaleźć się liczby od 1 do 30 podzielne przez 3,
    # a na drugiej liście liczby od 1 do 30 podzielne przez 5. Następnie, połącz obie listy w jedną i wypisz wynik.
    # Zadanie nr 2 Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi,
    # pomijając pierwszy sport z listy.
    numbers_3 = [number for number in range(31) if number % 3 == 0]
    numbers_5 = [number for number in range(31) if number % 5 == 0]
    numbers_3 += numbers_5
    favorite_sports = []
    sport = "a"
    while sport != "":
        sport = input("podaj ulubiony sport:")
        favorite_sports.append(sport)
    print(numbers_3)
    print(favorite_sports[1::2])


if __name__ == "__main__":
    run()
