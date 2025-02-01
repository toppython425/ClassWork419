def process_number(value: int):
    if not isinstance(value, int):
        raise TypeError(f'Ожидалось значение типа int, получено {type(value).__name__}')
    return value ** 2


print(process_number(5))
print(process_number("5"))
