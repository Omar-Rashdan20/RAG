from fastapi import FastAPI, Depends,APIRouter,UploadFile,status
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from helpers.config import settings_loader,Settings
from controllers import Data_controller,Project_controller
import aiofiles
import logging
from models.enums import ResponseEnum
from routes.schemes.data import ProcessRequest
from controllers import Process_controller
logger=logging.getLogger("uvicorn.error")
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
   # return is_valid, {"message": "success upload"}
    #get project directory
    project_path = Project_controller().get_project_dir(project_id=project_id)
    file_location,file_id = Data_controller().genertate_unique_filename(
        original_filename=file.filename,project_id=project_id)
    try:
     async with aiofiles.open(file_location, 'wb') as out_file:
      while content := await file.read(settings.chunk_size):  # Read file in chunks
            await out_file.write(content)  # Write chunk to the destination file
    except Exception as e:
        logger.error(f"Error uploading file: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": f"An error occurred while uploading the file: {str(e)}"}
        )
    return JSONResponse(
        content={"message": ResponseEnum.SUCCESS.value, 
                 "file_id": file_id})   
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str,process_request:ProcessRequest):
   file_id=process_request.file_id
   chunk_size=process_request.chunk_size
   overlap=process_request.overlap  
   process_controller=Process_controller(project_id=project_id)
   file_content=process_controller.get_file_content(file_id=file_id)   
   file_cunks=process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap=overlap)       
    if file_cunks==None or len(file_cunks)==0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseEnum.File_empty.value}
        )
   