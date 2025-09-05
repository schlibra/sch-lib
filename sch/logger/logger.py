import logging
import os


class Logger:
    logger = None
    formatter = None
    file_handler = None
    console_handler = None
    def __init__(self, log_name, log_level=logging.INFO):
        os.makedirs('log', exist_ok=True)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler = logging.FileHandler(f'log/main.log', encoding='utf-8')
        self.file_handler.setFormatter(self.formatter)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
