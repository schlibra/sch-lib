import json
import yaml
import toml
from pprint import pprint
from ..logger.logger import Logger


class ConfigConverter:
    data = {}
    logger: Logger
    def __init__(self):
        self.logger = Logger('ConfigConverter')
    def load_json(self, file_path='config/config.json'):
        self.logger.info(f'Loading JSON config file: {file_path}')
        self.data = json.load(open(file_path, 'r', encoding='utf-8'))
    def save_json(self, file_path='config/config.json', pretty=True):
        self.logger.info(f'Saving JSON config file: {file_path}')
        if pretty:
            json.dump(self.data, open(file_path, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
        else:
            json.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    def load_yaml(self, file_path='config/config.yaml'):
        self.logger.info(f'Loading YAML config file: {file_path}')
        self.data = yaml.load(open(file_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    def save_yaml(self, file_path='config/config.yaml'):
        self.logger.info(f'Saving YAML config file: {file_path}')
        yaml.dump(self.data, open(file_path, 'w', encoding='utf-8'), default_flow_style=False, allow_unicode=True)
    def load_toml(self, file_path='config/config.toml'):
        self.logger.info(f'Loading TOML config file: {file_path}')
        self.data = toml.load(open(file_path, 'r', encoding='utf-8'))
    def save_toml(self, file_path='config/config.toml'):
        self.logger.info(f'Saving TOML config file: {file_path}')
        toml.dump(self.data, open(file_path, 'w', encoding='utf-8'))
    def save_ini(self, file_path='config/config.ini'):
        self.logger.info(f'Dumping INI config file: {file_path}')
        with open(file_path, 'w', encoding='utf-8') as f:
            for section, options in self.data.items():
                f.write(f'[{section}]\n')
                for option, value in options.items():
                    f.write(f'{option} = {value}\n')
    def load_ini(self, file_path='config/config.ini'):
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
    def dump_data(self):
        self.logger.info(f'Dumping data:')
        pprint(self.data)
    def load_data(self, data: dict):
        self.logger.info('Loading data:')
        self.data = data