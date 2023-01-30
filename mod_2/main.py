
import random


def hellow_to_you():
    name = input("podaj swoje imie: ").strip()
    surname = input("podaj swoje nazwisko: ").strip()
    # print(f"Nazywasz się {name} {surname} - jak miło Cię poznać :)")
    print("Nazywasz się {} {} - jak miło Cię poznać :)".format(name, surname))


def id_generator():
    return str(random.randint(1, 9999)).zfill(5)


def your_favorite_colors(*args):
    colors = ", ".join(args)
    if "niebieski" in colors.lower():
        print("lubisz niebieski!")
    else:
        print("nie lubisz niebieskiego")


def run():
    # Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko,
    # “wyczyści je” z białych znaków na początku i końcu tekstu, a następnie wypisze jakieś zdanie z tymi danymi np.
    # “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”
    hellow_to_you()
    # Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001,
    # tzn. zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.
    print(id_generator())
    # Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
    # Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.
    print(your_favorite_colors("brozowy", "czarny", "czerwony"))


if __name__ == "__main__":
    run()
