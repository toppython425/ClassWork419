def add_book(library, title, author):
    if title in library:
        return f'Книга {title} уже существует'
    library[title] = author
    return f'Книга {title} добавлена'


def remove_book(library, title):
    if title in library:
        del library[title]
        return f'Книга {title} удалена'
    return 'Книга не найдена'


def list_books(library):
    books_list = []
    # if not library:
    if len(library) == 0:
        return "Библиотека пуста"
    for title, author in library.items():
        books_list.append(f'{title} - {author}')
    return "\n".join(books_list)
