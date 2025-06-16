import pytesseract
from PIL import Image

# Windows path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def process_image(filepath):
    image = Image.open(filepath)
    text = pytesseract.image_to_string(image)
    return text
