from fastapi import FastAPI, APIRouter
import os
from dotenv import load_dotenv
load_dotenv(".env")

base_router=APIRouter(
    prefix="/rag/v01",
    tags=["rag_v01"],
)
@base_router.get("/")
async def base_info():
    app_name = os.getenv("app_name")
    app_version = os.getenv("app_version")
    return {"app_name": app_name, 
            "app_version": app_version}
