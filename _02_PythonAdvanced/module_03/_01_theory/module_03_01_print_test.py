def calculate_total(price, discount):
    print(f'Price: {price}, Discount: {discount}')
    total = price - discount
    return total


if __name__ == '__main__':
    print(calculate_total(1000, 100))
