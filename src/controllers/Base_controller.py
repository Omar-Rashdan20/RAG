from helpers.config import settings_loader#,Settings
class Base_controller:
    def __init__(self):
        self.settings = settings_loader()