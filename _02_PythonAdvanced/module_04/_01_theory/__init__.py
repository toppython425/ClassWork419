def greet(name):
    """
    Эта функция получает строку, которая содержит имя персоны
    и возвращает строку с приветствием для этой персоны.
    :param name: str - имя персоны
    :return: str - greeting

    #  Parameters:
    #     name (str): person's name
    #
    # Returns:
    #     str: greeting
    """
    greeting = f'Hello, {name}'
    return greeting


greet(name='Иван')
