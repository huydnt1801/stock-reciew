import logging
import logging.handlers

def get_logger(name: str, path: str) -> logging.Logger:
    fmt = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(fmt=fmt)
    handler = logging.handlers.RotatingFileHandler(
        filename=path,
        maxBytes=1024 ** 2,
        backupCount=10)
    handler.setLevel(level=logging.INFO)
    handler.setFormatter(fmt=formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger