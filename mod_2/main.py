
from shop.data_generator import generate_order_elements
from shop.product import ExpiringProduct


def run():
    product = ExpiringProduct("Mleko", "picie", 12.13, 2022, 1)
    print(product.dose_expire(2023))
    print(product.dose_expire(2024))


if __name__ == "__main__":
    run()
