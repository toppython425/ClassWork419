class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f'{self.brand} {self.color} едет!')


car_toyota_red = Car('Toyota', 'red')
car_toyota_red.drive()
