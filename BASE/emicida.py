# encoding=utf-8

"""
    Desafio:

    No diretório base existe um arquivo main.txt e nele está registrado um texto.

    O desafio criar um algoritmo que extraia o texto deste arquivo e o tranfira para um novo arquivo com extensão .txt

    Dica: utilize as técnicas dos algoritmos anteriores para encontrar o arquivo que está no diretório data.
"""

# imports
import os

# 1. Obtendo o caminho exato da pasta em que o arquivo emicida.py está salvo

caminho = os.getcwd()

print(caminho)
# saída: C:\Users\m913685\Documents\repos\stag-tasks\BASE

# 2. Dentro do diretório BASE há uma pasta com o nome data na qual há um arquivo main.txt
# buscando pelo pasta data
for dirs, folders, files in os.walk(caminho):
    # se em dirs houver uma pasta com nome data, percorrer esta pasta
    # se em file existir algum com o nome de main.txt ele será salvo em uma variável de nome data
    #print(dirs)
    #print(folders)
    #print(files)
    for file in files:
        if file == 'main.txt':
            data = 'main.txt'
    
print(data)
