#Escrevendo arquivos com função py

def EscreveArquivo():
	arquivo = open("NovoArquivo.txt", "w+") #w de write

	arquivo.write("linha gerada com a func 'EscreveArquivo' \r\n")

	arquivo.close()
EscreveArquivo()

#Altera arquivos com função py

def AlteraArquivo():
	arquivo = open("NovoArquivo.txt", "a+") #a de append

	arquivo.write("linha gerada com a func 'AlteraArquivo' \r\n")

	arquivo.close()
AlteraArquivo()