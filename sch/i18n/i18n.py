from ..logger import Logger


class I18n:
    __lang: str
    __lang_data: dict
    logger: Logger
    def __init__(self, lang="auto"):
        self.logger = Logger("I18n")
        import os
        import locale
        import json
        if lang == "auto":
            self.__lang = locale.getdefaultlocale()[0]
        else:
            self.__lang = lang
        if os.path.exists(f"i18n/{self.lang}.json"):
            self.__lang_data = json.load(open(f"i18n/{self.lang}.json", "r"))
        else:
            if os.path.exists("i18n/en_US.json"):
                self.__lang_data = json.load(open("i18n/en_US.json", "r"))
                self.__lang = "en_US"
                self.logger.warning(f"Language file for {self.lang} not found, using en_US instead.")
            elif os.path.exists("i18n/zh_CN.json"):
                self.__lang_data = json.load(open("i18n/zh_CN.json", "r"))
                self.__lang = "zh_CN"
                self.logger.warning(f"Language file for {self.lang} not found, using zh_CN instead.")
            else:
                self.__lang_data = {}
                self.logger.error("No language file found.")
    @property
    def lang(self):
        return self.__lang
    @lang.setter
    def lang(self, value):
        import os
        import json
        self.__lang = value
        if os.path.exists(f"i18n/{self.lang}.json"):
            self.__lang_data = json.load(open(f"i18n/{self.lang}.json", "r"))
            self.logger.info(f"Language set to {self.lang}.")
        else:
            self.logger.error(f"Language file for {self.lang} not found.")
    def __call__(self, key):
        return self.__lang_data.get(key, key)
