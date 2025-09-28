import datetime

from .database import Database
from typing import TypeVar, Tuple, Any
from sch.logger import Logger

class MySQL(Database):
    _TP = TypeVar("_TP", bound=Tuple[Any, ...])
    engine = None
    connection = None
    logger: Logger
    def __init__(self, config, echo=False):
        self.logger = Logger("MySQL")
        try:
            from sqlalchemy import create_engine, Engine, Connection
        except (ModuleNotFoundError, ImportError):
            self.logger.error('sch-lib[db] is required for MySQL support')
            exit(1)
        self.logger.info("Initializing MySQL...")
        self.engine = create_engine(
            f"mysql+pymysql://{config.get('mysql.user')}:{config.get('mysql.pass')}@{config.get('mysql.host')}:{config.get('mysql.port')}/{config.get('mysql.name')}?charset=utf8mb4",
            echo=echo
        )
        self.connection = self.engine.connect()

    @staticmethod
    def table(name, columns):
        try:
            from sqlalchemy import Table, Column, Integer, String, Boolean, Float, DateTime, Date, MetaData
            from sqlalchemy.schema import SchemaItem
        except (ModuleNotFoundError, ImportError):
            logger = Logger("MySQL")
            logger.error('sch-lib[mysql] is required for MySQL support')
            exit(1)
        args = []

        def get_column_type(_type, _length=None):
            if _type == int or _type == 'int' or _type == 'integer':
                return Integer()
            elif _type == str or _type == 'str' or _type == 'string':
                if _length is None:
                    return String(255)
                return String(_length)
            elif _type == bool or _type == 'bool' or _type == 'boolean':
                return Boolean()
            elif _type == float or _type == 'float':
                return Float()
            elif _type == datetime or _type == datetime.datetime or _type == 'datetime':
                return DateTime()
            elif _type == datetime.date or _type == 'date':
                return Date()
            else:
                return None

        for _item in columns:
            if len(_item) == 2:
                _name, _type = _item
                args.append(Column(_name, get_column_type(_type)))
            elif len(_item) == 3:
                _name, _type, _ext = _item
                if type(_ext) == bool:
                    if _ext:
                        args.append(Column(_name, get_column_type(_type), primary_key=True, autoincrement=True))
                    else:
                        args.append(Column(_name, get_column_type(_type)))
                else:
                    args.append(Column(_name, get_column_type(_type, _ext)))
        return Table(name, MetaData(), *args, mysql_engine='InnoDB', mysql_charset='utf8mb4')

    def get_tables(self):
        self.logger.info("Getting MySQL tables...")
        result = self.fetchall("SHOW TABLES")
        return [row[0] for row in result]

    def get_version(self) -> str:
        self.logger.info("Getting MySQL version...")
        result = self.fetchone("SELECT VERSION()")
        return result[0]





