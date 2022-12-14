# Programa que añada números a una lista hasta que introducimos un número negativo.
# A continuación crea una nueva lista igual que la anterior
# pero eliminando los números duplicados.
lista = []


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


num = int(input('Introduzca un número entero positivo (negativo para terminar): '))
while num >= 0:
    lista.append(num)
    num = int(
        input('Introduzca un número entero positivo (negativo para terminar): '))

lista_sin_dup = []
for num in lista:
    if num not in lista_sin_dup:
        lista_sin_dup.append(num)

print('=============')
print('Lista inicial')
print('=============')
mostrarLista(lista)

print('====================')
print('Lista sin duplicados')
print('====================')
mostrarLista(lista_sin_dup)
