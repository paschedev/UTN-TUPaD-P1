def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente < 0:
    print("¡¡¡ Ingrese un exponente mayor o igual que 0 !!!")
else:
    print(f"{base} elevado a {exponente} = {potencia(base, exponente)}")