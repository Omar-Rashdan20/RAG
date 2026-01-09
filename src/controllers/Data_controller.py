from fastapi import UploadFile
from .Base_controller import Base_controller

class Date_controller(Base_controller):
    def __init__(self):
        super().__init__()
    def validate_file(self,file:UploadFile):
        allowed_types = self.settings.file_type
        max_size = self.settings.max_file_size
        if file.content_type not in allowed_types:
            return False, "Unsupported file type."
        if file.size > max_size:
            return False, "File size exceeds the maximum limit."
        return True, "File is valid."    
    