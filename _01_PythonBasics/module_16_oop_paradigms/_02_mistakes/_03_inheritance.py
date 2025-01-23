# class Animal:
#     def speak(self):
#         return f'Я животное'
#
#
# class Dog(Animal):
#     def speak(self):
#         return f'Я собака. Гав-гав!'
#
#

class Animal:
    def speak(self):
        return f'Я животное'


class Dog(Animal):
    def speak(self):
        return f'{super().speak()}\nЯ собака. Гав-гав!'


if __name__ == '__main__':
    dog = Dog()
    print(dog.speak())
