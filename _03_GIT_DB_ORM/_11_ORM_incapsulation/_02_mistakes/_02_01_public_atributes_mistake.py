# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# if __name__ == '__main__':
#     user = User("Ivan", 25)
#     print(user.name)
#     print(user.age)


class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value


if __name__ == '__main__':
    user = User('Ivan', 25)
    user.age = 30
    print(user.age)
