class Dog:
    def speak(self):
        return f'Я собака. Гав-гав!'


class Cat:
    def speak(self):
        return f'Я кот. Мяу-мяу!'


class Robot:
    def speak(self):
        return f'Я робот. Убить всех людей!'


# cat = Cat()
# dog = Dog()
# animals_obj_list = [cat, dog]

animals_obj_list = [Cat(), Dog(), Robot()]
for animal_obj in animals_obj_list:
    print(animal_obj.speak())
