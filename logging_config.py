import logging
from colorlog import ColoredFormatter


def configure_logging(name="root", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-3s%(reset)s %(log_color)s%(name)-4s%(reset)s %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
