nombre = input("Ingrese su nombre: ")
n = int(input("\nIngrese un numero segun lo que desee\n"
"1. Si quiere su nombre en mayusculas.\n"
"2. Si quiere su nombre en minusculas.\n"
"3. Si quiere su nombre con la primera letra mayuscula.\n"))

longitud = len(nombre)

if n < 0 or n > 3:
    print("Opcion no valida.")
elif n == 1:
    print(nombre.upper())
elif n == 2:
    print(nombre.lower())
else:
    print(nombre.title())