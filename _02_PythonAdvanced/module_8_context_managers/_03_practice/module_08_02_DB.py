class DBConnection:

    def __enter__(self):
        print("Открываем соединение с БД")
        return self  # возвращаем 'соединение'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Закрываем соединение с БД")
        if exc_type:
            print(f'Произошла ошибка: {exc_type.__name__} - {exc_val}')
        return True


with DBConnection():
    print('Работем с БД')
