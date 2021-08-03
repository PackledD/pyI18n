from pyI18n.I18n import PyI18n


def format(string: str) -> str:
    return session.format(string)


def set_lang(lang: str) -> None:
    session.set_lang(lang)


def set_path(path: str) -> None:
    session.set_path(path)


def get_lang() -> str:
    return session.get_lang()


def get_path() -> str:
    return session.get_path()


def get_all_langs() -> list:
    return session.get_all_langs()


def add_lang(lang: str, trans: dict) -> None:
    session.add_lang(lang, trans)


session = PyI18n()
