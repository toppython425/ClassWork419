class User:
    all_users = []

    def __init__(self, id, name, email):
        self._id = id  # Приватный атрибут
        self._name = name  # Приватный атрибут
        self._email = email  # Приватный атрибут

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def save(self):
        User.all_users.append({'id': self._id, 'name': self._name, 'email': self._email})
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")

    def delete_user(self, user_id):
        for user in User.all_users:
            if user['id'] == user_id:
                User.all_users.remove(user)
                print(f'Администратор удалил пользователя с id = {user_id}')
                break
        else:
            print('Пользователя с таким id не существует')


class Admin(User):
    def __init__(self, id, name, email, role):
        super().__init__(id, name, email)
        self._role = role

    @property
    def role(self):
        return self._role


if __name__ == '__main__':
    new_user = User(100, 'User Userov', 'user@web.top')
    new_user.save()
    admin = Admin(101, 'Admin Adminov', 'admin@web.top', 'superuser')
    admin.save()
    print(User.all_users)
    admin.delete_user(100)
    print(User.all_users)
