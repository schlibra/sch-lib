from sqlalchemy import Table, MetaData, Column, Integer, String
from sch import SQLite

table = Table(
    'user',
    MetaData(),
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('email', String(100)),
    Column('password', String(100)),
    sqlite_autoincrement=True
)

if __name__ == '__main__':
    sqlite = SQLite()
    sqlite.echo = True
    sqlite.drop_table(table)