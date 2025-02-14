import logging

# logger = logging.getLogger('example_logger')
# logger.setLevel(logging.DEBUG)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
#
# logger.addHandler(console_handler)
#
# logger.info('Это сообщение INFO')
# logger.warning('Это сообщение WARNING')


logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.info('Это сообщение INFO')
logger.warning('Это сообщение WARNING')



