def mostrar_impares(numero):
    impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    return ', '.join(impares)

try:
    numero = int(input("Por favor, ingresa un número entero positivo: "))

    if numero <= 0:
        print("Por favor, ingresa un número entero positivo mayor que cero.")
    else:
        impares_hasta_numero = mostrar_impares(numero)
        print("Números impares hasta el número ingresado:", impares_hasta_numero)
except ValueError:
    print("Debes ingresar un número entero válido.")
