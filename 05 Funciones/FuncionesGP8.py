import misFunciones as gp
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = gp.calcular_imc(peso, altura)
print(f"El IMC es: {imc}")