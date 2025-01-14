my_tuple = (1, 2, 3)
# my_tuple[1] = 10

new_tuple = my_tuple[:1] + (10,) + my_tuple[2:]
print(new_tuple)

# my_dict = {[1, 2, 3]: 'value'}
my_dict = {(1, 2, 3): 'value'}
print(my_dict)

# my_operator = "мтс"
# called_operator = 'билайн'
# tariffs_dict = {("мтс", 'билайн'): 50}
# time = 10
# call_cost = tariffs_dict[(my_operator, called_operator)] * time
# print(call_cost)

# person = {'name': 'Ivan', 'age': 30}
# # print(person['city'])
# print(person.get('city'))
# if person.get('city') is None:
#     person['city'] = 'не указан'
# print(person)


my_dict = {"a": 1, "b": 2, "c": 3}
for key in list(my_dict.keys()):
    if my_dict.get('a') == 1:
        my_dict.pop(key)
print(my_dict)

my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()
print(my_dict)