# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.breed = breed


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         Animal.__init__(self, name, age)
#         self.breed = breed


if __name__ == '__main__':
    dog = Dog("Шарик", 3, "Овчарка")
    print(dog.name)
    print(dog.age)
    print(dog.breed)
