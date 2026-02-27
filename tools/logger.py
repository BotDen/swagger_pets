import logging


def get_logger(name: str) -> logging.Logger:
    """Функция создания логгера"""
    # инициализация логгера
    logger = logging.getLogger(name)
    # установка уровня логирования
    logger.setLevel(level=logging.DEBUG)

    # создание обработчика
    handler = logging.StreamHandler()
    # установка уровня логирования
    handler.setLevel(level=logging.DEBUG)

    # настройка формата сообщения
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    # передача формата в обработчик
    handler.setFormatter(formatter)
    # передача обработчика в логгер
    logger.addHandler(handler)
    return logger
