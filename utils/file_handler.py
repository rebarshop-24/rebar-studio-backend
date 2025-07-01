import shutil
from fastapi import UploadFile
import os
from uuid import uuid4

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(upload_file: UploadFile) -> str:
    file_ext = upload_file.filename.split('.')[-1]
    file_path = os.path.join(UPLOAD_DIR, f"{uuid4()}.{file_ext}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path