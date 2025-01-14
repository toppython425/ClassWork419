def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Ошибка: деление на ноль.'
        return a / b
    else:
        return 'Ошибка: некорректная операция!'
