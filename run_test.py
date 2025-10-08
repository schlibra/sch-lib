from sch import LoggerConfig
from test import *

if __name__ == '__main__':
    LoggerConfig.set_enable(False)
    suite = unittest.TestSuite()
    suite.addTests([
        TestConfig('test_create_config'),
        TestConfig('test_read_config'),
        TestConfig('test_remove_config'),
        TestMySQL('test_connect'),
        TestMySQL('test_create_table'),
        TestMySQL('test_insert'),
        TestMySQL('test_select'),
        TestMySQL('test_select_condition'),
        TestMySQL('test_delete'),
        TestAvatar('test_generate_avatar'),
        TestBzip('test_compress_text'),
        TestBzip('test_decompress_text'),
        TestBzip('test_compress_file'),
        TestBzip('test_decompress_file'),
        TestGzip('test_compress_text'),
        TestGzip('test_decompress_text'),
        TestGzip('test_compress_file'),
        TestGzip('test_decompress_file'),
        TestLzma('test_compress_text'),
        TestLzma('test_decompress_text'),
        TestLzma('test_compress_file'),
        TestLzma('test_decompress_file'),
        TestS3('test_list_buckets'),
        TestS3('test_set_bucket'),
        TestS3('test_write_file'),
        TestS3('test_delete_file'),
    ])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)