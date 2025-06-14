
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n - 1)

numero = int(input("Ingrese un entero mayor que 0: "))
#Validacion
if numero < 1:
    print("¡¡¡ Ingrese un entero mayor que 0 !!!")
else:
    print(f"\nFactoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {facto(i)}")
