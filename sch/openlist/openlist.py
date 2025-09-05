from typing import Union
from .model import OpenListConfig
from sqlalchemy.engine.row import Row
from .user import User
from ..logger import Logger


class OpList:
    __config: OpenListConfig
    user: User
    logger: Logger
    def __init__(self, config: Union[dict, Row, OpenListConfig]):
        if isinstance(config, dict):
            self.__config = OpenListConfig(config)
        elif isinstance(config, Row):
            self.__config = OpenListConfig({
                'name': config.name,
                'host': config.host,
                'port': config.port,
                'token': config.token,
                'ssl': config.ssl,
                'enable': config.enable
            })
        else:
            self.__config = config
        self.user = User(self.__config)