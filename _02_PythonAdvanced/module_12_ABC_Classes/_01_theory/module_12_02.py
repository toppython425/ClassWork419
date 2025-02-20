from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return self.width * 4


if __name__ == '__main__':
    circle = Circle(5)
    print(f'Площадь круга: {circle.area()}')
    print()

    square = Square(6)
    print(f'Площадь квадрата: {square.area()}')
    print(f'Периметр квадрата: {square.perimeter()}')


