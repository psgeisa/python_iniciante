#Leitura de arquivo

def leituraArquivo():
    arquivo = open("NovoArquivo.txt", "r") #R de read
    if (arquivo.mode == "r"):
        conteudo = arquivo.read()
        print(conteudo)
    arquivo.close

#leituraArquivo() #pequeno arquivo

def leituraArquivoGrande():
    arquivo = open("NovoArquivo.txt", "r") #r de read
    if (arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal:
            print(conteudo)

    arquivo.close()
leituraArquivoGrande()
