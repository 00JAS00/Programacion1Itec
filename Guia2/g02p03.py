# 3-Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.

mayor = 0
for i in range(5):
    num = int(input("ingrese un numero: "))
    if (num > 23):
        mayor += 1
print("la cantidad de numeros mayores de 23 es: ",mayor)
