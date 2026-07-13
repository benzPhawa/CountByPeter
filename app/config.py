"""
Count By Peter

config.py

Version : 0.1.0
Commit : #0001
"""

from pathlib import Path

from dotenv import load_dotenv
import os

# โหลดค่าจาก .env
load_dotenv()

# ==========================
# Application
# ==========================

APP_NAME = os.getenv("APP_NAME", "Count By Peter")

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

HOST = os.getenv("HOST", "127.0.0.1")

PORT = int(os.getenv("PORT", "8000"))

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# ==========================
# Database
# ==========================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///data/count.db"
)

# ==========================
# Security
# ==========================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "CountByPeter"
)

# ==========================
# Logging
# ==========================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

# ==========================
# Directories
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

LOG_DIR = BASE_DIR / "logs"

STATIC_DIR = BASE_DIR / "app" / "static"

TEMPLATE_DIR = BASE_DIR / "app" / "templates"