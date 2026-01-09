from helpers.config import settings_loader#,Settings
import os
import string
import random
class Base_controller:
    def __init__(self):
        self.settings = settings_loader()
        self.base_dir=os.path.dirname(os.path.abspath(__file__))
        self.file_dir=os.path.join(self.base_dir,"../assets/files")
    def generate_random_string(self,length:int=8):
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for i in range(length))
    
    
    