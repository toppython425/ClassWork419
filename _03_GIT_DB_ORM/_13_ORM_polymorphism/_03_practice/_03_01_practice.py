class Model:
    def save(self):
        print("Начало процесса сохранения")


class UserModel(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        super().save()
        print(f'Сохранение пользователя: {self.name}, email: {self.email}')


class ProductModel(Model):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def save(self):
        super().save()
        print(f'Сохранение товара: {self.title}, цена: {self.price}')


if __name__ == '__main__':
    user = UserModel('Alice', 'alice@mail.ru')
    user.save()
    product = ProductModel('RTX 4070 Ti Super', 100000)
    product.save()
