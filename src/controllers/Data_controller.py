from fastapi import UploadFile
from .Base_controller import Base_controller
from models import ResponseEnum
class Data_controller(Base_controller):
    def __init__(self):
        super().__init__()
    def validate_file(self,file:UploadFile):
        allowed_types = self.settings.file_type
        max_size = self.settings.max_file_size
        if file.content_type not in allowed_types:
            return False,ResponseEnum.INVALID_FILE_TYPE.value
        if file.size > max_size:
            return False, ResponseEnum.FILE_TOO_LARGE.value
        return True, ResponseEnum.SUCCESS.value    
    