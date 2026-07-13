"""
Count By Peter

main.py

Version : 0.1.0
Commit : #0002
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.config import APP_NAME

app = FastAPI(
    title=APP_NAME,
    version="0.1.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


@app.get("/")
async def home():

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