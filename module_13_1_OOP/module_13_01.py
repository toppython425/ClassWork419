class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        # print("Объект Car создан")


my_car = Car("Toyota", "красный")
friend_car = Car("Ford", "синий")
print(my_car.brand)
print(my_car.color)
print(my_car.wheels)
print()
print(friend_car.brand)
print(friend_car.color)
print(friend_car.wheels)
print()

print(Car.wheels)

