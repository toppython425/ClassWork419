class User:
    def __init__(self, id, name, email):
        self.__id = id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__email = email  # Приватный атрибут

    # Task1
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Имя не может быть пустым')
        self.__name = value.strip().title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Некорректный email")
        self.__email = value

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.__name}, email: {self.__email}")
