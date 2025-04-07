num = int(input("Ingresa un numerito: "))
# string = str(num)
# long = len(string)
# print("El numero tiene", long, "digitos")
# Asi lo haria si no tuviera que usar ciclos...


count = 1 #Contador iniciado en 1 porque el 0 cuenta como un digito
# Y si cambio la configuracion del ciclo, el 0 no contaria como un digito
#Check por positivos
while num >= 10:
    num = num / 10
    count += 1
#Check por negativos
while num <= -10:
    num = num / 10
    count += 1

print("El numero tiene", count, "digitos")