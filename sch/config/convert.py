import json
import yaml
import toml
from Crypto.Cipher import AES
from xml.etree import ElementTree
from pprint import pprint
from ..logger.logger import Logger
from ..util import password_hide


class ConfigConverter:
    data = {}
    logger: Logger
    def __init__(self):
        self.logger = Logger('ConfigConverter')
    @staticmethod
    def load_json(file_path='config/config.json', password=None):
        self = ConfigConverter()
        self.logger.info(f'Loading JSON config file: {file_path}')
        _data = open(file_path, 'rb').read()
        if password:
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).decrypt(_data)
        self.data = json.loads(_data.decode('utf-8'))
        return self
    def save_json(self, file_path='config/config.json', password=None, pretty=True):
        self.logger.info(f'Saving JSON config file: {file_path}')
        if password:
            _data = json.dumps(self.data)
            length = len(_data)
            _data += ' ' * (16 - length % 16)
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).encrypt(_data.encode('utf-8'))
            with open(file_path, 'wb') as f:
                f.write(_data)
        else:
            if pretty:
                json.dump(self.data, open(file_path, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
            else:
                json.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    @staticmethod
    def load_yaml(file_path='config/config.yaml', password=None):
        self = ConfigConverter()
        self.logger.info(f'Loading YAML config file: {file_path}')
        _data = open(file_path, 'rb').read()
        if password:
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).decrypt(_data)
        self.data = yaml.load(_data.decode('utf-8'), Loader=yaml.FullLoader)
        return self
    def save_yaml(self, file_path='config/config.yaml', password=None):
        self.logger.info(f'Saving YAML config file: {file_path}')
        if password:
            _data = yaml.dump(self.data, default_flow_style=False, allow_unicode=True)
            length = len(_data)
            _data += ' ' * (16 - length % 16)
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).encrypt(_data.encode('utf-8'))
            with open(file_path, 'wb') as f:
                f.write(_data)
        else:
            yaml.dump(self.data, open(file_path, 'w', encoding='utf-8'), default_flow_style=False, allow_unicode=True)
    @staticmethod
    def load_toml(file_path='config/config.toml', password=None):
        self = ConfigConverter()
        self.logger.info(f'Loading TOML config file: {file_path}')
        _data = open(file_path, 'rb').read()
        if password:
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).decrypt(_data)
        self.data = toml.loads(_data.decode('utf-8'))
        return self
    def save_toml(self, file_path='config/config.toml', password=None):
        self.logger.info(f'Saving TOML config file: {file_path}')
        if password:
            _data = toml.dumps(self.data)
            length = len(_data)
            _data += ' ' * (16 - length % 16)
            _data = AES.new(password.encode('utf-8'), AES.MODE_ECB).encrypt(_data.encode('utf-8'))
            with open(file_path, 'wb') as f:
                f.write(_data)
        else:
            toml.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    def dump_data(self):
        self.logger.info(f'Dumping data:')
        pprint(self.data)
    def load_data(self, data: dict):
        self.logger.info('Loading data:')
        self.data = data

    def get(self, key, default=None):
        """
        获取配置值
        :param key: 配置键值，可以使用"."分割多级键值
        :param default: 默认值
        :return: 返回配置值

        """
        _data = self.data
        for _key in key.split('.'):
            _data = _data.get(_key, {})
        self.logger.info(f'Getting config value for key: {key} = {password_hide(str(_data))}')
        return _data if _data else default
    def set(self, key, value):
        self.data[key] = value
