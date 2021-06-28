#exibir mensagens personalizadas

from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print("Valores encontrados: ", a[0], " ", a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada")

    def handle_comment(self, data):
        print("Comentario encontrado.")

    def handle_data(self, data):
        print("Valores encontrados")
        if data.isspace():
            print("� espa�o")
        else:
            print("O valor �: ", data)

def meuObjeto():
    meuParser1 = meuParser()
    arquivo = open("C:\\Users\\psgei\\OneDrive\\Área de Trabalho\\Academico\\Impacta\\Treinamento\\Programação Prática\\Linkedin - Python\\exemplo.html")
    dados = arquivo.read()
    meuParser1.feed(dados)
meuObjeto()