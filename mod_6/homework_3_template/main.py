from shop.persistence import load_store, save_store
from shop.store import Store
from shop import user_interface


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    user_interface.handle_customer()
    save_store()


if __name__ == '__main__':
    run_homework()
