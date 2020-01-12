mi_lista = []
compra = input("Que quieres comprar (Escribe Fin para terminar la lista)")

while compra != "Fin":
    mi_lista.append(compra)
    compra = input("Que quieres comprar (Escribe Fin para terminar la lista)")
largo_lista = len(mi_lista)
indice_actual = 0

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Esta es tu lista de la compraa")

