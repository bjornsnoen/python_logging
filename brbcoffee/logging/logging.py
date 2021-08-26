from logging import DEBUG, Formatter, Logger, getLogger
from logging.handlers import TimedRotatingFileHandler
from os import getenv
from pathlib import Path


def make_logger(name: str) -> Logger:
    home = Path(getenv("HOME"))
    log_directory = home / ".logs"
    if not log_directory.exists():
        log_directory.mkdir(mode=0o775)

    logger = getLogger("pypewire")
    logger.setLevel(DEBUG)

    handler = TimedRotatingFileHandler(filename=home / f".logs/{name}.log")
    handler.setLevel(DEBUG)

    formatter = Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
