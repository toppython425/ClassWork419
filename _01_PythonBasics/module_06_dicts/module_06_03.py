person = {'name': 'Ivan', 'age': 32, 'surname': 'Ivanov', 'city': 'Moscow'}

for key in person:
    print(f'Key - {key}')
print()

for key in person.keys():
    print(f'Key - {key}')
print()

for value in person.values():
    print(f'Value - {value}')
print()

for key, value in person.items():
    print(f'Key - {key}, Value - {value}')
print()

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for a, b, c in matrix:
#     print(a, b, c)