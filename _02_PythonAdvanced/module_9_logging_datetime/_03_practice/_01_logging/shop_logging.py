import logging

logger = logging.getLogger('order_logger')
logger.setLevel(level=logging.ERROR)

file_handler = logging.FileHandler(r'log_errors\order_errors.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

try:
    raise ValueError('Некорректные данные заказа!')
except ValueError as ex:
    logger.error(f'Ошибка обработки заказа: {ex}')
