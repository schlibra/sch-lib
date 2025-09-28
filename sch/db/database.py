from abc import ABC, abstractmethod

from sch import Logger


class Database(ABC):
    engine = None
    connection = None
    logger: Logger
    @abstractmethod
    def __init__(self):
        pass
    @staticmethod
    @abstractmethod
    def table(name, columns):
        pass
    def connect(self):
        self.logger.info("Connecting to database...")
        self.connection = self.engine.connect()
    @property
    def echo(self):
        return self.engine.echo
    @echo.setter
    def echo(self, echo=False):
        self.logger.info(f"Setting echo to {echo}")
        self.engine.echo = echo
    def create_table(self, table):
        from sqlalchemy import Table
        if isinstance(table, Table):
            self.logger.info(f"Creating table {table.name}...")
            table.create(self.engine)
        else:
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)
    def fetchall(self, statement):
        from sqlalchemy import Executable, text
        if isinstance(statement, str):
            statement = text(statement)
        if isinstance(statement, Executable):
            self.logger.info(f"Executing statement {statement}...")
            return self.connection.execute(statement).fetchall()
        else:
            self.logger.error("statement must be a sqlalchemy.Executable object or a string")
            exit(1)
    def fetchone(self, statement):
        from sqlalchemy import Executable, text
        if isinstance(statement, str):
            statement = text(statement)
        if isinstance(statement, Executable):
            self.logger.info(f"Executing statement {statement}...")
            return self.connection.execute(statement).fetchone()
        else:
            self.logger.error("statement must be a sqlalchemy.Executable object or a string")
            exit(1)
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
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)
    def exists(self, table, *where):
        from sqlalchemy import Table
        if isinstance(table, Table):
            result = self.select(table, *where)
            if len(result):
                return True
            else:
                return False
        else:
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)

    def insert(self, table, values: dict, commit=True):
        from sqlalchemy import Table, insert
        if isinstance(table, Table):
            statement = insert(table).values(values)
            self.logger.info(f"Executing statement {statement}...")
            self.connection.execute(statement)
            if commit:
                self.commit()
        else:
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)

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
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)
    def delete(self, table, *where, commit=True):
        from sqlalchemy import Table
        if isinstance(table, Table):
            if where:
                statement = table.delete().where(*where)
                self.logger.info(f"Executing statement {statement}...")
                self.connection.execute(statement)
                if commit:
                    self.commit()
            else:
                statement = table.delete()
                self.logger.info(f"Executing statement {statement}...")
                self.connection.execute(statement)
                if commit:
                    self.commit()
        else:
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)
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
            self.logger.error("statement must be a sqlalchemy.Executable object or a string")
            exit(1)
    def commit(self):
        self.logger.info("Committing...")
        self.connection.commit()
    @abstractmethod
    def get_version(self):
        pass
    @abstractmethod
    def get_tables(self):
        pass
    def table_exists(self, table):
        from sqlalchemy import Table
        if isinstance(table, Table):
            table_name = table.name
        elif isinstance(table, str):
            table_name = table
        else:
            self.logger.error("table must be a sqlalchemy.Table object or a string")
            exit(1)
        self.logger.info(f"Checking if table {table_name} exists...")
        return table_name in self.get_tables()

    def drop_table(self, table):
        from sqlalchemy import Table
        if isinstance(table, Table):
            self.logger.info(f"Dropping table {table.name}...")
            table.drop(self.engine)
        else:
            self.logger.error("table must be a sqlalchemy.Table object")
            exit(1)