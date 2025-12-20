import datetime
from typing import TypeVar, Tuple, Any

from .database import Database
from ..logger import Logger

class PgSQL(Database):
    _TP = TypeVar("_TP", bound=Tuple[Any, ...])
    engine = None
    connection = None
    logger: Logger
    def __init__(self, config, echo=False):
        self.logger = Logger('PostgreSQL')
        try:
            from sqlalchemy import create_engine, Engine, Connection
        except (ModuleNotFoundError, ImportError):
            self.logger.error('sch-lib[db] is required for PostgreSQL support')
            exit(1)
        self.logger.info("Initializing MySQL...")
        _user = config.get('mysql.user', 'root')
        _pass = config.get('mysql.pass', '123456')
        _host = config.get('mysql.host', 'localhost')
        _port = config.get('mysql.port', 3306)
        _name = config.get('mysql.name', 'root')
        self.engine = create_engine(
            f"postgresql+pg8000://{_user}:{_pass}@{_host}:{_port}/{_name}"
        )
        self.connection = self.engine.connect()

    @staticmethod
    def table(name, columns):
        try:
            from sqlalchemy import Table, Column, Integer, String, Boolean, Float, DateTime, Date, MetaData
            from sqlalchemy.schema import SchemaItem
        except (ModuleNotFoundError, ImportError):
            logger = Logger("PostgreSQL")
            logger.error('sch-lib[db] is required for MySQL support')
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


    def get_version(self):
        self.logger.info("Getting PostgreSQL version...")
        result = self.fetchall("SELECT VERSION()")
        return result[0]

    def get_tables(self):
        pass