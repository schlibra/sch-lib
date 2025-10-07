import configparser
import json
from io import BytesIO

import yaml
import toml
from Crypto.Cipher import AES
from xml.etree import ElementTree
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

    @staticmethod
    def load_json(file_path='config/config.json', password=None):
        """
        加载JSON配置文件
        :param file_path: JSON配置文件路径
        :param password: 密码
        """
        self = Config()
        self.logger.info(f'Loading config from {file_path}')
        with open(file_path, 'rb') as f:
            _data = f.read()
        if password:
            _data = AES.new(password.encode('utf8'), AES.MODE_ECB).decrypt(_data)
        else:
            _data = json.loads(_data)
        self.config = json.loads(_data)
        return self

    @staticmethod
    def load_yaml(file_path='config/config.yaml', password=None):
        """
        加载YAML配置文件
        :param file_path: YAML配置文件路径
        :param password: 密码
        """
        self = Config()
        self.logger.info(f'Loading YAML config file: {file_path}')
        with open(file_path, 'rb') as f:
            _data = f.read()
        if password:
            _data = AES.new(password.encode('utf8'), AES.MODE_ECB).decrypt(_data)
        self.config = yaml.load(_data, Loader=yaml.FullLoader)
        return self

    @staticmethod
    def load_toml(file_path='config/config.toml', password=None):
        """
        加载TOML配置文件
        :param file_path: TOML配置文件路径
        :param password: 密码
        """
        self = Config()
        self.logger.info(f'Loading TOML config file: {file_path}')
        with open(file_path, 'rb') as f:
            _data = f.read()
        if password:
            _data = AES.new(password.encode('utf8'), AES.MODE_ECB).decrypt(_data)
        self.config = toml.loads(_data.decode('utf-8'))
        return self

    def get(self, key, default=None):
        """
        获取配置值
        :param key: 配置键值，可以使用"."分割多级键值
        :param default: 默认值
        :return: 返回配置值

        """
        _data = self.config
        for _key in key.split('.'):
            _data = _data.get(_key, {})
        self.logger.info(f'Getting config value for key: {key} = {password_hide(str(_data))}')
        return _data if _data else default

    def __getitem__(self, item):
        return self.get(item)
