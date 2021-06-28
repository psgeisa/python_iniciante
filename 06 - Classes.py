
class minhaClasse():
    def __init__(self): #init é meu construtor
        self.meuAtributo = "Passou pelo contrutor"

    def meuMetodo(self):
        print("Passou pelo meuMetodo")

    def meuMetodo2(self, valor):
        self.outroAtributo = valor
        print(self.outroAtributo)

def criaObjeto():
    meuObj = minhaClasse()
    var1 = meuObj.meuAtributo
    print(var1)

    meuObj.meuMetodo()
    meuObj.meuMetodo2("Excuta um metodo")

criaObjeto()

