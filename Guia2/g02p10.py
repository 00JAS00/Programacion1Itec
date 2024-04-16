# 10-Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar 
#     el nombre de la persona que menos gana.

switch=""
nombre=""
salarioMin=0
while switch!="no":
    n=input("ingrese un nombre: ")
    salario=float(input("ingrese el salario: "))
    if salario>0:
        if salarioMin==0 or salario<salarioMin:
            salarioMin=salario
            print(salarioMin)
            nombre=n
    elif salario<0:
        print("el numero ingresado no es valido")
    switch=input("desea seguir? (si/no): ")
if salarioMin==0:
    print("no hay datos")
else:
    print("el nombre del que menos gana es: ",nombre)
    print("el salario minimo es: ",salarioMin)

