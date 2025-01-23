numbers_list = [1, 2, 3]
numbers_iterator = iter(numbers_list)
print(type(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print()

numbers_list = [1, 2, 3]
for number in numbers_list:
    print(number)