import logging

# logger = logging.getLogger('example_logger')
#
# logger.debug('Это сообщение DEBUG')
# logger.info('Это сообщение INFO')
# logger.warning('Это сообщение WARNING')
# logger.error('Это сообщение ERROR')
# logger.critical('Это сообщение CRITICAL')

logger = logging.getLogger('example_logger')
logger.setLevel(level=logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(level=logging.DEBUG)
logger.addHandler(handler)

logger.debug('Это сообщение DEBUG')
logger.info('Это сообщение INFO')
logger.warning('Это сообщение WARNING')
logger.error('Это сообщение ERROR')
logger.critical('Это сообщение CRITICAL')
