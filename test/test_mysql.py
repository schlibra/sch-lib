import unittest
from sqlalchemy import Table
from sch import Config, MySQL


class TestMySQL(unittest.TestCase):
    def setUp(self):
        self.config = Config.load_dict({
            'mysql': {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'pass': '123456',
                'name': 'root'
            }
        })
        self.mysql = MySQL(self.config)
        self.assertIsInstance(self.mysql, MySQL)
        self.table = MySQL.table(
            'test_table',
            [
                ('id', int, True),
                ('name', str, 20),
                ('description', str, 100)
            ]
        )
        self.assertIsInstance(self.table, Table)

    def test_connect(self):
        version = self.mysql.get_version()
        self.assertIsInstance(version, str)

    def test_create_table(self):
        if self.mysql.table_exists(self.table):
            self.mysql.drop_table(self.table)
        self.mysql.create_table(self.table)
        self.assertTrue(self.mysql.table_exists(self.table))

    def test_insert(self):
        self.mysql.insert(self.table, {'name': 'test1', 'description': 'test1 description'})
        self.mysql.insert(self.table, {'name': 'test2', 'description': 'test2 description'})
        self.mysql.insert(self.table, {'name': 'test3', 'description': 'test3 description'})

    def test_select(self):
        result = self.mysql.select(self.table)
        self.assertEqual(len(result), 3)

    def test_select_condition(self):
        result = self.mysql.select(self.table, self.table.c.id == 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].name, 'test1')
        self.assertEqual(result[0].description, 'test1 description')

    def test_delete(self):
        self.mysql.delete(self.table, self.table.c.id == 1)
        result = self.mysql.select(self.table, self.table.c.id == 1)
        self.assertFalse(result)
