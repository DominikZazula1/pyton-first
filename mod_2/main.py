from collections import namedtuple


def run():
    Apple = namedtuple("Apple", ["species_name", "size", "price"])

    apple = Apple("green apple", "M", 11.1)
    print(apple.species_name)
    print(apple.size)
    print(apple.price)
    for x in range(3):
        print(apple[x])
    for item in apple:
        print(item)




if __name__ == "__main__":
    run()
