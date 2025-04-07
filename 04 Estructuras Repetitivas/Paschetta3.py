print("Ingrese dos numeros para crear un rango")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1 != n2 and n1 < n2:
    for i in range(n1+1, n2):
        print(i)
elif n1 != n2 and n1 > n2:
    for i in range(n2+1, n1):
        print(i)
else:
    print("Los numeros no pueden ser iguales")