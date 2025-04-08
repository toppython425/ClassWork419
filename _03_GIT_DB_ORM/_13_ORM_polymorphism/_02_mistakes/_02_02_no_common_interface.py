# магические методы (__getattr__, __getattribute__, __setattr__);
# динамическое создание атрибутов и методов (например, через setattr);
# декораторы (например, @property), которые позволяют управлять доступом к атрибутам.


# class DynamicModel:
#     def __getattr__(self, name):
#         print(f'Атрибут {name} не найден, но мы его создали!')
#         value = f'Значение для {name}'
#         setattr(self, name, value)
#         return value


class DynamicModel:

    def __init__(self, username=None):
        self.__username = username

    @property
    def username(self):
        if not self.__username:
            raise AttributeError("Атрибут username не задан")
        return self.__username


if __name__ == '__main__':
    model = DynamicModel("name")
    print(model.username)
    print(model.username)
