# Programa que crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.
# tabla = [] # Tabla vacía para inicializarla mediante la línea de comando
tabla = [
        [12, 20, 30, 45, 50],  # FILA 1
        [61, 74, 85, 19, 10],  # FILA 2
        [11, 22, 53, 14, 65],  # FILA 3
        [36, 17, 18, 49, 20],  # FILA 4
        [21, 82, 93, 24, 45]   # FILA 5
    # C1  C2  C3  C4  C5
]
total = 5
# Este bloque de código permite crear la tabla mediante la línea de comando.
# for i in range(total):
#    fila = []  # Crea las filas de la tabla
#    for j in range(total):
#        numero = (int)(
#            input(f'Introduzca el número de la fila {i+1} y de la columna {j+1}: '))
#        fila.append(numero)
#    tabla.append(fila)
print('=============')
print('Suma de filas')
print('=============')

for indice_fila, fila in enumerate(tabla):
    suma_fil = sum(fila)
    print(
        f'La suma de los elementos de la fila {indice_fila+1} es de {suma_fil}.')

print('================')
print('Suma de columnas')
print('================')

for i_col in range(len(tabla)):
    suma_col = 0
    for fila in tabla:
        suma_col += fila[i_col]
    print(
        f'La suma de los elementos de la columna {i_col+1} es de {suma_col}.')
