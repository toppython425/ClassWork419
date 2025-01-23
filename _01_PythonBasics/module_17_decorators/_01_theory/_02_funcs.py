def decorator(func):
    def wrapper():
        print('До вызова функции')
        func()
        print('После вызова функции')

    return wrapper


@decorator
def say_hello():
    print('Hello, world!')


@decorator
def say_good_bye():
    print('Good bye!')


say_hello()
print()
say_good_bye()
