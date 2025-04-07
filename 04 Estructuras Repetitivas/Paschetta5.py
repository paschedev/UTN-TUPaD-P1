import random as r
num = r.randint(0,9)
intentos = 0

n = int(input("Ingrese numeros hasta adivinar el numero correcto (del 0 al 9):"))
intentos += 1
if n == num:
    print("Adivinaste el numero a la primera!!!")
else:
    while n != num:
        print("Fallaste, intenta de nuevo")
        intentos += 1
        n = int(input("Ingrese otro numero: "))
print(f"Adivinaste el numero en {intentos} intentos")
