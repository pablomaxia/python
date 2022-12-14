# Pide 3 números por teclado y dice si alguno es mayor de 10.
total = 3
mayor_10 = False

for i in range(total):
    num = int(input(f'Introduzca el número {i + 1}: '))
    if num > 10:
        mayor_10 = True
if mayor_10:
    print('Alguno de los 3 números es mayor que 10')
else:
    print('No hay ningún número mayor que 10')
