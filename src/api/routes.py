from fastapi import APIRouter, Request
from utils.sql import Logger
from fastapi.responses import FileResponse
from src.api.classes import Authorize_Class
from src.api.misc import Response


router = APIRouter()

# basic logger route
@router.get("/{logger_id}")
async def logger(logger_id: str, request: Request) -> FileResponse:
    headers = request.headers.get("X-Real-IP")
    await Logger.addLog(headers, logger_id)
    return FileResponse(f"image.png")

@router.post("/api/create", responses=Response.Create_Response)
async def create_logger() -> dict:
    log = await Logger.createLogger()
    if (log != False):
        return {"status": "success", "logger_id": log}
    else:
        return {"status": "error", "message": ""}

@router.delete("/{logger_id}", responses=Response.Delete_Response)
async def delete_logger(data: Authorize_Class, logger_id: str):
    token = data.token
    log = await Logger.removeLogger(logger_id)
    if(log == True):
        return {"status": "success", "message": ""}
    else:
        return {"status": "error", "message": ""}

@router.put("/{logger_id}", responses=Response.GetLogs_Response)
async def get_logs(data: Authorize_Class, logger_id: str):
    token = data.token
    log = await Logger.getLogs(logger_id)
    if(log != False):
        return {"status": "success", "logger_id": logger_id, "logs": log}
    else:
        return {"status": "error", "message": "Logs not found"}