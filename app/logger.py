"""
Count By Peter

logger.py

Version : 0.1.0
Commit : #0001
"""

import logging
from pathlib import Path

from app.config import LOG_DIR, LOG_LEVEL

# สร้างโฟลเดอร์ logs ถ้ายังไม่มี
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("CountByPeter")

if not logger.handlers:

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_DIR / "countbypeter.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)