from library import add_book, remove_book, list_books

library = {}
while True:
    command = input("Введите команду (add, remove, list, exit): ").strip().lower()
    if command == 'add':
        title = input('Введите название книги: ').strip()
        author = input('Введите автора книги: ').strip()
        print(add_book(library, title, author))

    elif command == 'remove':
        title = input('Введите название книги для удаления: ').strip()
        print(remove_book(library, title))

    elif command == 'list':
        print('Список книг:')
        print(list_books(library))

    elif command == 'exit':
        print('Выход и из программы')
        break

    else:
        print('Неизвестная команда')
