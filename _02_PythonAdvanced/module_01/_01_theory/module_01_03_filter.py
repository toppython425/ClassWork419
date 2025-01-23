# my_list = list(range(8 + 1))
# print(my_list)
#
# even_list = []
# odd_list = []
#
# for item in my_list:
#     if item % 2 == 0:
#         even_list.append(item)
#     else:
#         odd_list.append(item)
#
# print(even_list)
# print(odd_list)


my_list = list(range(8 + 1))
is_even = lambda x: x % 2 == 0
print(is_even(2))
print(is_even(3))
result = filter(is_even, my_list)
print(result)
print(list(result))


def is_even1(x):
    return x % 2 == 0


result = filter(is_even1, my_list)
print(result)
print(list(result))
