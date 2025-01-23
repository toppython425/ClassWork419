def log(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(3, 4))
