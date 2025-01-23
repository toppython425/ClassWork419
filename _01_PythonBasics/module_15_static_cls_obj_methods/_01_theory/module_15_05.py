# class Car:
#
#     def general_info():  # Ожидалось @staticmethod
#         print("Машины — это транспортные средства.")
#
#
# Car.general_info()


class Car:
    @staticmethod
    def general_info():  # Ожидалось @staticmethod
        print("Машины — это транспортные средства.")


Car.general_info()
