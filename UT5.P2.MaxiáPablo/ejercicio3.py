# Escribir un programa que pida al usuario un número entero y
# muestre por pantalla un triángulo rectángulo de altura el número introducido.

altura = -1
while altura < 0:
    altura = int(input('Escriba la altura del triángulo: '))
    if altura < 0:
        print('La altura del triángulo tiene que ser positiva.')

for i in range(1, altura+1):
    # i indica el número de veces que debe mostrarse el astersico en una línea.
    print(i*'* ')
