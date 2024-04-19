# 5- Guardar en una lista los números pares mayores que 0 y menores que 31. 

pares=[]

for i in range(10):
    numero=int(input("Ingrese un numero: "))
    if numero%2 == 0 and numero>0 and numero<31:
        pares.append(numero)
print ( "Numeros pares y Mayores que 0 y menores que 31: ",pares )
