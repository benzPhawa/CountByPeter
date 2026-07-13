"""
Count By Peter

main.py

Version : 0.1.0
Commit : #0001
"""

from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.config import (
    APP_NAME,
    APP_VERSION,
    HOST,
    PORT,
    STATIC_DIR,
    TEMPLATE_DIR,
    DATA_DIR,
    LOG_DIR,
)
from app.logger import logger

# ======================================================
# Create Required Directories
# ======================================================

for directory in [
    STATIC_DIR,
    TEMPLATE_DIR,
    DATA_DIR,
    LOG_DIR,
]:
    Path(directory).mkdir(parents=True, exist_ok=True)

# ======================================================
# FastAPI
# ======================================================

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


# ======================================================
# Startup
# ======================================================

@app.on_event("startup")
async def startup():

    logger.info("=" * 60)
    logger.info(f"{APP_NAME} {APP_VERSION}")
    logger.info("Application Started")
    logger.info("=" * 60)


# ======================================================
# Routes
# ======================================================

@app.get("/")
async def home():

    return JSONResponse(
        {
            "project": APP_NAME,
            "version": APP_VERSION,
            "status": "Running",
        }
    )


@app.get("/health")
async def health():

    return JSONResponse(
        {
            "status": "OK"
        }
    )


# ======================================================
# Run
# ======================================================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True,
    )