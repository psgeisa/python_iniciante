import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

#cria arquivo zipado
def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\psgei\\OneDrive\\Área de Trabalho\\Academico\\Impacta\\Treinamento\\Programação Prática\\Linkedin - Python")
#CriaZipModo1()

#cria arquivo 
def CriaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
        novoZip.write("ArquivoAlterado.txt") #inclusão de arquivo
        novoZip.write("NovoArquivo.txt") #inclusão de arquivo
        novoZip.write("zipModo1.zip.zip") #inclusão de arquivo
#CriaZipModo2()

def deletaArquivo():
    os.remove("ArquivoZipModo2.zip")
deletaArquivo()