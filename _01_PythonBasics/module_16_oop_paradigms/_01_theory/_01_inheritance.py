class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'Я животное по имени: {self.name}'


class Dog(Animal):
    def speak(self):
        return f'Я собака {self.name}. Гав-гав!'


class Cat(Animal):
    def speak(self):
        return f'Я кот {self.name}. Мяу-мяу!'


if __name__ == '__main__':
    dog = Dog("Шарик")
    print(dog.name)
    print(dog.speak())
    print()

    cat = Cat("Мурзик")
    print(cat.name)
    print(cat.speak())

