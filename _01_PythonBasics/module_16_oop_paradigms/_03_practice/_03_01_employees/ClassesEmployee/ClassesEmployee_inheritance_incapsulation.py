class Employee:
    def __init__(self, first_name, last_name, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    def get_info(self):
        return f'{self.__first_name} {self.__last_name}'

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, bonus):
        super().__init__(first_name, last_name, salary)
        self.__bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.__bonus


class Intern(Employee):
    def __init__(self, first_name, last_name, salary, discount_rate):
        super().__init__(first_name, last_name, salary)
        self.__discount_rate = discount_rate

    def get_salary(self):
        return super().get_salary() * self.__discount_rate



