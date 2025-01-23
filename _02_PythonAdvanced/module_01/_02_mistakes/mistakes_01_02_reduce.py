from functools import reduce

# my_list = list(range(5))
# print(my_list)
# print(reduce(lambda a: a ** 2, my_list))

my_list = list(range(1, 5))
print(my_list)
print(reduce(lambda a, b: a * b, my_list))

