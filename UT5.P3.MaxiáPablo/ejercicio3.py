# Programa que inicializa una lista de números con valores aleatorios (10 valores),
# y posterior ordena los elementos de menor a mayor.

import random


def mostrarLista(lista):
    '''
    Muestra los elementos de una lista pasada por parámetro.
    '''
    for inx, elem in enumerate(lista):
        if inx == len(lista)-1:
            str_elem = (str)(elem)
        else:
            str_elem = (str)(elem) + ', '
        print(str_elem, end='')
    print()


numeros = []
for i in range(10):
    numeros.append(random.randint(1, 10))

print('=================')
print('Lista de números:')
print('=================')
mostrarLista(numeros)

numeros.sort()  # Ordena la lista en orden ascendente
print('==========================')
print('Lista en orden ascendente:')
print('==========================')
mostrarLista(numeros)

numeros.sort(reverse=True)  # Ordena la lista en orden descendiente
print('==========================')
print('Lista en orden descendente:')
print('==========================')
mostrarLista(numeros)
