from typing import TypeVar, Tuple, Any, Sequence
from sqlalchemy import create_engine, Table, Executable, Engine, Connection, Row
from sch.logger import Logger

class MySQL:
    _TP = TypeVar("_TP", bound=Tuple[Any, ...])
    engine: Engine
    connection: Connection
    logger: Logger
    def __init__(self, config, echo=False):
        self.logger = Logger("MySQL")
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

    def create_table(self, table: Table):
        self.logger.info(f"Creating table {table.name}...")
        table.create(self.engine)

    def fetchall(self, statement: Executable) -> Sequence[Row[_TP]]:
        self.logger.info(f"Executing statement {statement}...")
        return self.connection.execute(statement).fetchall()

    def fetchone(self, statement: Executable) -> Row[_TP]:
        self.logger.info(f"Executing statement {statement}...")
        return self.connection.execute(statement).fetchone()

    def update(self, statement: Executable, commit=True):
        self.logger.info(f"Executing statement {statement}...")
        self.connection.execute(statement)
        if commit:
            self.connection.commit()

    def execute(self, statement: Executable, commit=True):
        self.logger.info(f"Executing statement {statement}...")
        self.update(statement, commit)

    def commit(self):
        self.logger.info("Committing...")
        self.connection.commit()
