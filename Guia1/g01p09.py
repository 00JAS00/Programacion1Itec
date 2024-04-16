# Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.
print("ingrese un numero para saber si tiene dos digitos y es positivo\n")
n1 = int(input("ingrese un numero: "))
if (n1>9 and n1<100):
    print("el numero ",n1," tiene dos digitos y es positivo")
elif (n1<0):
    print("el numero ",n1," negativo")
else:
    print("el numero ",n1," no tiene dos digitos y es positivo")

