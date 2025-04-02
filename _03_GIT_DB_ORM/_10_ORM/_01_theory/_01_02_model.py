class User:
    def __init__(self, uid, name, age):
        self.uid = uid
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User(1, "Alice", 25)
