import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "ERROR")
FORMAT = (
    '{"level": "%(levelname)s", "ts": %(created)f, "caller": "%(filename)s:%(lineno)s - %(funcName)s()", '
    '"msg": "%(message)s", "error": "%(exc_info)s", "stacktrace": "%(stack_info)s"}'
)
logger = logging.getLogger()

formatter = logging.Formatter(FORMAT)
logger.setLevel(LOG_LEVEL)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
if logger.hasHandlers():
    logger.handlers.clear()

logger.addHandler(handler)
