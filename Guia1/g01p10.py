# Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
print("\n**************************************************************************************")
print("* Para saber si califica para un descuento de la cuota ingrese los siguientes datos: *")
print("**************************************************************************************\n")
nombre=input("ingrese su nombre: ")
carrera=input("ingrese la carrera en la que se va a inscribir: Electromecanica con E o Desarrollo de Software con DS: ")
ciudad=input("ingrese la ciudad donde vive: ")
montoCuota=51500
if (ciudad!="Río Cuarto" and carrera=="E"):
    montoCuota*=0.15
    print("Felicidades usted califica para el descuento de 15% por no residir en Rio Cuarto y inscribirse en Electromecanica!!!!!!!!")
    print("Nombre del Alumno: ",nombre,"\n Ciudad: ",ciudad,"\n Carrera: ",carrera,"\n Monto Cuota: ",montoCuota)
else:
    print("Lamentamos informarle  señor o señorita ",nombre,", no califica para el descuento de la cuota Vanquesela y quejese con la institución.!!")