from fastapi import FastAPI, Depends,APIRouter,UploadFile
import os
from dotenv import load_dotenv
from helpers.config import settings_loader,Settings
from controllers import Data_controller

data_router=APIRouter(
    prefix="/rag/v01/upload",
    tags=["rag_v01","data_upload"],
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                       settings:Settings=Depends(settings_loader)):
    #settings = settings_loader()
    app_name = settings.app_name
    app_version = settings.app_version
    return {"app_name": app_name, 
            "app_version": app_version}
    #validate file type and size
    data_controller = Date_controller()
    is_valid, message = data_controller.validate_file(file=file) 