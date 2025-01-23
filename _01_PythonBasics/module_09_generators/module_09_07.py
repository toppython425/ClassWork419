def get_multiples_by_second_param(limit, divisor):
    for number in range(1, limit + 1):
        if number % divisor == 0:
            yield number


user_limit = int(input("Введите верхний предел: "))
user_divisor = int(input("Введите делитель: "))

print(f'Числа от 1 до {user_limit}, кратные {user_divisor}: ')
for multiple in get_multiples_by_second_param(user_limit, user_divisor):
    print(multiple)


def get_multiples_by_second_param_with_lc(limit, divisor):
    return [number for number in range(1, limit + 1) if number % divisor == 0]


user_limit = int(input("Введите верхний предел: "))
user_divisor = int(input("Введите делитель: "))
print(f'Числа от 1 до {user_limit}, кратные {user_divisor}: ')
print(get_multiples_by_second_param_with_lc(user_limit, user_divisor))
