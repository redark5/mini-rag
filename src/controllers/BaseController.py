from helpers.config import get_settings, settings


class BaseController:
    def __init__(self):
        self.settings = get_settings()