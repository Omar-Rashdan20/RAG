from .Base_controller import Base_controller
from fastapi import UploadFile
from models import ResponseEnum
import os
class Project_controller(Base_controller):
    def __init__(self):
        super().__init__()
    def get_project_dir(self,project_id:str):
        project_path=os.path.join(self.file_dir,project_id)
        if not os.path.exists(project_path):       
          os.makedirs(project_path,exist_ok=True)
        return project_path