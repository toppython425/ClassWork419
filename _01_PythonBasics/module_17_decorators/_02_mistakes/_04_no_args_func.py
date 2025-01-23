# def decorator(func):
#     def wrapper():
#         print('Обертка')
#         func()
#
#     return wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print('Обертка')
        func(*args, **kwargs)

    return wrapper


@decorator
def add(a, b, c, d):
    print(a + b + c + d)


if __name__ == '__main__':
    add(3, 4, 5, 6)
