# TCC-MACK
Repositório git do projeto TCC 2021

## **Links**
 - [**Tesseract-Git**](https://github.com/tesseract-ocr/tessdoc)

 - [**Tesseract-Download**](https://github.com/UB-Mannheim/tesseract/wiki)

## **Como usar**
1. Python 3.8.8 instalado ou superior
2. Instalar o Tesseract e selecionar a linguagem portugues no auxiliar de instalação
3. Instalar os pacotes do arquivo *requeriments.txt*
4. Configurar o caminho para importar o tesseract

```py
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
```
5. Rodar o arquivo main.py