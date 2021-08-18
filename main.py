from pytesseract import pytesseract,Output
from PIL import Image


def get_confidence(image_path,lang):
    
    texto = pytesseract.image_to_data(Image.open(image_path),lang=lang,output_type=Output.DICT)

    result = {'TEXTO':[],'ACURACIA':[]}
    for i in range(len(texto['text'])):
        if len(texto['text'][i]) > 0:
            #print('TEXTO: {}\nACURÁCIA: {}\n'.format(texto['text'][i],texto['conf'][i]))

            result['TEXTO'].append(texto['text'][i])
            result['ACURACIA'].append(texto['conf'][i])
            
    return result

a = get_confidence('./imgs/img3.jpg','por')
b = get_confidence('./imgs/img3.jpg','eng')

print(a['ACURACIA'])
print(b['ACURACIA'])