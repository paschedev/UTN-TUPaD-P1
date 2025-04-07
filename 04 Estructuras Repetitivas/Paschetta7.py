n = int(input("Ingrese un numero:\n"))
suma = 0
if n > 0:
    for i in range(0, n+1):
        suma += i
    print("La suma es: ", suma)
else:
    print("El numero no es positivo")