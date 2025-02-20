from abc import ABC, abstractmethod


class Person(ABC):
    @property
    @abstractmethod
    def name(self):
        pass


class Student(Person):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    student = Student("Иван")
    print(student.name)