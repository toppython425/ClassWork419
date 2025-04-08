class Model:
    def __init__(self):
        self._data = {}

    def save(self):
        raise NotImplementedError("Метод save() должен быть переопределен в подклассе")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, dict):
            raise ValueError('Данные должны быть словарем')
        self._data = value


class User(Model):
    def save(self):
        print(f'Пользователь сохранен: {self.data}')


class Product(Model):
    def save(self):
        print(f'Товар сохранен: {self.data}')


if __name__ == '__main__':
    user = User()
    user.data = {'id': 1, 'name': 'Alice'}
    user.save()

    product = Product()
    product.data = {'id': 1, 'name': 'RTX 4070 Ti Super'}
    product.save()
