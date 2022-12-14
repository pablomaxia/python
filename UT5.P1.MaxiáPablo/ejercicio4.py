# Pide 7 números enteros positivos por teclado y los suma y los multiplica.
mult = 1
suma = 0
total = 7
for i in range(total):
    num = int(input(f'Introduzca el número {i + 1}: '))
    if num < 0:
        print(f'El número {i + 1} no es positivo')
        break
    else:
        suma += num
        mult *= num
    if i == total - 1:
        print(f'La suma de los números es: {suma}')
        print(f'La multiplicación de los números es: {mult}')
