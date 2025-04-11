import misFunciones as gp
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))
promedio = gp.calcular_promedio(n1, n2, n3)
print(f"El promedio de {n1}, {n2} y {n3} es: {promedio}")