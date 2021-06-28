#Dados do arquivo

from os import path
import time

def DadosArquivo():
    ArquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir("NovoArquivo.txt")
    pathArquivo = path.realpath("NovoArquivo.txt")
    pathRelativo = path.relpath("NovoArquivo.txt")
    dataCria = time.ctime(path.getctime("NovoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCria)
    print(dataModificacao)
DadosArquivo()
