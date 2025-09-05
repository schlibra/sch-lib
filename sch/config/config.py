import configparser
import json
import yaml
import toml
from ..logger import Logger
from ..util.password import password_hide

class Config:
    """
    配置文件管理类
    Attributes:
        config: 配置对象
        logger: 日志对象
    """
    config = {}
    logger = None
    def __init__(self):
        """
        初始化日志对象
        """
        self.logger = Logger('Config')
    def load_json(self, file_path='config/config.json'):
        """
        加载JSON配置文件
        :param file_path: JSON配置文件路径
        """
        self.logger.info(f'Loading config from {file_path}')
        self.config = json.load(open(file_path, 'r', encoding='utf-8'))
    def load_yaml(self, file_path='config/config.yaml'):
        """
        加载YAML配置文件
        :param file_path: YAML配置文件路径
        """
        self.logger.info(f'Loading YAML config file: {file_path}')
        self.config = yaml.load(open(file_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    def load_toml(self, file_path='config/config.toml'):
        """
        加载TOML配置文件
        :param file_path: TOML配置文件路径
        """
        self.logger.info(f'Loading TOML config file: {file_path}')
        self.config = toml.load(open(file_path, 'r', encoding='utf-8'))
    def load_ini(self, file_path='config/config.ini'):
        """
        加载INI配置文件
        :param file_path: INI配置文件路径
        """
        self.logger.info(f'Loading INI config file: {file_path}')
        config = configparser.ConfigParser()
        config.read(file_path)
        self.config = {s: dict(config.items(s)) for s in config.sections()}
    def get(self, key):
        """
        获取配置值
        :param key: 配置键值，可以使用"."分割多级键值
        :return: 返回配置值
        """
        _data = self.config
        for _key in key.split('.'):
            _data = _data.get(_key, {})
        self.logger.info(f'Getting config value for key: {key} = {password_hide(str(_data))}')
        return _data
