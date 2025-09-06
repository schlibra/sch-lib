class LoggerConfig:
    @staticmethod
    def set_enable(_enable: bool=True):
        globals()['__SCH_LOGGING_CONFIG__ENABLE__'] = _enable
    @staticmethod
    def get_enable() -> bool:
        return globals().get('__SCH_LOGGING_CONFIG__ENABLE__', True)
    @staticmethod
    def set_level(_level: str='INFO'):
        globals()['__SCH_LOGGING_CONFIG__LEVEL__'] = _level
    @staticmethod
    def get_level() -> str:
        return globals().get('__SCH_LOGGING_CONFIG__LEVEL__', 'INFO')
    @staticmethod
    def set_format(_format: str='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        globals()['__SCH_LOGGING_CONFIG__FORMAT__'] = _format
    @staticmethod
    def get_format() -> str:
        return globals().get('__SCH_LOGGING_CONFIG__FORMAT__', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    @staticmethod
    def set_enable_console(_enable_console: bool=True):
        globals()['__SCH_LOGGING_CONFIG__ENABLE_CONSOLE__'] = _enable_console
    @staticmethod
    def get_enable_console() -> bool:
        return globals().get('__SCH_LOGGING_CONFIG__ENABLE_CONSOLE__', True)
    @staticmethod
    def set_enable_file(_enable_file: bool=True):
        globals()['__SCH_LOGGING_CONFIG__ENABLE_FILE__'] = _enable_file
    @staticmethod
    def get_enable_file() -> bool:
        return globals().get('__SCH_LOGGING_CONFIG__ENABLE_FILE__', True)
    @staticmethod
    def set_file_path(_file_path: str='log/main.log'):
        globals()['__SCH_LOGGING_CONFIG__FILE_PATH__'] = _file_path
    @staticmethod
    def get_file_path() -> str:
        return globals().get('__SCH_LOGGING_CONFIG__FILE_PATH__', 'log/main.log')