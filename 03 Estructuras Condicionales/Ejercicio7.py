frase = input("Escribe una frase: ")

#Para terminar ese ejercicio, primero tuve que hacer el ejercicio 8, usando .lower()
#El indice -1 se refiere a la ultima letra de la cadena
if frase[-1].lower() in "aeiou":
    print(f"{frase}!")
else:
    print(frase)