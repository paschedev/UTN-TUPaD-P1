mag = int(input("Ingrese la magnitud del terremoto:"))
if mag < 3:
    print("Muy leve")
elif 3 <= mag < 4:
    print("Leve")
elif 4 <= mag < 5:
    print("Moderado")
elif 5 <= mag < 6:
    print("Fuerte")
elif 6 <= mag < 7:
    print("Muy fuerte")
elif 7 <= mag:
    print("Extremo")