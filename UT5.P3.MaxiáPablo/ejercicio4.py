# Programa que guarda la temperatura mínima y máxima de 5 días.
# El programa da la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima
# coincide con ella. si no existe ningún día se muestra un mensaje de información.

# Guarda las temperaturas
temperaturas = []
total = 5
for indice in range(total):
    temperatura_max = (int)(
        input(f'Escriba la temperatura máxima del día {indice + 1}: '))
    temperatura_min = (int)(
        input(f'Escriba la temperatura mínima día {indice + 1}: '))
    temperatura = []  # Guarda las temperaturas de cada día
    temperatura.append(temperatura_max)
    temperatura.append(temperatura_min)
    temperaturas.append(temperatura)

# Muestra temperatura media
print('===================')
print('Temperaturas medias')
print('===================')
num = 1
for temperatura in temperaturas:
    media = sum(temperatura)/len(temperatura)
    print(
        f'La temperatura media del día {num} es: {media}')
    num += 1

# Calcula la temperatura mínima más pequeña
temp_min = temperaturas[0][1]  # Se empieza por la primera
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]

# Muestra los días con menos temperatura
print('==========================')
print('Días con menos temperatura')
print('==========================')
num = 1
print(f'Los días con la temperatura mínima de {temp_min} son:')
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print(f'Día {num}')
    num += 1

# Muestra los días con temperatura máxima
existe_temperatura = False
print('===========================')
print('Días con temperatura máxima')
print('===========================')
temp_max = int(input('Introduce una temperatura: '))
num = 1
print(f'Los días con la temperatura máxima de {temp_max} son:')
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print(f'Día {num}')
        existe_temperatura = True
    num += 1
if not existe_temperatura:
    print('No hay ningún día con dicha temperatura.')
