from Classes import Book, Library

library = Library()

while True:
    command = input('Введите команду: 1 - добавить, 2 - изменить статус, 3 - показать, 0 - выход: ').strip()
    if command == '0':
        print('Программа завершена.')
        break
    elif command == '1':
        title = input('Название книги: ').strip()
        author = input('Автор: ').strip()
        library.add_book(Book(title, author))
        print(f'Книга: {title}. Автора: {author}. Добавлена в библиотеку.')
    elif command == '2':
        title = input('Название книги: ').strip()
        new_status = input("Введите новый статус книги (по умолчанию 'в наличии'): ").strip()
        print(library.change_status(title, new_status))
    elif command == '3':
        library.show_books()
    else:
        print('Неизвестная команда. Попробуйте снова!')
