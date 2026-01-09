from fastapi import FastAPI, APIRouter, Depends
import os
from dotenv import load_dotenv
from helpers.config import settings_loader,Settings

load_dotenv(".env")

base_router=APIRouter(
    prefix="/rag/v01",
    tags=["rag_v01"],
)
@base_router.get("/")
async def base_info(settings:Settings=Depends(settings_loader)):
    #settings = settings_loader()
    app_name = settings.app_name
    app_version = settings.app_version
    return {"app_name": app_name, 
            "app_version": app_version}
