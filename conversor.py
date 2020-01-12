fahren = float(input("Grados fahrenheit"))
conversor = round((fahren - 32) * 5 / 9, 4)
print("{}° Fahrenheit son {}° Celsiuss".format(fahren, conversor))