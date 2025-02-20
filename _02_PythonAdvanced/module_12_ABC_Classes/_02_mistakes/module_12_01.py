from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'Woof! Woof!'


if __name__ == '__main__':
    """НЕПРАВИЛЬНО! Попытка инстанцировать абстрактный класс (создать объект абстрактного класса)"""
    # animal = Animal()

    """ПРАВИЛЬНО! Работа через конкретный класс (подкласс абстрактного класса)"""
    dog = Dog()
    print(dog.make_sound())

