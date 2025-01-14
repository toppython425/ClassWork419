class Library(object):

    def __init__(self):
        """Инициализатор класса"""
        self.book_matrix = []

    def add_book(self, title, author):
        """Метод для добавления книги,
        :param=title - название книги,
        :param=author - автор книги,
        :return - строку"""
        self.book_matrix.append([title, author])
        return f'Книга: {title}. Автора {author}. Добавлена в библиотеку.'

    def show_books(self):
        """Метод отображающий в терминале все книги в библиотеке"""
        if not self.book_matrix:
            print("Библиотека пуста!")
        else:
            print("Книги в библиотеке")
            for i, book in enumerate(self.book_matrix, start=1):
                print(f'{i}. Название: {book[0]}. Автор: {book[1]}')

    def find_book(self, title):
        """Метод для поиска книг в библиотеке.
        :param=title - название искомой книги.
        :return - строку"""
        for book in self.book_matrix:
            if title == book[0]:
                return f'Найдена книга: {book[0]} - {book[1]}'
        return 'Книга не найдена!'



