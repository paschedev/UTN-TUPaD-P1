n = int(input("Ingresa un número entero: "))

n2 = abs(n)
invertido = 0

while n2 > 0:
    digito = n2 % 10
    invertido = invertido * 10 + digito
    n2 = n2 // 10

#Si el numero original era negativo, lo hacemos negativo
if n < 0:
    invertido = -invertido

print(f"El numero invertido es: {invertido}")