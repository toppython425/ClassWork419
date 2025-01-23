from functools import wraps


# def decorator(func):
#     def wrapper():
#         print('Обертка')
#         func()
#
#     return wrapper
#
#
# @decorator
# def greet():
#     print("Привет")

def decorator(func):
    @wraps(func)
    def wrapper():
        print('Обертка')
        func()

    return wrapper


@decorator
def greet():
    print("Привет")


if __name__ == '__main__':
    print(greet.__name__)
