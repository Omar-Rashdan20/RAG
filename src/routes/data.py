from fastapi import FastAPI, Depends,APIRouter,UploadFile,status
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from helpers.config import settings_loader,Settings
from controllers import Data_controller

data_router=APIRouter(
    prefix="/rag/v01/upload",
    tags=["rag_v01","data_upload"],
)
@data_router.post("/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                       settings:Settings=Depends(settings_loader)):

    #validate file type and size
    is_valid, message = Data_controller().validate_file(file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message}
        )
    return is_valid, {"message": "success upload"}