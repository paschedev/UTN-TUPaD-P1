edad = int(input("¿Cuántos años tenes? "))

if edad < 0:
    print("Edad no válida.")
elif edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")