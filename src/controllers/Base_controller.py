from helpers.config import settings_loader#,Settings
class Base_Controller:
    def __init__(self):
        self.settings = settings_loader()