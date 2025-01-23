from functools import wraps


def authorise_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("role") == 'admin':
            return func(user, *args, **kwargs)
        else:
            print(f'Доступ для пользователя: {user['name']} запрещен!')
    return wrapper



