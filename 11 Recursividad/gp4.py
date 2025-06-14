def decimal_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    if n == 0:
        return "0"
    return decimal_binario(n)


numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = convertir_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")