from fastapi import FastAPI, APIRouter

base_router=APIRouter(
    prefix="/rag/v01",
    tags=["rag_v01"],
)
@base_router.get("/")
def base_info():
    return {"message": "RAG API Base Endpoint"}
