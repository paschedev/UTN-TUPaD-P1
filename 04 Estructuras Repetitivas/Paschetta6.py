pares = 0
for i in range(101, 0, -1):
    if i % 2 == 0:
        pares += 1
print(f"Hay {pares} numeros pares entre 100 (inclusive) y 0")