# Calcula si el número pedido por teclado es primo o no
num = int(input('Introduzca el número: '))
esPrimo = True

for n in range(2, num):
    if num % n == 0:
        esPrimo = False

if not esPrimo:
    print(f'{num} no es un número primo')
else:
    print(f'{num} es un número primo')
