from utils_auth.utils_auth import view_secret_data

if __name__ == '__main__':
    admin_user = {"name": "Alice", "role": "admin"}
    regular_user = {"name": "Bob", "role": "user"}
    view_secret_data(admin_user)
    print()
    view_secret_data(regular_user)
