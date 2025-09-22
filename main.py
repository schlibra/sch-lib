from sch import ConfigConverter

if __name__ == '__main__':
    config = ConfigConverter.load_json()
    config.save_xml()