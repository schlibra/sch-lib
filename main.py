from sch.util.base64 import base64_encode, base64_decode

if __name__ == '__main__':
    text = base64_encode('hello world')
    print(text)