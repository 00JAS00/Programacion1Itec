# 6-Preguntar cuántas personas se van a cargar y luego solicitar sus edades, 
#     mostrando al final la edad promedio.


cantPersonas=int(input("ingrese la cantidad de personas a cargar: "))
edad=0 #acumulador

for i in range(cantPersonas):
    edad+=int(input("ingrese la edad de la persona: "))

print("la edad promedio es: ",edad/cantPersonas)
