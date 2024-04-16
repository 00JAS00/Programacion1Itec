# 1 Pedir dos números enteros, sumarlos y mostrar el resultado.
n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
resultadoSuma = n1+n2
print("la suma de los dos numeros es: ",resultadoSuma)
# Funcion de ejercicio 1 en python
def sumar():
    n1 = int(input("ingrese el primer numero: "))
    n2 = int(input("ingrese el segundo numero: "))
    resultadoSuma = n1+n2
    print("la suma de los dos numeros es: ",resultadoSuma)
    

# 2 Pedir tres notas, calcular el promedio y mostrarlo.
nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota: "))
nota3 = float(input("ingrese la tercera nota: "))
promedio = (nota1+nota2+nota3)/3
print("el promedio de las tres notas es: ",promedio)

# 3 Leer un número real y emitir una leyenda informando si es mayor o igual a cero o bien es negativo (son dos opciones).
numero = float(input("ingrese un numero real: "))
if (numero>=0):
    print("el numero es positivo")
else:
    print("el numero es negativo")

# 4 Leer dos números y decir cuál es el mayor.
n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
if (n1>n2):
    print("el primer numero es mayor")
else:
    print("el segundo numero es mayor")

# 5 Leer dos números reales y mostrarlos en orden creciente.
n1 = float(input("ingrese el primer numero: "))
n2 = float(input("ingrese el segundo numero: "))
if (n1<n2):
    print("el primer numero es menor: /n")
    print("Orden Creciente: ",n1,n2)
else:
    print("el primer numero es mayor y el segundo es menor: /n")
    print("Orden Creciente: ",n2,n1)

# 6 Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
operacion = input("ingrese la operacion (+ o -): ")
if (operacion=="+"):
    print("la suma de los dos numeros es: ",n1+n2)
else:
    print("la resta de los dos numeros es: ",n1-n2)



# 7 Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
    name=input("ingrese su nombre: ")
    opcion=input("ingrese la opcion ( > o < ): ")
    if (opcion==">"):
        print(name, "es mayor de edad")
    else:
        print(name, "es menor de edad")

# 8 Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.

entrada=input("ingrese un periodo en segundos: ")
segundosXdia=24*60*60
segundosXhora=60*60
segundosXminuto=60
resto=entrada
entradaAdias=entrada/segundosXdia
resto*=segundosXdia
entradaAhora=resto/segundosXhora
resto*=segundosXhora
entradaAminutos=resto/segundosXminuto
resto*=segundosXminuto
print("El periodo igresado es de: dias,horas, minutos y segundos ",entradaAdias,":",entradaAhora,":",entradaAminutos,":",resto)
# 9 Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.
n1 = int(input("ingrese un numero: "))
    if (n1>99 and n1<1000):
        print("el numero tiene dos digitos")



# 10 Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
    nombre=input("ingrese su nombre: ")
    carrera=input("ingrese la carrera en la que se inscribe: ")
    ciudad=input("ingrese la ciudad donde vive: ")
    montoCuota=51500
    if (ciudad!="Río Cuarto"):
        montoCuota*=0.15
        print("Nombre del Alumno: ",nombre," Ciudad: ",ciudad," Carrera: ",carrera," Monto Cuota: ",montoCuota," Descuento de 15% por no residir en Rio Cuarto")

# 11 El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % 
# sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). 
# Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
costoPasaje=2000
nombre=input("ingrese su nombre: ")
edad=input("ingrese su edad: ")
if(edad>4 and edad<10 or edad > 65):
    costoPasaje*=0.6
    print("Nombre del Pasajero: ",nombre," Edad: ",edad," Monto Pasaje: ",costoPasaje," Descuento de 40% por ser menor de 10 o mayor de 65 años")


# 12 Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  
# cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). 
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
diasNoTrabajados=int(input("ingrese la cantidad de días no trabajados: "))
anioIngreso=int(input("ingrese el año de ingreso en la empresa: "))
sueldoBase=47000
if (diasNoTrabajados==0 and anioIngreso>5):
    sueldoBase*=1.3
    print("su sueldo es: ",sueldoBase)
else:
    print("su sueldo es: ",sueldoBase)

