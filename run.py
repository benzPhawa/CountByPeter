"""
Count By Peter

run.py

Version : 0.1.0
Commit : #0002
"""

import os
from pathlib import Path
import subprocess
import sys


def create_folder(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def create_environment():

    folders = [
        "data",
        "logs",
        "app/static",
        "app/templates",
        "app/database",
        "app/models",
        "app/api",
        "app/camera",
        "app/utils",
    ]

    for folder in folders:
        create_folder(folder)


def run_server():

    subprocess.run(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "main:app",
            "--reload"
        ]
    )


if __name__ == "__main__":

    print("=" * 50)
    print("Count By Peter")
    print("=" * 50)

    create_environment()

    run_server()