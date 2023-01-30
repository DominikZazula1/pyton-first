import math
import random


def run():
    float_numbers = []
    for _ in range(6):
        float_numbers.append(random.uniform(-20, 20))
    print(float_numbers)

    int_numbers = []
    for _ in range(3):
        int_numbers.append(random.randint(1, 10))
    print(int_numbers)

    print(round(float_numbers[0]))
    print(math.ceil(float_numbers[1]))
    print(math.floor(float_numbers[2]))

    print(float_numbers[3] ** int_numbers[0])
    print(pow(float_numbers[4], int_numbers[1]))
    print(math.pow(float_numbers[5], int_numbers[2]))


if __name__ == "__main__":
    run()
