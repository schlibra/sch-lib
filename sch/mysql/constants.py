def Or(*args):
    from sqlalchemy import or_
    return or_(*args)

def And(*args):
    from sqlalchemy import and_
    return and_(*args)

def Not(*args):
    from sqlalchemy import not_
    return not_(*args)

def Null():
    from sqlalchemy import null
    return null()
