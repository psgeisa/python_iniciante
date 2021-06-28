#função sem parametros
def func1():
    print("Eu sou uma função")
func1()

#função com parametros
def func2(arg1, arg2):
    print(arg1 + " " + arg2)
func2("Geisa", "Souza")

#função que retorna valores
def cubo(x):
    return x * x * x
f = cubo(3) #recebe cubo de 3
print(f) #imprime cubo de 3
print(cubo(2)) #recebe e imprime cubo de 2


