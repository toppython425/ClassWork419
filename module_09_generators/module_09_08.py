def even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


user_start = int(input("Введите начало диапазона: "))
user_end = int(input("Введите конец диапазона: "))

print(f'Четные числа от {user_start} до {user_end}:')
for even in even_numbers(user_start, user_end):
    print(even)


def even_numbers_with_lc(start, end):
    return [number for number in range(start, end + 1) if number % 2 == 0]


user_start = int(input("Введите начало диапазона: "))
user_end = int(input("Введите конец диапазона: "))

print(f'Четные числа от {user_start} до {user_end}:')
print(even_numbers_with_lc(user_start, user_end))
print()

even_numbers_gen = (number for number in range(user_start, user_end + 1) if number % 2 == 0)
for even in even_numbers_gen:
    print(even)