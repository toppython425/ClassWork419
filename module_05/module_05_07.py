# my_set = {1, 2, [3, 4]}
# print(my_set)

my_set = {1, 2, (3, 4)}
# print(my_set)

# my_set.remove(6)
my_set.discard(6)


# my_set = {1, 2, 3, 4}
# for item in my_set:
#     my_set.add(5)
# print(my_set)

my_set = {1, 2, 3, 4}
for item in my_set.copy():
    my_set.add(5)
print(my_set)