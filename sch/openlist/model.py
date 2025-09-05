import json
from typing import Any


class OpenListConfig:
    name: str
    host: str
    port: int
    token: str
    ssl: bool
    enable: bool
    url: str
    def __init__(self, data: dict):
        self.name = data.get('name', '')
        self.host = data.get('host', '')
        self.port = data.get('port', 0)
        self.token = data.get('token', '')
        self.ssl = data.get('ssl', False)
        self.enable = data.get('enable', False)
        protocol = 'https' if self.ssl else 'http'
        self.url = f'{protocol}://{self.host}:{self.port}'

class UserItem:
    id: int
    username: str
    password: str
    base_path: str
    role: int
    disable: bool
    permission: int
    sso_id: str
    def __init__(self, data: dict):
        self.id = data.get('id', 0)
        self.username = data.get('username', '')
        self.password = data.get('password', '')
        self.base_path = data.get('base_path', '')
        self.role = data.get('role', 0)
        self.disable = data.get('disable', False)
        self.permission = data.get('permission', 0)
        self.sso_id = data.get('sso_id', '')
    def __str__(self):
        return f"UserItem {{\n\t\t\t\tid = {self.id}, \n\t\t\t\tusername = {self.username}, \n\t\t\t\tpassword = {self.password}, \n\t\t\t\tbase_path = {self.base_path}, \n\t\t\t\trole = {self.role}, \n\t\t\t\tdisable = {self.disable}, \n\t\t\t\tpermission = {self.permission}, \n\t\t\t\tsso_id = {self.sso_id}\n\t\t\t}}"

class UserList:
    content: list[UserItem]
    def __init__(self, data: dict):
        self.content = []
        for item in data['content']:
            self.content.append(UserItem(item))
    def __str__(self):
        text = f"UserList {{\n\t\tcontent = ["
        for item in self.content:
            text += f"\n\t\t\t{item}"
        text += "\n\t\t]\n\t}"
        return text

class Response:
    code: int
    message: str
    data: Any
    def __init__(self, _data: dict, data_model: Any = None):
        self.code = _data.get('code', 0)
        self.message = _data.get('message', '')
        self.data = data_model(_data.get('data', {}))
    def __str__(self):
        return f"Response {{\n\tcode = {self.code}, \n\tmessage = {self.message}, \n\tdata = {self.data}\n}}"