# Programa que crear una lista de palabras y que tiene las siguientes opciones:
# Contar: Pide una cadena, y me cuantas veces aparece en la lista
# Modificar: Pide una cadena, y otra cadena a modificar, y modifica todas
# las apariciones de la primera por la segunda en la lista.
# Eliminar: Pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar

lista = []


def contar(lista_param):
    '''Cuenta la cantidad de veces que la cadena aparece en la lista'''
    cad = input("Introduce una cadena a buscar: ")
    print("La cadena aparece %d veces" % lista_param.count(cad))


def modificar(lista_param):
    '''Modifica una cadena concreta de la lista'''
    cad = input("Introduce una cadena a modificar: ")
    cadena2 = input("Introduce la nueva cadena: ")
    indice = 0
    for indice, elemento in enumerate(lista_param):
        if elemento == cad:
            lista_param[indice] = cadena2


def eliminar(lista_param):
    '''Elimina una cadena concreta de la lista'''
    cad = input("Introduce una cadena a eliminar: ")
    if cad in lista_param:
        while cad in lista_param:
            lista_param.remove(cad)
    else:
        print("No existe la cadena en la lista.")


def mostrarLista(lista_param):
    '''
    Muestra los elementos de una lista pasada por parámetro.
    '''
    for inx, elem in enumerate(lista_param):
        if inx == len(lista_param)-1:
            str_elem = (str)(elem)
        else:
            str_elem = (str)(elem) + ','
        print(str_elem, end='')
    print()


cadena = input("Introduce una cadena. (* para terminar): ")
while cadena != "*":
    lista.append(cadena)
    cadena = input("Introduce una cadena. (* para terminar): ")

while True:
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")
    opcion = int(input("Introduzca una opción (1-5): "))
    match opcion:
        case 1:
            contar(lista)
        case 2:
            modificar(lista)
        case 3:
            eliminar(lista)
        case 4:
            mostrarLista(lista)
        case 5:
            break
        case other:
            print("La opción es incorrecta. No está comprendida entre el 1 y el 5.")
print('Fin del programa.')
