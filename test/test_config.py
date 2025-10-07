import os
import unittest
from sch import ConfigConverter, Config


class TestConfig(unittest.TestCase):
    def test_create_config(self):
        converter = ConfigConverter()
        key = 'test' * 4
        self.assertIsInstance(converter, ConfigConverter)
        converter.set('test', {'key': 'value'})
        self.assertEqual(converter.get('test.key'), 'value')
        os.makedirs('test_config', exist_ok=True)
        self.assertTrue(os.path.exists('test_config'))
        converter.save_json('test_config/config.json', key)
        self.assertTrue(os.path.exists('test_config/config.json'))
        converter.save_yaml('test_config/config.yaml', key)
        self.assertTrue(os.path.exists('test_config/config.yaml'))
        converter.save_toml('test_config/config.toml', key)
        self.assertTrue(os.path.exists('test_config/config.toml'))

    def test_read_config(self):
        key = 'test' * 4
        config = Config.load_json('test_config/config.json', key)
        self.assertIsInstance(config, Config)
        self.assertEqual(config.get('test.key'), 'value')
        config = Config.load_yaml('test_config/config.yaml', key)
        self.assertIsInstance(config, Config)
        self.assertEqual(config.get('test.key'), 'value')
        config = Config.load_toml('test_config/config.toml', key)
        self.assertIsInstance(config, Config)
        self.assertEqual(config.get('test.key'), 'value')

    def test_remove_config(self):
        os.remove('test_config/config.json')
        self.assertFalse(os.path.exists('test_config/config.json'))
        os.remove('test_config/config.yaml')
        self.assertFalse(os.path.exists('test_config/config.yaml'))
        os.remove('test_config/config.toml')
        self.assertFalse(os.path.exists('test_config/config.toml'))
        os.rmdir('test_config')
        self.assertFalse(os.path.exists('test_config'))