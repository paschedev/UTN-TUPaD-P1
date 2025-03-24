print("Ingrese una cantidad de segundos")
segundos = int(input())
horas = segundos // 3600
segundos = segundos % 3600
if(segundos > 0):
    print(f"Horas {horas} con {segundos} segundos.")
else:
    print(f"Horas {horas}.")
