from ..logger import Logger


def copy_text(text):
    logger = Logger("Clipboard")
    try:
        from pyperclip import copy
    except (ModuleNotFoundError, ImportError):
        logger.error("sch-lib[clip] is required to use this function.")
        exit(1)
    copy(text)

def paste_text():
    logger = Logger("Clipboard")
    try:
        from pyperclip import paste
    except (ModuleNotFoundError, ImportError):
        logger.error("sch-lib[clip] is required to use this function.")
        exit(1)
    return paste()
