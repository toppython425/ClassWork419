class Wheels:
    def __init__(self, radius):
        self.radius = radius


class Doors:
    def __init__(self, wheels_obj, num_of_doors):
        self.wheels_obj = wheels_obj
        self.num_of_doors = num_of_doors


class Engine:
    def __init__(self, doors_obj, type_of_engine):
        self.doors_obj = doors_obj
        self.type_of_engine = type_of_engine


class Car:
    def __init__(self, engine_obj):
        self.engine_obj = engine_obj

    def display_info(self):
        print("Автомобиль:")
        print(f'Радиус дисков: {self.engine_obj.doors_obj.wheels_obj.radius}')
        print(f'Количество дверей: {self.engine_obj.doors_obj.num_of_doors}')
        print(f'Тип двигателя: {self.engine_obj.type_of_engine}')


if __name__ == '__main__':
    wheels = Wheels(19)
    doors = Doors(wheels, 4)
    engine = Engine(doors, "Бензиновый")
    car = Car(engine)
    car.display_info()
