import random


def napis(*args):
    return "-".join(args)


def print_dic(**kwargs):
    print("\n")
    for name, value in kwargs.items():
        print(f"first_name={name}, age={value}")
    print("\n")


def list_generator():
    lista = []
    for a in range(5):
        lista.append(random.randint(1, 40))
    return lista


def run():
    print(napis("aaaaa", "bbbbb", "cccccc"))
    print_dic(dominik=12, marysi=31, Adrian=42, barbara=69)
    first_list = list_generator()
    second_list = list_generator()
    final_list = [*first_list, *second_list]
    print(final_list)
    first_dic = {
        "dominik": 40,
        "marysi": 4,
        "lucyna": 53,
    }
    second_dic = {
        "Adrian": 14,
        "barbara": 41,
        "emilka": 25,
    }
    final_dic = {**first_dic, **second_dic}
    print_dic(**final_dic)


if __name__ == "__main__":
    run()
