from sch import Config, MySQL

if __name__ == '__main__':
    config = Config.load_json()
    mysql = MySQL(config)
    version = mysql.get_version()
    print(version)
