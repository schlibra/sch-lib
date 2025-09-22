def qrcode_print(data, border: int = 1, invert: bool = False):
    from ..logger import Logger
    logger = Logger("qrcode")
    try:
        import qrcode
    except (ModuleNotFoundError, ImportError):
        logger.error("sch-lib[qrcode] is required to use this function.")
        exit(1)
    qr = qrcode.QRCode()
    qr.border = border
    qr.add_data(data)
    qr.make()
    qr.print_ascii(out=None, tty=False, invert=invert)

def qrcode_image(data, filename, border: int = 1):
    from ..logger import Logger
    logger = Logger("qrcode")
    try:
        import qrcode
    except (ModuleNotFoundError, ImportError):
        logger.error("sch-lib[qrcode] is required to use this function.")
        exit(1)
    try:
        import PIL as __
    except (ModuleNotFoundError, ImportError):
        logger.error("sch-lib[image] is required to use this function.")
        exit(1)
    qr = qrcode.make(data, border=border)
    qr.save(filename)