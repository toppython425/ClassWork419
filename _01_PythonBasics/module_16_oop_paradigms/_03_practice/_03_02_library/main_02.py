from ClassesLibrary import ClassesLibrary_polymorphism

if __name__ == '__main__':
    library = [
        ClassesLibrary_polymorphism.Book("Мастер и Маргарита"),
        ClassesLibrary_polymorphism.Journal("National Geographic"),
        ClassesLibrary_polymorphism.Audiobook("Война и мир", 1200)
    ]

    for item in library:
        print(item.get_info())
