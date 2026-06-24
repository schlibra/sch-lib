import urllib.parse


def urldecode(text):
    return urllib.parse.unquote(text)

def urlencode(text):
    return urllib.parse.quote(text)