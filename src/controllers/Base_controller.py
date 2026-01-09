from heplers.config import settings_loader,Settings
class BaseController:
    def __init__(self):
        self.settings = settings_loader()