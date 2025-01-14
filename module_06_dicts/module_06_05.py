# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# #           0  1  2  3  4  5  6  7  8
# #          -9 -8 -7 -6 -5 -4 -3 -2 -1
# print(my_tuple[1])
# print(my_tuple[1:6])
#
# new_tuple = my_tuple + (10, 11,)
# print(new_tuple)
#
# base_tuple = (1, 2, 3,)
# repeated_tuple = base_tuple * 3
# print(base_tuple)
# print(repeated_tuple)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#           0  1  2  3  4  5  6  7  8
#          -9 -8 -7 -6 -5 -4 -3 -2 -1

print(5 in my_tuple)
print(11 in my_tuple)
print(len(my_tuple))

my_tuple = (1, 2, 3, 4, 5, 6, 1, 2, 3)
print(my_tuple.count(3))
print(my_tuple.count(5))

print(my_tuple.index(3))

