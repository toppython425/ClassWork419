# my_list = [1, 2, 3]
# squares_list = []
#
# for elem in my_list:
#     squares_list.append(elem ** 2)
#
# print(squares_list)


my_list = [1, 2, 3, 4]
results = map(lambda x: x ** 2, my_list)
print(results)
print(list(results))

my_list = [1, 2, 3, 4]


def get_square(x):
    return x ** 2


results = map(get_square, my_list)
print(results)
print(list(results))
