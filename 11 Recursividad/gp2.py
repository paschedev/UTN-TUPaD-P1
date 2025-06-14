def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

numero = int(input("Ingrese un entero mayor que 0: "))
# Validacion
if numero < 0:
    print("¡¡¡ Ingrese un entero mayor o igual que 0 !!!")
else:
    print(f"\nFibonacci del 0 al {numero}:")
    for i in range(numero + 1):
        print(f"{i} = {fibo(i)}")