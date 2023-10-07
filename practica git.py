num= int(input("ingresa un numero: "))
if num <= 0:
    print("Ingresa un numero entero positivo")
else:
    impares=[]
    for i in range (num):
        if (i%2) != 0:
            impares.append(i)

    print(impares)


