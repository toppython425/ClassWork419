class Square:
    """
    Класс для представления квадрата
    Attributes:
        width (float): длина стороны квадрата

    Methods:
        __init__(width) - инициализирует объект класса Square со стороной width
        calculate_area(): float - рассчитывает и возвращает площадь квадрата
    """

    def __init__(self, width: float):
        """
        Инициализирует квадрат с переданной стороной width
        :param width: float - длина стороны квадрата
        """
        self.width = width

    def calculate_area(self) -> float:
        """
        Рассчитывает площадь квадрата
        :return: float - площадь квадрата
        """
        return self.width ** 2
