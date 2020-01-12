print("ESTO ES UNA CALCULADORA")
num_uno = float(input("Escibe el primer numeroo"))
operador = (input("Que quieres realizar (+, -, *, /)")).upper()
num_dos = float(input("Escibe el segundo numero"))
if operador == "+":
    resultado = num_uno + num_dos
    print("{} + {} = {}".format(num_uno, num_dos, resultado))
elif operador == "-":
    resultado = num_uno - num_dos
    print("{} - {} = {}".format(num_uno, num_dos, resultado))
elif operador == "*":
    resultado = num_uno * num_dos
    print("{} X {} = {}".format(num_uno, num_dos, resultado))
elif operador == "/":
    resultado = num_uno / num_dos
    print("{} / {} = {}".format(num_uno, num_dos, resultado))
