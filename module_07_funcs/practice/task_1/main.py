from math_operations import calculator

while True:
    print('\nПростой калькулятор: ')
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        operation = input('Введите операцию (add, subtract, multiply, divide): ').strip().lower()

        result = calculator(a, b, operation)
        print(f'Результат: {result}')
    except ValueError:
        print('Ошибка введите корректные числа.')
    user_input = input('Хотите продолжить? (yes/no)').strip().lower()
    if user_input != 'yes':
        break
