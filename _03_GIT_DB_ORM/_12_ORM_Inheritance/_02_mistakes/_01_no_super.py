class Animal:
    def __init__(self, name):
        self.name = name


# class Dog(Animal):
#
#     def __init__(self, name, breed):
#         self.breed = breed

# class Dog(Animal):
    #
    # def __init__(self, name, breed):
    #     super().__init__(name)
    #     self.breed = breed


class Dog(Animal):

    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed


if __name__ == '__main__':
    dog = Dog('Бобик', 'Дворняжка')
    print(dog.name)
