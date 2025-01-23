# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'obj - class Student({self.name}, {self.age})'
#
#
# if __name__ == '__main__':
#     student = Student('Иван', 16)
#     print(student.name)
#     print(student.age)
#     print(student)
#     print(repr(student))
#     student_1 = Student(Иван, 16)
#     # print(student.__repr__())


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Student("{self.name}", {self.age})'


if __name__ == '__main__':
    student = Student('Иван', 16)
    print(student)
    student1 = Student("Иван", 16)
    print(student1)
    print(student is student1)