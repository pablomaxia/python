# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input('Escriba una frase: ')
letra = input('Escriba una letra: ')
vecesLetra = 0
while len(letra) > 1:
    letra = input('Escriba una letra: ')

for l in frase.lower():
    if l == letra.lower():
        vecesLetra += 1
print(f'La letra "{letra}" aparece {vecesLetra} veces en la frase: "{frase}"')
