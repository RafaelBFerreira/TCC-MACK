from PIL import Image
import pytesseract 
import os
import pandas as pd


#Importa o tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Dicionario para guardar o resultado das imgs
my_dict = {}

#Passa o tesseract nas imagens da pasta imgs e salva o resultado no dicionario
for root, dirs, files in os.walk("imgs"):
    for filename in files:
        try:
            texto = pytesseract.image_to_string(Image.open('imgs/' + filename), lang='por')
            my_dict[filename] = texto
        except Exception as msg:
            print("Erro: {}".format(msg))
        
#Transforma o dicionário em um dataframe
df = pd.DataFrame(my_dict.items(), columns=['NOME_IMG', 'TEXTO_EXT'])

#Transforma dataframe em um .csv
df.to_csv('dataframe.csv', encoding="utf-8")

print(df)