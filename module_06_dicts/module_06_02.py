# person = {'name': 'Ivan', 'age': 30}
# age = person.get('age')
# print(age)
# surname = person.get('surname', 'Ivanov')
# print(surname)
# print(person)
# surname = person.setdefault('surname', 'Ivanov')
# print(surname)
# print(person)

# person = {'name': 'Ivan', 'age': 30, 'surname': 'Ivanov'}
# keys = person.keys()
# print(keys)
# # keys_list = list(keys)
# # print(keys_list)
# print(type(keys))
#
# values = person.values()
# print(values)
# print(type(values))
#
# items = person.items()
# print(items)
# print(type(items))

person = {'name': 'Ivan', 'age': 30, 'surname': 'Ivanov'}
data_to_update = {'age': 32, 'city': 'Moscow'}
person.update(data_to_update)
print(person)

popped_item = person.pop('city')
print(popped_item)
print(person)

# popped_item = person.pop('last_name')
# print(popped_item)
# print(person)

print(person['name'])
person['age'] = 35
print(person)

print('name' in person)