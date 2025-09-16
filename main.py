from sch.util.qrcode import qrcode_print, qrcode_image

if __name__ == '__main__':
    url = "https://sch-lib.schhz.cn"
    qrcode_print(url, border=1, invert=True)
    qrcode_image(url, "2.png")

