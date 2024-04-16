# 9-Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final. Se deberá 
#     ir preguntando si hay más números para ingresar.

switch=""
nmax=0
while switch!="no":
    n=float(input("ingrese un numero: "))
    if n>0:
        if n>nmax:
            nmax=n
    elif n<0:
        print("el numero es negativo ",n," no es valido")
    switch=input("desea seguir? (si/no): ")

print("el valor maximo es: ",nmax)

