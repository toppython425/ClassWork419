from classes1 import FileDataManager, DatabaseDataManager

if __name__ == '__main__':
    file_manager = FileDataManager()
    file_manager.save("Данные для записи в файл и последующего чтения из файла")
    print(file_manager.load())
    print()

    db_manager = DatabaseDataManager()
    db_manager.save("Данные для БД")
    print(db_manager.load())
