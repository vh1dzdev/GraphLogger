from fastapi import APIRouter, Request
from src.utils.sql import Logger
from fastapi.responses import FileResponse
from src.api.classes import Authorize_Class


router = APIRouter()

# basic logger route
@router.get("/{logger_id}.png")
async def logger(logger_id: str, request: Request) -> FileResponse:
    ip = request.get_headears.get("x-real-ip")
    await Logger.addLog(ip, logger_id)
    return FileResponse(f"image.png")

@router.post("/api/create")
async def create_logger() -> dict:
    log = await Logger.createLogger()
    if (log != False):
        return {"status": "success", "logger_id": log}
    else:
        return {"status": "error", "message": ""}

@router.delete("/{logger_id}")
async def delete_logger(data: Authorize_Class, logger_id: str):
    token = data.token
    log = await Logger.removeLogger(logger_id)
    if(log == True):
        return {"status": "success", "message": ""}
    else:
        return {"status": "error", "message": ""}

@router.put("/{logger_id}")
async def get_logs(data: Authorize_Class, logger_id: str):
    token = data.token
    log = await Logger.getLogger(logger_id)
    if(log != False):
        return {"status": "success", "logger_id": logger_id, "logs": log}
    else:
        return {"status": "error", "message": "Logs not found"}