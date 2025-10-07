import os
import unittest
from sch import Bzip, Gzip, Lzma

class TestBzip(unittest.TestCase):
    def test_compress_text(self):
        data = Bzip.compress_text("test data")
        self.assertEqual(data, "QlpoOTFBWSZTWbS8hN8AAAQRgEAAJgAMACAAIhhoMAImqHYXckU4UJC0vITf")
    def test_decompress_text(self):
        data = Bzip.decompress_text("QlpoOTFBWSZTWbS8hN8AAAQRgEAAJgAMACAAIhhoMAImqHYXckU4UJC0vITf")
        self.assertEqual(data, "test data")
    def test_compress_file(self):
        with open("test.txt", "w") as f:
            f.write("test data")
        Bzip.compress_file("test.txt", "test.txt.bz2")
        self.assertTrue(os.path.exists("test.txt.bz2"))
        os.remove("test.txt")
        self.assertFalse(os.path.exists("test.txt"))
    def test_decompress_file(self):
        Bzip.decompress_file('test.txt.bz2', 'test.txt')
        self.assertTrue(os.path.exists("test.txt"))
        os.remove("test.txt.bz2")
        self.assertFalse(os.path.exists("test.txt.bz2"))
        with open("test.txt", "r") as f:
            data = f.read()
        self.assertEqual(data, "test data")

class TestGzip(unittest.TestCase):
    def test_compress_text(self):
        data = Gzip.compress_text("test data")
        self.assertEqual(data, "eNorSS0uUUhJLEkEABG+A3s=")
    def test_decompress_text(self):
        data = Gzip.decompress_text("eNorSS0uUUhJLEkEABG+A3s=")
        self.assertEqual(data, "test data")
    def test_compress_file(self):
        with open("test.txt", "w") as f:
            f.write("test data")
        Gzip.compress_file("test.txt", "test.txt.gz")
        self.assertTrue(os.path.exists("test.txt.gz"))
        os.remove("test.txt")
        self.assertFalse(os.path.exists("test.txt"))
    def test_decompress_file(self):
        Gzip.decompress_file('test.txt.gz', 'test.txt')
        self.assertTrue(os.path.exists("test.txt"))
        os.remove("test.txt.gz")
        self.assertFalse(os.path.exists("test.txt.gz"))
        with open("test.txt", "r") as f:
            data = f.read()
        self.assertEqual(data, "test data")

class TestLzma(unittest.TestCase):
    def test_compress_text(self):
        data = Lzma.compress_text("test data")
        self.assertEqual(data, "/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQAIdGVzdCBkYXRhAAAAAKVxsP0Y2EmNAAEhCWwYxdUftvN9AQAAAAAEWVo=")
    def test_decompress_text(self):
        data = Lzma.decompress_text("/Td6WFoAAATm1rRGAgAhARYAAAB0L+WjAQAIdGVzdCBkYXRhAAAAAKVxsP0Y2EmNAAEhCWwYxdUftvN9AQAAAAAEWVo=")
        self.assertEqual(data, "test data")
    def test_compress_file(self):
        with open("test.txt", "w") as f:
            f.write("test data")
        Lzma.compress_file("test.txt", "test.txt.lz")
        self.assertTrue(os.path.exists("test.txt.lz"))
        os.remove("test.txt")
        self.assertFalse(os.path.exists("test.txt"))
    def test_decompress_file(self):
        Lzma.decompress_file('test.txt.lz', 'test.txt')
        self.assertTrue(os.path.exists("test.txt"))
        os.remove("test.txt.lz")
        self.assertFalse(os.path.exists("test.txt.lz"))
        with open("test.txt", "r") as f:
            data = f.read()
        self.assertEqual(data, "test data")