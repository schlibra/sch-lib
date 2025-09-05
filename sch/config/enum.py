from enum import Enum

class ConfigFormat(Enum):
    JSON = 'json'
    YAML = 'yaml'
    INI = 'ini'
    TOML = 'toml'
    ENV = 'env'