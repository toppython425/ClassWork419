import ClassLibrary

library = ClassLibrary.Library()
library.add_book('1984', 'Джордж Оруэлл')
library.add_book('Мастер и Маргарита', 'Михаил Булгаков')
library.show_books()
print(library.find_book('1984'))
print(library.find_book('Собачье сердце'))
print()
print(library.book_matrix)

# books_dict = {'автор': ['книга1', 'книга2']}
