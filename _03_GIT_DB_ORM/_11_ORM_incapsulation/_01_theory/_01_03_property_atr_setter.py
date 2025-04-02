class User:

    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.__age = value


if __name__ == '__main__':
    user = User("Ivan", 25)
    print(user.age)
    user.age = 30
    print(user.age)
    user.age = -5