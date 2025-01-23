my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["d", "e", "f"]

print(list(zip(my_list1, my_list2, my_list3)))

for item1, item2, item3 in zip(my_list1, my_list2, my_list3):
    print(f'item1: {item1}; item2: {item2}; item3: {item3}')