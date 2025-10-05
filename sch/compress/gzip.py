import zlib, base64

from .compress import Compress


class Gzip(Compress):
    @staticmethod
    def compress_text(text: str, level=9) -> str:
        return base64.b64encode(zlib.compress(text.encode('utf-8'), level)).decode('utf-8')
    @staticmethod
    def decompress_text(text: str) -> str:
        return zlib.decompress(base64.b64decode(text.encode('utf-8'))).decode('utf-8')
    @staticmethod
    def compress_file(input_file: str, output_file: str) -> None:
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(zlib.compress(_input.read()))
    @staticmethod
    def decompress_file(input_file: str, output_file: str) -> None:
        with open(input_file, 'rb') as _input, open(output_file, 'wb') as _output:
            _output.write(zlib.decompress(_input.read()))
