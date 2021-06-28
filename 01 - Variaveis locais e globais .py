#Exemplo de código
print("Hello, World")

#Variaveis
f = "abc"
print(f)

#Concatenar str
print("Isto é uma str" + str( 123))

#variavel global x Variavel local
def AlgumaFuncao():
    global f #essa função substitui o primeiro valor de f
    f = "def"
    print(f)
AlgumaFuncao()
print(f)

