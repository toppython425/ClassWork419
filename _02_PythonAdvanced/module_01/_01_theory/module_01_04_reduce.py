from functools import reduce

my_list = list(range(1, 6))
multiply = lambda a, b: a * b
print(reduce(multiply, my_list))
# (((1 * 2) * 3) * 4) * 5
