class User:

    def __init__(self, name, age):
        self._name = name  # protected attr
        self._age = age  # protected attr

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value
    #
    # @property
    # def age(self):
    #     return self._age
    #
    # @age.setter
    # def age(self, value):
    #     self._age = value

    def __str__(self):
        return f'Пользователь: {self._name}, возраст регистрации: {self._age}'


if __name__ == '__main__':
    user = User("Ivan", 25)
    print(user)

