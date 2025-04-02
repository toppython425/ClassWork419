from ClassUserProtected import User

if __name__ == '__main__':
    user = User(1, "Иван Иванов", "ivan@example.com")
    print(user.name, user.email)
    # user.name = "   "  # Некорректное значение
    # user.email = "invalid-email"  # Некорректный email
    user.name = " петр петров   "
    user.email = 'petr@example.com'

    user.save()  # Сохранение некорректных данных
