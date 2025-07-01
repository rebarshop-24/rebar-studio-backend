import os
from google.cloud import vision
import io
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".env/vision_key.json"

def extract_text_from_image(image_path: str) -> str:
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    return response.full_text_annotation.text