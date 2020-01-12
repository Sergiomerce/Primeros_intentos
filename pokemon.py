pokemon_luchar = input("¿contra que pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ").upper()
vida_pikachu=100
vida_enemigo=0
if pokemon_luchar == "SQUIRTLE":
    vida_enemigo = 90
    daño_ataque = 8
if pokemon_luchar == "CHARMANDER":
    vida_enemigo = 90
    daño_ataque = 7
if pokemon_luchar == "BULBASAUR":
    vida_enemigo = 90
    daño_ataque = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    print("Te toca atacar")
    nuestro_ataque = input("Que ataque quieres usar (Chispazo / Bola voltio)").upper()
    if nuestro_ataque == "CHISPAZO":
        vida_enemigo-=10
    if nuestro_ataque == "BOLA VOLTIO":
        vida_enemigo-=12
    print("La vida de {} es de {}".format(pokemon_luchar, vida_enemigo))
    print("{} ha atacado y ha hecho un daño de {}" .format(pokemon_luchar, daño_ataque))
    vida_pikachu -= daño_ataque
    print("Tu vida es {}".format(vida_pikachu))
if vida_enemigo <= 0:
    print("¡Has ganado!")
if vida_pikachu <= 0:
    print("¡Sorry bby has perdido!")
