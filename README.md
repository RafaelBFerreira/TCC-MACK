# TCC-MACK 2021
Repositório git do projeto TCC 2021

## **Links**
 - [**Tesseract-Git**](https://github.com/tesseract-ocr/tessdoc)

 - [**Tesseract-Download**](https://github.com/UB-Mannheim/tesseract/wiki)

## **Como usar**
1. Python 3.7.2 instalado ou superior
2. Instalar o Tesseract e selecionar a linguagem portugues no auxiliar de instalação
3. Instalar os pacotes do arquivo *requeriments.txt*

```cmd
<TERMINAL> pip install -r requeriments.txt
```
4. Configurar o caminho para importar o tesseract no arquivo main.py

```py
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
```
5. Rodar o arquivo main.py

## **Autores**

Rafael Barbosa Ferreira - 31785311

Lucas Kenji Uezima - 41723643

Henrique Yudi Yassuda Nishimoto - 41719654
