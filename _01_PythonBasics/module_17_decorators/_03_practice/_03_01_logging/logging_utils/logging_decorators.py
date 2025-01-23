from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        with open(r'logs\actions.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'Пользователь {username}, действие: {func.__name__}\n')
        return func(username, *args, *kwargs)

    return wrapper
