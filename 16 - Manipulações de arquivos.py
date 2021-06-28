#Criando copia de arquivo

import os
from os import path
import shutil

def copiaArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.realpath("NovoArquivo.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        shutil.copystat(pathAtual, novoPath)
#copiaArquivo()

#Renomeando arquivo
def renomearArquvo():
    if path.exists("NovoArquivo.txt.bkp"):
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")
renomearArquvo()
