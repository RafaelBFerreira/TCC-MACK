#!/bin/bash

# Cria as caixas ao redor dos caracteres que ele reconhece
tesseract --psm 6 --oem 3 $1.font.exp0.tif $1.font.exp0 makebox

#sleep 2

# Arquivo de texto com as caracteristicas da imagem, recebe 0 caso false e 1 caso true | <fontname> <italic> <bold> <fixed> <serif> <fraktur>
echo "$1 0 0 0 0 0" > font_properties.txt

read -p "Abrir o jTessBoxEditor e ajustar as caixas delimitadoras no arquivo .tiff... [PRESS ENTER]"

# Cria o arquivo de treinamento .tr 
tesseract $1.font.exp0.tif $1.font.exp0 nobatch box.train
# Create a unicharset file
unicharset_extractor $1.font.exp0.box
# Create a shapetable file
shapeclustering -F font_properties.txt -U unicharset -O $1.unicharset $1.font.exp0.tr
# Create a pffmtable, intemp file
mftraining -F font_properties.txt -U unicharset -O $1.unicharset $1.font.exp0.tr
# Create a normproto file
cntraining $1.font.exp0.tr

#Renomear arquivos 

mv inttemp $1.inttemp
mv normproto $1.normproto
mv pffmtable $1.pffmtable
mv shapetable $1.shapetable

#Cria o tessdata
combine_tessdata $1.