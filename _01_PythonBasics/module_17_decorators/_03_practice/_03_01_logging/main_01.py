from logging_utils.logging_utlis import login, update_profile

if __name__ == '__main__':
    login("Alice")
    update_profile('Alice', {'age': 25, 'city': 'Moscow'})
