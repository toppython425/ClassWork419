def validate_email(func):
    def wrapper(self, *args, **kwargs):
        if hasattr(self, 'email'):
            if '@' not in self.email:
                raise ValueError('Некорректный email')
        return func(self, *args, **kwargs)

    return wrapper


class User:
    users_list = []

    def __init__(self, email):
        self.email = email

    @validate_email
    def save(self):
        User.users_list.append(self.email)
        print(f'Пользователь с email: {self.email} сохранен')


if __name__ == '__main__':
    valid_user = User('alice@example.com')
    invalid_user = User('invalid_email')
    users_list = [valid_user, invalid_user]
    for user in users_list:
        try:
            user.save()
        except ValueError as ex:
            print(ex)

    print(User.users_list)
