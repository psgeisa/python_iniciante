#Quebra loop
def LoopBreak():
    for x in range(5, 10):
        if x == 7: #encontrando o 7, o continue interrompe todas as execuções
            break
        print("O valor de x é: ", x)
LoopBreak()


#Continue loop
def LoopCont():
    for x in range(5, 10):
        if x == 7: #encontrando o 7, o continue interrompe apenas esta executação
            continue
        print("O valor de x é: ", x)
LoopCont()
