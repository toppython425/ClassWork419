def find_discount(price, discount):
    """Calculate discount"""
    return price - price * discount


def find_discount_good(price, discount):
    """
    Функция принимает число в качестве цены,
    и числовое значение скидки как десятичную дробь
    :param price: int - цена
    :param price: float - скидка
    :return price - price * discount float: - итоговая цена с учетом скидки
    """
    return price - price * discount
