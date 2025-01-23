# class Dog:
#     def speak(self, times):
#         return f'Я собака. Гав-гав!' * times
#
#
# class Cat:
#     def speak(self, ):
#         return f'Я кот. Мяу-мяу!'


class Dog:
    def speak(self):
        return f'Я собака. Гав-гав!'


class Cat:
    def speak(self):
        return f'Я кот. Мяу-мяу!'


animals_obj_list = [Cat(), Dog()]
for animal_obj in animals_obj_list:
    print(animal_obj.speak())
