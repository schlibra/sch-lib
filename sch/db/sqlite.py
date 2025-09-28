import os.path
import datetime

from .database import Database
from .. import Logger


class SQLite(Database):
    engine = None
    connection = None
    logger: Logger
    def __init__(self, filename="data/main.db", echo=False):
        self.logger = Logger("SQLite")
        try:
            from sqlalchemy import Engine, create_engine
        except (ImportError, ModuleNotFoundError):
            self.logger.error('sch-lib[db] is required for SQLite support')
            exit(1)
        os.makedirs(os.path.split(filename)[0], exist_ok=True)
        self.logger.info("Initializing SQLite engine...")
        self.engine = create_engine(f"sqlite:///{filename}", echo=echo)
        self.connection = self.engine.connect()

    @staticmethod
    def table(name, columns):
        try:
            from sqlalchemy import Table, Column, Integer, String, Boolean, Float, DateTime, Date, MetaData
            from sqlalchemy.schema import SchemaItem
        except (ModuleNotFoundError, ImportError):
            logger = Logger("SQLite")
            logger.error('sch-lib[db] is required for SQLite support')
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
        autoincrement = False
        for _item in columns:
            if len(_item) == 2:
                _name, _type = _item
                args.append(Column(_name, get_column_type(_type)))
            elif len(_item) == 3:
                _name, _type, _ext = _item
                if type(_ext) == bool:
                    if _ext:
                        args.append(Column(_name, get_column_type(_type), primary_key=True, autoincrement=True))
                        autoincrement = True
                    else:
                        args.append(Column(_name, get_column_type(_type)))
                else:
                    args.append(Column(_name, get_column_type(_type, _ext)))
        return Table(name, MetaData(), *args, sqlite_autoincrement=autoincrement)

    def get_version(self):
        self.logger.info("Getting SQLite version...")
        result = self.fetchone("SELECT sqlite_version();")
        return result[0]

    def get_tables(self):
        self.logger.info("Getting SQLite tables...")
        result = self.fetchall("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in result]