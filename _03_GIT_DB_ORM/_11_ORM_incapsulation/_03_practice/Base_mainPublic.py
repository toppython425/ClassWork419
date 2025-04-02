from Base_ClassUserPublic import User

if __name__ == '__main__':
    user = User(1, "Иван Иванов", "ivan@example.com")
    user.name = ""  # Некорректное значение
    user.email = "invalid-email"  # Некорректный email
    user.save()  # Сохранение некорректных данных
