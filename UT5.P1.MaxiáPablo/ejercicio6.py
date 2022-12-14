# Calcula si el empleado aumenta de sueldo según su sueldo y antigüedad
sueldo = int(input('Introduzca el sueldo: '))
antiguedad = int(input('Introduzca la antigüedad: '))

if sueldo < 500 and antiguedad > 10:
    total = sueldo*3
    print(f'Su sueldo se triplicará. Ahora vale: {total}')
elif sueldo < 500 and antiguedad < 10:
    total = sueldo*2
    print(f'Su sueldo se duplicará. Ahora vale: {total}')
else:
    print('Su sueldo se queda igual.')
