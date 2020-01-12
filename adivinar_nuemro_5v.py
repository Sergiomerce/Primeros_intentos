numero_adivinar=5
num_persona=int(input("Intente adivinar el numero: "))
if numero_adivinar==num_persona:
    print("Has ganado")
else:
    print("Numero incorrecto, tienes 4 intentos mass")
    num_persona = int(input("Intente adivinar el numero: "))
    if numero_adivinar == num_persona:
        print("Has ganado")
    else:
        print("Numero incorrecto, tienes 3 intentos mas")
        num_persona = int(input("Intente adivinar el numero: "))
        if numero_adivinar == num_persona:
            print("Has ganado")
        else:
            print("Numero incorrecto, tienes 2 intentos mas")
            num_persona = int(input("Intente adivinar el numero: "))
            if numero_adivinar == num_persona:
                print("Has ganado")
            else:
                print("Numero incorrecto, tienes 1 intentos mas")
                num_persona = int(input("Intente adivinar el numero: "))
                if numero_adivinar == num_persona:
                    print("Has ganado")
                else:
                    print("Eres un torpe bby")

