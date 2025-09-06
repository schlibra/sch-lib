import logging
import os
from .config import LoggerConfig

class Logger:
    logger = None
    formatter = None
    file_handler = None
    console_handler = None
    def __init__(self, log_name):
        os.makedirs(
            os.path.split(
                LoggerConfig.get_file_path()
            )[0],
            exist_ok=True
        )
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(LoggerConfig.get_level())
        self.formatter = logging.Formatter(LoggerConfig.get_format())
        if LoggerConfig.get_enable_file():
            self.file_handler = logging.FileHandler(LoggerConfig.get_file_path(), encoding='utf-8')
            self.file_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.file_handler)
        if LoggerConfig.get_enable_console():
            self.console_handler = logging.StreamHandler()
            self.console_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.console_handler)

    def debug(self, message):
        if LoggerConfig.get_enable():
            self.logger.debug(message)

    def info(self, message):
        if LoggerConfig.get_enable():
            self.logger.info(message)

    def warning(self, message):
        if LoggerConfig.get_enable():
            self.logger.warning(message)

    def error(self, message):
        if LoggerConfig.get_enable():
            self.logger.error(message)

    def critical(self, message):
        if LoggerConfig.get_enable():
            self.logger.critical(message)
