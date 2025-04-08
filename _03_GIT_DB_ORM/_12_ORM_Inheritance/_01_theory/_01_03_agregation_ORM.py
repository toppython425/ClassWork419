class Animal:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, animal_obj, breed):
        self.animal_obj = animal_obj
        self.breed = breed


if __name__ == '__main__':
    animal = Animal('Бобик')
    dog = Dog(animal, 'Дворняжка')
    print(dog.animal_obj.name)
    print(dog.breed)
