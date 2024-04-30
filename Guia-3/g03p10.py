# 10- Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 

dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
lluviaDias=[]
respuesta=[0,""]
lluviaMayor=0
for i in range(len(dias)):
    lluvia=float(input("Ingrese la lluvia caida el dia "+dias[i]+": "))
    lluviaDias.append(lluvia)
    respuesta[0]+=lluvia
    if lluvia>lluviaMayor:
        lluviaMayor=lluvia
        respuesta[1]=dias[i] #dia que mas llovio
print("La cantidad de lluvia es: ",respuesta[0],"\n El dia que mas llovio fue: ", respuesta[1])


