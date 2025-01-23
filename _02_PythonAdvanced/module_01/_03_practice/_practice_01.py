from functools import reduce


def calculate_total(cart):
    item_totals = map(lambda x: x[0] * x[1], cart)
    return reduce(lambda x, y: x + y, item_totals, 0)


if __name__ == '__main__':
    cart = [(10.99, 2), (5.49, 4), (3.99, 1)]
    print(calculate_total(cart))
