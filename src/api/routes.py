from fastapi import APIRouter, Request
from loguru import logger
from fastapi.responses import FileResponse
from src.api.classes import Authorize_Class

router = APIRouter()

# basic logger route
@router.get("/{logger_id}.png")
async def logger(logger_id: str, request: Request) -> FileResponse:
    ip = request.get_headears.get("x-real-ip")
    logger.info(ip) # here will be the method for adding an IP to the DB, but for now here is the console output
    return FileResponse(f"image.png")

@router.post("/api/create")
async def create_logger() -> dict:
    return {"message": "So far this method does not create anything."}

@router.delete("/{logger_id}")
async def delete_logger(data: Authorize_Class, logger_id: str):
    token = data.token
    return {"message": "At the moment, there is no functionality for deleting the logger."}

@router.put("/{logger_id}")
async def get_logger_info(data: Authorize_Class, logger_id: str):
    token = data.token
    return {"message": "At the moment, the functionality for receiving logger information has not been implemented."}