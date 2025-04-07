print("Ingrese 100 numeros para verificar si son pares, impares, positivos o negativos.")
par = 0
impar = 0
pos = 0
neg = 0
ceros = 0
for i in range(1, 10):
    n = int(input(f"Ingrese el numero {i}: "))
    if n > 0:
        pos += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    elif n < 0:
        neg += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    else:
        ceros += 1

print(f"Cantidad de numeros positivos: {pos}")
print(f"Cantidad de numeros negativos: {neg}")
print(f"Cantidad de numeros pares: {par}")
print(f"Cantidad de numeros impares: {impar}")
print(f"Cantidad de numeros cero: {ceros}")