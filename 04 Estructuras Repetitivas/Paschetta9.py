print("Ingrese 100 numeros para verificar el promedio de ellos.")
sum = 0
numeros = 100
for i in range(1, numeros+1):
    n = int(input(f"Ingrese el numero {i}: "))
    sum += n
prom = sum / numeros
print(f"El promedio de los numeros ingresados es: {prom}")