edad = int(input("¿Cuántos años tenes? "))
if edad < 0:
    print("Edad no válida.")
elif edad < 12:
    print("Sos un niño.")
elif edad >= 12 and edad < 18:
    print("Sos un adolescente.")
elif edad >= 18 and edad < 30:
    print("Sos un adulto joven.")
else:
    print("Sos adulto.")