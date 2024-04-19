# 6- Ingresar nombres en una lista sin repetir, luego buscar un nombre y de encontrarlo decir en qué posición está.

nombres=[]
toggle=""

print("ESTE PROGRAMA TIENE DOS PARTES UNA PARA LA INTRODUCCION DE NOMBRES Y OTRA PARA SU POSTERIOR BUSQUEDA\n")
# Ingresar nombres en una lista sin repetir
print("EN ESTA PARTE DEL PROGRAMA DEBE INGRESAR NOMBRES")
while toggle != "off":
    inputNombre=str(input("Ingrese un nombre: "))
    
    if not(inputNombre in nombres):
        nombres.append(inputNombre)
    toggle=str(input("para seguir 'on' para terminar 'off': "))
    print    
    if toggle=="off" and len(nombres)<3:
        toggle="on"
        print("debe ingresar un minimo de 3 nombres para poder cerrar el programa \n")

# luego buscar un nombre y de encontrarlo decir en qué posición está.
print("AHORA DEBERA BUSCAR UN NOMBRE PARA SABER SI SE ENCUENTRA\n")
inputNombre=str(input("Ingrese el nombre a buscar: "))
posicionNombre=""
for i in range(len(nombres)):
    if nombres[i]==inputNombre:
        posicionNombre=i
        print("Nombre encontrado en la posicion: ",i)
        break
if posicionNombre=="":
    print("El nombre no ha sido encontrado")
    