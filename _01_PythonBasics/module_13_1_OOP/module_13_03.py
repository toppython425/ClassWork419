# class Car:
#
#     def drive(self):
#         print("Машина едет")
#
#
# my_car = Car()
# my_car.drive()


# class Car:
#
#     def __init__(self, brand):
#         self.brand = brand
#
#     def drive(self):  # self = my_car
#         print(f"Машина {self.brand} едет")
#
#
# my_car = Car("Toyota")
# my_car.drive()
# print(my_car.brand)


# class Car:
#     wheels = 4
#
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         Car.wheels = 3
#
#
# my_car = Car("Toyota", "Красный")
# print(my_car.wheels)
# print(my_car.brand)
# friend_car = Car('Honda', 'Зеленый')
# print(friend_car.wheels)


# class Car:
#
#     def __init__(self, brand, color="Красный"):
#         self.brand = brand
#         self.color = color
#
#
# my_car = Car('Toyota')
# print(my_car.color)
#
# friend_car = Car('Honda', 'Зеленый')
# print(friend_car.color)

class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


Car.wheels = 3
my_car = Car('Toyota', 'красный')
print(my_car.wheels)
print(Car.wheels)

my_car.doors = 2
print(my_car.doors)
print()

friend_car = Car('Honda', 'Зеленый')
print(friend_car.wheels)
print(friend_car.brand)
print(friend_car.color)
