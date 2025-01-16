# class Car:
#     wheels = 4
#
#     @classmethod
#     def describe(self):
#         print(f'Большинство машин имеют {self.wheels} колеса')
#
#
# Car.describe()


class Car:
    wheels = 4

    @classmethod
    def describe(cls):
        print(f'Большинство машин имеют {cls.wheels} колеса')


Car.describe()

