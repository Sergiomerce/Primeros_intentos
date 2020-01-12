num_adivinar = input("Que numero quieres que intenten adivinarr")
num_adivinado = 0
## Numero de intentos
a = -1
while num_adivinar != num_adivinado:
    a = a + 1
    print("Lleva {} intento".format(a))
    num_adivinado = input("Que numero crees que hay que adivinar")
print("¡Enhorabuena has acertado el numero!")