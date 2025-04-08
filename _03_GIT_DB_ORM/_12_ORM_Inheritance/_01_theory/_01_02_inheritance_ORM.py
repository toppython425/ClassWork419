from datetime import datetime

class BaseModel:

    def __init__(self, id):
        self.__id = id
        self.__created_at = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    def save(self):
        print(f"Объект с id = {self.__id} сохранен в базу данных")


class User(BaseModel):

    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

class Product(BaseModel):

    def __init__(self, id, title, price):
        super().__init__(id)
        self.__title = title
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price


if __name__ == '__main__':
    user = User(1, "Alice")
    product = Product(101, "Laptop", 999.99)

    user.save()
    product.save()

    print(user.created_at)
    print(product.created_at)

