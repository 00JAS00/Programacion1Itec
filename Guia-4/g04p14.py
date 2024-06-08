# 14 Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que 
# muestre el nombre del mayor y cuanto le lleva al menor. 
# (Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')
nombre1 =input("Ingrese su nombre: ")
edad1 =int(input("Ingrese su edad: ")) 
nombre2 =input("Ingrese su nombre: ") 
edad2 =int(input("Ingrese su edad: "))  
if edad1 > edad2:
    mayor= f'{nombre1} le lleva {edad1-edad2} años a {nombre2}'
else:
    mayor= f'{nombre2} le lleva {edad2-edad1} años a {nombre1}'
print(mayor)
