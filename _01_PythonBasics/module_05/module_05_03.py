data_set_1 = {1, 2, 3, 4, 5}
data_set_2 = {3, 4, 5, 6, 7}
# data_list_2 = [3, 4, 5, 6, 7]
print(data_set_1.union(data_set_2))
# print(data_set_1.union(data_list_2))
print(data_set_1 | data_set_2)
print()

print(data_set_1.intersection(data_set_2))
print(data_set_1 & data_set_2)
print()

print(data_set_1.difference(data_set_2))
print(data_set_2.difference(data_set_1))

print(data_set_1 - data_set_2)
print(data_set_2 - data_set_1)
print()

print(data_set_1.symmetric_difference(data_set_2))
print(data_set_1 ^ data_set_2)

