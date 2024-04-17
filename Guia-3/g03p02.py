# 2- Cargar letras en una lista hasta que el usuario ingrese un asterisco.
# Contar las vocales. Mostrar el total.

switch=""
vocales=[]
while switch!="*":
    letra=str(input("Ingrese una letra: "))
    # Se verifica si ingresa una sola letra
    if len(letra)==1:
        # se comprueba si la letra ingresada es vocal
        if letra in "aeiou":
            vocales.append(letra)
    else:
        print("no pueden ser mas de una letra")
    #Elecion de fin de programa 
    switch=str(input("Si desea finalizar Presione Tecla '*' : "))
# Fin Bucle
if len(vocales)>0:
    print ("La cantidad de vocales ingresadas son: ",vocales,"\n Y son una total de: ",len(vocales))
else:
    print("No se encontro ninguna vocal")