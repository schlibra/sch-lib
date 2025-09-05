from sch.config import Config
from sch.image_api import Lsky
from sch.mysql import MySQL
from sch.mysql.model import SteamUser

if __name__ == '__main__':
    config = Config()
    config.load_json()
    mysql = MySQL(config)
    for row in mysql.fetchall(SteamUser.select()):
        print(row)
