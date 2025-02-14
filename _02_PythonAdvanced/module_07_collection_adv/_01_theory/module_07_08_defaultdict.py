from collections import defaultdict


# dd = defaultdict(list)
# print(dd)
# dd['a'].append(1)
# dd['b'].append(2)
# dd['c'].append(3)
# print(dd)
# dd['a'].append(4)
# print(dd)

# dd1 = defaultdict(int)
# print(dd1)
# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# for fruit in data:
#     dd1[fruit] += 1
#     print(dd1)
# print(dd1)

def default_value():
    return 'Значение по умолчанию'


dd_func = defaultdict(default_value)
print(dd_func['missing_key'])

data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped = defaultdict(list)

for key, value in data:
    grouped[key].append(value)

print(grouped)
