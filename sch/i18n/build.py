import json
from typing import Union

from ..logger import Logger


class I18nBuilder:
    template: dict
    logger: Logger
    def __init__(self, template_path: str="i18n/template.yaml"):
        import yaml
        self.logger = Logger("I18nBuilder")
        self.template = yaml.load(open(template_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        self.logger.info(f"Loaded template from {template_path}")
    @staticmethod
    def flatten_dict(data, parent_key='', separator='.'):
        items = []
        for key, value in data.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            if isinstance(value, dict):
                items.extend(I18nBuilder.flatten_dict(value, new_key, separator).items())
            else:
                items.append((new_key, value))
        return dict(items)
    def build(self, save_path: Union[str, None] = None):
        self.logger.info("Building i18n json file...")
        if save_path:
            if not save_path.endswith('.json'):
                save_path += '.json'
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(self.flatten_dict(self.template), f, ensure_ascii=False, indent=4)
            return None
        else:
            return self.flatten_dict(self.template)