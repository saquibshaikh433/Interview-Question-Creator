import os 
from pathlib import Path

import logging


logging.basicConfig(level=logging.INFO,
                    format = '[%(asctime)s] %(message)s'
                    )

files_and_folders = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "app.py"

]

for filepath in files_and_folders:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating filedir {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating file {filepath}")
    else:
        logging.info(f"file {filepath} already exists")




    