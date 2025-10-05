import lzma
import base64
import zlib

from .compress import Compress

class Lzma(Compress):
    @staticmethod
    def compress_text(text: str) -> str:
        return base64.b64encode(lzma.compress(text.encode('utf-8'))).decode('utf-8')

    @staticmethod
    def decompress_text(text: str) -> str:
        return base64.b64decode(lzma.decompress(text.encode('utf-8'))).decode('utf-8')

    @staticmethod
    def compress_file(input_file, output_file):
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(zlib.compress(_input.read()))

    @staticmethod
    def decompress_file(input_file, output_file):
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(zlib.decompress(_input.read()))