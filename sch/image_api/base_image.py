class BaseImage:
    server = None
    proxies = None
    def __init__(self, server=None, proxies=None):
        pass
    def login(self, username, password):
        pass
    def get_user_info(self):
        pass
    def upload_image(self, image_data):
        pass