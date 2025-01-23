# my_list = [1, 2, 'ab', 3, 'cd', 4]
# results = map(lambda x: len(x), my_list)
# print(list(results))

my_list = [1, 2, 'ab', 3, 'cdad', 4]
str_list = filter(lambda x: type(x) is str, my_list)

results = map(lambda x: len(x), list(str_list))
print(list(results))
