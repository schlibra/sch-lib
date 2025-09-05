def password_hide(password):
    length = len(password)
    if length > 2:
        if length > 30:
            length = 30
        return password[0] + '*' * (length - 2) + password[-1]
    else:
        return '*' * length