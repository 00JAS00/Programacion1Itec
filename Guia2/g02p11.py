# 11-Ingresar 7 números enteros y en el caso de que sean naturales de una sola 
#     cifra mostrar un cartel en cada uno.

for i in range(7):
    num = int(input("ingrese un numero entero: "))
    if (num<10):
        print("el numero ",num," tiene una sola cifra y es natural")
    elif (num>9):
        print("el numero ",num," tiene mas de una cifra y es natural")
