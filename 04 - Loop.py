#Loop com while

def Loop():
    x = 0
    while (x < 5):
        print(x)
        x = x +1
Loop()


#Loop com for

def LoopFor():
    for x in range(5, 10):
        print(x)
LoopFor()


#Loop com uma coleção

def LoopArray():
    dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    for d in dias:
        print(d)
LoopArray()


#Loop com uma enumerate
def LoopEnum():
    dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    for i, d in enumerate(dias):
        print(i, d)
LoopEnum()


