class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


circle = Circle(5)
print(circle.radius)


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)
