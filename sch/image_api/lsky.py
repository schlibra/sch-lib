from .base_image import BaseImage
from .exception import LoginError, RequestError
from .constants import (
    lsky_user_info_tag_bind
)
import requests
from bs4 import BeautifulSoup
import uuid
from ..logger import Logger
from ..util.password import password_hide

class Lsky(BaseImage):
    server = ""
    proxies = None
    cookies = None
    _req = None
    logger: Logger
    config = None
    def __init__(self, server="", proxies=None, config=None):
        super().__init__(server)
        self.server = server
        if config:
            self.config = config
            _server = config.get('lsky.server')
            if _server:
                self.server = _server
            else:
                self.logger.warning(f"No server in config, use default {self.server}")
        self.proxies = proxies
        self._req = requests.session()
        self.logger = Logger('Lsky')
        self.logger.info(f"Init Lsky {self.server}")

    def login(self, username="", password=""):
        if self.config:
            _username = self.config.get('lsky.username')
            _password = self.config.get('lsky.password')
            if _username and _password:
                username = _username
                password = _password
            else:
                self.logger.warning(f"No username or password in config, use default ({password_hide(username)}, {password_hide(password)})")
        self.logger.info(f"Login ({password_hide(username)}, {password_hide(password)}) to {self.server}")
        res = self._req.get(f"{self.server}/login", proxies=self.proxies)
        soup = BeautifulSoup(res.text, "html.parser")
        _token = soup.find("input", {"name": "_token"})["value"]
        res = self._req.post(f"{self.server}/login", data={
            "_token": _token,
            "email": username,
            "password": password
        }, proxies=self.proxies)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            reason = soup.select_one("div>div>div>ul>li")
            if reason:
                reason = reason.text.strip()
                self.logger.error(f"Login failed: {reason}")
                raise LoginError(reason)
            else:
                self.logger.info('Login success')
        else:
            self.logger.error(f"Login failed: {res.status_code}")
            raise LoginError("Login failed")
    def get_user_info(self):
        self.logger.info(f"Get user info from {self.server}")
        res = self._req.get(f"{self.server}/dashboard")
        soup = BeautifulSoup(res.text, "html.parser")
        data = {}
        for item in soup.select("div>div>div>div>div>div>div>div.flex"):
            item_p = item.select("p")
            item_tag = item_p[0].text.strip()
            item_value = item_p[1].text.strip()
            data[lsky_user_info_tag_bind.get(item_tag, item_tag)] = item_value
        return data
    def upload_image(self, file_data: bytes):
        self.logger.info(f"Upload image to {self.server}")
        res = self._req.get(f"{self.server}/upload", proxies=self.proxies)
        soup = BeautifulSoup(res.text, "html.parser")
        _token = soup.find("input", {"name": "_token"})["value"]
        res = self._req.post(f"{self.server}/upload", files={
            "file": (f'{uuid.uuid4()}.png', file_data, 'image/png')
        }, headers={
            "X-CSRF-TOKEN": _token
        }, proxies=self.proxies)
        self.logger.info(f"Upload image result: {res.text}")
        return res.json()
    def get_all_images(self):
        self.logger.info(f"Get all images from {self.server}")
        page_url = f"{self.server}/user/images?page=1"
        image_list = []
        while page_url:
            self.logger.info(f"Get images from {page_url}")
            res = self._req.get(page_url, proxies=self.proxies)
            data = res.json()
            if data.get('status', False):
                image_list += data.get('data', {}).get('images', {}).get('data', [])
                page_url = data.get('data', {}).get('images', {}).get('next_page_url')
            else:
                message = data.get('message', '')
                self.logger.error(f"Get images failed: {message}")
                raise RequestError(message)
        return image_list
