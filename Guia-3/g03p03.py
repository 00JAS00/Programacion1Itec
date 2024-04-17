# 3- Primer bucle: Almacenar en dos listas paralelas, nombres y sexos de personas hasta 
# que el usuario diga que no hay más. 
# Segundo bucle: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
# Tercer bucle: Mostrar los elementos de la lista resultante.

nombres=[]
sexos=[]
listaResultante=[]
switch=""
while switch!="no hay mas":
    nombres.append(str(input("Ingrese un nombre: ")))
    sexos.append(str(input("Ingrese el sexo 'm' de masculino o 'f' de femenino: ")))
    switch=str(input(" Si termino escriba: 'no hay mas': "))
    
# Segundo bucle: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
for i in range(len(nombres)):
    # en caso que no sea valida (por el anciano profe, chiste no se enoje) esta 
    # forma lo haria asi if sexos[i] == "f" or sexos[i] == "F": lo que sigue...
    if sexos[i] in "fF":
        # Le asigno a la lista resultante el nombre femenino seguido de un - y el sexo que es pór ejemplo ana - f
        auxiliar= nombres[i] + " - " + sexos[i]
        listaResultante.append(auxiliar)

# Tercer bucle: Mostrar los elementos de la lista resultante.
for elementos in listaResultante:
    print(elementos,"\n")
