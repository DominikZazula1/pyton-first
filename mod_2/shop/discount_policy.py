def default_policy(total_price):
    return total_price


def loyal_customer_policy(total_price):
    return total_price - total_price * 0.05


def christmas_policy(total_price):
    if total_price >= 100:
        return total_price - 20
    return total_price
