num= int(input("ingresa un numero: "))
if num <= 0:
    print("Ingresa un numero entero positivo")
else:
    impares=[]
    for i in range (num):
        if (i%2) != 0:
            impares.append(i)

    print(impares)


def promedio(numeros):
    prom = sum(numeros)/len(numeros)
    print (prom)
numeros=[3,5,6,6,73,3,1]

promedio(numeros)
