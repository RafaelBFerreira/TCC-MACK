import pytesseract 
import os
from PIL import Image


#pytesseract.pytesseract.tesseract_cmd = os.environ['TESSERACT']

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

phrase = pytesseract.image_to_string(Image.open('test.jpeg'), lang='por')
print(phrase)