class Wheels:
    def __init__(self, radius):
        self.radius = radius


class Doors:
    def __init__(self, num_of_doors):
        self.num_of_doors = num_of_doors


class Engine:
    def __init__(self, type_of_engine):
        self.type_of_engine = type_of_engine


class Car:
    def __init__(self, wheels, doors, engine):
        self.wheels = wheels
        self.doors = doors
        self.engine = engine

    def display_info(self):
        print("Автомобиль:")
        print(f'Радиус дисков: {self.wheels.radius}')
        print(f'Количество дверей: {self.doors.num_of_doors}')
        print(f'Тип двигателя: {self.engine.type_of_engine}')


if __name__ == '__main__':
    car = Car(Wheels(18), Doors(4), Engine("Бензин"))
    car.display_info()