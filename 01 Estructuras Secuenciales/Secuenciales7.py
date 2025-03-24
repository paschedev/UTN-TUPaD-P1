print("Ingrese dos numero que no sean 0")
n1 = int(input())
n2 = int(input())
if n1 == 0 or n2 == 0:
    print("ERROR: Alguno o ambos de los numeros ingresados son 0")
else:
    print(f"Suma = {n1 + n2} \nDiferencia = {n1 - n2} \nProducto = {n1 * n2} \nCociente = {n1 / n2}")
    #Al parecer \n tambien funciona en pyhton :D