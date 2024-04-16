# 13-Ingresar la lluvia caída en milímetros para cada día de la semana. Mostrar al final 
#     el total de lluvia caída y la cantidad de días que no llovió.
cantidadLluvia=0
contadorNoLluvia=0
for i in range(7):
    pregunta=input("Llovió el dia " + str(i+1) + "? (s/n): ")
    if (pregunta=="s"):
        lluvia=float(input("ingrese la lluvia de la del dia " + str(i+1) + " en milimetros: "))
        if (lluvia<0):
            print("la lluvia no puede ser negativa")
        else:
            cantidadLluvia+=lluvia
    elif (pregunta=="n"):
        contadorNoLluvia+=1

print("la cantidad de dias que no llovió es: ",contadorNoLluvia)
print("la cantidad de lluvia es: ",cantidadLluvia)


