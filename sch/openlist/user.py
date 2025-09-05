from .model import OpenListConfig, Response, UserList, UserItem
import requests

class User:
    __config: OpenListConfig
    def __init__(self, config: OpenListConfig):
        self.__config = config

    def list(self):
        res = requests.get(f'{self.__config.url}/api/admin/user/list', headers={
            'Authorization': self.__config.token
        })
        response = Response(res.json(), UserList)
        return response

    def info(self, user_id: int):
        res = requests.get(f'{self.__config.url}/api/admin/user/get', headers={
            'Authorization': self.__config.token
        }, params={
            'id': user_id
        })
        response = Response(res.json(), UserItem)
        print(response)