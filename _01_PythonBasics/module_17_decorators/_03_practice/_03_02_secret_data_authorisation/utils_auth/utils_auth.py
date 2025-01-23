from _01_PythonBasics.module_17_decorators._03_practice._03_02_secret_data_authorisation.utils_auth.decorators_auth import \
    authorise_admin

@authorise_admin
def view_secret_data(user):
    print(f'Секретные данные доступны для {user['name']}.')
