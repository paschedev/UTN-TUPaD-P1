def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro

def calcular_area_y_perimetro_circulo(radio):
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area}\nEl perímetro del círculo es: {perimetro}")

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    resto_segundos = segundos % 60
    print(f"{horas} horas, {minutos} minutos y {resto_segundos} segundos.")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")

def operaciones_basicas(a, b):
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    if b != 0:
        print(f"División: {a / b}")
    else:
        print("No se puede dividir entre cero.")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio