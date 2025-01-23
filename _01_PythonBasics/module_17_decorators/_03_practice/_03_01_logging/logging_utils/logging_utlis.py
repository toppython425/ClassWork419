from _01_PythonBasics.module_17_decorators._03_practice._03_01_logging.logging_utils.logging_decorators import log_action


@log_action
def login(username):
    print(f'{username} вошел в систему.')


@log_action
def update_profile(username, profile_data):
    print(f'{username} обновил профиль с данными: {profile_data}')
