def password_hide(password):
    length = len(password)
    if length > 2:
        if length > 30:
            length = 30
        return password[0] + '*' * (length - 2) + password[-1]
    else:
        return '*' * length

def md5(string: str):
    from hashlib import md5 as _
    return _(string.encode()).hexdigest()

def generate_password(length=8, strong_password=False):
    import uuid as _
    if strong_password:
        return "A" + _.uuid5(_.NAMESPACE_DNS, _.uuid4().hex).hex.split("-")[0][:length-2] + "a"
    else:
        return _.uuid5(_.NAMESPACE_DNS, _.uuid4().hex).hex.split("-")[0][:length]

def uuid():
    import uuid as _
    return _.uuid4().hex

#新功能，暂未测试，不确定是否可用，但一定仅限大小写字母
def caesar(text, key):
    import string

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = '=/'

    all_chars = lowercase + uppercase + digits + symbols
    total = len(all_chars)
    shifted = all_chars[(key % total):] + all_chars[:(key % total)]

    table = str.maketrans(all_chars, shifted)

    return text.translate(table)