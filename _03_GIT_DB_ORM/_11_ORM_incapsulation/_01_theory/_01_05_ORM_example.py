class User:
    def __init__(self, uid, name, email):
        self.__id = uid
        self.__name = name
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Некорректный email")
        self.__email = value

    def save(self):
        # логика для сохранения
        print(f'Сохранение пользователя: {self.__name}, email: {self.__email}')


if __name__ == '__main__':
    user = User(1, "Иван Иванов", 'ivan@web.top')

    user.email = 'ivanBest@web.top'
    # user.email = 'ivanBestweb.top'

    user.save()
