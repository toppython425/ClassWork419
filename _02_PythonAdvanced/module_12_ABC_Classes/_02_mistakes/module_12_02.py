from abc import ABC, abstractmethod
from math import pi


# class Shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     # def area(self):
#     #     return pi * self.radius ** 2
#
#
# if __name__ == '__main__':
#     circle = Circle(5)

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5)
    print(round(circle.area(), 2))

