import os
import cv2
import pytesseract

# -----------------------------
# Set Tesseract executable path (Windows)
# -----------------------------
# Change this path if your Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------
# Extract text from license plate image
# -----------------------------
def extract_text_from_plate(plate_img):
    # Convert to grayscale
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    
    # OCR using Tesseract
    text = pytesseract.image_to_string(gray, config='--psm 7')
    
    return text.strip()

# -----------------------------
# Create folder if it does not exist
# -----------------------------
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
