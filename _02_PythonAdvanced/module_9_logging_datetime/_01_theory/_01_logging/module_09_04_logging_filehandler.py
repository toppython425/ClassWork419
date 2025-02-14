import logging

# Создание логгера
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler(r'logs\app.log', encoding='utf-8')  # КОДИРОВКА!!!
file_handler.setLevel(logging.ERROR)

# Форматирование сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Логирование
logger.debug("Это сообщение DEBUG")
logger.info("Это сообщение INFO")
logger.warning("Это сообщение WARNING")
logger.error("Это сообщение ERROR")
logger.critical("Это сообщение CRITICAL")
