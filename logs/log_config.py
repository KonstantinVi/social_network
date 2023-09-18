import logging


def setup_logging():
    logging.basicConfig(
        filename='logs/application.log',
        level=logging.DEBUG,
        # level=logging.INFO,
        # level=logging.WARNING,
        # level=logging.ERROR,
        # level=logging.CRITICAL,
        format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        encoding='utf-8',
    )
    # Регулирует логирование сообщений от дебагера Flask
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
