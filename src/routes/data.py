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

    #validate file type and size
    is_valid = Data_controller().validate_file(file)
    return is_valid