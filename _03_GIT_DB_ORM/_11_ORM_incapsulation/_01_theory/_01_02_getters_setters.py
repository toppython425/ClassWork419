class User:

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.__age = value


if __name__ == '__main__':
    user = User("Ivan", 25)
    print(user.get_age())
    user.set_age(30)
    print(user.get_age())
    user.set_age(-5)