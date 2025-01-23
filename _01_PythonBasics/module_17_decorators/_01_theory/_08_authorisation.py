def authorise(func):
    def wrapper(user):
        if user == 'admin':
            return func()
        else:
            print('Доступ запрещен!')

    return wrapper


@authorise
def secret():
    print("Секретная информация")


if __name__ == '__main__':
    secret('guest')
    print()
    secret('admin')
