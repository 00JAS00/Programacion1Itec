# El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % 
# sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). 
# Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

costoPasaje=2000
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
if(edad>=5 and edad<=10 or edad > 65):
    costoPasaje*=0.6
    print("Felicidades usted califica para el descuento del 40% !")
    print("Nombre del Pasajero: ",nombre,"\n Monto Pasaje: ",costoPasaje)
else:
    print("Lamentamos informarle ",nombre,"que no califica para el descuento de la cuota.!!")