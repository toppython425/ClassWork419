def create_phone_list(filename, contacts):
    with open(fr'files\{filename}.txt', 'w', encoding='utf-8') as file:
        for name, phone in contacts.items():
            file.write(f'{name}: {phone}\n')
    return rf'Данные записаны успешно! Путь к файлу из текущей директории files\{filename}.txt'


def read_phone_list(filename):
    try:
        with open(fr'files\{filename}.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
        return 'Данные успешно получены'
    except FileNotFoundError:
        return 'Файл с контактами не найден!'
    except IOError:
        return 'Ошибка ввода-вывода!'


my_contacts = {'Иван': '123-456', 'Мария': '798-012'}
my_filename = input('Введите имя файла для записи: ')
print(create_phone_list(my_filename, my_contacts))
print(read_phone_list(my_filename))
