class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student('Иван', 16)
s2 = Student('Иван', 16)
s3 = Student('Peter', 17)

print(s1 == s2)
print(s1 == s3)


