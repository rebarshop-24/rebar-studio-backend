from fastapi import APIRouter, UploadFile, File
from services.ocr_service import extract_text_from_image
from utils.file_handler import save_upload_file
from models.estimation import OCRResponse

router = APIRouter()

@router.post("")
async def analyze(file: UploadFile = File(...)) -> OCRResponse:
    file_path = await save_upload_file(file)
    text = extract_text_from_image(file_path)
    return {"text": text}