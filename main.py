from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.core.config import APP_NAME, HOST, PORT
from app.core.logger import logger

# ---------- Create Required Directories ----------
Path("app/static").mkdir(parents=True, exist_ok=True)
Path("app/templates").mkdir(parents=True, exist_ok=True)
Path("data").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)

# ---------- FastAPI ----------
app = FastAPI(
    title=APP_NAME,
    version="0.1.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)


@app.on_event("startup")
async def startup():

    logger.info("====================================")
    logger.info(" Count By Peter Started ")
    logger.info("====================================")


@app.get("/")
async def root():

    return {
        "project": APP_NAME,
        "version": "0.1.0",
        "status": "Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "ok"
    }


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True
    )