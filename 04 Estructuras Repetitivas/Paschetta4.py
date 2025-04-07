n = int(input("Ingresa numeros para acumularlos, para frenar ingrese 0: "))
suma = 0

while n != 0:
    suma += n
    n = int(input("Ingresa otro (frenar con 0): "))
print("La suma es: ", suma)