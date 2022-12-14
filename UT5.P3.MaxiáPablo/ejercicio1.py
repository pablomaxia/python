# Programa que inicializa una lista con 10 valores aleatorios (del 1 al 10) y muestra en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

numeros = []
for i in range(10):
    numeros.append(random.randint(1, 10))

for numero in numeros:
    print(f"Número: {numero} - Cuadrado: {numero**2} - Cubo: {numero**3}")
