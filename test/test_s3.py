import unittest

from sch import Config, S3


class TestS3(unittest.TestCase):
    def setUp(self):
        self.config = Config.load_dict({
            's3': {
                'endpoint': 'http://localhost:5246',
                'access_key': 'test',
                'secret_key': 'test',
            }
        })
        self.s3 = S3(self.config)
    def test_list_buckets(self):
        buckets = self.s3.list_buckets()
        self.assertEqual(buckets[0], 'test')
    def test_set_bucket(self):
        self.s3.set_bucket('test')
        self.assertEqual(self.s3.bucket.name, 'test')
    def test_write_file(self):
        self.s3.set_bucket('test')
        self.s3.write_file('test.txt', 'test')
        self.assertEqual(self.s3.read_file('test.txt'), 'test')
    def test_delete_file(self):
        self.s3.set_bucket('test')
        self.s3.delete_file('test.txt')
        self.assertNotEqual(self.s3.read_file('test.txt'), 'test')