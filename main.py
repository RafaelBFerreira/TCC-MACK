from pytesseract import pytesseract,Output
from PIL import Image
import pandas as pd



def get_confidence(image_path,lang):
    img  = Image.open(image_path)
    texto = pytesseract.image_to_data(img, lang=lang,output_type=Output.DICT)

    result = {}

    for i in range(len(texto['text'])):
        if len(texto['text'][i]) > 0:
            #print('TEXTO: {}\CONFIDENCIA: {}\n'.format(texto['text'][i],texto['conf'][i]))
            
            result[texto['text'][i]] = texto['conf'][i]

    #Transforma o dicionário em um dataframe
    df_result = pd.DataFrame(result.items(),columns=['TEXTO', 'CONFIDENCIA'])

    #Transforma dataframe em um .csv
    df_result.to_csv('dataframe.csv', encoding="utf-8")

    return df_result


a = get_confidence('./imgs/img5.png','por.rafael')

print(a)




'''a = get_confidence('./imgs/img.png','por')
b = get_confidence('./imgs/img.png','por.raff+por')
c = get_confidence('./imgs/img.png','por+por.raff')
d = get_confidence('./imgs/img.png','por.raff')

print(a['TEXTO'],a['CONFIDENCIA'])
print(b['TEXTO'],b['CONFIDENCIA'])
print(c['TEXTO'],c['CONFIDENCIA'])
print(d['TEXTO'],d['CONFIDENCIA'])'''

