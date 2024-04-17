# 1- Pedir el ingreso de 10 números. Contar los mayores de 23 
# y almacenar los que cumplen la condición.  Mostrar la cantidad y los números guardados.

numMay = []
for i in range(10):
    num=int(input("ingresa un numero:"))
    if num>23:
        numMay.append(num)
print("Los numeros Mayores a 23 son: ",numMay,"\n Y con una cantidad de : ",len(numMay)," numeros")

    