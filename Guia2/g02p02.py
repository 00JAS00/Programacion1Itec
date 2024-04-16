# Preguntar si hay datos para ingresar, en caso afirmativo solicitar un número entero y 
#     decir si es negativo o no. Preguntar si repite.

i = ""

while i!="no":
    numero = int(input("ingrese un numero entero: "))
    if (numero<0):
        print("el numero ",numero," es negativo")
    else:
        print("el numero ",numero," es positivo")
    i = input('Desea Continuar? "si" o "no" : ')

