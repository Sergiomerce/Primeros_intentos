helado=input("Quieres un Helado? (Si/No)").upper()
if helado=="SI":
    helado=True
elif helado=="NO":
    helado=False
else:
    print("El valor introducido no corresponde asi que lo considero como que no")
dinero=input("Tienes dinero? (Si/No)").upper()
if dinero=="SI":
    dinero=True
elif dinero=="NO":
    dinero=False
else:
    print("El valor introducido no corresponde asi que lo considero como que no")

if helado and dinero:
    print("Pues come bby")
else:
    print("Pues nada bby")
