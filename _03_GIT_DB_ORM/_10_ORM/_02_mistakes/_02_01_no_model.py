# # работа с моделью без модели
# user = User(name="Алиса", age=25)  # Ошибка: класс User не объявлен
# session.add(user)
# session.commit()

# добавляем модель
class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User(name="Алиса", age=25)
    # session.add(user)
    # session.commit()