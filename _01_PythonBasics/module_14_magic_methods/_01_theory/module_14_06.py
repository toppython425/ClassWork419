# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.age
#
#
# student = Student('Иван', 16)
# print(student)


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Студент: {self.name}, возраст: {self.age}'


student = Student('Иван', 16)
print(student)