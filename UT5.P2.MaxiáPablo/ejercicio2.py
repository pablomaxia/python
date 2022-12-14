# Escribir un programa que num1 través de un menú
# permita al usuario sumar, restar, multiplicar o dividir dos operandos.
# El menú tendrá la opción 5 de salir.

def sumar(numA, numB):
    '''
    Esta función suma 2 números y muestra el resultado.
    '''
    suma = numA+numB
    print(f'{numA} + {numB} = {suma}')


def restar(numA, numB):
    '''
    Esta función resta 2 números y muestra el resultado.
    '''
    resta = numA - numB
    print(f'{numA} - {numB} = {resta}')


def multiplicar(numA, numB):
    '''
    Esta función multiplica 2 números y muestra el resultado.
    '''
    mult = numA * numB
    print(f'{numA} * {numB} = {mult}')


def dividir(numA, numB):
    '''
    Esta función divide 2 números y muestra el resultado.
    '''
    if numB != 0:
        resultado = numA/numB
        print(f'{numA} / {numB} = {resultado}')
    else:
        print('No se puede dividir entre 0.')


def mostrarMenu():
    '''
    Esta función muestra el menú.
    '''
    print('1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir')


op = None
while op != 5:
    mostrarMenu()
    op = int(input('Escoja una opción (1-5): '))
    if 1 <= op <= 4:
        num1 = float(input('Introduzca un número: '))
        num2 = float(input('Introduzca otro número: '))
    match op:
        case 1:
            sumar(num1, num2)
        case 2:
            restar(num1, num2)
        case 3:
            multiplicar(num1, num2)
        case 4:
            dividir(num1, num2)
        case 5:
            print('Fin del programa.')
        case other:
            op = int(
                input('La opción escogida no es válida. Escoja una opción (1-5): '))
print('Fin del programa.')
