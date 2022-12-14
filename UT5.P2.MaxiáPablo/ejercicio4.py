# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis,
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = int(input('Escriba la edad del cliente: '))
while edad < 0:
    if edad < 0:
        print('Los clientes no pueden tener edad negativa.')
        edad = int(input('Escriba la edad del cliente: '))
if edad < 4:
    print('Puede entrar de forma gratuita.')
elif 4 <= edad <= 18:
    print('Tiene que pagar 5€')
else:
    print('Tiene que pagar 10€')
