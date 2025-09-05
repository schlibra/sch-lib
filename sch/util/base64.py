import base64

def base64_encode(data: str, encoding='utf-8'):
    return base64.b64encode(data.encode(encoding)).decode(encoding)

def base64_decode(data: str, encoding='utf-8'):
    return base64.b64decode(data.encode(encoding)).decode(encoding)