from typing import TypeVar, Tuple, Any
from sch.logger import Logger

class MySQL:
    _TP = TypeVar("_TP", bound=Tuple[Any, ...])
    engine = None
    connection = None
    logger: Logger
    def __init__(self, config, echo=False):
        self.logger = Logger("MySQL")
        try:
            from sqlalchemy import create_engine, Engine, Connection
        except (ModuleNotFoundError, ImportError):
            self.logger.error('sch-lib[mysql] is required for MySQL support')
            exit(1)
        self.logger.info("Initializing MySQL...")
        self.engine = create_engine(
            f"mysql+pymysql://{config.get('mysql.user')}:{config.get('mysql.pass')}@{config.get('mysql.host')}:{config.get('mysql.port')}/{config.get('mysql.name')}?charset=utf8mb4",
            echo=echo
        )
        self.connection = self.engine.connect()

    def connect(self):
        self.logger.info("Connecting to MySQL...")
        self.connection = self.engine.connect()

    def set_echo(self, echo=False):
        self.logger.info(f"Setting echo to {echo}...")
        self.engine.echo = echo

    def create_table(self, table):
        from sqlalchemy import Table
        if isinstance(table, Table):
            self.logger.info(f"Creating table {table.name}...")
            table.create(self.engine)
        else:
            raise TypeError("table must be a sqlalchemy.Table object")

    def fetchall(self, statement):
        from sqlalchemy import Executable, text

        if isinstance(statement, str):
            statement = text(statement)
        if isinstance(statement, Executable):
            self.logger.info(f"Executing statement {statement}...")
            return self.connection.execute(statement).fetchall()
        else:
            raise TypeError("statement must be a sqlalchemy.Executable object or a string")

    def fetchone(self, statement):
        from sqlalchemy import Executable, text
        if isinstance(statement, str):
            statement = text(statement)
        if isinstance(statement, Executable):
            self.logger.info(f"Executing statement {statement}...")
            return self.connection.execute(statement).fetchone()
        else:
            raise TypeError("statement must be a sqlalchemy.Executable object or a string")

    def select(self, table, *where):
        from sqlalchemy import Table
        if isinstance(table, Table):
            if where:
                statement = table.select().where(*where)
                self.logger.info(f"Executing statement {statement}...")
                return self.connection.execute(statement).fetchall()
            else:
                statement = table.select()
                self.logger.info(f"Executing statement {statement}...")
                return self.connection.execute(statement).fetchall()
        else:
            raise TypeError("table must be a sqlalchemy.Table object")

    def exists(self, table, *where):
        from sqlalchemy import Table
        if isinstance(table, Table):
            result = self.select(table, *where)
            if len(result):
                return True
            else:
                return False
        else:
            raise TypeError("table must be a sqlalchemy.Table object")


    def insert(self, table, values: dict, commit=True):
        from sqlalchemy import Table, insert
        if isinstance(table, Table):
            statement = insert(table).values(values)
            self.logger.info(f"Executing statement {statement}...")
            self.connection.execute(statement)
            if commit:
                self.commit()
        else:
            raise TypeError("table must be a sqlalchemy.Table object")

    def update(self, table, values: dict, *where, commit=True):
        from sqlalchemy import Table
        if isinstance(table, Table):
            if where:
                statement = table.update().where(*where).values(values)
                self.logger.info(f"Executing statement {statement}...")
                self.connection.execute(statement)
                if commit:
                    self.commit()
            else:
                statement = table.update().values(values)
                self.logger.info(f"Executing statement {statement}...")
                self.connection.execute(statement)
                if commit:
                    self.commit()
        else:
            raise TypeError("table must be a sqlalchemy.Table object")

    def execute(self, statement, commit=True):
        from sqlalchemy import text, Executable
        if isinstance(statement, str):
            statement = text(statement)
        if isinstance(statement, Executable):
            self.logger.info(f"Executing statement {statement}...")
            self.connection.execute(statement)
            if commit:
                self.commit()
        else:
            raise TypeError("statement must be a sqlalchemy.Executable object or a string")

    def commit(self):
        self.logger.info("Committing...")
        self.connection.commit()

    def get_version(self) -> str:
        self.logger.info("Getting MySQL version...")
        result = self.fetchone("SELECT VERSION()")
        return result[0]