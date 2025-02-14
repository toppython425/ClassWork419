import logging

# Настройка логгера
logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Произошла ошибка - деление на 0")
