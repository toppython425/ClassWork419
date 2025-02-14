class DBConnection:
    def __enter__(self):
        print("Открываем соединение с БД")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Закрываем соединение с БД")
        if exc_type:
            print(f'Ошибка: {exc_type.__name__} - {exc_val}')
        return True


class FileWriter:

    def __enter__(self):
        self.file = open(r'files\log.txt', 'w', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f'Ошибка в файле: {exc_type.__name__} - {exc_val}')
        return True


if __name__ == '__main__':
    with DBConnection() as db, FileWriter() as file:
        file.file.write("Запись в лог файл")
        print('Работаем с БД')
