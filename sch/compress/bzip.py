import bz2
import base64
from .compress import Compress

class Bzip(Compress):
    @staticmethod
    def compress_text(text: str, level=9) -> str:
        return base64.b64encode(bz2.compress(text.encode('utf-8'), level)).decode('utf-8')

    @staticmethod
    def decompress_text(text: str) -> str:
        return base64.b64decode(bz2.decompress(text.encode('utf-8'))).decode('utf-8')

    @staticmethod
    def compress_file(input_file: str, output_file: str) -> None:
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(bz2.compress(_input.read()))

    @staticmethod
    def decompress_file(input_file: str, output_file: str) -> None:
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(bz2.decompress(_input.read()))