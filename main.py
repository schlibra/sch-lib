from sch.mysql.model import HelloGithub
from sch import Config, MySQL

if __name__ == '__main__':
    config = Config.load_json()
    mysql = MySQL(config)
    mysql.select(HelloGithub)

