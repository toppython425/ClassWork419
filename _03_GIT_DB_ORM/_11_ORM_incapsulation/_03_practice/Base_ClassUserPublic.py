class User:
    def __init__(self, id, name, email):
        self.id = id  # Публичный атрибут
        self.name = name  # Публичный атрибут
        self.email = email  # Публичный атрибут

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")
