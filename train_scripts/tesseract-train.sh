#!/bin/bash
# Cria as caixas ao redor dos caracteres que ele reconhece
tesseract --psm 6 --oem 3 $1.exp0.tif $1.exp0 makebox

# Arquivo de texto com as caracteristicas da imagem, recebe 0 caso false e 1 caso true | <fontname> <italic> <bold> <fixed> <serif> <fraktur>
echo "$1 0 0 0 0 0" > font_properties.txt
read -p "Abrir o jTessBoxEditor e ajustar as caixas delimitadoras no arquivo .tiff... [PRESS ENTER]"

# Cria o arquivo de treinamento .tr 
tesseract $1.exp0.tif $1.exp0 -l por nobatch box.train

# Cria o arquivo unicharset que contem informações sobre cada caractere que o tesseract reconhecer
unicharset_extractor $1.exp0.box

# Cria o arquivo shapeclustering que melhora a qualidade dos caracteres encontrados no unicharset
shapeclustering -F font_properties.txt -U unicharset -O $1.unicharset $1.exp0.tr
 
# Cria os arquivos pffmtable e intemp a partir do .tr gerado
mftraining -F font_properties.txt -U unicharset -O $1.unicharset $1.exp0.tr

# Cria o arquivo normproto a partir do arquivo .tr gerado
cntraining $1.exp0.tr

#Renomear arquivos 
mv inttemp $1.inttemp
mv normproto $1.normproto
mv pffmtable $1.pffmtable
mv shapetable $1.shapetable

#Combina os arquivos gerados para gerar o arquivo tessdata
combine_tessdata $1.


