# 12-Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una.

switch=""
nombres=""
contador=0

while switch!="no":
    # pedir datos
    nombre=input("ingrese el nombre: ")
    sexo=input("ingrese el sexo (f(femenino) o m(masculino)): ")
    # procesar
    if(sexo=="f"):
        contador+=1
        nombres+=","+nombre
    switch=input("desea seguir? (si/no): ")

# Mostrar resultados
if(contador==0):
    print("no hay datos")
else:
    print("los nombres de las mujeres son:",nombres)
    print("la cantidad de mujeres es: ",contador)

