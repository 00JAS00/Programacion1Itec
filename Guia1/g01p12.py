# Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  
# cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). 
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
print("******************************************************************************************")
print("* Calculador de sueldo a cobrar, Segun la antiguedad y la cantidad de dias no trabajados *")
print("******************************************************************************************\n")
diasNoTrabajados=int(input("ingrese la cantidad de días no trabajados: "))
anioIngreso=2024-int(input("ingrese el año de ingreso en la empresa: "))
sueldoBase=47000
if (diasNoTrabajados==0 and anioIngreso>5):
    sueldoBase*=1.3
    print("su sueldo es: ",sueldoBase)
else:
    print("su sueldo es: ",sueldoBase)
