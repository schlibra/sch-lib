import os.path
import unittest
from sch import generate_avatar


class TestAvatar(unittest.TestCase):
    def test_generate_avatar(self):
        if os.path.exists('test.png'):
            os.remove('test.png')
        generate_avatar('test', filename='test', output_dir='.')
        self.assertTrue(os.path.exists('test.png'))
        os.remove('test.png')
        self.assertFalse(os.path.exists('test.png'))
