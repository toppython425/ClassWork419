def add(a, b):
    return a + b


def product(a, b):  # a = result, b = 3
    return a * b


# def product_inside(a, b, c):  # a = result, b = 3
#     add_result = add(a, b)
#     total_result = add_result * c
#     return total_result


result = add(3, 5)  # 8
print(result)
print(add(3, 5))
product_result = product(result, 3)
print(product_result)
print(product(add(3, 4), 5))
