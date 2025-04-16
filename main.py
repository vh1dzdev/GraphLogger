from fastapi import FastAPI
import uvicorn
from loguru import logger
from contextlib import asynccontextmanager

from src.api.routes import router as api_router
from fastapi.responses import RedirectResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    await YOUR_FUNCTION()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

@app.get("/")
async def root():
    return RedirectResponse("/docs")

if name == "main":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(e)