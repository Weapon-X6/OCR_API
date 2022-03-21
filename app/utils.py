import shutil
import os
from pathlib import Path


def save_file_to_server(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file


def get_project_root() -> Path:
    return Path(__file__).parent.parent
