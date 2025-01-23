# def decorator(func):
#     def wrapper():
#         print('Декоратор работает')
#
#
# @decorator
# def say_hello():
#     print("Привет!")


def decorator(func):
    def wrapper():
        print('Декоратор работает')
        func()

    return wrapper


@decorator
def say_hello():
    print("Привет!")


if __name__ == '__main__':
    say_hello()
