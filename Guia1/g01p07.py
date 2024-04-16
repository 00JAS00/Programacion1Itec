# Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad

name=input("ingrese su nombre: ")
opcion=input("ingrese la opcion ( > o < ): ")
if (opcion==">"):
    print(name, "es mayor de edad")
elif (opcion=="<"):
    print(name, "es menor de edad")
else:
    print("la opcion no es valida")
