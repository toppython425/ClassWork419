class BaseModel:

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def save(self):
        print(f"Объект с id = {self.__id} сохранен в базу данных")


class User(BaseModel):

    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def display_info(self):
        print(f'Пользователь: {self.name}, ID: {self.id}')


if __name__ == '__main__':
    user = User(1, "Alice")
    user.save()
    user.display_info()
