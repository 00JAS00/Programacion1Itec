# 5-Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.

indice=""
total=0
while indice!="no":
    indice=input("ingrese el sueldo: ")
    if(indice!="no"):
        total+=int(indice)
    indice=input("Desea continuar? (si/no): ")
print("el total de sueldos es: ",total)


