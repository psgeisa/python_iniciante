#Potencia com while
x = int(input("Base: "))
y = int(input("Expoente: "))

pot = 1
count = 1

while count <= y:
    pot *= x
    count += 1

print("O numero base é:", x)
print("O expoente é:", y)
print("A potência é:", pot)

#Simples
x = int(input("Base: "))
y = int(input("Expoente: "))

pot = x**y

print("O numero base é:", x)
print("O expoente é:", y)
print("A potência é:", pot)

#Com for
x = int(input("Base: "))
y = int(input("Expoente: "))

pot = 1
for count in range(y):
    pot = pot * x
print("O numero base é:", x)
print("O expoente é:", y)
print("A potência é:", pot)
