# class Car:
#     wheels = 4
#
#     @classmethod
#     def change_color(cls, color):
#         cls.color = color


class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def set_color(self, color):
        self.color = color
