# Programa que pide números hasta que se introduce el 0.
# Calcula la suma y la media de los números introducidos.
suma = 0
media = 0
total = 0
num = None

while num != 0:
    num = int(input('Introduzca un número: '))
    total += 1
    suma += num
    media = suma/total

print(f'La suma de los números introducidos es {suma}')
print(f'La media de los números introducidos es {media}')
