from module_14_magic_methods._01_theory.module_14_01 import Student


# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other: object):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f'Vector({self.x}, {self.y})'
#
#
# v1 = Vector(1, 2)
# s1 = Student('Name', 17)
# v3 = v1 + s1
# # v2 = Vector(3, 4)
# # v3 = v1 + v2
# # print(v3)
# # print(v3.x)
# # print(v3.y)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: object):
        if not isinstance(other, Vector):
            raise TypeError('Сложение возможно только между объектами класса Vector')
            # return 'Сложение возможно только между объектами класса Vector'
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'


v1 = Vector(1, 2)
v2 = Vector(3, 4)
s1 = Student('Name', 17)
print(v1 + s1)
v3 = v1 + v2


print(v3)
print(v3.x)
print(v3.y)
