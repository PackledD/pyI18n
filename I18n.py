import os


class PyI18n():
    """Class for making simply internationalization in Python"""
    def __init__(self, lang: str="en_EN", path: str="./assets/lang"):
        self.__lang = lang
        self.__path = path

    def get_lang(self) -> str:
        """Get current selected language"""
        return self.__lang

    def set_lang(self, newLang: str) -> None:
        """Set current selected language"""
        if(newLang in self.get_all_langs()):
            self.__lang = newLang

    def get_path(self) -> str:
        """Get path for directory with .lang files"""
        return self.__path

    def set_path(self, newPath: str) -> None:
        """Set path for directory with .lang files"""
        self.__path = newPath

    def get_cur_path(self, isDefault: bool=False) -> str:
        """Get path for current .lang file"""
        if isDefault:
            return f"{self.__path}/en_EN.lang"
        return f"{self.__path}/{self.__lang}.lang"

    def get_all_langs(self) -> list:
        langs = [i[:-5] for i in os.listdir(self.get_path()) if (".lang" in i and
                                                                 os.path.isfile(f"{self.get_path()}/{i}"))]
        return langs

    def add_lang(self, langName: str, trans: dict) -> None:
        """Add new lang file"""
        if(not langName in self.get_all_langs()):
            self.set_lang(langName)
            PyI18n.writeLangFile(self.get_cur_path(), trans)

    def format(self, string: str) -> str:
        """This method locale input string in selected lang or in EN. If can't
locale return in-string"""
        if os.path.isfile(self.get_cur_path()):
            lang = PyI18n.readLangFile(self.get_cur_path())
            if lang.get(string):
                return lang[string]
        # If can't find match in selected lang, try to find it in en_EN
        if os.path.isfile(self.get_cur_path(True)):
            lang = PyI18n.readLangFile(self.get_cur_path(True))
            if lang.get(string):
                return lang[string]
        # If can't locale return in-string
        return string

    @staticmethod
    def readLangFile(cur_path: str) -> dict:
        lang = {}
        try:
            with open(cur_path, "r") as file:
                for line in file.read().split("\n"):
                    if("=" in line):
                        data = line.split("=")
                        lang[data[0]] = data[1]
        except:
            return {}
        return lang

    @staticmethod
    def writeLangFile(cur_path: str, lang: dict) -> None:
        with open(cur_path, "a") as file:
            for elem in lang:
                file.write(f"{elem}={lang[elem]}\n")
