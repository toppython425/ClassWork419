class User:
    def __init__(self, uid, name, email):
        self.__id = uid
        self.__name = name
        self.__email = email

    @property
    def email(self):
        return self.__email

    # @email.setter
    # def email(self, value):
    #     self.__email = value

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Некорректный ввод")
        self.__email = value


if __name__ == '__main__':
    user = User(1, "Иван Иванов", 'ivan@web.top')
    # user.email = 'ivanBestweb.top'
    user.email = 'ivanBest@web.top'
    print(user.email)
