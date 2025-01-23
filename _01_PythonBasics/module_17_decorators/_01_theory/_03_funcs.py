def decorator(func):
    def wrapper(name):
        print('До вызова функции')
        func(name)
        print('После вызова функции')

    return wrapper


@decorator
def say_hello(name):
    print(f'Hello, {name}')


@decorator
def say_good_bye(name):
    print(f'Good bye! {name}')


say_hello("John")
print()
say_good_bye("John")
