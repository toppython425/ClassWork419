class Calculator:
    """
    Класс для совершения арифметических операций

    Methods:
        add(cls, a, b) - @classmethod возвращает сумму a и b
    """

    @classmethod
    def add(cls, a, b):
        """
        Складываем два числа
        :param a: int - первое число
        :param b: int - второе число
        :return: int - сумма первого и второго числа
        """
        s = a + b
        return s


print(Calculator.__doc__)
