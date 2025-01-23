from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        # return 3.14 * self.radius ** 2
        return round(pi * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print(circle.calculate_area())
    print(rectangle.calculate_area())



