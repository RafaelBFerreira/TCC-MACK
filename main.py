import pytesseract 
import os
from PIL import Image


#Guarda os nomes das imgs em uma lista
my_imgs = []
for root, dirs, files in os.walk("imgs"):
    for filename in files:
        my_imgs.append(filename)

#pytesseract.pytesseract.tesseract_cmd = os.environ['TESSERACT']

#Importa o tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Caminho das imgs
path = 'imgs/'

#Passa o tesseract nas imagens da pasta img
for img in my_imgs:
    phrase = pytesseract.image_to_string(Image.open(path + img), lang='por')
    print(img + "--->" + phrase)