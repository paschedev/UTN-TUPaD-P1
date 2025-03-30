nota = int(input("¿Qué nota sacaste? "))
if nota < 0 or nota > 10:
    print("Nota no válida.")
elif nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")