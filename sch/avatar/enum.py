from enum import Enum


class Algo(Enum):
    """
    哈希算法枚举
    :argument MD5: MD5算法
        SHA1: SHA1算法
        SHA224: SHA224算法
        SHA256: SHA256算法
        SHA384: SHA384算法
        SHA512: SHA512算法
    """
    MD5 = "md5"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"