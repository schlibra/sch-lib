from abc import abstractmethod, ABC


class Compress(ABC):
    @staticmethod
    @abstractmethod
    def compress_text(text: str) -> str:
        pass
    @staticmethod
    @abstractmethod
    def decompress_text(text: str) -> str:
        pass
    @staticmethod
    @abstractmethod
    def compress_file(input_file: str, output_file: str) -> None:
        pass
    @staticmethod
    @abstractmethod
    def decompress_file(input_file: str, output_file: str) -> None:
        pass