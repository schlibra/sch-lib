import json
import yaml
import toml
from xml.etree import ElementTree
from pprint import pprint
from ..logger.logger import Logger


class ConfigConverter:
    data = {}
    logger: Logger
    def __init__(self):
        self.logger = Logger('ConfigConverter')
    @staticmethod
    def load_json(file_path='config/config.json'):
        self = ConfigConverter()
        self.logger.info(f'Loading JSON config file: {file_path}')
        self.data = json.load(open(file_path, 'r', encoding='utf-8'))
        return self
    def save_json(self, file_path='config/config.json', pretty=True):
        self.logger.info(f'Saving JSON config file: {file_path}')
        if pretty:
            json.dump(self.data, open(file_path, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        else:
            json.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    @staticmethod
    def load_yaml(file_path='config/config.yaml'):
        self = ConfigConverter()
        self.logger.info(f'Loading YAML config file: {file_path}')
        self.data = yaml.load(open(file_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        return self
    def save_yaml(self, file_path='config/config.yaml'):
        self.logger.info(f'Saving YAML config file: {file_path}')
        yaml.dump(self.data, open(file_path, 'w', encoding='utf-8'), default_flow_style=False, allow_unicode=True)
    @staticmethod
    def load_toml(file_path='config/config.toml'):
        self = ConfigConverter()
        self.logger.info(f'Loading TOML config file: {file_path}')
        self.data = toml.load(open(file_path, 'r', encoding='utf-8'))
        return self
    def save_toml(self, file_path='config/config.toml'):
        self.logger.info(f'Saving TOML config file: {file_path}')
        toml.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    def save_ini(self, file_path='config/config.ini'):
        self.logger.info(f'Saving INI config file: {file_path}')
        with open(file_path, 'w', encoding='utf-8') as f:
            for section, options in self.data.items():
                f.write(f'[{section}]\n')
                for option, value in options.items():
                    f.write(f'{option} = {value}\n')
    @staticmethod
    def load_ini(file_path='config/config.ini'):
        self = ConfigConverter()
        self.logger.info(f'Loading INI config file: {file_path}')
        config = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            section = None
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('['):
                    section = line.strip('[]')
                    config[section] = {}
                else:
                    option, value = line.split('=')
                    config[section][option.strip()] = value.strip()
        self.data = config
        return self
    @staticmethod
    def load_xml(file_path='config/config.xml'):
        self = ConfigConverter()
        self.logger.info(f'Loading XML config file: {file_path}')
        _tree = ElementTree.parse(file_path)
        _config = {}
        for _item in _tree.getroot():
            if _text := _item.text.strip():
                _config[_item.get('key')] = _text
            else:
                _config[_item.get('key')] = {}
                for _subitem in _item:
                    _config[_item.get('key')][_subitem.get('key')] = _subitem.text
        self.data = _config
        return self
    def save_xml(self, file_path='config/config.xml'):
        self.logger.info(f'Saving XML config file: {file_path}')
        _config = self.data
        _root = ElementTree.Element('config')
        for _item in _config:
            _tmp = ElementTree.SubElement(_root, 'config', key=_item)
            for _subitem in _config[_item]:
                ElementTree.SubElement(_tmp, 'config', key=_subitem).text = str(_config[_item][_subitem])
        _tree = ElementTree.ElementTree(_root)
        _tree.write(file_path, encoding='utf-8', xml_declaration=True)
    def dump_data(self):
        self.logger.info(f'Dumping data:')
        pprint(self.data)
    def load_data(self, data: dict):
        self.logger.info('Loading data:')
        self.data = data