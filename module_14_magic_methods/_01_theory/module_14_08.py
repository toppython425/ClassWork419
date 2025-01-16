class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name


s1 = Student('Иван', 16)
s2 = Student('Иван', 16)
s3 = Student('Иван', 18)
s4 = Student('Peter', 17)

print(s1 == s2)
print(s1 == s3)
print(s1 == s4)
print()


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student('Иван', 16)
s2 = Student('Иван', 16)
s3 = Student('Иван', 18)
s4 = Student('Peter', 17)

print(s1 == s2)
print(s1 == s3)
print(s1 == s4)
