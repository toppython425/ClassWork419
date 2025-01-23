from abc import ABC, abstractmethod


# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#
# class Circle(Shape):
#     pass


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def calculate_area(self):
        return 3.14 * 5 ** 2
