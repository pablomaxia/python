# Solicita una nota y muestra un mensaje
nota = float(input('Introduzca su nota: '))

if nota < 3 and nota >= 0:
    print('Muy deficiente')
elif nota < 5:
    print('Insuficiente')
elif nota < 6:
    print('Suficiente')
elif nota < 7:
    print('Bien')
elif nota < 9:
    print('Notable')
elif nota < 10:
    print('Sobresaliente')
