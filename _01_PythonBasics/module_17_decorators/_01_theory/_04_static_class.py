class MyClass:
    @staticmethod
    def greet():
        print('Привет от статического метода')


MyClass.greet()
print()

class MyClass1:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
        print(f'Счётчик: {cls.count}')


print(MyClass1.count)
MyClass1.increment_count()
