from PIL import Image
import pytesseract 
import os
import pandas as pd


#Guarda os nomes das imgs em uma lista
my_imgs = []
for root, dirs, files in os.walk("imgs"):
    for filename in files:
        my_imgs.append(filename)

#Importa o tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Dicionario para guardar o resultado das imgs
my_dict = {}

#Passa o tesseract nas imagens da pasta img
for img in my_imgs:
    texto = pytesseract.image_to_string(Image.open('imgs/' + img), lang='por')

    my_dict[img] = texto
    #print(img)
    #print(texto)

#Transforma o dicionário em um dataframe
df = pd.DataFrame(my_dict.items(), columns=['NOME_IMG', 'TEXTO_EXT'])


df.to_csv('dataframe.csv', encoding="utf-8")

print(df)