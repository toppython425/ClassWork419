from utils import is_file_exists, add_participants, display_participants

if __name__ == '__main__':
    file_name = r'files\participants.txt'
    print(is_file_exists(file_name))

    while True:
        command = input('Введите команду (1 - add, 2 - show, 0 - exit): ').strip().lower()
        if command == '1':
            name = input("Введите имя участника: ").strip().title()
            add_participants(file_name, name)
            print("Участник добавлен!")

        elif command == '2':
            print()
            display_participants(file_name)
            print()

        elif command == '0':
            print('Программа завершена')
            break

        else:
            print('Неизвестная команда, попробуйте снова!')
