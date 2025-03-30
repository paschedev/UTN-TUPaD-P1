from statistics import mode, median, mean
import random
randnums = [random.randint(1, 100) for _ in range(50)]
moda = mode(randnums)
mediana = median(randnums)
media = mean(randnums)

if moda == mediana and mediana == media:
    print("No hay sesgo.")
elif media > mediana and mediana > moda:
    print("Sesgo a la derecha.")
else:
    print("Sesgo a la izquierda.")

#Hago este print para ver los valores calculados de la lista de randoms.
print(f"Moda: {moda}     Mediana: {mediana}    Media: {media}")