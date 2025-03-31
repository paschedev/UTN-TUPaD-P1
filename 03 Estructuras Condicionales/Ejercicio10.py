#Input de datos
hemisfer = input("¿En qué hemisferio se encuentra el país? (Norte o Sur): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

#Check por hemisferio norte
if hemisfer == "NORTE":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 21:
        print("Es invierno en el hemisferio norte.")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
        print("Es primavera en el hemisferio norte.")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 21:
        print("Es verano en el hemisferio norte.")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
        print("Es otoño en el hemisferio norte.")
    else:
        print("Fecha no válida.")
#Check por sur
elif hemisfer == "SUR":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 21:
        print("Es verano en el hemisferio sur.")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
        print("Es otoño en el hemisferio sur.")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 21:
        print("Es invierno en el hemisferio sur.")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
        print("Es primavera en el hemisferio sur.")
    else:
        print("Fecha no válida.")
else:
    print("Hemisferio no válido. Ingrese 'Norte' o 'Sur'.")