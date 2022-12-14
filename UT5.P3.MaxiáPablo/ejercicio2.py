# Programa que lee por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
# Muestra todas las notas, la nota media, la nota más alta que ha sacado y la menor.
total = 5
notas = []


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


while len(notas) < total:
    nota = (float)(input(f'Introduzca la nota {len(notas)+1}: '))
    if nota < 0 or nota > 10:
        print(f'La nota {nota} no está entre 0 y 10.')
    else:
        notas.append(nota)

media = sum(notas)/len(notas)
mayor = max(notas)
menor = min(notas)

print("======")
print("Notas:")
print("======")
mostrarLista(notas)
print("Nota media:", media)
print("Nota mayor:", mayor)
print("Nota menor:", menor)
