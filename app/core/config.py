from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Count By Peter")

HOST = os.getenv("HOST", "0.0.0.0")

PORT = int(os.getenv("PORT", "8000"))

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

DATABASE_URL = os.getenv(
    "DATABASE",
    "sqlite:///data/count.db",
)