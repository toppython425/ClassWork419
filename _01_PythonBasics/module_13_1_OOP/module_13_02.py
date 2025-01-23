class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} цвет {self.color} - едет!')

    def stop(self):
        print(f'{self.brand} цвет {self.color} остановился!')


my_car = Car("Toyota", "красный")
friend_car = Car("Ford", "синий")

my_car.drive()  # drive(my_car)
my_car.stop()
print()

friend_car.drive()
friend_car.stop()


