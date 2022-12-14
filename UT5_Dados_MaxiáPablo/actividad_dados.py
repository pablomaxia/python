# Vamos a crear una aplicación que tire miles de dados por segundo, la aplicación parara cuando todos
# los dados que le digamos estén en 6, por ejemplo si le digo que quiero que 5 dados coinciden en 6
# hará tiradas hasta que 5 dados seguidos de 6. Para esto usaremos una lista!

# El script que vais a crear empezará preguntando cuántos dados queremos, después de esto se pondrá a
# hacer las tiradas, cuando se dé el caso de que ha salido el dado 6 el número de veces que le
# indicamos, parara, nos printeara la lista y el número de intentos que hemos hecho.

# RETO: En las tiradas, si más de la mitad de los dados están en seis que nos printee la lista también!

from random import randint


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


dados = []
cont = 0
numDados = (int)(input('Introduzca el número de dados que quieres: '))

while len(dados) < numDados:
    dado = randint(1, 6)
    dados.append(dado)
    count = dados.count(6)

    if count < numDados and len(dados) == numDados:
        dados = []
        cont += 1

mostrarLista(dados)

print(f'Número de intentos: {cont}')
