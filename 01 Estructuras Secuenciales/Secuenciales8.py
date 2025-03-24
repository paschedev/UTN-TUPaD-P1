print("Ingrese su altura (en cmentimetros) y peso (en kilogramos)")
altura = float(input("Altura: "))
peso = float(input("Peso: ")) / 100
imc = peso / (altura ** 2)
print(f"Su IMC es de {imc}.")