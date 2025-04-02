# class User:
#
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#
# if __name__ == '__main__':
#     user = User("Ivan", 25)
#     print(user._name)
#     print(user._User__age)


class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age  # protected attr


if __name__ == '__main__':
    user = User("Ivan", 25)
