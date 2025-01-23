class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Студент: {self.name}, возраст: {self.age}'

    def __repr__(self):
        return f'obj - class Student("{self.name}", {self.age})'


if __name__ == '__main__':
    student = Student('Иван', 16)
    print(student.name)
    print(student.age)
    print(student)
    print(repr(student))
    # print(student.__repr__())

