class LibraryBook:
    total_books = 0

    def __init__(self, title, status='доступна'):
        self.title = title
        self.status = status
        LibraryBook.total_books += 1

    @classmethod
    def get_number_total_books(cls):
        return f'Всего книг в библиотеке: {cls.total_books}'

    @staticmethod
    def is_available(status):
        return status == 'доступна'

    def change_status(self, new_status):
        self.status = new_status


book_1 = LibraryBook('Мастер и маргарита')
book_2 = LibraryBook('1984')

# print(book_1.title, '-', 'Доступна' if LibraryBook.is_available(book_1.status) else "Недоступна")
if LibraryBook.is_available(book_1.status):
    print(f'{book_1.title} - Доступна')
else:
    print(f'{book_1.title} - Недоступна')

book_1.change_status('в аренде')
# print(book_1.title, '-', 'Доступна' if LibraryBook.is_available(book_1.status) else "Недоступна")
if LibraryBook.is_available(book_1.status):
    print(f'{book_1.title} - Доступна')
else:
    print(f'{book_1.title} - Недоступна')
print(LibraryBook.total_books)
