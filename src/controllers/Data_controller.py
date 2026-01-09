from fastapi import UploadFile
from .Base_controller import Base_controller
from models import ResponseEnum
from .Project_controller import Project_controller
import os
import re
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
    def genertate_unique_filename(self,original_filename:str,project_id:str):
        random_file_name=self.generate_random_string(8)
        project_path=Project_controller().get_project_dir(project_id=project_id)
        cleaned_filename=self.get_cleaned_filename(original_filename)
        new_filepath=os.path.join(project_path,f"{random_file_name}_{cleaned_filename}")
        while os.path.exists(new_filepath):
            random_file_name=self.generate_random_string(8)
            new_filepath=os.path.join(project_path,f"{random_file_name}_{cleaned_filename}")
        return new_filepath    
    def get_cleaned_filename(self,original_filename:str):
        #remove special characters,except for underscores,dots,and hyphens
        cleaned_filename=re.sub(r"[^\w.]","",original_filename.strip())
     
        cleaned_filename=cleaned_filename.replace(" ","_")
        return cleaned_filename
    