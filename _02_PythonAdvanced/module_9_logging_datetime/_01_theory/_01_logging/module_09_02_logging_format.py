import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
# %(filename)s - имя файла, из которого было вызвано лог-сообщение.
# %(lineno)s - номер строки, где было вызвано лог сообщение.

logging.debug("Это сообщение отладочного уровня")
logging.info("Это информационное сообщение")
logging.warning("Это предупреждение")
logging.error("Это сообщение об ошибке")
logging.critical("Это критическая ошибка")
